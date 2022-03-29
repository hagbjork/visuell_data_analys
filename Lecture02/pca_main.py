from pca_knn import *

def main():
    X_train = pd.read_csv('Lecture02/mnist.csv')
    Y_train = X_train.pop('label')

    plot2dMNIST(X_train, Y_train, size = 20)

    plot_explained_variance(X_train)

    #Utan PCA
    #run_PCA_kNN(X_train, Y_train)

    #Med PCA
    run_PCA_kNN(X_train, Y_train, n_components = 100)

if __name__ == "__main__":
    main()