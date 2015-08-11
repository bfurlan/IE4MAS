__author__ = 'User'

from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk
import json
from random import shuffle


def load_data(path='data.json'):
    """
    load data, shuffle and return list of articles

    :param path:
    :return: list of articles
    """

    # load articles and shuffle
    with open(path) as data_file:
        articles = json.load(data_file)

    shuffle(articles)
    return articles

def get_tokens(articles, small_set=False):
    """
    :param articles:
    :param small_set: use for testing small set
    :return: list of tokens
    """
    # make it smaller for testing
    if small_set:
        articles = articles[:150]

    # make vector-space
    all_tokens = []
    for a in articles:
        all_tokens.extend(word_tokenize(a['content']))
    return all_tokens


stemmer = SnowballStemmer("english")
stopwords = set(nltk.corpus.stopwords.words('english'))

def pre_process(tokens):
    """
    tokenize, remove all nonASCII characters from words, lower and stem
    :param tokens: list of words
    :return: list of words
    """
    all_words = []
    for w in tokens:
        if w.isalpha():
            w = w.encode(encoding='ascii', errors='ignore')
            w = w.lower()
            w = stemmer.stem(w)
            if w not in stopwords:
                all_words.append(w)
    return all_words


def wrap_document_features(word_features):
    """
    :param word_features: list of word features
    :return: func that create feature vector for given list of word features
    """
    def document_features(document):
        """
        create word features
        :param document:
        :return:
        """
        document_words = word_tokenize(document)
        all_processed_words = pre_process(document_words)
        unique_document_words = set(all_processed_words)
        features = {}
        for word in word_features:
            # !!!! PROBLEM for nonASCII characters in words (IN doesn't work)
            features['contains({word})'.format(word=word)] = word in unique_document_words
        return features

    return document_features
