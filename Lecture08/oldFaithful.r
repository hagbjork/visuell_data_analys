library(tidyverse)
library(dplyr)
library(ggplot2)
library(mclust)
library(factoextra)


data <- as_tibble(read.csv("faithful.csv"))

print(data)
#Tillagt f�r att trimma av f�rsta columnen!
data <- data[, 2:3]
print(data)
#Empirisk densitet, beh�ver inte ha n�got att g�ra med eventuella
#gaussiska distributioner
ggplot(data, aes(eruptions, waiting)) + geom_point()# + geom_density2d(adjust = 0.3)


dens <- densityMclust(data)
plot(dens)
plot(dens, what = 'density', type = 'persp')

#H�gre BIC -> b�ttre. Vi vill inte overfitta och s�ga att vi har lika m�nga egna 
#kluster som vi har samples som exempel - d�lig och icke-informativ generalisering!
mc <- Mclust(data)
plot(mc)
#V�ljer vi f�r classification kan vi f� f�ljande resultat..

#�r vi intresserade av regioner som kan vara sv�ra att klassificera anv�nder vi 
#uncertainty


print(str(summary(mc)))
print(summary(mc)$mean)
print(summary(mc)$variance)



#Fr�n factoextra
fviz_mclust_bic(mc)

print(mc$parameters)

#Om vi VET att vi har 2 distributioner kan vi tvinga p� G = 2
mc_2 <- Mclust(data, G = 3)

plot(mc_2)

print(summary(mc_2)$variance)

ggpairs(data)



