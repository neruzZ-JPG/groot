import networkx as nx
import pandas as pd
import os
from matplotlib import pyplot as plt


def group_csv_by_traceid(csv_file):
    """
    按 traceID 分组 CSV 数据（使用 pandas）

    参数:
    csv_file (str): CSV 文件路径

    返回:
    dict: {traceID: DataFrame, ...}
    """
    # 读取 CSV 文件
    df = pd.read_csv(csv_file)
    
    # 按 traceID 分组
    grouped = df.groupby('traceID').apply(lambda x: x.reset_index(drop=True)).groupby(level=0)
    
    # 转换为字典：{traceID: DataFrame}
    trace_groups = {name: group for name, group in grouped}
    
    return trace_groups

def dfs(G, trace, parent_span, span):
    import pandas as pd

def dfs(G, trace, parent_span, span):
    # 确保 parentSpanID 列和 span["spanID"] 的数据类型一致
    trace["parentSpanID"] = trace["parentSpanID"].astype(str)
    span["spanID"] = str(span["spanID"])
    if parent_span is not None:
        G.add_edge(get_node_name(parent_span), get_node_name(span))
    # 筛选出 parentSpanID 等于当前 spanID 的行
    next_spans = trace[trace["parentSpanID"] == span["spanID"]]
    # 筛选出 parentSpanID 等于当前 spanID 的行
    next_spans = trace[trace["parentSpanID"] == span["spanID"]]
    # print("筛选结果：")
    # print(next_spans)
    # print("筛选结果的索引：", next_spans.index)
    
    # 重置索引
    next_spans = next_spans.reset_index(drop=True)
    
    if not next_spans.empty:
        # 如果筛选结果不为空，遍历每一行
        for _, row in next_spans.iterrows():
            # 添加边到图中
            if parent_span is not None:
                G.add_edge(get_node_name(parent_span), get_node_name(span))
            # 递归调用 dfs 函数
            dfs(G, trace, span, row)

def get_node_name(span):
    method = str(span["operationName"])
    prefix = str(span["serviceName"])
    return prefix + ":" + method

def get_span_topology(dir_name):
    G = nx.DiGraph()
# 遍历当前目录下的所有文件
    for _, dirs, _ in os.walk(dir_name):
        for dir in dirs:
            for _, _, files in os.walk(dir_name + "/" + dir):
                for file in files:
                    file_path = os.path.join(dir_name, dir,  file)
                    print(file_path)
                    traces = group_csv_by_traceid(file_path)
                    for trace in traces.values():
                        #print(trace)
                        try:
                            root_span = trace[trace["parentSpanID"].isna()].iloc[0]
                            dfs(G, trace, None, root_span)
                        except:
                            print(trace)
                        # print(root_span)
    return G
                
def draw(G: nx.DiGraph):
    plt.figure(figsize=(20, 16))
    nx.draw(G, pos=nx.spring_layout(G), with_labels=True)
    plt.savefig("span_topology.png")

if __name__ == '__main__':
    G = get_span_topology("../trace_data")
    draw(G)
    print(G.nodes)
    print("G has " + str(len(G.nodes)) + " nodes")
    nx.write_gml(G, "span_topology.gml")