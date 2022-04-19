import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import dbscan
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from yellowbrick.cluster import SilhouetteVisualizer

plot = True

file = 'data5.csv'
data = np.asarray(pd.read_csv(file))
data2 = pd.read_csv(file)

if plot:
    plt.scatter(data[:,0], data[:, 1])
    plt.title(file)
    plt.show()

    sns.pairplot(data2)
    plt.show()



elbow_metrics = []
silhouette_metrics = []
ch_metrics = []
db_metrics = []
min = 2
max = 8
all_labels = []
for i in range(min,max):
    kmeans = KMeans(n_clusters=i, random_state=0).fit(data)
    labels = kmeans.labels_
    all_labels.append(labels)
    full_data = np.append(data, labels.reshape(-1,1), axis = 1)

    sse = kmeans.inertia_
    elbow_metrics.append(sse)

    silhouette = silhouette_score(data, labels)
    silhouette_metrics.append(silhouette)

    ch_score = calinski_harabasz_score(data, labels)
    ch_metrics.append(ch_score)

    db_score = davies_bouldin_score(data, labels)
    db_metrics.append(db_score)



print(labels)



fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(np.arange(min,max), elbow_metrics)
axs[0, 0].set_title('Elbow Metrics')
axs[0, 1].plot(np.arange(min, max), silhouette_metrics)
axs[0, 1].set_title('Silhouette Metrics')
axs[1, 0].plot(np.arange(min, max), ch_metrics)
axs[1, 0].set_title('Calinski Harabasz Metrics')
axs[1, 1].plot(np.arange(min, max), db_metrics)
axs[1, 1].set_title('Davies Bouldin Metrics')

plt.show()
plt.scatter(data[:, 0], data[:, 1], c = all_labels[2])
plt.show()
