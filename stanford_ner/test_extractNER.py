from unittest import TestCase
from stanford_combined_ner_extractor import stanford_extract_ner
from stanford_series_ner_extractor import stanford_extract_ner_series
from mit_ie.mitie import tokenize

__author__ = 'User'


class TestExtractNER(TestCase):
    def test_extractNER_person(self):
        demo = 'Rami Eid is studying at Stony Brook University in NY.'
        res = stanford_extract_ner(demo)
        self.failUnless('PERSON' in res)
        self.failUnless('Rami Eid' in res['PERSON'])

    def test_extractNER_date(self):
        demo = "Jordan was born in Ponchatoula, Louisiana, to a working class family, and received his BS magna cum laude in Psychology in 1978 from the Louisiana State University, his MS in Mathematics in 1980 from the Arizona State University and his PhD in Cognitive Science in 1985 from the University of California, San Diego. At the University of California, San Diego Jordan was a student of David Rumelhart and a member of the PDP Group in the 1980s."
        res = stanford_extract_ner(demo)
        self.failUnless('DATE' in res)
        self.failUnless('1978' in res['DATE'])

    def test_extractNER_date(self):
        demo = "Jordan was born in Ponchatoula, Louisiana, to a working class family, and received his BS magna cum laude in Psychology in 1978 from the Louisiana State University, his MS in Mathematics in 1980 from the Arizona State University and his PhD in Cognitive Science in 1985 from the University of California, San Diego. At the University of California, San Diego Jordan was a student of David Rumelhart and a member of the PDP Group in the 1980s."

        res = stanford_extract_ner_series(tokenize(demo))
        self.assertEqual(res["Ponchatoula"], "LOCATION")
        self.assertEqual(res["David"], "PERSON")
        self.assertEqual(res["PDP"], "ORGANIZATION")

