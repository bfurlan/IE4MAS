from nltk.tag.stanford import StanfordNERTagger
import os
from stanford_combined_ner_extractor import path, ner_jar_path
import pandas as pd

__author__ = 'User'


classifier_path = os.path.join(path, "classifiers/english.conll.4class.distsim.crf.ser.gz")

st = StanfordNERTagger(classifier_path, ner_jar_path)

def stanford_extract_ner_series(tokens):
    """

    :param tokens:
    :return:
    """

    ent = st.tag(tokens)



    res = [e[1] for e in ent]

    res = pd.Series(data=res,index=tokens)

    return res
