__author__ = 'User'

from mitie_ner_extractror import ner
import pandas as pd

def mitie_extract_ner_series(tokens):

    """
    :param tokens:
    :return: list of ners
    """

    entities = ner.extract_entities(tokens)

    # entities is a list of tuples, each containing the entity tag and a xrange
    # that indicates which tokens are part of the entity.  The entities are also
    # listed in the order they appear in the input text file.

    res = ['O']*len(tokens)
    res = pd.Series(data=res, index=tokens)

    for e in entities:
        ent_range = e[0]
        ent_tag = e[1]
        res.iloc[ent_range[0]:ent_range[-1]+1] = ent_tag

    return res


