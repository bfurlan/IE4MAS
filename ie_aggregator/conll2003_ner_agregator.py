__author__ = 'User'

import pandas as pd
from evaluate import evaluate
from agregator_utils import add_sent_indices
from agregator_ner_utils import add_ner_tags_dataframe_by_sentences, add_ner_tags_dataframe_all_tokens_at_once
from mit_ie.mitie_series_ner_extractror import mitie_extract_ner_series
from stanford_ner.stanford_series_ner_extractor import stanford_extract_ner_series
from csv import QUOTE_NONE

"""
CONLL2003 data
https://github.com/benjamin-adrian/scoobie/tree/master/corpora
https://github.com/benjamin-adrian/scoobie/blob/master/README.md

eng_testb-NOT_VALID_TAGS!!!!!
"""

file_path = 'corpuses\conll2003_eng_train'

df = pd.read_csv(file_path, delimiter=' ', usecols=[0, 3], names=['word', 'real_tag'],
                 dtype={'word': unicode, 'real_tag': unicode},
                 skip_blank_lines=False, quoting=QUOTE_NONE)
# testing
df = df[:5000]

# strip chars in real_tag
stripped_tags = df.loc[df.real_tag.str.len() > 1].real_tag.str[2:]
df.real_tag = stripped_tags
df.real_tag[df.real_tag.isnull()] = 'O'

# split to sentences
df = add_sent_indices(df)

df['real_tag'] = list(df['real_tag'])

print("######## all tokens at once ############")

df = add_ner_tags_dataframe_all_tokens_at_once(df=df, ner_extractor=mitie_extract_ner_series)

print('###### MIT IE NER evaluation #####')
evaluate(df.real_tag, df["mitie_extract_ner_series"])
print('')

df = add_ner_tags_dataframe_all_tokens_at_once(df=df, ner_extractor=stanford_extract_ner_series)

print('###### Stanford NER evaluation #####')
evaluate(df.real_tag, df["stanford_extract_ner_series"])
print('')


# df.to_pickle('conll2003_train_output_all_tokens_at_once.pkl')
