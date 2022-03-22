import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from umap import UMAP
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score


data = load_wine()


labels = data.target
features = data.data


def run_SVM(features, labels, k):
    """
    Performs SVM on 
    """
    results = []
    best_result = -1
    best_k = 0
    
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
    for i in range(1,k):
        neigh = KNeighborsClassifier(n_neighbors=i)
        neigh.fit(X_train, y_train)
        predictions = neigh.predict(X_test)
        f1 = metrics.f1_score(y_test, predictions,average='macro')
        if f1 > best_result:
            best_result = f1
            best_k = i
        results.append((f1, i))
        cv_scores = cross_val_score(neigh, features, labels, cv=5)
        print(np.mean(cv_scores))

    results = sorted(results, key = lambda x: x[0], reverse = True)
    print(best_k)

    return results


results = run_kNN(features, labels, 9)
print(results)