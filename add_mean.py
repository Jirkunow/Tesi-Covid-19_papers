import pandas as pd
import numpy as np

dataset = pd.read_csv('csv/data_all.csv')

count = 0
avg = 0
indexes = dataset.head()
mean_vector_load = []
vector_of_mean = []

for i in range(len(indexes)-2):
    mean_vector_load = dataset.iloc[j+2,i]
    for j in  range(len(mean_vector_load)):
        if mean_vector_load[j + 2 , i] > 0 and j+2%5 != 2:
            avg = mean_vector_load[j + 2 , i]
            count += 1;
        elif j+2%5 != 2:
            avg = mean_vector_load[j + 2, i]
            count += 1;
    avg = avg/count
    vector_of_mean[j] = avg

vector_of_mean.to_csv('csv/data_all.csv', mode='a', header=False)
