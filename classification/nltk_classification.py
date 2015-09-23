from __future__ import division  # Python 2 users only
import nltk
import utils
from pprint import pprint

articles = utils.load_data()

# other values: 'content', 'summary_en', 'headline_en'
content_type = 'summary_en'
test_set_size = 300
corpus_size = len(articles)

articles = articles[:1500]
feature_sets = utils.extract_features(articles, content_type)

print("Test set size:", test_set_size," ****************\n")

for train_set_size in range(500, corpus_size, 300):

    print("Train set size:", train_set_size)

    # Split in test - train
    train_set = feature_sets[test_set_size:train_set_size]
    test_set = feature_sets[:test_set_size]

    classifier = nltk.NaiveBayesClassifier.train(train_set)

    print("train set", nltk.classify.accuracy(classifier, train_set))
    print("test set", nltk.classify.accuracy(classifier, test_set))
    print

    # classifier.show_most_informative_features(5)