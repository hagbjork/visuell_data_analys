#Old faithfull - demo

library(tidyverse)
library(dplyr)
library(mclust)
library(factoextra)

data <- as.tibble(read.csv('faithful.csv'))
print(data)
data <- data[ ,2:3]


#eruption and waiting is time in minutes

ggplot(data, aes(eruptions, waiting)) + geom_point()

#use dens to see concentration
dens <- densityMclust(data)
plot(dens)
#High BIC score is best

#Don't use more clusters then you have variables

mc <- Mclust(data)
plot(mc)

summary(mc)
str(summary(mc))

summary(mc)$mean


fviz_mclust_bic(mc)

####################
# SVM
library(ggplot2)
library(dplyr)
library(tidyverse)
library(e1071) #package to use SVM


nr_of_sample <- 2740

x_min <- 2
x_max <- 6
y_min <- 4
y_max <- 8

x_vals <- runif(nr_of_sample, min = x_min, max = x_max) 
y_vals <- runif(nr_of_sample, min = y_min, max = y_max)

data <- cbind(x_vals, y_vals)
data <- as_tibble(data)
print(data)

data_outside <- data %>% filter(x_vals^2 + y_vals^2 > 1.8^2)
data_within <- data %>% filter(x_vals^2 + y_vals^2 > 1.6^2)

data_outside$label <- 1
data_within$label <- 0

all_data <- rbind(data_outside, data_within)
print(all_data)

#Need to use "factor" to transform
all_data$label <- factor(all_data$label)
print(all_data)

sc <- ggplot(all_data(aes(x_vals, y_vals)) + geom_point(aes(color = label)))
sc

svmfit <- svm(label~ x_vals, y_vals + x_vals*y_vals, data = all_data,
              kernel = 'linear', cost = 1000, scale = F)

plot(svmfit, all_data)

print(svmfit)

str(svmfit)

all_data <- all_data %>% mutate(radius = sqrt(x_vals^2 + y_vals^2),
                                angle = atan2(y_vals, x_vals))
print(all_data)
sc <- ggplt(aes(radius, angle)) + geom_point(aes(color = label))
