__author__ = 'User'

import pandas as pd
import sys
sys.stdout = open('outputs/conll2003_train_diff_output_real_tag.txt', 'w')


df = pd.read_pickle("pickles/conll2003_train_output_all_tokens_at_once.pkl")
df.columns = [u'word', u'real_tag', u'mitie_ner', u'stanford_ner']

# get DataFrame with all tags that differ from real results
diff_idx = df[(df.mitie_ner != df.real_tag) | (df.stanford_ner != df.real_tag)].index
diff = df.loc[diff_idx]

# get sentences ids for these diff tagged words
idx_sents_with_diff_tags = pd.Series(index=diff.index.labels[0], data=diff.index.labels[1])
# remove duplicates
idx_sents_with_diff_tags = idx_sents_with_diff_tags.groupby(level=0).first()

for i in idx_sents_with_diff_tags.index:
    print("##########################################################################")
    print("#### Different tags: #### ")
    print(diff.loc[i])
    print
    print("#### Whole sentence: #########")
    print
    print(df.loc[i])

    # raw_input("Press Enter to continue...")
    # if i > 100:
    #     break