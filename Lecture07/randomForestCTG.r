#CTG Random Forest
library(readxl)
library(dplyr)
library(tidyverse)
library(randomForest)
library(tree)
library(caret)

#https://www.kaggle.com/akshat0007/fetalhr

#data <- as_tibble(read.csv("CTG.csv"))
data <- as_tibble(read_excel("CTG.xls", sheet = "Raw Data"))


#Standardinspektion
print(data)
print(colnames(data))
print(str(data))
#Vi har en del NA-värden. För mycket data att traggla sig igenom.
print(sum(is.na(data)))
print(dim(data)[1]*dim(data)[2])
boolean_df <- as.data.frame(rowSums(is.na(data)))
colnames(boolean_df) <- "na_rows"
print(filter(boolean_df,na_rows > 0))

#Verkar bara ha att göra med 4 observationer med MÅNGA NA-värden. Vi omittar.
data <- na.omit(data)


print(str(data))

#NSP är det vi söker och vill göra predictions på
data$NSP <- factor(data$NSP)

#Detta innebär att vi har 1655 är friska, 295 är misstänkta, 176 sjuka
table(data$NSP)

#Genom att sätta seed kan vi garantera att ha samma resultat varje gång,
#även vid slumpade försök
set.seed(2)

#Vi delar upp i 70% train och 30% test set med bootstrapping
indices <- sample(2, nrow(data), replace = TRUE, prob = c(0.7, 0.3))
rows <- sample(nrow(data))

train <- data[indices == 1, ]
test <- data[indices == 2, ]

#Här säger vi att vi vill bestämma NSP med ALLA våra variabler
forest_classifier <- randomForest(NSP ~., data = train)

#Vi kan kolla lite matnyttig information här
print(forest_classifier)
predictions <- predict(forest_classifier,train)

#Vi kan jämföra head av train med predictions
head(predictions)
head(train$NSP)

#Vi kan även kalla på confusionmatrix såhär
confusionMatrix(predictions, train$NSP)

#Då allt detta är evaluerat på vårt train set lär vi oss egentligen inte jättemycket nytt.
#däremot om vi inspekterar OOB estimate of error rate:


#Ser snabbt att det minsann går att få lite fel!
real_predictions <- predict(forest_classifier, test)
head(real_predictions)
head(test$NSP)

confusionMatrix(real_predictions, test$NSP)


#Error rates av random forest:
#Vi får summering av vår classifier där vi kan se att vi egentligen inte hade behövt
#fler än cirka 150 trees.
plot(forest_classifier)

#Ger oss importance för varje feature
varImpPlot(forest_classifier)

#Vi kan också intressera oss för de 10 viktigaste
varImpPlot(forest_classifier, sort = TRUE, n.var = 10)

