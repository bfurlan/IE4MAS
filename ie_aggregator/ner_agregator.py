__author__ = 'User'

import pandas as pd
from evaluate import evaluate
from agregator_ner_utils import add_ner_tags_dataframe_by_sentences, add_ner_tags_dataframe_all_tokens_at_once
from agregator_utils import read_data_frame_from_corpus
from mit_ie.mitie_series_ner_extractror import mitie_extract_ner_series
from stanford_ner.stanford_series_ner_extractor import stanford_extract_ner_series


def save_to_excel(output_path, sheet_name):
    global writer
    writer = pd.ExcelWriter(output_path)
    df.to_excel(writer, sheet_name)
    writer.save()

file_path = 'corpuses/train-Socher'

df = read_data_frame_from_corpus(file_path)

# testing
df = df.ix[:500, :]


df['real_tag'] = list(df['real_tag'])


# print("######### Sentence by sentence ############")
# df = add_ner_tags_dataframe_by_sentences(df=df, ner_extractor=mitie_extract_ner_series)
#
# print('###### MIT IE NER evaluation #####')
# evaluate(df.real_tag, df["mitie_extract_ner_series"])
# print('')

#
#
# df = add_ner_tags_dataframe_by_sentences(df=df, ner_extractor=stanford_extract_ner_series)
#
# print('###### Stanford NER evaluation #####')
# evaluate(df.real_tag, df["stanford_extract_ner_series"])
# print('')
#
# output_path = 'output.xlsx'
# sheet_name = 'tagged_by_sentences'
# save_to_excel(output_path=output_path, sheet_name=sheet_name)


print("######## all tokens at once ############")

df = add_ner_tags_dataframe_all_tokens_at_once(df=df, ner_extractor=mitie_extract_ner_series)

print('###### MIT IE NER evaluation #####')
evaluate(df.real_tag, df["mitie_extract_ner_series"])
print('')

df = add_ner_tags_dataframe_all_tokens_at_once(df=df, ner_extractor=stanford_extract_ner_series)

print('###### Stanford NER evaluation #####')
evaluate(df.real_tag, df["stanford_extract_ner_series"])
print('')


# df.to_pickle('output-all_tokens_at_once.pkl')

# output_path = 'output.xlsx'
# sheet_name = 'tagged_all_tokens_at_once'
# save_to_excel(output_path=output_path, sheet_name=sheet_name)
