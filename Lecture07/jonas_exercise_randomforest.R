library(dplyr)
library(tidyverse)
library(randomForest)
library(tree)
library(ggplot2)

#läs in dataset
data <- as_tibble(iris)

#fit samt skriv ut trädet
decision_tree <- tree(Species~., data = data)
print(decision_tree)

#se hur trädet ser ut plottat
plot(decision_tree)
text(decision_tree)

pairs(iris)

#Dela in i train/test
indices <- sample(2, nrows(data), replace = T, prob = c(0.7, 0.3))
train <- data[indices == 1,]
test <- data[indices == 2,]

#Predikterat NSP o
iris_classifier <- randomForest(Species ~., data = train)
print(iris_classifier)
