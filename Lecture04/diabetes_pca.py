import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.pipeline import make_pipeline
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns

from sklearn.preprocessing import StandardScaler


diabetes_data = load_diabetes()

features = diabetes_data.data
labels = diabetes_data.target
print(features.shape)

#print(features)
features = StandardScaler().fit_transform(features)
#print(features)
#print(features.shape)

pca = PCA(n_components = 6)

#features = pca.fit_transform(features)

#print(features.shape)


#plt.scatter(features[:,0], features[:,1], c = labels)
#plt.plot(np.cumsum(pca.explained_variance_ratio_))
#print(pca.explained_variance_ratio_)
#plt.show()