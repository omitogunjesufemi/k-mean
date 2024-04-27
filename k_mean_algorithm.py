#!/usr/bin/env python3
"""
"""
import pandas as pd
from k_mean_functions import random_centroids, get_labels, new_centroids
from visualize_result import plot_clusters


def k_mean_algorithm(data, k, max_iterations):
    """
    Pseudocode:
    1. Scale data to standardize values
    2. Initialize random centroids
    3. Get labels for each data point
    4. Create new centroids
    5. Plot the centroids
    6. Repeat 3-5 until the centroids stop   changing
    
    Args:
    - data: The data set for clustering
    - max_iterations: number of time the algorithm will iterate
    - k: number of clusters
    """

    centroids = random_centroids(data, k)
    old_centroids = pd.DataFrame()
    iteration = 1

    while iteration < max_iterations and not centroids.equals(old_centroids):
        old_centroids = centroids
        labels = get_labels(data, centroids)
        centroids = new_centroids(data, labels)
        #plot_clusters(data, labels, centroids, iteration, False)
        iteration += 1

    plot_clusters(data, labels, centroids, iteration, True)
    
    return centroids, labels