from agregator_utils import strip_tag_characters

__author__ = 'User'


def add_ner_tags_dataframe_by_sentences(df, ner_extractor):
    """

    :param df:
    :param ner_extractor:
    :return:
    """
    ner_extractor_name = ner_extractor.__name__

    ner_list = []
    for sent_ind in df.index.levels[0]:
        tokens = df.loc[sent_ind].word
        # convert to unicode
        tokens = map(unicode, tokens)
        # tag ners
        res = ner_extractor(tokens)
        res = strip_tag_characters(res)
        ner_list += res

    assert len(ner_list) == len(df.word)

    df.loc[:, ner_extractor_name] = ner_list

    return df


def add_ner_tags_dataframe_all_tokens_at_once(df, ner_extractor):
    """

    :param df:
    :param ner_extractor:
    :return:
    """
    ner_extractor_name = ner_extractor.__name__

    tokens = list(df.word)
    # convert to unicode
    tokens = map(unicode, tokens)
    # tag ners
    ner_list = ner_extractor(tokens)
    ner_list = strip_tag_characters(ner_list)

    assert len(ner_list) == len(df.word)

    df.loc[:, ner_extractor_name] = ner_list

    return df

from operator import itemgetter
from itertools import groupby


def index_to_xrange(l, start):
    ranges = []
    for key, group in groupby(enumerate(l), lambda (index, item): index - item):
        group = map(itemgetter(1), group)
        if len(group) > 1:
            ranges.append(xrange(group[0]-start, group[-1] - start))
        else:
            ranges.append(group[0] - start)
    return ranges


def get_ner_tags_xrange(df, ner_extractor_name):
    """

    :param df:
    :param ner_extractor:
    :return:
    """

    for sent_ind in df.index.levels[0]:
        sent = df.loc[sent_ind]

    # assert len(ner_list) == len(df.word)

    # df.loc[:, ner_extractor_name] = ner_list

    return df

