library(ggplot2)
library(dplyr)
library(tidyverse)
library(testit)

#generate data

data_generator <- function(params){
  p <- params
  x_vals <- runif(p$n_vals, min = p$x_min, max = p$x_max)
  y_vals <- runif(p$n_vals, min = p$y_min, max = p$y_max)
}

df <- as_tibble(data_generator)

  # r_min inte lägre än noll
  # r_max inte tsörre än antal datapunkter


#Generera data, sätt upp intervall med mera

  
  #Slumpar värden från uniform distribution
  x_vals <- runif(p$n_vals, min = p$x_min, max = p$x_max)
  y_vals <- runif(p$n_vals, min = p$y_min, max = p$y_max)
  
  # spara x och y värden i dataframe
  df <- as_tibble(cbind(x_vals, y_vals))