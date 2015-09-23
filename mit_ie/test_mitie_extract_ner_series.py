from unittest import TestCase
from mitie_series_ner_extractror import mitie_extract_ner_series
from mitie import tokenize

__author__ = 'User'

def test(text):
    tokens = tokenize(text)
    res = mitie_extract_ner_series(tokens)
    return res

class TestMitie_extract_ner_series(TestCase):
    def test_mitie_extract_ner_series2(self):
        text = 'Rami Eid is studying at Stony Brook University in NY.'
        res = test(text)
        self.assertEqual (res["NY"], "LOCATION")
        self.assertEqual (res["Eid"], "PERSON")
        self.assertEqual (res["Stony"], "ORGANIZATION")

    def test_mitie_extract_ner_series1(self):
        text = "Jordan"
        res = test(text)
        self.assertEqual(res["Jordan"], "LOCATION")



