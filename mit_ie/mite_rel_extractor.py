__author__ = 'User'

import sys, os
# Make sure you put the mitielib folder into the python search path.  There are
# a lot of ways to do this, here we do it programmatically with the following
# two statements:
parent = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent + '/../../mitielib')

from mitie import *
from collections import defaultdict
from mitie_ner_extractror import ner, ent_dict
import re
from pprint import pprint

path = os.path.dirname(sys.modules[__name__].__file__)
rel_models_path = os.path.join(path, "MITIE-models/english/binary_relations/")

rel_detectors = []

for f in os.listdir(rel_models_path):
    file_path = os.path.join(rel_models_path, f)
    if not os.path.isfile(file_path):
        continue
    rel_name = re.findall(r'.*rel_classifier_.*\..*\.(.*)\.svm', file_path)[0]

    # Also add relation range and domain for each relation
    rel_detectors.append((rel_name, binary_relation_detector(os.path.join(file_path))))


"""
List of trained relations: http://www.freebase.com/[...]
["['book/written_work/author']",
 "['film/film/directed_by']",
 "['influence/influence_node/influenced_by']",
 "['law/inventor/inventions']",
 "['location/location/contains']",
 "['location/location/nearby_airports']",
 "['location/location/partially_contains']",
 "['organization/organization/place_founded']",
 "['organization/organization_founder/organizations_founded']",
 "['organization/organization_scope/organizations_with_this_scope']",
 "['people/deceased_person/place_of_death']",
 "['people/ethnicity/geographic_distribution']",
 "['people/person/ethnicity']",
 "['people/person/nationality']",
 "['people/person/parents']",
 "['people/person/place_of_birth']",
 "['people/person/religion']",
 "['people/place_of_interment/interred_here']",
 "['time/event/includes_event']",
 "['time/event/locations']",
 "['time/event/people_involved']"]
 """

"""
# author(person,book) => author(person,misc)
author_rel_detector = binary_relation_detector("MITIE-models/english/binary_relations/rel_classifier_book.written_work.author.svm")

# directed_by(film,person) => directed_by(misc,person)
directed_by_rel_detector = binary_relation_detector("MITIE-models/english/binary_relations/rel_classifier_film.film.directed_by.svm")

# influenced_by(person, person)
influenced_by_rel_detector = binary_relation_detector("MITIE-models/english/binary_relations/rel_classifier_influence.influence_node.influenced_by.svm")

# ethnicity(person,ethnicity) => ethnicity(person,misc)
ethnicity_rel_detector = binary_relation_detector("MITIE-models/english/binary_relations/rel_classifier_people.person.ethnicity.svm")



# born_in(person, location)
born_in_rel_detector = binary_relation_detector(os.path.join(path, "MITIE-models/english/binary_relations/rel_classifier_people.person.place_of_birth.svm"))
"""

def detect_rel(entities, tokens, threshold=0):
    d = defaultdict(list)
    # Now that we have our list, let's check each entity pair and see which one the
    # detector selects.
    for ent1, ent2 in entities:
        # Detection has two steps in MITIE. First, you convert a pair of entities
        # into a special representation.
        rel = ner.extract_binary_relation(tokens, ent1, ent2)
        # Then you ask the detector to classify that pair of entities.  If the
        # score value is > 0 then it is saying that it has found a relation.  The
        # larger the score the more confident it is.  Finally, the reason we do
        # detection in two parts is so you can reuse the intermediate rel in many
        # calls to different relation detectors without needing to redo the
        # processing done in extract_binary_relation().

        for rel_type, rel_detector in rel_detectors:
            score = rel_detector(rel)
            # Print out any matching relations.
            if score > threshold:
                ent1_text = " ".join(tokens[i] for i in ent1)
                ent2_text = " ".join(tokens[i] for i in ent2)
                d[str(rel_type)].append((ent1_text, ent2_text, score))
    return d


def get_neighbouring_entities(entities):
    #only for neighbouring entities

    # First, let's make a list of neighboring entities.  Once we have this list we
    # will ask the relation detector if any of these entity pairs is an example of
    # the "person born in place" relation.
    neighboring_entities = [(entities[i][0], entities[i+1][0]) for i in xrange(len(entities)-1)]
    # Also swap the entities and add those in as well.  We do this because "person
    # born in place" mentions can appear in the text in as "place is birthplace of
    # person".  So we must consider both possible orderings of the arguments.
    neighboring_entities += [(r,l) for (l,r) in neighboring_entities]

    return neighboring_entities

if __name__ == '__main__':
    """
    test REL extractor
    """

    demo_text = [
        # 'Rami Eid is studying at Stony Brook University in NY.',
        #  "Barack Obama, the 44th and current President of the United States, and the first African American to hold the office, was born in Honolulu, Hawaii.",
        #  "Michael Irwin Jordan (born 1956) is an American scientist, Professor at the University of California, Berkeley and leading researcher in machine learning and artificial intelligence.",
        #  "Jordan was born in Ponchatoula, Louisiana, to a working class family, and received his BS magna cum laude in Psychology in 1978 from the Louisiana State University, his MS in Mathematics in 1980 from the Arizona State University and his PhD in Cognitive Science in 1985 from the University of California, San Diego.",
        #  "At the University of California, San Diego Jordan was a student of David Rumelhart and a member of the PDP Group in the 1980s.",
          "Elvis Presley was born on January 8, 1935, in Tupelo, Mississippi, the son of Gladys Love and Vernon Elvis Presley, in the two-room shotgun house built by Vernon's father in preparation for the child's birth."
    ]

    print('###### MIT IE NER #####')

    threshold = 1


    for text in demo_text:

        print('Processing text: ', text)
        print('')

        tokens = tokenize(text)

        entities = ner.extract_entities(tokens)
        entities_dict = ent_dict(entities, tokens)

        print("Entities detected:")
        pprint(dict(entities_dict))
        print('')

        # neighboring_entities = get_neighbouring_entities(entities)
        #
        # relations = detect_rel(neighboring_entities, tokens, threshold)
        #
        # print('Relations for neighboring entities:')
        # pprint(dict(relations))
        # print('')
        #

        # all possible combinations
        neighboring_entities = [(ent1[0], ent2[0]) for ent1 in entities for ent2 in entities if ent1 != ent2]

        relations = detect_rel(neighboring_entities, tokens, threshold)

        print('Relations for all possible combinations of entities:')
        pprint(dict(relations))
        print('')


        """
        #specific entities - person, location
        persons = entities_dict["PERSON"]
        locations = entities_dict["LOCATION"]

        neighboring_entities = [(per[1], loc[1]) for per in persons for loc in locations if loc != per]

        neighboring_entities += [(r,l) for (l,r) in neighboring_entities]

        relations = detect_rel(neighboring_entities, tokens)

        print('Relations for all entities:')
        print(relations)
        """