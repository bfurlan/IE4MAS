__author__ = 'User'


from nltk.corpus import movie_reviews
import nltk
from random import shuffle

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = all_words.keys()[:2000]


def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# print document_features(movie_reviews.words('pos/cv957_8737.txt'))

feature_sets = []
for (d, c) in documents:
    feature_sets.append((document_features(d), c))
train_set, test_set = feature_sets[100:], feature_sets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print nltk.classify.accuracy(classifier, test_set)
classifier.show_most_informative_features(5)