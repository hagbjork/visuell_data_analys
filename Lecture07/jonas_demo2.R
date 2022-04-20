library(readxl)
library(dplyr)
library(tidyverse)
library(randomForest)
library(tree)
library(caret)

data <- as_tibble(read_excel('CTG.xls', sheet = 'Raw Data'))

head(data)
colnames(data)
str(data)

sum(is.na(data))
dim(data)

boolean_df <- as.data.frame(rowSum(is.na(data)))
colnames(boolean_df) <- 'na_rows'
filter(boolean_df, na_rows > 0)

data <- na.omit(data)

str(data)

set.seed(2)

indices <- sample(2, nrows(data), replace = T, prob = c(0.7, 0.3))
train <- data[indices == 1,]
test <- data[indices == 2,]

#Predikterat NSP o
forest_classifier <- randomForest(NSP ~., data = train)
print(forest_classifier)

predictions <- predict(forest_classifier, test)

head(predictions)

cm <- confusionMatrix(predictions, test$NSP)
cm
cm$byClass

varImpPlot(forets_classifier, sort = T, n.var = 10)