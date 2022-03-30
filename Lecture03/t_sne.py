from cProfile import label
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('Lecture03/mnist.csv')
train = data
labels = train.pop('label')

train = np.asarray(train)
labels = np.asarray(labels)

def run_tsne(train: np.array, labels: np.array, n_components: int = None) -> None:
    """ tSNE plot of feature vectors with added labels. If n_components is added, 
    PCA will be run as preprocessing

    Args:
        train (np.array): feature vectors in dataset
        labels (np.array): dataset labels (target)
        n_components (int, optional): number of components used by PCA
    """
    
    if n_components:
        pca = PCA(n_components=n_components)
        train = pca.fit_transform(train)
    
    # default TSNE n_dimensions=2
    tsne = TSNE(random_state=0, perplexity=5)
    tsne_res = tsne.fit_transform(train)
    sns.scatterplot(x=tsne_res[:,0], y=tsne_res[:,1], hue=labels, palette=sns.hls_palette(10), legend='full')

    
run_tsne(train, labels, n_components=60)