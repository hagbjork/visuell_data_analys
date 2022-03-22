import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from umap import UMAP
from palmerpenguins import load_penguins

data = sns.load_dataset("penguins")

#Datainspektion
print(data.head())
sns.pairplot(data, hue = "species")
plt.show()
sns.jointplot(data = data, x = "bill_length_mm", y = "bill_depth_mm", hue = "species", kind = "kde")
plt.show()


print(f"Shape of data before dropping NA: {data.shape}")
data = data.dropna()
print(f"Shape of data after dropping NA: {data.shape}")


labels = data.pop("species")

#Vi exkluderar islands då vi har fler än 2 kategoriska variabler
print(f"Unique islands: {len(set(data['island']))}")
data.pop('island')


#Encoder till kategorisk variabel sex
sex_encoder = LabelEncoder().fit(data['sex'])


#Applicera sex_encoder för att få numerisk data
data['sex'] = sex_encoder.transform(data['sex'])



#Utred scores för onormaliserad data
sse = []
silhouette = []
min_clusters = 2
max_clusters = 10
for i in range(min_clusters,max_clusters):
    kmeans = KMeans(n_clusters = i).fit(data)
    sse.append(kmeans.inertia_)
    silhouette.append(silhouette_score(data, kmeans.labels_))

print(f"Silhouette scores: {silhouette}")
plt.plot(np.arange(min_clusters, max_clusters), sse)
plt.title("SSE/Clust graph")
plt.xlabel("Number of clusters")
plt.ylabel("Sum of inertia")
plt.show()


#Normalisera data
data = (data-data.mean())/data.std()

#... och gör igen. Spara bästa inställningar baserat på silhouette score. Jämför med plot med elbow rule.
sse = []
silhouette = []
min_clusters = 2
max_clusters = 10

best_silhouette = -1
best_settings_silhouette = None
for i in range(min_clusters,max_clusters):
    kmeans = KMeans(n_clusters = i).fit(data)
    sse.append(kmeans.inertia_)
    silhouette_score_ = silhouette_score(data, kmeans.labels_)
    silhouette.append(silhouette_score_)

    if silhouette_score_ > best_silhouette:
        best_settings_silhouette = {"Clusters": i, "Score": silhouette_score_, "Centers": kmeans.cluster_centers_}
        best_silhouette = silhouette_score_

print(f"Silhouette scores: {silhouette}")

plt.plot(np.arange(min_clusters, max_clusters), sse)
plt.title("SSE/Clust graph")
plt.xlabel("Number of clusters")
plt.ylabel("Sum of inertia")
plt.show()

print(data.head())

print(list(best_settings_silhouette.values()))

#Silhouette score och eventuellt elbow rule tyder på 6 kluster. Kanske 3 species * n_sex? 