library(tidyverse)
library(dplyr)
library(ggplot2)
library(mclust)
library(factoextra)


data <- as_tibble(read.csv("faithful.csv"))

print(data)
#Tillagt för att trimma av första columnen!
data <- data[, 2:3]
print(data)
#Empirisk densitet, behöver inte ha något att göra med eventuella
#gaussiska distributioner
ggplot(data, aes(eruptions, waiting)) + geom_point()# + geom_density2d(adjust = 0.3)


dens <- densityMclust(data)
plot(dens)
plot(dens, what = 'density', type = 'persp')

#Högre BIC -> bättre. Vi vill inte overfitta och säga att vi har lika många egna 
#kluster som vi har samples som exempel - dålig och icke-informativ generalisering!
mc <- Mclust(data)
plot(mc)
#Väljer vi för classification kan vi få följande resultat..

#Är vi intresserade av regioner som kan vara svåra att klassificera använder vi 
#uncertainty


print(str(summary(mc)))
print(summary(mc)$mean)
print(summary(mc)$variance)



#Från factoextra
fviz_mclust_bic(mc)

print(mc$parameters)

#Om vi VET att vi har 2 distributioner kan vi tvinga på G = 2
mc_2 <- Mclust(data, G = 3)

plot(mc_2)

print(summary(mc_2)$variance)

ggpairs(data)



