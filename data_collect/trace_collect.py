import requests
from datetime import datetime, timezone
import json
import csv
import os

def get_current_timestamp_microseconds():
    """获取当前 UTC 时间的微秒级时间戳"""
    now = datetime.now(timezone.utc)
    return int(now.timestamp() * 1e6)  # 转换为微秒

service_names = [
    "currencyservice","loadgenerator","accountingservice","frontendproxy",
    "cartservice","quoteservice","paymentservice","productcatalogservice",
    "recommendationservice","flagd","emailservice","checkoutservice",
    "frontend-web","imageprovider","adservice","frauddetectionservice",
    "shippingservice","jaeger-all-in-one","frontend"
]
# service_names = [
#     "quoteservice"
# ]

config = {
    "JAEGER_QUERY_URL" : "http://localhost:8080/jaeger/ui/api/traces",
    "start_time" : get_current_timestamp_microseconds() - 60 * 60 * 1000 * 1000,  # 过去 60 分钟
    "end_time" : get_current_timestamp_microseconds(),
    "limit" : 100
}


def get_traces(service_name, config):
    """
    从 Jaeger 拉取追踪数据

    :param service_name: 服务名
    :param start_time: 开始时间（毫秒），可选
    :param end_time: 结束时间（毫秒），可选
    :param limit: 要返回的追踪数量，默认为 10
    :return: 追踪数据的 JSON 响应
    """
    JAEGER_QUERY_URL = config["JAEGER_QUERY_URL"]
    start_time = config["start_time"]
    end_time = config["end_time"]
    limit = config["limit"]
    params = {
        "service": service_name,
        "limit": limit
    }

    if start_time:
        params["start"] = start_time
    if end_time:
        params["end"] = end_time

    try:
        response = requests.get(JAEGER_QUERY_URL, params=params)
        response.raise_for_status()  # 检查请求是否成功
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求出错: {e}")
        return None

def process_trace(trace):
    """
    处理单个 trace 数据，提取所需的信息
    :param trace: 单个 trace 的数据
    :return: 包含所需信息的列表
    """
    result = []
    if not isinstance(trace, dict) or 'spans' not in trace or 'processes' not in trace:
        return result

    processes = trace['processes']
    for span in trace['spans']:
        process_id = span.get('processID')
        service_name = processes.get(process_id, {}).get('serviceName')

        span_info = {
            "traceID": span.get("traceID"),
            "spanID": span.get("spanID"),
            "parentSpanID": next((ref.get("spanID") for ref in span.get("references", []) if ref.get("refType") == "CHILD_OF"), None),
            "operationName": span.get("operationName"),
            "serviceName": service_name
        }
        result.append(span_info)

    return result


if __name__ == "__main__":
    # 示例用法
    trace_dir = "../trace_data/3"
    if not os.path.exists(trace_dir):
        os.makedirs(trace_dir)
    for service_name in service_names:
        csv_file = open(trace_dir + "/" + service_name + ".csv", 'w', newline='', encoding='utf-8')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["traceID", "spanID", "parentSpanID", "operationName", "serviceName"])
        traces = get_traces(service_name, config)
        if traces:
            for trace in traces['data']:
                res = process_trace(trace)
                for re in res:
                    csv_writer.writerow([re["traceID"], re["spanID"], re["parentSpanID"], re["operationName"], re["serviceName"]])
        csv_file.close()