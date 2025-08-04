import glob
from algorithms import *
import pandas as pd
import os
import numpy as np
import json

def anomaly_detection(normal_data, abnormal_data):
    
    # res = NSigmaAD(normal_data, abnormal_data)
    
    # res = NsigmaAD2(pd.concat([normal_data, abnormal_data]))
    
    res = birch_ad_with_smoothing(pd.concat([normal_data, abnormal_data]), 0.05)
    
    return res
    

def get_parent_folders(file_path):
    """
    获取文件的所有父文件夹名称
    """
    parent_folders = []
    current_path = os.path.dirname(file_path)
    while current_path != os.path.dirname(current_path):
        parent_folders.append(os.path.basename(current_path))
        current_path = os.path.dirname(current_path)
    return parent_folders[::-1]


def separate_fields(row):
    """
    分离行数据中的非数值字段和 metric 字段
    """
    non_numeric_fields = []
    metric_values = []
    for value in row:
        if isinstance(value, (int, float)):
            if np.isnan(value):
                # 若为 NaN，当作数值字段处理
                metric_values.append(value)
            else:
                metric_values.append(value)
        else:
            non_numeric_fields.append(value)
    return non_numeric_fields, metric_values


def process_csv_file(dir_path, csv_file):
    """
    处理单个 CSV 文件，返回每行数据的信息列表
    """
    parent_folders = get_parent_folders(os.path.relpath(csv_file, dir_path))
    df = pd.read_csv(csv_file, header=None)
    return [
        {
            'parent_folders': parent_folders,
            'non_numeric_fields': non_numeric_fields,
            'metric': metric_values
        }
        for _, row in df.iterrows()
        for non_numeric_fields, metric_values in [separate_fields(row)]
    ]


def combine_normal_abnormal(normal_dir, abnormal_dir):
    """
    合并 normal_dir 和 abnormal_dir 中的数据
    """
    all_data = []
    normal_csv_files = glob.glob(f"{normal_dir}/**/*.csv", recursive=True)
    for normal_csv_file in normal_csv_files:
        relative_path = os.path.relpath(normal_csv_file, normal_dir)
        abnormal_csv_file = os.path.join(abnormal_dir, relative_path)
        normal_rows = process_csv_file(normal_dir, normal_csv_file)
        if os.path.exists(abnormal_csv_file):
            abnormal_rows = process_csv_file(abnormal_dir, abnormal_csv_file)

        for normal_row, abnormal_row in zip(normal_rows, abnormal_rows):
            combined_row = {
                "metric_name": normal_csv_file.split("/")[-1].split('.')[0],
                "parent_folders": normal_row['parent_folders'],
                "non_numeric_fields": normal_row['non_numeric_fields'],
                "normal_metric": pd.Series(normal_row['metric']).fillna(1e-9),
                "abnormal_metric": pd.Series(abnormal_row['metric']).fillna(1e-9)
            }
            all_data.append(combined_row)
    return all_data


if __name__ == '__main__':
    normal_dir = "../datas/week2/normal"
    abnormal_dir = "../datas/week2/adservice_failure_long"


    combined_data = combine_normal_abnormal(normal_dir, abnormal_dir)
    abnormal_metrics = []
    for data in combined_data:
        # print(data["non_numeric_fields"])
        res = anomaly_detection(data['normal_metric'], data['abnormal_metric'])
        # print(res)
        if(res):
            print(data["parent_folders"], data["metric_name"], data["non_numeric_fields"], data["normal_metric"], data["abnormal_metric"])
            abnormal_metrics.append({
                "parent_folders": data["parent_folders"],
                "metric_name": data["metric_name"],
                "non_numeric_fields" : data["non_numeric_fields"]
            })
    with open("abnormal_metrics.json", "w") as f:
        json.dump(abnormal_metrics, f, indent=4)