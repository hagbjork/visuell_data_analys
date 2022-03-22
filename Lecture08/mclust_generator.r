library(tidyverse)
library(dplyr)
library(ggplot2)
library(mclust)

x0 <- as.data.frame(mvrnorm(n = 200, 
                            mu = c(8,12),
                            Sigma = matrix(c(5,8,8,20), nrow = 2)))
x1 <- as.data.frame(mvrnorm(n = 80,
                            mu = c(-4,5),
                            Sigma = matrix(c(8,-2,-2,8), nrow = 2)))
x2 <- as.data.frame(mvrnorm(n = 320,
                            mu = c(0,-4),
                            Sigma = matrix(c(12,3,3,3), nrow = 2)))
x3 <- as.data.frame(mvrnorm(n = 240,
                            mu = c(3, 12),
                            Sigma = matrix(c(1, 0, 0, 20), nrow = 2)))
print(x0)
# 
# data <- rbind(x0,x1,x2,x3)
# sc <- ggplot(data, aes(V1, V2)) + geom_point()
# sc
# 
# write.csv(data, "gaussian_clusters.csv", row.names = FALSE)
