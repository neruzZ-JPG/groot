from prometheus_api_client import PrometheusConnect
from prometheus_api_client.utils import parse_datetime
import os
import json
import csv

config = {
    "prom_url" : "http://localhost:9090",
    "start_time" : parse_datetime("2025-03-22 00:00:00"),  # 从 24 小时前开始
    "end_time" : parse_datetime("2025-03-22 23:59:59"),  # 到现在结束
    "step" : '4m45s'  
}

metric_dir_path = "metrics"
servcie_metrics_path = metric_dir_path + "/" + "service_metrics.json"
span_metrics_path = metric_dir_path + "/" + "span_metrics.json"
job_metrics_path = metric_dir_path + "/" + "job_metrics.json"
bussiness_metrics_path = metric_dir_path + "/" + "bussiness_metrics.json"

def service_metrics_collect(metrics, config):
    # 连接到 Prometheus 服务器
    dir_path = "../data/service_metrics"
    # if not os.path.exists(dir_path)
    #     os.makedirs(dir_path)
    prom = PrometheusConnect(url=config["prom_url"], disable_ssl=True)
    for metric in metrics:
        dir_type_path = dir_path + "/" + metric["type"]
        dir_type_name_path = dir_type_path + "/" + metric["file_name"]
        if not os.path.exists(dir_type_path):
            os.makedirs(dir_type_path)
        # 构建自定义查询
        custom_query = metric["promql"]
        print(custom_query)
        result = prom.custom_query_range(
            query=custom_query,
            start_time=config["start_time"],
            end_time=config["end_time"],
            step=config["step"]
        )
        # 打印查询结果
        csv_file = open(dir_type_name_path + ".csv", 'w', newline='', encoding='utf-8')
        writer = csv.writer(csv_file)
        for metric in result:
            row = []
            service_name = metric['metric'].get('service_name', 'Unknown')
            #print(f"Service Name: {service_name}")
            row.append(service_name)
            for value in metric['values']:
                timestamp = value[0]
                value_data = value[1]
                #print(f"Timestamp: {timestamp}, Value: {value_data}")
                row.append(value_data)
            #print("-" * 50)
            writer.writerow(row)
        csv_file.close()
        
def span_metrics_collect(metrics, config):
    # 连接到 Prometheus 服务器
    dir_path = "../data/span_metrics"
    # if not os.path.exists(dir_path)
    #     os.makedirs(dir_path)
    prom = PrometheusConnect(url=config["prom_url"], disable_ssl=True)
    for metric in metrics:
        dir_type_path = dir_path + "/" + metric["type"]
        dir_type_name_path = dir_type_path + "/" + metric["file_name"]
        if not os.path.exists(dir_type_path):
            os.makedirs(dir_type_path)
        # 构建自定义查询
        custom_query = metric["promql"]
        print(custom_query)
        result = prom.custom_query_range(
            query=custom_query,
            start_time=config["start_time"],
            end_time=config["end_time"],
            step=config["step"]
        )
        # 打印查询结果
        csv_file = open(dir_type_name_path + ".csv", 'w', newline='', encoding='utf-8')
        writer = csv.writer(csv_file)
        for metric in result:
            row = []
            service_name = metric['metric'].get('service_name', 'Unknown')
            span_name = metric['metric'].get('span_name', 'Unknown')
            #print(f"Service Name: {service_name}")
            row.append(service_name)
            row.append(span_name)
            for value in metric['values']:
                timestamp = value[0]
                value_data = value[1]
                #print(f"Timestamp: {timestamp}, Value: {value_data}")
                row.append(value_data)
            #print("-" * 50)
            writer.writerow(row)
        csv_file.close()

def job_metrics_collect(metrics, config):
    # 连接到 Prometheus 服务器
    dir_path = "../data/job_metrics"
    # if not os.path.exists(dir_path)
    #     os.makedirs(dir_path)
    prom = PrometheusConnect(url=config["prom_url"], disable_ssl=True)
    for metric in metrics:
        dir_type_path = dir_path + "/" + metric["type"]
        dir_type_language_path = dir_type_path + "/" + metric["language"]
        dir_type_name_path = dir_type_language_path + "/" + metric["file_name"]
        if not os.path.exists(dir_type_language_path):
            os.makedirs(dir_type_language_path)
        # 构建自定义查询
        custom_query = metric["promql"]
        print(custom_query)
        result = prom.custom_query_range(
            query=custom_query,
            start_time=config["start_time"],
            end_time=config["end_time"],
            step=config["step"]
        )
        # 打印查询结果
        csv_file = open(dir_type_name_path + ".csv", 'w', newline='', encoding='utf-8')
        writer = csv.writer(csv_file)
        for metric in result:
            row = []
            job = metric['metric'].get('job', 'Unknown')
            #print(f"Service Name: {service_name}")
            row.append(job)
            for value in metric['values']:
                timestamp = value[0]
                value_data = value[1]
                #print(f"Timestamp: {timestamp}, Value: {value_data}")
                row.append(value_data)
            #print("-" * 50)
            writer.writerow(row)
        csv_file.close()

def bussiness_metrics_collect(metrics, config):
    # 连接到 Prometheus 服务器
    dir_path = "../data/business_metrics"
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    prom = PrometheusConnect(url=config["prom_url"], disable_ssl=True)
    for metric in metrics:
        dir_type_name_path = dir_path + "/" + metric["service"]
        # 构建自定义查询
        custom_query = metric["promql"]
        print(custom_query)
        result = prom.custom_query_range(
            query=custom_query,
            start_time=config["start_time"],
            end_time=config["end_time"],
            step=config["step"]
        )
        # 打印查询结果
        csv_file = open(dir_type_name_path + ".csv", 'w', newline='', encoding='utf-8')
        writer = csv.writer(csv_file)
        for metric in result:
            row = []
            job = metric['metric'].get('job', 'Unknown')
            #print(f"Service Name: {service_name}")
            row.append(job)
            for value in metric['values']:
                timestamp = value[0]
                value_data = value[1]
                #print(f"Timestamp: {timestamp}, Value: {value_data}")
                row.append(value_data)
            #print("-" * 50)
            writer.writerow(row)
        csv_file.close()

service_metrics = json.load(open(servcie_metrics_path, 'r'))
service_metrics_collect(service_metrics, config)
span_metrics = json.load(open(span_metrics_path, 'r'))
span_metrics_collect(span_metrics, config)
job_metrics = json.load(open(job_metrics_path, 'r'))
job_metrics_collect(job_metrics, config)
bussiness_metrics = json.load(open(bussiness_metrics_path, 'r'))
bussiness_metrics_collect(bussiness_metrics, config)