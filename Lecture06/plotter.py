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