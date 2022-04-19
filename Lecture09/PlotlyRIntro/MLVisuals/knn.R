library(pracma)
library(plotly)
library(tidyverse)
library(tidymodels)
library(plyr)


data(iris) # We will use the iris data, which is included in R by default

mesh_size = .02
margin = 1

db_split <- initial_split(iris, prop = 3/4)
train_data <- training(db_split)
test_data <- testing(db_split)

# Create a mesh grid on which we will run our model
l_min = min(iris$Sepal.Length) - margin
l_max = max(iris$Sepal.Length) + margin
w_min = min(iris$Sepal.Width) - margin
w_max = max(iris$Sepal.Width) + margin
lrange = seq(l_min, l_max, mesh_size)
wrange = seq(w_min, w_max, mesh_size)

mg = meshgrid(lrange, wrange)
ll = mg$X
ww = mg$Y

# Create classifier, run predictions on grid
model = nearest_neighbor( neighbors = 15, weight_func = 'inv' ) %>% 
  set_engine("kknn") %>% 
  set_mode("classification") %>% 
  fit(Species ~ Sepal.Length + Sepal.Width, data = train_data)

ll1 <- matrix(ll, length(ll), 1)
ww1 <- matrix(ww, length(ww), 1)
final <- data.frame(ll1, ww1)

colnames(final) = c("Sepal.Length", "Sepal.Width" )

pred <- model %>%
  predict(final, type = 'prob')

dim_val <- dim(ll)
proba_setosa <- matrix(pred$.pred_setosa, dim_val[1], dim_val[2])
proba_versicolor <- matrix(pred$.pred_versicolor, dim_val[1], dim_val[2])
proba_virginica <- matrix(pred$.pred_virginica, dim_val[1], dim_val[2])

# Compute the classifier confidence
Z <- array(c(proba_setosa, proba_versicolor, proba_virginica), dim = c(dim_val[1],dim_val[2],3))
diff = aaply(Z, c(1,2), max) -  (aaply(Z, c(1,2), sum) - aaply(Z,c(1,2), max))

# Overlay the heatmap of the confidence on the scatter plot of the examples
fig <- plot_ly() 
fig <- fig %>% add_trace(data=test_data, x = ~Sepal.Length, y = ~Sepal.Width, symbol = ~Species, split = ~Species, symbols = c('square-dot','circle-dot','diamond'),
                         type = 'scatter', mode = 'markers',  
                         marker = list(size = 12, line = list(width = 1.5), color = 'lightyellow'))%>% layout(title="Prediction Confidence on Test Split")
fig <- fig %>% add_trace(x = lrange, y = wrange, z = diff, type = 'heatmap')

fig
