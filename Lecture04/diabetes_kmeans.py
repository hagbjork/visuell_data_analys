import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd


import seaborn as sns


data = pd.read_csv("diabetes.csv")

labels = data.pop("Outcome")
print(labels)


print(data.head())
#Normalisera datasetet
data = (data-data.mean())/data.std()

#Analysera distribution

distributions = {}

for lab in labels:
    if lab not in distributions:
        distributions[lab] = 1
    else:
        distributions[lab] += 1
print(distributions)

kmeans = KMeans(n_clusters=3, random_state=0).fit(data)

print(kmeans.labels_)

sse = []
for i in range(10):
    kmeans = KMeans(n_clusters = i + 1, random_state = 0).fit(data)
    sse.append(kmeans.inertia_)

#Få ut klustercenter
print(kmeans.cluster_centers_)
plt.plot(1 + np.arange(len(sse)), sse)
plt.show()


#Silhouette score: (b_i - a_i)/max(a_i,b_i)  där a_i är mean distance från alla datapunkter i samma 
silhouette_scores = []
for i in range(10):
    kmeans = KMeans(n_clusters = i + 2, random_state = 0).fit(data)
    predicted_labels = kmeans.labels_
    #print(predicted_labels)
    silhouette_scores.append(metrics.silhouette_score(data, predicted_labels))

print(silhouette_scores)