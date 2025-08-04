from utils import *
import json
import networkx as nx

if __name__ == '__main__':
    new_metrics = []
    with open("../anomaly_detection/abnormal_metrics.json", "r") as f:
        metrics = json.load(f)
        for m in metrics:
            new_metrics.append(process_anomaly_metrics(m))
    with open("new_metrics.json", "w") as f:
        json.dump(new_metrics, f, indent=4)
    service_graph = nx.read_gml("../topology/service_topology.gml")
    span_graph = nx.read_gml("../topology/span_topology.gml")
    with open("rules.json", "r") as f:
        rules = json.load(f)
    event_graph = nx.DiGraph()
    for i in range(len(new_metrics)):
        for j in range(len(new_metrics)):
            if j == i:
                continue
            m1 = new_metrics[i]
            m2 = new_metrics[j]
            if check_relation(rules, service_graph, span_graph, m1, m2):
                def get_node_name(m):
                    name = m["service_name"] + ":" + m["metric_name"]
                    if "span_name" in m.keys():
                        name = name + ":" + m["span_name"]
                    return name
                event_graph.add_node(get_node_name(m1))
                event_graph.add_node(get_node_name(m2))
                event_graph.add_edge(get_node_name(m1), get_node_name(m2))
    print(len(event_graph.nodes))
    nx.write_gml(event_graph, "event_graph.gml")
    draw(event_graph, "event_graph.png")