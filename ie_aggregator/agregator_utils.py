import pandas as pd
from csv import QUOTE_NONE


__author__ = 'User'


def strip_tag_characters(l, slice_range=slice(0, 3)):
    """
    strip last chars - to get PER, ORG, LOC

    :param l:
    :param slice_range: for slice(n,end) pass slice(n,None)
    :return:
    """
    r = []
    for x in l:
            if len(x) > 4:
                r.append(unicode(x[slice_range]))
            else:
                r.append(unicode(x))
    return r


def add_sent_indices(df):
    # sentences are delimited by NaN
    sent_ends = list(df[df.isnull().any(axis=1)].index)
    # add column with sentence index
    sent_label = []
    sent_start_ind = 0
    for sent_ind, sent_end_ind in enumerate(sent_ends):
        sent_label = sent_label + [sent_ind] * (sent_end_ind - sent_start_ind)
        sent_start_ind = sent_end_ind

    # if last word is not delimiter add this sent indices too
    if sent_ends and (not sent_ends[-1] == len(df.word)):
        final_sent_ind = sent_label[-1]
        sent_end_ind = len(df.word)
        sent_label = sent_label + [final_sent_ind + 1] * (sent_end_ind - sent_start_ind)
    assert len(sent_label) == len(df.word), "Not of same len sent and df.index"
    df.loc[:, "sent_ind"] = sent_label
    # drop all sent delimiters
    df.drop(df.index[sent_ends], inplace=True)
    # make line_ind continuous (some were previously dropped)
    df.index = range(len(df.word))
    # add sent_ind as first index
    df.set_index("sent_ind", append=True, inplace=True)
    df.index.names = ["line_ind", "sent_ind"]
    df = df.reorder_levels(["sent_ind", "line_ind"])
    return df


def read_data_frame_from_corpus(file_path):
    """
    splits whole DataFrame to sentences by adding first level index (Multilevel Indexing) for each sentence
    it is possible to access sentences as well as individual words by index
    :param file_path:
    :return: DataFrame with word and real_tag cols and two level index: sentence ind and line ind
    """
    df = pd.read_csv(file_path, delimiter='\t', names=['word', 'real_tag'], dtype={'word': unicode, 'real_tag': unicode},
                     skip_blank_lines=False, quoting=QUOTE_NONE)

    df = add_sent_indices(df)

    return df


if __name__ == '__main__':
    """
    test add_sent_index
    """
    file_path = 'corpuses/dev-Socher'

    df = read_data_frame_from_corpus(file_path)

    print df.ix[:500, :]