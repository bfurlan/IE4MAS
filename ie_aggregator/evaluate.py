__author__ = 'User'

# These evaluations are not valid for NER - https://youtu.be/zUtAtPLrnts
# TODO change evaluate to work on entity level (not as now on word level)


from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np



# !!! fixed for 4 class NERs, can be changed
_target_names = ['PER', 'ORG', 'LOC', 'MISC']


def plot_confusion_matrix(cm, title='Confusion matrix', cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    tick_marks = np.arange(len(_target_names))
    plt.xticks(tick_marks, _target_names, rotation=45)
    plt.yticks(tick_marks, _target_names)

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def evaluate(reference_list, test_list, plot_conf_matrix=False):
    """
    prints results and plots confusion matrix
    :param reference_list:
    :param test_list:
    :return:
    """
    # print ('accuracy_score', accuracy_score(reference_list, test_list))
    print(classification_report(reference_list, test_list))

    if plot_conf_matrix:
        cm = confusion_matrix(reference_list, test_list)

        np.set_printoptions(precision=2)

        # Normalize the confusion matrix by row (i.e by the number of samples
        # in each class)
        cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        # print('Normalized confusion matrix')
        # print(cm_normalized)

        plt.figure()
        plot_confusion_matrix(cm_normalized, title='Normalized confusion matrix')

        plt.show()