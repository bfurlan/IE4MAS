__author__ = 'User'

from ie_aggregator.agregator_rel_utils import get_entities_and_relations_from_dataframe


def entities2datalog(entities):
    """

    :param entities: in format 'entities': defaultdict(<type 'list'>, {'PERSON': [(u'Sampras', xrange(1)),
    (u'David Rikl', xrange(10, 12)), (u'Graf', xrange(19, 20)), (u'Yayuk Basuki', xrange(25, 27))], ...
    :return: list of strings
    """

    res = []
    for ent_type in entities.keys():
        # if ent_type in ["MISC"]:
        # continue
        fac = str(ent_type).lower().strip()
        i = 1
        for ent in entities[ent_type]:
            var = fac + str(i)
            i += 1
            s1 = "{fac}({var}).".format(fac=fac, var=var)
            s2 = "{fac}_name({var},\'{text}\').".format(fac=fac, var=var, text=ent[0])

            res.extend([s1, s2])

    return res


def relations2datalog(relations):
    """

    :param relations: defaultdict(<type 'list'>, {'nationality': [(u'David Rikl', u'Czech Republic', 1.4531219459842886)
    :return: list of strings
    """

    res = []
    for rel_type in relations.keys():
        rel_name = str(rel_type).lower().strip()
        for rel in relations[rel_type]:
            s = "{rel}(\'{text1}\',\'{text2}\',\'{score}\').".\
                format(rel=rel_name, text1=rel[0], text2=rel[1], score=rel[2])
            res.append(s)

    return res



if __name__ == '__main__':
    """

    test

    """
    # import pandas as pd
    # from pprint import pprint
    # df = pd.read_pickle("ie_aggregator/pickles/output-train-Socher-all_tokens_at_once.pkl")
    # df.columns = [u'word', u'real_tag', u'mitie_ner', u'stanford_ner']
    #
    # # testing
    # df = df.ix[1182:1182, :]
    #
    # r = get_entities_and_relations_from_dataframe(df, "real_tag")[0]
    #
    # pprint(entities2datalog(r["entities"]))
    # pprint(relations2datalog(r["relations"]))

    from ie_aggregator.agregator_utils import read_data_frame_from_corpus

    file_path = 'ie_aggregator/corpuses/toy_example.txt'
    df = read_data_frame_from_corpus(file_path)
    r = get_entities_and_relations_from_dataframe(df, "real_tag", threshold=0)[1]
    # pprint(entities2datalog(r["entities"]))
    # pprint(relations2datalog(r["relations"]))
    print("\n".join(entities2datalog(r["entities"])))
    print("\n".join(relations2datalog(r["relations"])))




