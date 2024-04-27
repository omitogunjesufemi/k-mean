#!/usr/bin/env python3
"""
This module contain the functions for the algorithms
"""

import numpy as np
import pandas as pd


def random_centroids(data, k):
    """
    Calculating the initial centroids to be used for
    clustering
    """
    centroids = []
    for i in range(k):
        centroid = data.apply(lambda x: float(x.sample()))
        centroids.append(centroid)
    return pd.concat(centroids, axis=1)


def get_labels(data, centroids):
    """
    Calculating the Euclidean Distance to get the best position for
    the centroids and get a better clustering

    - The distances represent the collection distance from each datapoint
      to a particular cluster

    - We can figure out which cluster a data-point is in (i.e)
      the cluster with the shortest distance to the data-point

    - The cluster will be the label for the data-point
    """
    distances = centroids.apply(lambda x: np.sqrt((((data - x) ** 2)).sum(axis=1)))
    return distances.idxmin(axis=1)


def new_centroids(data, labels):
    """
    The get_label() assign data-point to a certain cluster of random centroid

    This function update the centroids based on proximity to the center.
    It finds all the points in the cluster, and then take the geometric mean
    for each feature

    This geometric mean gives us a new centroid for each cluster
    """
    return data.groupby(labels).apply(lambda x: np.exp(np.log(x).mean())).T
