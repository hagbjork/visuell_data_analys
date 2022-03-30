import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from umap import UMAP #https://umap-learn.readthedocs.io/en/latest/
#pip install umap-learn #(inte umap!)


data = pd.read_csv("Lecture03/mnist.csv")
train = data[0:1000]
labels = train.pop("label")

umap_2d = UMAP(random_state=0)
umap_2d.fit(train)

projections = umap_2d.transform(train)
print(projections.shape)

plt.scatter(projections[:,0], projections[:,1], c = labels)
plt.colorbar(boundaries=np.arange(11)-0.5).set_ticks(np.arange(10))
plt.show()