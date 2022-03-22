import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn import metrics
import seaborn as sns
import pandas as pd
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score



def run_PCA(features: pd.DataFrame, sum_range: int = 5):
    '''
    Plots cumulated sums of explained variance for the data and prints the cumulated sum of explained variance for the sum_range
    first principal components.
    '''
    
    pca = PCA()
    pca_full = pca.fit(features)

    print(f'Sum of the 10 most important features:{sum(pca_full.explained_variance_ratio_[:sum_range])}')

    plt.plot(np.cumsum(pca_full.explained_variance_ratio_))
    plt.xlabel('# of components')
    plt.ylabel('Cumulative explained variance')
    plt.title("Amount of total variance included in the principal components")
    plt.show()

def run_DBSCAN(features:pd.DataFrame, params: dict, plot: bool = True):
    '''
    Performs DBSCAN on provided DataFrame with grid_searched hyperparameters epsilon and number of core points.

    Args in: features - full dataset of features to cluster.
             params - parameters to use for grid search ranges.
    Returns:
            dictionary of grid searched results
    '''
    samples, dimension = features.shape
    eps_min = params["eps_min"]
    eps_max = params["eps_max"]
    eps_range = eps_max - eps_min
    eps_step = params["eps_step"]
    point_max = dimension*params["point_max"]
    point_min = dimension*params["point_min"]
    point_range = point_max - point_min

    heat_map = np.zeros((point_range,eps_range))
    results = {}
    #Sätt startvärde till värsta tänkbara för silhouette och DBI
    best_silhouette = -1
    best_dbi = np.inf
    #Grid search för olika hyperparametrar
    for i in range(point_min,point_max):
        for k in range(eps_min, eps_max):
            clustering = DBSCAN(eps=eps_step*k, min_samples=i).fit(features)
            n_clusters = len(set(clustering.labels_))
            heat_map[i - point_min][k - eps_min] = n_clusters

            results[(i,k)] = {"eps": 0.05*k,"n_clusters": n_clusters,"labels":clustering.labels_, 
            "Core indices":clustering.core_sample_indices_}

            features['labels'] = clustering.labels_

            reduced_features = features[features['labels'] != -1]
            reduced_labels = reduced_features.pop('labels')
            

            
            if len(set(reduced_labels)) > 1:
                #Ifall vi har 1 typ av label har en av två saker skett - antingen har vi ett enda sammanhängande kluster, eller så 
                #har allting kategoriserats som brus.
                s_score = silhouette_score(reduced_features, reduced_labels)
                dbi_score = davies_bouldin_score(reduced_features, reduced_labels)
                if s_score > best_silhouette:
                    best_silhouette = s_score
                    print(f"Best silhouette score ({s_score}) found for {n_clusters} clusters, epsilon = {eps_step}*{k}, min_point = {i}." )
                    print(f"Percentage of data clustered: {len(reduced_labels)/features.shape[0]}")
                if dbi_score < best_dbi:
                    best_dbi = dbi_score
                    print(f"Best DBI score ({dbi_score}) found for {n_clusters} clusters, epsilon = {eps_step}*{k}, min_point = {i}." )
                    print(f"Percentage of data clustered: {len(reduced_labels)/features.shape[0]}")
    print(f"Best DBI :{best_dbi}")
    print(f"Best Silhoeutte: {best_silhouette}")
    if plot:
        ax = sns.heatmap(heat_map, annot = False, xticklabels= np.arange(eps_min, eps_max), yticklabels=np.arange(point_min, point_max))
        ax.set_xlabel("epsilon")
        ax.set_ylabel("Number of core points")
    plt.show()

    return results

def main():

    diabetes_data = pd.read_csv("diabetes.csv")
    sns.pairplot(diabetes_data, hue = 'Outcome')
    plt.show()
    labels = diabetes_data.pop("Outcome")
    features = diabetes_data

    #Normalisering
    features = (features-features.mean())/features.std()
    print(features.head())
    features['Outcome'] = labels
    sns.pairplot(features, hue = 'Outcome')
    plt.show()

    features.pop('Outcome')


    run_PCA(features)

    params = {"eps_min": 10, "eps_max":50, "eps_step": 0.05, "point_max":2, "point_min":1}
    grid_search_results = run_DBSCAN(features = features, params = params, plot = True)

if __name__ == "__main__":
    main()








