#Source: https://medium.com/analytics-vidhya/principal-component-analysis-pca-with-code-on-mnist-dataset-da7de0d07c22
import numpy as np
from scipy.linalg import eigh
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import time
import seaborn as sn
from sklearn import decomposition




data = pd.read_csv("train.csv")
data = data[0:1000]
labels = data.pop("label")
print(data.head())
standardized_data = StandardScaler().fit_transform(data)
print(standardized_data.shape)
#labels = data['label']



sample_data = standardized_data
print(sample_data.shape)
sample_data2 = data[1000:2000]
print(sample_data2.shape)
# matrix multiplication using numpy
covar_matrix = np.matmul(sample_data.T , sample_data)



# the parameter ‘eigvals’ is defined (low value to heigh value) 
# eigh function will return the eigen values in asending order
# this code generates only the top 2 (782 and 783)(index) eigenvalues.
values, vectors = eigh(covar_matrix, eigvals=(782,783))
print(f'Shape of eigen vectors = {vectors.shape}')
# converting the eigen vectors into (2,d) shape for easyness of further computations
vectors = vectors.T
print(f'Updated shape of eigen vectors = {vectors.shape}')
# here the vectors[1] represent the eigen vector corresponding 1st principal eigen vector
# here the vectors[0] represent the eigen vector corresponding 2nd principal eigen vector



new_coordinates = np.matmul(vectors, sample_data.T)


new_coordinates = np.vstack((new_coordinates, labels)).T
dataframe = pd.DataFrame(data=new_coordinates, columns=('1st_principal', '2nd_principal', 'label'))
print(dataframe.head())


sn.FacetGrid(dataframe, hue='label', size=6).map(plt.scatter, '1st_principal', '2nd_principal').add_legend()

plt.show()


pca = decomposition.PCA()
# PCA for dimensionality redcution (non-visualization)
pca.n_components = 784
pca_data = pca.fit_transform(sample_data)
percentage_var_explained = pca.explained_variance_ / np.sum(pca.explained_variance_)
cum_var_explained = np.cumsum(percentage_var_explained)


plt.figure(1, figsize=(6, 4))
plt.clf()
plt.plot(cum_var_explained, linewidth=2)
plt.axis('tight')
plt.grid()
plt.xlabel('n_components')
plt.ylabel('Cumulative_explained_variance')
plt.show()


