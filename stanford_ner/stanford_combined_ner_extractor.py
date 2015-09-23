__author__ = 'User'

"""
    combines outputs of 3 Stanford NER models for NER tagging
"""


from nltk.tag.stanford import StanfordNERTagger
from collections import defaultdict
import string
import sys
import os
from mit_ie.mitie import tokenize


class NERComboTagger(StanfordNERTagger):

    def __init__(self, *args, **kwargs):
        self.stanford_ner_models = kwargs['stanford_ner_models']
        kwargs.pop("stanford_ner_models")
        super(NERComboTagger,self).__init__(*args, **kwargs)

    @property
    def _cmd(self):
        return ['edu.stanford.nlp.ie.NERClassifierCombiner',
                '-ner.model',
                self.stanford_ner_models,
                '-textFile',
                self._input_file_path,
                '-outputFormat',
                self._FORMAT,
                '-tokenizerFactory',
                'edu.stanford.nlp.process.WhitespaceTokenizer',
                '-tokenizerOptions',
                '\"tokenizeNLs=false\"']


# ADD Closure instead of this???

java_path = "C:/Program Files/Java/jre1.8.0_31/bin/java.exe"
os.environ['JAVAHOME'] = java_path

path = os.path.dirname(sys.modules[__name__].__file__)
ner_jar_path = os.path.join(path,"stanford-ner.jar")

all_classifiers = [
    "classifiers/english.all.3class.distsim.crf.ser.gz",
    "classifiers/english.conll.4class.distsim.crf.ser.gz",
    "classifiers/english.muc.7class.distsim.crf.ser.gz"
]

all_classifiers = [os.path.join(path, s) for s in all_classifiers]

default_classifier_path = all_classifiers[0]

st = NERComboTagger(default_classifier_path, ner_jar_path, stanford_ner_models=','.join(all_classifiers))


def stanford_extract_ner(text):
    tokens = tokenize(text)
    ent = st.tag(tokens)

    d = defaultdict(list)

    # keep the last class type
    c = 'O'
    #num = 0 # keep the order
    for e in ent:
        # if it is not null - O
        if not e[1] == ('O'):
            #remove puctuation
            s = str(e[0]).translate(string.maketrans("",""), string.punctuation)
            # last was O or now changed to different class
            if c != e[1]:
                d[e[1]].append(s)
                #num+=1 # if order is needed
            else:
                # else append to lest elem
                d[e[1]][-1]= d[e[1]][-1]+" "+s #change if order is needed
        c = e[1]
    return d


if __name__ == '__main__':
    """
    test NER
    """

    demo_text = ['Rami Eid is studying at Stony Brook University in NY.',
                 "Barack Obama, the 44th and current President of the United States, and the first African American to hold the office, was born in Honolulu, Hawaii.",
                 "Michael Irwin Jordan (born 1956) is an American scientist, Professor at the University of California, Berkeley and leading researcher in machine learning and artificial intelligence."
                 "Jordan was born in Ponchatoula, Louisiana, to a working class family, and received his BS magna cum laude in Psychology in 1978 from the Louisiana State University, his MS in Mathematics in 1980 from the Arizona State University and his PhD in Cognitive Science in 1985 from the University of California, San Diego. At the University of California, San Diego Jordan was a student of David Rumelhart and a member of the PDP Group in the 1980s."
    ]

    print('###### Stanford NER #####')

    for demo in demo_text:
        print('Processing text: ', demo)
        print('')
        print(stanford_extract_ner(demo))
        print('')



