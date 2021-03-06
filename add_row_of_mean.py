import pandas as pd
import numpy as np

dataset = pd.read_csv('csv/data_all.csv')

count = 0
avg = 0
indexes = dataset.columns
mean_vector_load = []
vector_of_mean = []
matrix_of_cos_sim = np.matrix
for i in range(len(indexes)-2):
    avg = 0
    count = 0
    mean_vector_load = dataset.iloc[:, i+2].values
    if i % 5 == 1:
        matrix_of_cos_sim = np.vstack(matrix_of_cos_sim, mean_vector_load)

    for j in range(len(mean_vector_load)):
        if int(mean_vector_load[j]) < 1:
            avg += mean_vector_load[j]
            count += 1
        elif i % 5 != 1:
            avg += mean_vector_load[j]
            count += 1
    avg = avg/count
    vector_of_mean.append(avg)

fst_two_columns = [999999, 'Mario Rossi']

for val in vector_of_mean:
    fst_two_columns.append(val)

df_fst_cl = pd.DataFrame(fst_two_columns)

df_fst_cl.index = indexes.to_list()

df_fst_cl.append(dataset)

df_fst_cl = df_fst_cl.transpose()

df_fst_cl.to_csv('mean.csv', index=False)

df_fst_cl.append(dataset).to_csv('csv/data_all_with_mean.csv', index=False)
