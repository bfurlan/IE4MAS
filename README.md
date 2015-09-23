# IE4MAS
Information Extraction from Text for Multi-Agent Systems

A framework for Information Extraction from text, particularly Named Entity Recognition (NER) and Relationship Extraction (RE), which can be embedded in multi-agent systems.

Supports 3 NER modules: 

- Maximum Entropy Chunker from Natural Language Toolkit (NLTK) 
(http://www.nltk.org/)

- Conditional Random Fields from StanfordCoreNLP 
(http://nlp.stanford.edu/software/CRF-NER.shtml)

- Structured Support Vector Machines from MIT Information Extraction 
(https://github.com/mit-nlp/MITIE)

Also, the framework includes Relationship Extraction module that can extract several types of binary relationships from sentences. 
The relationship extraction is based on identified named entities from NER modules. 

Information extracted from text (named entities and relationships) are converted to Datalog facts. 

Finally, in order to support evaluation of various experiments, the framework includes a package named IE aggregator. 
This module aggregates results gathered from IE agents and enables evaluation over the CoNLL-2003 dataset.

