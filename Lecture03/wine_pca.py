from sklearn.decomposition import PCA
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from umap import UMAP
from sklearn.manifold import TSNE
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns


clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf = SVC(kernel='linear')

data = load_wine()


labels = data.target
features = data.data

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.5, random_state=42)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)

print("F1-scores:",metrics.f1_score(y_test, predictions,average=None))
conf_mat = confusion_matrix(y_test, predictions)
ax = sns.heatmap(conf_mat)
plt.show()

pca = PCA(n_components=2)
pca.fit(X_train)
pca.transform(X_test)

X_test = pca.transform(X_train)

print(X_test.shape)
print(X_test[:, 0].shape)
print(X_test[:, 1].shape)
plt.scatter(X_test[:, 0], X_test[:, 1], c = y_train)
plt.show()


tsne= TSNE(n_components=2)

X_train = tsne.fit_transform(X_train)
print(X_train.shape)

plt.scatter(X_train[:, 0], X_train[:, 1], c = y_train)
plt.show()

umap_2d = UMAP(random_state=2 )
umap_2d.fit(X_train)

projections = umap_2d.transform(X_train)
print(projections.shape)


plt.scatter(projections[:, 0], projections[:, 1], c = y_train)
plt.show()



