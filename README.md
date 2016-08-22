# n-gram
n-gram language models for information retrieval/document
comparison tasks. In development. 
Requires the SRI Language Modeling Toolkit.

Attempts cross-corpus document comparsion in an information retrieval
framework. Corpus 1 is a set of statistics arxiv papers from 2016. 
Corpus 2 is a set of wikipedia articles, in mathematics and statistics.
Corpus 1 serves as the 'query', Corpus 2 is searched over.

A probabilistic language model is trained on each wikipedia article in Corpus 2.
We assume that a wikipedia article generated an arxiv paper, and 
rank the search results based on this probability.
P(q|M)
q: query
M: language model
