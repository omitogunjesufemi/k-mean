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
    
    print()
    print("-------------------------------------")
    print()
    
    print("Centroids:")
    print(centroids)
    
    print()
    print("-------------------------------------")
    print()
    
    print("Players in Cluster 0")
    print(players[labels == 0][['short_name'] + features])
    
    print()
    print("-------------------------------------")
    print()
    
    print("Players in Cluster 1")
    print(players[labels == 1][['short_name'] + features])
    
    print()
    print("-------------------------------------")
    print()
    
    print("Players in Cluster 2")
    print(players[labels == 2][['short_name'] + features])
    
    print()
    print("-------------------------------------")
    print()
    
    print("Players in Cluster 3")
    print(players[labels == 3][['short_name'] + features])
    
    print()
    print("-------------------------------------")
    print()
    
    print("Players in Cluster 4")
    print(players[labels == 4][['short_name'] + features])
    
    print()
    print("-------------------------------------")
    print()
    
    return (centroids, labels)
