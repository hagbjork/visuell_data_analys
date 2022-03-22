#Logistic regression
library(tidyverse)
library(psych)
library(dplyr)
library(car)
library(broom)

data <- as_tibble(read.csv("bmd.csv"))

print(head(data))
print(colnames(data))

data$fracture <- as.integer(factor(data$fracture))-1L
print(data)

#print(data$fracture)

#Vi laddar in dataset för diabetes
data <- as_tibble(read.csv("diabetes.csv"))

#Vi kollar efter na-värden:
print(any(is.na(data)))
#View(data)
print(head(data))
print(colnames(data))

#Vi kanske vill ha det på en lite annan form


diabetes_data <- data %>% select(Diabetes = Outcome, everything())
print(head(diabetes_data))
# Syntax - när vi säger glm(diabetes ~., data) menar vi att vi inkluderar ALL
#data för att förutspå diabetes.

model <- glm(Diabetes ~ ., data = diabetes_data,
             family = binomial) #Vi har binomial som family då vi har två 
#möjliga utfall

# Använd modellen för att generera probabilities för positiv respektive negativ
probabilities <- predict(model, type = "response")
predicted.classes <- ifelse(probabilities > 0.5, "pos", "neg") #Namnge utfallen
head(predicted.classes)



predictors <- colnames(data)

diabetes_data <- diabetes_data %>%
  mutate(logit = log(probabilities/(1-probabilities))) %>%
  gather(key = "predictors", value = "predictor.value", -logit)



sc_plt <- ggplot(diabetes_data, aes(logit, predictor.value))+
  geom_point(size = 0.5, alpha = 0.5) +
  geom_smooth(method = "loess") + 
  theme_bw() + 
  facet_wrap(~predictors, scales = "free_y")
sc_plt

#Här får vi ut alla våra observationer för att se om det finns
#några extrema outliers


vif(model)

print(colnames(model.data))



print(model)

#Är vi intresserade av correlation mellan varje värde kan vi skapa en correlations
#matris
print(matrix(cor(data), nrow = 9))

#På samma sätt kan vi få kovariansmatris
print(matrix(cov(data), nrow = 9))



