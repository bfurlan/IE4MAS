from unittest import TestCase

import utils
import nltk

__author__ = 'User'

text = """NEW YORK, N.Y. - A Californian and a New Yorker have won top honours
at the National High School Musical Theater Awards. Anthony Skillman, of Mission Viejo, California,
was named best actor, and Marla Louissaint, of New York City, was named best actress Monday night
at the sixth-annual "Glee"-like competition, nicknamed the Jimmy Awards after theatre owner James Nederlander.
Each will receive a $10,000 scholarship award, capping a monthslong winnowing process that began with
50,000 students from 1,000 schools and ended at the Minskoff Theatre, the long-term home of "The Lion King." """

class TestDocument_features(TestCase):
    def test_document_features(self):

        tokens = nltk.word_tokenize(text)

        all_processed_words = utils.pre_process(tokens)

        all_word_freq = nltk.FreqDist(all_processed_words)
        word_features = list(all_word_freq)

        document_features = utils.wrap_document_features(word_features)

        res = document_features(text)

        for name, val in res.iteritems():
            if val:
                s = name.replace('contains(', '').replace(')', '')
                self.assertIn(s, all_processed_words, msg="Does not contain the word feature:'{word}' from text given".format(word=s))

    def test_pre_process(self):

        tokens = nltk.word_tokenize(text)

        res = utils.pre_process(tokens)

        self.assertNotIn("the", res, msg="stopwords not excluded!!!")

        self.assertIn("student", res, msg="student in text but not in result!!!")