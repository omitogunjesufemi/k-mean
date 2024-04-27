#!/usr/bin/env python3
"""
"""
from k_mean_algorithm import k_mean_algorithm
from data_entry import read_data, scale_data


def main(file_name, features, k, iterations):
    """
    """
    players = read_data(file_name, features)
    
    data = scale_data(csv_data=players, features=features)

    centroids, labels = k_mean_algorithm(data, k, iterations)
    
    print(centroids)

    print(players[labels == 4][['short_name'] + features])
    
    return (centroids, labels)
