from unittest import TestCase
from results_to_datalog import entities2datalog
from mit_ie.mitie_ner_extractror import mitie_extract_ner
__author__ = 'User'


class TestEntities2prolog(TestCase):
    def test_entities2prolog(self):
        demo_text = 'Rami Eid is studying at Stony Brook University in NY.' # Michael Irwin Jordan (born 1956) is an American scientist, Professor at the University of California, Berkeley and leading researcher in machine learning and artificial intelligence.'

        entities = mitie_extract_ner(demo_text)

        pl_results = entities2datalog(entities)

        self.assertIn("organization_name(organization1,'Stony Brook University').", pl_results)

