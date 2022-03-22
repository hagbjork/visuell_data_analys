library(tidyverse)
library(tidymodels)
library(plotly)

make_moons <- read.csv(file = "data/make_moons.csv")
make_moons$y <- as.character(make_moons$y)
set.seed(123)
make_moons_split <- initial_split(make_moons, prop = 3/4)
make_moons_training <- make_moons_split %>%
  training()
make_moons_test <- make_moons_split %>%
  testing()
train_index <- as.integer(rownames(make_moons_training))
test_index <- as.integer(rownames(make_moons_test))
make_moons[train_index,'split'] = 'Train Split Label'
make_moons[test_index,'split'] = 'Test Split Label'
make_moons$y <- paste(make_moons$split,make_moons$y)

fig <- plot_ly(data = make_moons, x = ~X1, y = ~X2, type = 'scatter', mode = 'markers',alpha = 0.5, symbol = ~y, symbols = c('square','circle','square-dot','circle-dot'),
               marker = list(size = 12,
                             color = 'lightyellow',
                             line = list(color = 'black',width = 1)))

fig



