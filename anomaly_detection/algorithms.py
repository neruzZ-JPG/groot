import numpy as np
import pandas as pd
from sklearn.cluster import Birch
from sklearn import preprocessing



def NSigmaAD(abnormal, normal, n=3):
    #abnormal = abnormal.rolling(window=6, min_periods=1).mean()
    #normal = normal.rolling(window=6, min_periods=1).mean()
    abnormal = np.asarray(abnormal)
    normal = np.asarray(normal)
    mean = np.mean(normal, axis=0)
    std = np.std(normal, axis=0)
    index = np.where((abnormal < mean - n * std) | (abnormal > mean + n * std))
    anomaly = len(index[0]) > 0
    return anomaly


def NsigmaAD2(data, n=3, pri=False):
    data = np.asarray(data)
    normal = data[:len(data) // 2]
    mean = np.mean(normal, axis=0)
    std = np.std(normal, axis=0)
    if pri:
        print(mean, std)
    abnormal = data[len(data) // 2:]
    index = np.where((abnormal < mean - n * std) | (abnormal > mean + n * std))
    return len(index[0]) > 0


def birch_ad_with_smoothing(metrics: pd.Series, threshold):
    metrics = metrics.rolling(window=6, min_periods=1).mean()
    x = np.array(metrics)
    x = np.where(np.isnan(x), 0, x)
    normalized_x = preprocessing.normalize([x])

    X = normalized_x.reshape(-1, 1)

    #            threshold = 0.05

    brc = Birch(branching_factor=50, n_clusters=None, threshold=threshold, compute_labels=True)
    brc.fit(X)
    brc.predict(X)

    labels = brc.labels_
    n_clusters = np.unique(labels).size
    return n_clusters > 1

