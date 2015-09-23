__author__ = 'User'

from os import listdir
import os.path
import json

path = 'data-samples'
all_articles = []

for f in listdir(path):
    file_path = os.path.join(path, f)
    if not os.path.isfile(file_path):
        continue

    cls = f.replace("random-article-for-category-", "").replace(".json", "")

    with open(file_path) as data_file:
        data = json.load(data_file)

    articles = data['hits']['hits']

    def f(a):
        a['_source']['class'] = cls
        return a['_source']

    filtered_and_labeled = [f(a) for a in articles if a['_source']['content'] != ""]

    all_articles.extend(filtered_and_labeled)

with open('data.json', 'w') as outfile:
    json.dump(all_articles, outfile)




