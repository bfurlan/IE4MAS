from operator import itemgetter
from itertools import groupby
from agregator_utils import strip_tag_characters, read_data_frame_from_corpus
from pprint import pprint
from mit_ie.mite_rel_extractor import detect_rel
from mit_ie.mitie_ner_extractror import ent_dict
import pandas as pd

__author__ = 'User'


def index_to_xrange(ind_list, start_index, tag_type):
    """
    convert continuous tag indices to xrange list
    :param ind_list:
    :param start_index:
    :param tag_type:
    :return:
    """
    ranges = []
    for key, group in groupby(enumerate(ind_list), lambda (index, item): index - item):
        group = map(itemgetter(1), group)
        if len(group) > 1:
            ranges.append((xrange(group[0]-start_index, group[-1] - start_index+1), tag_type))
        else:
            ranges.append((xrange(group[0] - start_index, group[0] - start_index+1), tag_type))
    return ranges


full_tags = ["PERSON", "LOCATION", "ORGANIZATION", "MISC"]
striped_tags = strip_tag_characters(full_tags)




def get_relations(entities, sent, threshold=1):
    """

    :param entities: MITIE xrange entities
    :param sent: dataframe of sentence
    :return: dict of {'sentence': sent, 'entities': entities_dict, 'relations': relations}
    """
    # all possible combinations
    neighboring_entities = [(ent1[0], ent2[0]) for ent1 in entities for ent2 in entities if ent1 != ent2]
    tokens = map(unicode, sent.word.tolist())

    relations = detect_rel(neighboring_entities, tokens, threshold)

    entities_dict = ent_dict(entities, tokens)

    # if relations:
    #     print("Text: ", ' '.join(tokens))
    #
    #     print("Entities detected:")
    #     pprint(dict(entities_dict))
    #     print('')
    #
    #
    #     print('Relations for all possible combinations of entities:')
    #     pprint(dict(relations))
    #     print('')

    return {'sentence': sent, 'entities': entities_dict, 'relations': relations}


def get_entities_and_relations_from_dataframe(df, ner_column_name, threshold=1):
    """

    :param df: dataframe with tagged ner entites
    :param ner_column_name: where tags are
    :return: list of results as dicts {'sentence': sent, 'entities': entities_dict, 'relations': relations}
    """
    results = []
    # for each sentence
    for _, sent in df.groupby(level=0):
        entities = []
        # for each type of NE tag
        for i, tag in enumerate(striped_tags):
            # get words tagged with that tag
            all_tag_words = sent.ix[sent[ner_column_name] == tag]

            if all_tag_words.empty:
                continue

            all_tag_words_ind = all_tag_words.index.get_level_values('line_ind').unique()

            # start index of the sentence
            start = sent.index.get_level_values('line_ind').unique()[0]
            # get list of xranges with tags
            res = index_to_xrange(all_tag_words_ind, start, full_tags[i])
            # add to list of entities in sentence
            entities.extend(res)

        # get all relations in sentence and append to results
        # dicts {'sentence': sent, 'entities': entities_dict, 'relations': relations}
        results.append(get_relations(entities, sent, threshold))

    return results


if __name__ == '__main__':
    """
    test add_sent_index
    """

    df = pd.read_pickle("pickles/output-train-Socher-all_tokens_at_once.pkl")
    df.columns = [u'word', u'real_tag', u'mitie_ner', u'stanford_ner']

    # testing
    df = df.ix[:10000, :]

    results = get_entities_and_relations_from_dataframe(df, "real_tag")

    for r in results:
        if 'parents' in r["relations"]:
            pprint(r)







