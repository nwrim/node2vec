import networkx as nx
from node2vec_mod import node2vec
import random
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


def read_into_nx_digraph(text_directory):
    digraph = nx.DiGraph()
    with open(text_directory, 'r') as f:
        for line in f:
            l = line.split()
            digraph.add_edge(l[0], l[1])
    for edge in digraph.edges():
        digraph[edge[0]][edge[1]]['weight'] = 1
    return digraph


def simulate_and_write_walks(G, num_walks, walk_length, output_directory,
                             verbose=True):
    '''
    Repeatedly simulate random walks from each node.
    '''

    nodes = list(G.G.nodes())
    if verbose:
        print('Walk iteration:')
    with open(output_directory, 'w') as f:
        for walk_iter in range(num_walks):
            if verbose:
                print(str(walk_iter + 1), '/', str(num_walks))
            random.shuffle(nodes)
            for node in nodes:
                f.write(' '.join(G.node2vec_walk(walk_length=walk_length,
                                                 start_node=node)) + '\n')


def learn_embeddings_from_text(text_directory, out_directory, size=100, window=5,
                               min_count=5, sg=0, workers=3, iter_=5, seed=1):
    '''
    Learn embeddings by optimizing the Skipgram objective using SGD.
    '''

    model = Word2Vec(sentences=LineSentence(text_directory), size=size,
                     window=window, min_count=min_count, sg=sg, workers=workers,
                     iter=iter_, seed=seed)
    model.save(out_directory)
