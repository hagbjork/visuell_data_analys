from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = load_wine(as_frame = True)

print(type(data))


#df = pd.DataFrame(data)

data1 = pd.DataFrame(data= np.c_[data['data'], data['target']],
                     columns= data['feature_names'] + ['target'])

print(f'Dimensions of wine dataset: {data1.shape}')
print(data1.head())

labels = data1.pop("target")
print(labels)

# #data1 = np.asarray(data1)

# data1 = (data1-data1.mean())/data1.std()
# #covMatrix = pd.DataFrame.cov(data1)

# print(data1.std())

# #sns.heatmap(covMatrix, annot=True, fmt='g')
# plt.show()


# covMatrix = pd.DataFrame.cov(data)
# #sn.heatmap(covMatrix, annot=True, fmt='g')
# #plt.show()

# data = {'A': [45,37,42,35,39],
#         'B': [20,50,4,25,70],
#         'C': [1,5,-1,2,7]
#         }

# df = pd.DataFrame(data,columns=['A','B','C'])

# covMatrix = pd.DataFrame.cov(df)
# sns.heatmap(covMatrix, annot=True, fmt='g')
# plt.show()

# normalized_df = (df-df.mean())/df.std()

# covMatrix = pd.DataFrame.cov(normalized_df)
# sns.heatmap(covMatrix, annot=True, fmt='g')
# plt.show()