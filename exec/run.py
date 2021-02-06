import argparse
from node2vec_mod.functions import read_into_nx_digraph, simulate_and_write_walks, learn_embeddings_from_text
from node2vec_mod.node2vec import Graph


def parse_args():
    '''
    Parses the node2vec arguments.
    '''

    parser = argparse.ArgumentParser(description="Run node2vec.")
    parser.add_argument('--input', nargs='?', default='../graph/karate.edgelist',
                        help='Input graph path')
    parser.add_argument('--output-walks', nargs='?', default='../graph/karate_walk.txt',
                        help='Output path for walks')
    parser.add_argument('--output-model', nargs='?', default='../emb/karate.model',
                        help='Output path for model')
    parser.add_argument('--dimensions', type=int, default=128,
                        help='Number of dimensions. Default is 128.')
    parser.add_argument('--walk-length', type=int, default=80,
                        help='Length of walk per source. Default is 80.')
    parser.add_argument('--num-walks', type=int, default=10,
                        help='Number of walks per source. Default is 10.')
    parser.add_argument('--window-size', type=int, default=10,
                        help='Context size for optimization. Default is 10.')
    parser.add_argument('--iter', default=1, type=int,
                        help='Number of epochs in SGD')
    parser.add_argument('--workers', type=int, default=4,
                        help='Number of parallel workers. Default is 4.')
    parser.add_argument('--p', type=float, default=1,
                        help='Return hyperparameter. Default is 1.')
    parser.add_argument('--q', type=float, default=1,
                        help='Inout hyperparameter. Default is 1.')
    parser.add_argument('--not-verbose', dest='verbose', action='store_false')
    parser.set_defaults(directed=True)
    return parser.parse_args()


def main(args):
    '''
    Pipeline for representational learning for all nodes in a graph.
    '''

    nx_G = read_into_nx_digraph(args.input)
    G = Graph(nx_G, True, args.p, args.q)
    G.preprocess_transition_probs()
    simulate_and_write_walks(G, args.num_walks, args.walk_length,
                             args.output_walks, args.verbose)
    learn_embeddings_from_text(args.output_walks, args.output_model, args.dimensions,
                               args.window_size, 0, 1, args.workers, args.iter)
if __name__ == "__main__":
    args = parse_args()
    main(args)
