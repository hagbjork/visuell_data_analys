import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
from sklearn.metrics import davies_bouldin_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from yellowbrick.cluster import SilhouetteVisualizer

verbose = False
plot = False
file = 'mystery_data4.csv'
data = np.asarray(pd.read_csv(file))
data2 = pd.read_csv(file)

if plot:
    sns.pairplot(data2)
    plt.title(file)
    plt.show()
    
    plt.matshow(data2.corr())
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16)

    plt.show()




def plot_explained_variance(train_data: pd.DataFrame, plot_range: int = 300, sum_range: int = 5) -> None:
    '''
    Plots the explained_variance for the range of 
    Args in: train_data - data to fit PCA
             plot_range - number of principal components to include in the sum of explained variances
             sum_range - number of principal compontens explained variances to sum and print
    Returns: None
    '''
    pca = PCA(plot_range)
    pca_full = pca.fit(train_data)

    print(f'Sum of the 10 most important features:{sum(pca_full.explained_variance_ratio_[:sum_range])}')

    plt.plot(np.cumsum(pca_full.explained_variance_ratio_))
    plt.xlabel('# of components')
    plt.ylabel('Cumulative explained variance')
    plt.title("Amount of total variance included in the principal components")
    plt.show()


plot_explained_variance(data2, plot_range = 5)

pca = PCA(n_components=2)
print(f"Data shape before fit and transform: {data.shape}")
transformed_data = pca.fit_transform(data)

print(f"Data shape after fit and transform: {transformed_data.shape}")


silhouette_metrics = []
ch_metrics = []
db_metrics = []
min = 2
max = 8
all_labels = []
# #Måste göra om från att ansätta antal kluster till att testa olika parameterkombinationer för
#epsilon och min_points
eps_min = 0.3
eps_max = 3
core_point_min = 2
core_point_max = 10
eps_range = np.linspace(eps_min, eps_max, num = 30)
core_points = np.arange(core_point_min, core_point_max)
for eps in eps_range:
    silhouette_row = []
    ch_row = []
    db_row = []
    for core_point in core_points:

        clustering = DBSCAN(eps=eps, min_samples=core_point).fit(transformed_data)
        labels = clustering.labels_
        
        #Vi måste ha åtminstone 1 kluster + noise
        if len(set(labels)) > 1:
            if verbose: 
                print(f"Number of clusters (excluding noise): {len(set(labels)) - 1}")
            percentage_data_importance = 1
            all_labels.append(labels)
            #full_data = np.append(transformed_data, labels.reshape(-1,1), axis = 1)

            #Håll koll på hur stor andel utav datan som faktiskt är klustrad
            new_labels = [0 if lab == -1 else 1 for lab in labels]
            
            percentage_data = sum(new_labels)/len(labels)

            #Viktning med avseende på andel data som är klustrad:
            silhouette = silhouette_score(transformed_data, labels)*percentage_data**percentage_data_importance

            ch_score = calinski_harabasz_score(transformed_data, labels)*percentage_data**percentage_data_importance

            #
            db_score = davies_bouldin_score(transformed_data, labels)/(percentage_data**percentage_data_importance)



            #print(f"Percentage of data points included: {percentage_data}")
            silhouette_row.append(silhouette)
            ch_row.append(ch_score)
            db_row.append(db_score)
        else:
            silhouette_row.append(-1)
            ch_row.append(0)
            db_row.append(10)
    
    silhouette_metrics.append(silhouette_row)
    ch_metrics.append(ch_row)
    db_metrics.append(db_row)




ch_metrics = np.asarray(ch_metrics)
silhouette_metrics = np.asarray(silhouette_metrics)
db_metrics = np.asarray(db_metrics)

print(ch_metrics.shape)
print(silhouette_metrics.shape)
print(db_metrics.shape)


metrics = [ch_metrics, silhouette_metrics, db_metrics, db_metrics]
titles = ["Calinski Harabaz", "Silhouette", "Davies Bouldin", "Davies Bouldin"]
fig, axn = plt.subplots(2,2)
for i, ax in enumerate(axn.flat):
    sns.heatmap(metrics[i], ax = ax)
    ax.set_title(titles[i])

plt.show()



#Vi ser från våra heatmaps att sista värdet i eps_range och första värdet i core_points
#är bra kandidater
eps = eps_range[-1]

core_point = core_points[0]

clustering = DBSCAN(eps=eps, min_samples=core_point).fit(transformed_data)
labels = clustering.labels_


df = pd.DataFrame(data)

df["Labels"] = labels
sns.pairplot(df, hue = 'Labels')
plt.title(file)
plt.show()




