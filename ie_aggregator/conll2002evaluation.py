__author__ = 'User'

""" conll2002 is in Duch and Spanish so its not woriking well with that """


from nltk.corpus import conll2002
from nltk.chunk import tree2conlltags
import pandas as pd
from evaluate import evaluate
from mit_ie.mitie_series_ner_extractror import mitie_extract_ner_series
from stanford_ner.stanford_series_ner_extractor import stanford_extract_ner_series


chunked_words = tree2conlltags(conll2002.chunked_words())
df = pd.DataFrame(chunked_words, columns=['word', 'tmp', 'real_tag'])

# remove tmp col
df = df.loc[:, ["word", "real_tag"]]

# strip first two chars - "B-..." and "I-..."
df['real_tag'] = map(lambda x: x[2:] if len(x) > 2 else x, df['real_tag'])

# testing
df = df[:5000]

df.real_tag = list(df.real_tag)
df.word = map(unicode, df.word)

# df = add_dataframe_ner_tags(corpus_df=df, ner_extractor=mitie_extract_ner_series)
#
# print('###### MIT IE NER evaluation #####')
# evaluate(df.real_tag, df["mitie_extract_ner_list"])
# print('')
#
# df = add_dataframe_ner_tags(corpus_df=df, ner_extractor=stanford_extract_ner_series)
#
# print('###### Stanford NER evaluation #####')
# evaluate(df.real_tag, df["stanford_extract_ner_list"])
# print('')
#
