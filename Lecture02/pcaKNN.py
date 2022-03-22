
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from typing import List
import time




def plot2dMNIST(train_data: pd.DataFrame, labels: pd.DataFrame, size: int = 10, range: int = 4000, n_components: int = 2) -> None:
    '''
    Plots 2D representation of MNIST dataset using PCA and prints the explained variance ratio of the n_components.

    Args in: train_data - values/features for training data
             labels - labels for training data
             size - scatter plot point size
             range - number of points included from training_data
             n_components - number of components kept in the PCA
    Returns: None, plots the explained variance and prints values of explained variance in the PCA
    '''
    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(train_data)

    print(f'Explained variance ratio of the resulting {n_components} Principal Components: {pca.explained_variance_ratio_}')
    try:
        plt.scatter(pca_result[:range, 0], pca_result[:range, 1], c=labels[:range], edgecolor='none', alpha=0.5,
                cmap=plt.get_cmap('jet', 10), s=size)
        plt.colorbar()
        plt.title("2D representation of MNIST Dataset")
        plt.show()
    except:
        print(f'2D plot requires n_components = 2, current dimension is {n_components}.')

def plot_explained_variance(train_data: pd.DataFrame, plot_range: int = 300, sum_range: int = 10) -> None:
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




def run_PCA_kNN(X_train: pd.DataFrame, labels: pd.DataFrame,
                n_components: int = None, neighbours: List = [4, 5, 6, 7],
                components: List = [40, 45, 50, 55, 60]) -> None:
    '''
    PCA and kNN classifier. Lowers the dimensionality of the input data and performs kNN for a grid searched range
    specified by neighbours and components. If n_components is not passed, performs standard kNN.

    Args in: 
            X_train - dataframe of feature vectors
            labels - dataframe of labels
            n_components - number of principal components to use
            neighbours - list of values for the k neighbours used
            components - list of components to use from the PCA

    Returns:
            None
    '''

    if n_components:
        pca = PCA(n_components=n_components)
        print(f'Shape of data before PCA transform using {n_components} components:  {X_train.shape}')
        X_train = pca.fit_transform(X_train)
        print(f'Shape of data after PCA transform using {n_components} components:  {X_train.shape}')

    X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split( 
        X_train, labels, test_size=0.2, random_state=42)



    #Scores to keep track of grid searched performance
    scores_components = np.zeros( (components[len(components)-1]+1, neighbours[len(neighbours)-1]+1 ) )



    if n_components:
        for component in components:
            for n in neighbours:
                start_time = time.time()
                knn = KNeighborsClassifier(n_neighbors=n)
                knn.fit(X_train_pca[:,:component], y_train_pca)
                score = knn.score(X_test_pca[:,:component], y_test_pca)
 
                scores_components[component][n] = score
                
                print(f'Components = {component}, neighbors = {n}, Score = {score}')
                print(f'Execution time: {time.time() - start_time}') 
    else:
        scores = []
        for n in neighbours:
            start_time = time.time()
            knn = KNeighborsClassifier(n_neighbors=n)
            knn.fit(X_train_pca, y_train_pca)
            score = knn.score(X_test_pca, y_test_pca)
            scores.append(score)
            
            print(f'Components = FULL, neighbors = {n}, Score = {score}')
            print(f'Execution time: {time.time() - start_time}')



