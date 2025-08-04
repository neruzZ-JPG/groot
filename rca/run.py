import networkx as nx
import json

def pagerank(G, personalization):
    pagerank_scores = nx.pagerank(G ,max_iter=100, personalization=personalization)
    return pagerank_scores

def sort_and_dump_scores(score_dict, output_file):
    sorted_items = sorted(score_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {}
    rank = 1
    for node, score in sorted_items:
        sorted_dict[node] = {
            'score': score,
            'rank': rank
        }
        rank += 1
    with open(output_file, 'w') as f:
        json.dump(sorted_dict, f, indent=4)

if __name__ == '__main__':
    G = nx.read_gml("../event_graph/event_graph.gml")
    ### personalization:
    ### 1 for dangling nodes(leave nodes)
    ### 0.5 for other nodes
    out_degree_zero_nodes = [node for node, out_degree in G.out_degree() if out_degree == 0]
    personalization = {node: 1 for node in out_degree_zero_nodes}
    for node in G.nodes():
        if node not in personalization.keys():
            personalization[node] = 0.5
    pagerank_scores = pagerank(G, personalization)
    sort_and_dump_scores(pagerank_scores, "pagerank_scores.json")