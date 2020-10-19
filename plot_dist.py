import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('csv/data_all.csv')
matrix_of_cos_sim = np.matrix
indexes = dataset.columns

for i in range(len(indexes)-2):
    if i % 5 == 1:
        mean_vector_load = dataset.iloc[:, i+2].values
        mean_vector_load = -np.sort(-mean_vector_load)
        mean_vector_load = np.delete(mean_vector_load, np.where(mean_vector_load == 99))
        mean_vector_load = np.delete(mean_vector_load, np.where(mean_vector_load == 98))
        mean_vector_load = np.delete(mean_vector_load, np.where(mean_vector_load == 97))
        #matrix_of_cos_sim = np.vstack([matrix_of_cos_sim, mean_vector_load])
        plt.plot(mean_vector_load, label = indexes[i+2])
        plt.legend(loc='upper right')
        plt.ylabel('Distributions of cosine similarity')

plt.show()
