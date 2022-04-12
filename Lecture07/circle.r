#generate two circles
library(ggplot2)
library(dplyr)
library(tidyverse)
library(testit) # intall

#Generera data, s�tt upp intervall med mera

data_generator <- function(params){
  #Accepts a params list and returns
  p <- params
  
  #Slumpar v�rden fr�n uniform distribution
  x_vals <- runif(p$n_vals, min = p$x_min, max = p$x_max)
  y_vals <- runif(p$n_vals, min = p$y_min, max = p$y_max)
  
  # spara x och y v�rden i dataframe
  df <- as_tibble(cbind(x_vals, y_vals))
  
  #Kollar v�ra assertions
  assert("r_min is greater than 0", p$r_min > 0)
  assert("r_max is lesser than sqrt(x_max^2 + y_max^2)", 
         p$r_max < sqrt(p$x_max^2 + p$y_max^2))
  
  #Filtrering p� avst�nd fr�n origo
  df <- df %>% filter(sqrt(x_vals^2 + y_vals^2) > p$r_max | 
                               sqrt(x_vals^2 + y_vals^2) < p$r_min)
  
  #Filtrering p�  krysset
  df <- df %>% filter(x_vals + y_vals < -p$tol | x_vals + y_vals > p$tol)
  df <- df %>% filter(x_vals - y_vals < -p$tol | x_vals - y_vals > p$tol)

  sc <- ggplot(df, aes(x_vals, y_vals)) + geom_point()

  return(list(plot = sc, df = df))
}

