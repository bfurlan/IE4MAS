__author__ = 'User'

import os
import json

from stanford_ner.stanford_combined_ner_extractor import stanford_extract_ner
from nltk_ner_extractor import nltk_extract_ner
from alchemyapi_ner_extractor import alchemyapi_extract_ner

path = os.path.join(os.getcwd(), 'data-samples/random-article-for-category-News.json')


with open(path) as data_file:
    data = json.load(data_file)

articles = data['hits']['hits']

for i in range(10):
    print('************* NUM : %d **************' % i)
    line = articles[i]['_source']['summary_en']
    try:
        line = line.decode('utf-8', 'ignore')
    except UnicodeEncodeError:
        continue

    print('Processing text: ', line)
    print('')
    print('###### NLTK NER #####')
    print(nltk_extract_ner(line))
    print('')

    print('###### Stanford NER #####')
    print(stanford_extract_ner(line))
    print('')

    print('###### AlchemyAPI NER #####')
    print(alchemyapi_extract_ner(line))
    print('')