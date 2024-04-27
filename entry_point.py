#!/usr/bin/env python3
"""
"""
from k_mean_algorithm import k_mean_algorithm
from data_entry import get_data

file_name = "../../Downloads/fifa_dataset/archive/players_22.csv"

features = ["overall", "potential", "wage_eur", "value_eur", "age"]

data = get_data(file_name, features)

k_mean_algorithm(data, 5, 100)
