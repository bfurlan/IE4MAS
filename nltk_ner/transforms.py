from nltk.tree import Tree

# NOT WORKING: Just to try something like this
'''

text = 'An enhanced Interactive Python.'
import nltk
sentences = nltk.sent_tokenize(text)
tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=False)
chunked_sentences
list(chunked_sentences)
from nltk.chunk import tree2conlltags
tree2conlltags(chunked_sentences)
t = list(chunked_sentences)

t = flatten_deeptree(chunked_sentences) ???

'''
if hasattr(Tree, 'label'):
    def node_label(node):
        return node.label()
else:
    def node_label(node):
        return node.node

def flatten_deeptree(tree):
    '''
    flatten_deeptree(Tree('S', [Tree('NP-SBJ', [Tree('NP', [Tree('NNP', ['Pierre']), Tree('NNP', ['Vinken'])]), Tree(',', [',']), Tree('ADJP', [Tree('NP', [Tree('CD', ['61']), Tree('NNS', ['years'])]), Tree('JJ', ['old'])]), Tree(',', [','])]), Tree('VP', [Tree('MD', ['will']), Tree('VP', [Tree('VB', ['join']), Tree('NP', [Tree('DT', ['the']), Tree('NN', ['board'])]), Tree('PP-CLR', [Tree('IN', ['as']), Tree('NP', [Tree('DT', ['a']), Tree('JJ', ['nonexecutive']), Tree('NN', ['director'])])]), Tree('NP-TMP', [Tree('NNP', ['Nov.']), Tree('CD', ['29'])])])]), Tree('.', ['.'])]))
    Tree('S', [Tree('NP', [('Pierre', 'NNP'), ('Vinken', 'NNP')]), (',', ','), Tree('NP', [('61', 'CD'), ('years', 'NNS')]), ('old', 'JJ'), (',', ','), ('will', 'MD'), ('join', 'VB'), Tree('NP', [('the', 'DT'), ('board', 'NN')]), ('as', 'IN'), Tree('NP', [('a', 'DT'), ('nonexecutive', 'JJ'), ('director', 'NN')]), Tree('NP-TMP', [('Nov.', 'NNP'), ('29', 'CD')]), ('.', '.')])
    '''
    return Tree(node_label(tree), flatten_childtrees([c for c in tree]))

def flatten_childtrees(trees):
    children = []

    for t in trees:
        if t.height() < 3:
            children.extend(t.pos())
        elif t.height() == 3:
            children.append(Tree(node_label(t), t.pos()))
        else:
            children.extend(flatten_childtrees([c for c in t]))

    return children

def shallow_tree(tree):
    '''
    shallow_tree(Tree('S', [Tree('NP-SBJ', [Tree('NP', [Tree('NNP', ['Pierre']), Tree('NNP', ['Vinken'])]), Tree(',', [',']), Tree('ADJP', [Tree('NP', [Tree('CD', ['61']), Tree('NNS', ['years'])]), Tree('JJ', ['old'])]), Tree(',', [','])]), Tree('VP', [Tree('MD', ['will']), Tree('VP', [Tree('VB', ['join']), Tree('NP', [Tree('DT', ['the']), Tree('NN', ['board'])]), Tree('PP-CLR', [Tree('IN', ['as']), Tree('NP', [Tree('DT', ['a']), Tree('JJ', ['nonexecutive']), Tree('NN', ['director'])])]), Tree('NP-TMP', [Tree('NNP', ['Nov.']), Tree('CD', ['29'])])])]), Tree('.', ['.'])]))
    Tree('S', [Tree('NP-SBJ', [('Pierre', 'NNP'), ('Vinken', 'NNP'), (',', ','), ('61', 'CD'), ('years', 'NNS'), ('old', 'JJ'), (',', ',')]), Tree('VP', [('will', 'MD'), ('join', 'VB'), ('the', 'DT'), ('board', 'NN'), ('as', 'IN'), ('a', 'DT'), ('nonexecutive', 'JJ'), ('director', 'NN'), ('Nov.', 'NNP'), ('29', 'CD')]), ('.', '.')])
    '''
    children = []

    for t in tree:
        if t.height() < 3:
            children.extend(t.pos())
        else:
            children.append(Tree(node_label(t), t.pos()))

    return Tree(node_label(tree), children)