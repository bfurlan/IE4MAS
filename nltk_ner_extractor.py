__author__ = 'User'

import nltk
from collections import defaultdict

ne_types = ["ORGANIZATION", "PERSON", "LOCATION", "DATE", "TIME", "MONEY", "PERCENT", "FACILITY", "GPE"]

def nltk_extract_ner(text):
    """
    Use of NLTK NE
    :param text:
    :return: list of all extracted NE
    """
    sentences = nltk.sent_tokenize(text)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)

    d = defaultdict(list)

    def extract_entity_names(t):
        entity_names = []

        if hasattr(t, 'label') and t.label:
            #if it is recognized as NE add with key of its type
            if t.label() in ne_types:
                d[t.label()].append(' '.join([child[0] for child in t]))
            else:
                for child in t:
                    entity_names.extend(extract_entity_names(child))

        return entity_names

    for tree in chunked_sentences:
        # Get results per sentence
        extract_entity_names(tree)


    # return all entity names
    return d
