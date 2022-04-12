#Tree classification

library(randomForest)
library(tree)
library(ggplot2)
library(GGally)
library(dplyr)

iris %>% head()

decision_tree <- tree(Species ~ ., data = iris) # Interpretation
# 1. use tree function  
# 2. sort species
# 3. based on all(.) variables
# 4. data is iris dataset
decision_tree


plot(decision_tree)
text(decision_tree)
ggpairs(iris[,1:5])



index_row <- sample(2, 
                    nrow(iris), 
                    replace = T, 
                    prob = c(0.7, 0.3)
)                 #assign values to the rows (1: Training, 2: Test)
train_data <- iris[index_row == 1,]
test_data <- iris[index_row == 2,]


iris_classifier <- randomForest(Species ~., 
                                data = train_data, #train data set 
                                importance = T) 
iris_classifier       

plot(iris_classifier)

importance(iris_classifier)

varImpPlot(iris_classifier)

qplot(Petal.Width, Petal.Length, data=iris, color = Species)

qplot(Sepal.Width, Sepal.Length, data=iris, color = Species)

predicted_table <- predict(iris_classifier, test_data[,-5])
table(observed = test_data[,5], predicted = predicted_table)

