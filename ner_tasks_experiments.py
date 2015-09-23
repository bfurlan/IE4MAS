__author__ = 'Bojan Furlan'

from noun_phrases_extractors.np_extractor import regex_np_extract,ml_np_extract
from stanford_ner.stanford_combined_ner_extractor import stanford_extract_ner
from nltk_ner_extractor import nltk_extract_ner
from mit_ie.mitie_ner_extractror import mitie_extract_ner
from alchemyapi_ner_extractor import alchemyapi_extract_ner
from pprint import pprint

#************************* START TEST *************************


print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')


demo_text = [
    # 'Rami Eid is studying at Stony Brook University in NY.',
    #  "Barack Obama, the 44th and current President of the United States, and the first African American to hold the office, was born in Honolulu, Hawaii.",
     "Michael Irwin Jordan (born 1956) is an American scientist, Professor at the University of California, Berkeley and leading researcher in machine learning and artificial intelligence."
    ]


for demo in demo_text:
    print('Processing text: ', demo)
    print('')

    print('###### Noun Phrases: ML Extractor #####')
    pprint(ml_np_extract(demo))
    print('')

    print('###### Noun Phrases: RegEx Extractor #####')
    pprint(regex_np_extract(demo))
    print('')

    print('###### NLTK NER #####')
    pprint(dict(nltk_extract_ner(demo)))
    print('')

    print('###### Stanford NER #####')
    pprint(dict(stanford_extract_ner(demo)))
    print('')

    print('###### MIT_IE NER #####')
    pprint(dict(mitie_extract_ner(demo)))
    print('')

    print('###### AlchemyAPI NER #####')
    pprint(dict(alchemyapi_extract_ner(demo)))
    print('')


