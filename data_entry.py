#!/usr/bin/env python3
import pandas as pd


def get_data(file_name, features):
    """
    """
    csv_data_point = pd.read_csv(file_name)
    csv_data_point = csv_data_point.dropna(subset=features)
    data = csv_data_point[features].copy()
    """
    Scaling of the data [since it is a real life dataset] since sthere would
    be values that would have a very large difference between them
    Hence, we scale the data in the range of 1 - 10, so that no one column
    dominate another in the clusters.
    min-max scaling is used here
    """
    data = (((data - data.min()) / (data.max() - data.min())) * 9) + 1

    return (data)
