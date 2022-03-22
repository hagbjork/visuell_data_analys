#generate two circles
library(ggplot2)
library(dplyr)
library(tidyverse)
library(testit)

#Generera data, sätt upp intervall med mera

data_generator <- function(params){
  #Accepts a params list and returns
  p <- params
  
  #Slumpar värden från uniform distribution
  x_vals <- runif(p$n_vals, min = p$x_min, max = p$x_max)
  y_vals <- runif(p$n_vals, min = p$y_min, max = p$y_max)
  
  #Kollar våra assertions
  assert("r_min is greater than 0", p$r_min > 0)
  assert("r_max is lesser than sqrt(x_max^2 + y_max^2)", p$r_max < (p$x_max^2))
  
  df <- as.tibble(cbind(x_vals, y_vals))
  
  
  #Filtrering 1 på condition avstånd från origo
  df_subset <- df %>% filter((x_vals-mean(x_vals))^2 +
                               (y_vals-mean(y_vals))^2 > p$r_max^2)
  df_subset2 <- df %>% filter((x_vals-mean(x_vals))^2 +
                                (y_vals-mean(y_vals))^2 < p$r_min^2)
  
  df <- rbind(df_subset, df_subset2)
  
  #Mutate och filter
  
  #Mutate och filter (eller bara filter condition)
  df <- df %>% filter(x_vals + y_vals < -p$tol | x_vals + y_vals > p$tol)
  df <- df %>% filter(x_vals - y_vals < -p$tol | x_vals - y_vals > p$tol)

  
  
  
  sc <- ggplot(df, aes(x_vals, y_vals)) + geom_point()
  sc
  print(df)
  
  return(list(plot = sc, df = df))
  
  
  
}
