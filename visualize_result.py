#!/usr/bin/env python3

"""
A function to visualize on a two-plane plot for all iteration
To decompose a n-dimensional data into 2-dimensional data
"""

from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from IPython.display import clear_output


def plot_clusters(data, labels, centroids, iteration):
    """
    A function to visualize on a two-plane plot for all iteration
    - PCA: decomposes a n-dimensional data into 2-dimensional data
    """
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(data)
    centroids_2d = pca.transform(centroids.T)
    clear_output(wait=True)
    plt.title(f"Iteration {iteration}")
    plt.scatter(x=data_2d[:, 0], y=data_2d[:, 1], c=labels)
    plt.scatter(x=centroids_2d[:, 0], y=centroids_2d[:, 1])
    plt.show()
