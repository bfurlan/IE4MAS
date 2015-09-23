__author__ = 'User'

## pogledaj ovo: http://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html

import random
import nltk
import json
from sklearn.svm import LinearSVC
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.metrics import classification_report

with open('feature_sets_headline_en.json') as data_file:
    feature_sets = json.load(data_file)

random.shuffle(feature_sets)

# other values: 'content', 'summary_en', 'headline_en'
content_type = 'headline_en'
test_set_size = 400
corpus_size = len(feature_sets)

print("Test set size:", test_set_size, " ****************\n")


test_set = feature_sets[:test_set_size]

test_skl = []
t_test_skl = []
for d in test_set:
    test_skl.append(d[0])
    t_test_skl.append(d[1])

# cls_set = list(set(t_test_skl))

# SVM with a Linear Kernel and default parameters
classifier = SklearnClassifier(LinearSVC())

for train_set_size in range(1000, corpus_size, 300):

    print("Train set size:", train_set_size)

    # Split in train
    train_set = feature_sets[test_set_size:train_set_size]

    classifier.train(train_set)

    # run the classifier on the train test
    p = classifier.classify_many(test_skl)

    # getting a full report
    print classification_report(t_test_skl, p)

    cm = nltk.ConfusionMatrix(p,t_test_skl)

    print(cm.pretty_format(sort_by_count=True, show_percents=True))

