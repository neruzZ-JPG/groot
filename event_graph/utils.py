import networkx as nx
from matplotlib import pyplot as plt

def process_anomaly_metrics(metrics):
    new_metrics = {}
    new_metrics["service_name"] = metrics["non_numeric_fields"][0]
    if len(new_metrics["service_name"].split("/")) > 1:
        new_metrics["service_name"] = new_metrics["service_name"].split("/")[1]
    new_metrics["type"] = metrics["parent_folders"][0]
    # service_metric
    if new_metrics["type"] == "service_metrics":
        new_metrics["metric_name"] = metrics["parent_folders"][1] + " & " + metrics["metric_name"]
    # span_metric
    if new_metrics["type"] == "span_metrics":
        new_metrics["metric_name"] = metrics["parent_folders"][1] + " & " +  metrics["metric_name"]
        new_metrics["span_name"] = metrics["non_numeric_fields"][1]
    # job_metric
    if new_metrics["type"] == "job_metrics":
        new_metrics["metric_name"] = metrics["parent_folders"][1] + " & " + metrics["parent_folders"][2] + " & " + metrics["metric_name"]
    # bussiness_metric
    if new_metrics["type"] == "business_metrics":
        new_metrics["metric_name"] = "bussiness_" + " & " + metrics["metric_name"]
    return new_metrics


def check_relation(rules, service_graph, span_graph, metric1, metric2):
    for rule in rules:
        if rule["SourceType"] == metric1["type"] and rule["TargetType"] == metric2["type"]:
            if rule["condition"] == "same_service" and metric1["service_name"] == metric2["service_name"]:
                return True
            if rule["condition"] == "in_service_graph":
                if service_graph.has_edge(metric1["service_name"], metric2["service_name"]):
                    return True
            if rule["condition"] == "in_span_graph":
                def get_node_name(m):
                    return m["service_name"] + ":" + m["span_name"]
                if span_graph.has_edge(get_node_name(metric1), get_node_name(metric2)):
                    return True
    print(metric1, metric2)
    return False

def draw(G: nx.DiGraph, path: str):
    plt.figure(figsize=(20, 16))
    nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
    plt.savefig(path)