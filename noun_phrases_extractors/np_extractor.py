__author__ = 'User'


"""
http://textblob.readthedocs.org/en/latest/quickstart.html#noun-phrase-extraction

TextBlob currently has two noun phrases chunker implementations,
textblob.np_extractors.FastNPExtractor (default, based on Shlomi Babluki's implementation from this blog post)
and textblob.np_extractors. ConllExtractor, which uses the CoNLL 2000 corpus to train a tagger.

You can change the chunker implementation (or even use your own) by explicitly passing
an instance of a noun phrase extractor to a TextBlob's constructor.

>>> from textblob import TextBlob
>>> from textblob.np_extractors import ConllExtractor
>>> extractor = ConllExtractor()
>>> blob = TextBlob("Python is a high-level programming language.", np_extractor=extractor)
>>> blob.noun_phrases
WordList(['python', 'high-level programming language'])
"""

from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

extractor = ConllExtractor()


def ml_np_extract(text):
    """
    CoNLLExtractor
    :param text:
    :return:
    """
    blob = TextBlob(text, np_extractor=extractor)
    return blob.noun_phrases


def regex_np_extract(text):
    """
    # regular expressions extractor
    :param text:
    :return:
    """
    blob = TextBlob(text)
    return blob.noun_phrases

if __name__ == '__main__':
    """
    test
    """

    demo_text = ['Rami Eid is studying at Stony Brook University in NY.',
                 "Barack Obama, the 44th and current President of the United States, and the first African American to hold the office, was born in Honolulu, Hawaii.",
                 "Michael Irwin Jordan (born 1956) is an American scientist, Professor at the University of California, Berkeley and leading researcher in machine learning and artificial intelligence."
                 ]

    for text in demo_text:
        print('Processing text: ', text)
        print('')

        print("ML extracted NPs:", ml_np_extract(text))
        print("Regex extracted NPs:", regex_np_extract(text))
        print('')