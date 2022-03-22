library(factoextra)
#library(dendextend)
#library(broom)
#library(kableExtra)
library(dbscan)
library(cluster)
library(viridis)
library(tidyverse)


# dbscan.out <- dbscan(sample_df, eps = 0.13, minPts = 7)
# 
# sample_df <- sample_df %>%
#   mutate(
#     kmeans.cluster = kmeans.out$cluster,
#     hclust.cluster = cutree(hclust.out, k = 4),
#     dbscan.cluster = dbscan.out$cluster
#   )