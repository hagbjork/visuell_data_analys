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
#Vi har en del NA-v�rden. F�r mycket data att traggla sig igenom.
print(sum(is.na(data)))
print(dim(data)[1]*dim(data)[2])
boolean_df <- as.data.frame(rowSums(is.na(data)))
colnames(boolean_df) <- "na_rows"
print(filter(boolean_df,na_rows > 0))

#Verkar bara ha att g�ra med 4 observationer med M�NGA NA-v�rden. Vi omittar.
data <- na.omit(data)


print(str(data))

#NSP �r det vi s�ker och vill g�ra predictions p�
data$NSP <- factor(data$NSP)

#Detta inneb�r att vi har 1655 �r friska, 295 �r misst�nkta, 176 sjuka
table(data$NSP)

#Genom att s�tta seed kan vi garantera att ha samma resultat varje g�ng,
#�ven vid slumpade f�rs�k
set.seed(2)

#Vi delar upp i 70% train och 30% test set med bootstrapping
indices <- sample(2, nrow(data), replace = TRUE, prob = c(0.7, 0.3))
rows <- sample(nrow(data))

train <- data[indices == 1, ]
test <- data[indices == 2, ]

#H�r s�ger vi att vi vill best�mma NSP med ALLA v�ra variabler
forest_classifier <- randomForest(NSP ~., data = train)

#Vi kan kolla lite matnyttig information h�r
print(forest_classifier)
predictions <- predict(forest_classifier,train)

#Vi kan j�mf�ra head av train med predictions
head(predictions)
head(train$NSP)

#Vi kan �ven kalla p� confusionmatrix s�h�r
confusionMatrix(predictions, train$NSP)

#D� allt detta �r evaluerat p� v�rt train set l�r vi oss egentligen inte j�ttemycket nytt.
#d�remot om vi inspekterar OOB estimate of error rate:


#Ser snabbt att det minsann g�r att f� lite fel!
real_predictions <- predict(forest_classifier, test)
head(real_predictions)
head(test$NSP)

confusionMatrix(real_predictions, test$NSP)


#Error rates av random forest:
#Vi f�r summering av v�r classifier d�r vi kan se att vi egentligen inte hade beh�vt
#fler �n cirka 150 trees.
plot(forest_classifier)

#Ger oss importance f�r varje feature
varImpPlot(forest_classifier)

#Vi kan ocks� intressera oss f�r de 10 viktigaste
varImpPlot(forest_classifier, sort = TRUE, n.var = 10)

