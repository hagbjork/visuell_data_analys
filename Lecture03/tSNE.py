import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("Lecture03/mnist.csv")
train = data[0:1000]
labels = train.pop("label")

train = np.asarray(train)
labels = np.asarray(labels)

def run_tsne(train: np.array, labels: np.array, n_components: int = None) -> None:
    '''
    tSNE-plot of feature vectors with added labels. If n_components is added, PCA will be run
    as preprocessing.

    Args in:
            train - feature vectors in dataset
            labels - dataset labels
            n_components - number of principal components used by PCA
    Returns: 
            None

    '''
    if n_components:

        pca = PCA(n_components=60)
        train = pca.fit_transform(train)

    tsne = TSNE(n_components = 2, random_state=0, perplexity = 2)
    tsne_res = tsne.fit_transform(train)
    sns.scatterplot(x = tsne_res[:,0], y = tsne_res[:,1], hue = labels, palette = sns.hls_palette(10), legend = 'full')
    plt.show()


run_tsne(train, labels)