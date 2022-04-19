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

