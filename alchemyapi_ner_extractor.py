__author__ = 'User'

from alchemyapi_python.alchemyapi import AlchemyAPI
from collections import defaultdict

'''
AlchemyAPI available at http://www.alchemyapi.com/developers/sdks
'''

alchemyapi = AlchemyAPI()

def alchemyapi_extract_ner(text):
    response = alchemyapi.entities('text', text)

    d = defaultdict(list)

    if response['status'] == 'OK':
         for entity in response['entities']:
            d[entity['type']].append(entity['text'].encode('utf-8'))
    else:
        raise ValueError('Error in entity extraction call: ', response['statusInfo'])

    return d

if __name__ == '__main__':
    """
    test NER
    """

    demo_text = ['Rami Eid is studying at Stony Brook University in NY']

    for demo in demo_text:
        print('Processing text: ', demo)
        print('')
        print(alchemyapi_extract_ner(demo))
        print('')
