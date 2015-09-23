__author__ = 'User'


import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../mitielib')

from mitie import *
from collections import defaultdict

path = os.path.dirname(sys.modules[__name__].__file__)
ner_model_path = os.path.join(path, 'MITIE-models/english/ner_model.dat')

ner = named_entity_extractor(ner_model_path)
#print ("\nTags output by this NER model:", ner.get_possible_ner_tags())


def ent_dict(entities, tokens):

    d = defaultdict(list)
    # entities is a list of tuples, each containing the entity tag and a xrange
    # that indicates which tokens are part of the entity.  The entities are also
    # listed in the order they appear in the input text file.
    for e in entities:
        ent_range = e[0]
        tag = e[1]
        entity_text = " ".join(tokens[i] for i in ent_range)
        d[tag].append((entity_text, ent_range))
    return d


def mitie_extract_ner(text):

    tokens = tokenize(text)

    entities = ner.extract_entities(tokens)

    return ent_dict(entities, tokens)


if __name__ == '__main__':
    """
    test NER
    """

    demo_text = [
        # 'Rami Eid is studying at Stony Brook University in NY.',
        #  "Barack Obama, the 44th and current President of the United States, and the first African American to hold the office, was born in Honolulu, Hawaii.",
         "Michael Irwin Jordan (born 1956) is an American scientist, Professor at the University of California, Berkeley and leading researcher in machine learning and artificial intelligence."
         # "Jordan was born in Ponchatoula, Louisiana, to a working class family, and received his BS magna cum laude in Psychology in 1978 from the Louisiana State University, his MS in Mathematics in 1980 from the Arizona State University and his PhD in Cognitive Science in 1985 from the University of California, San Diego. At the University of California, San Diego Jordan was a student of David Rumelhart and a member of the PDP Group in the 1980s.",
         # "Elvis Presley was born on January 8, 1935, in Tupelo, Mississippi, the son of Gladys Love and Vernon Elvis Presley, in the two-room shotgun house built by Vernon's father in preparation for the child's birth."
    ]

    print('###### MIT IE NER #####')

    for text in demo_text:
        print('Processing text: ', text)
        print('')
        print(mitie_extract_ner(text))
        print('')

