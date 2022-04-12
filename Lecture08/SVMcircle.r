#generate two circles
library(ggplot2)
library(dplyr)
library(tidyverse)
library(e1071)

#Generera data, sätt upp intervall med mera
nr_of_samples <- 2740

xmin = 2
xmax = 6
ymin = 4
ymax = 8

x_vals <- runif(nr_of_samples, min = xmin, max = xmax)
y_vals <- runif(nr_of_samples, min = ymin, max = ymax)

data <- cbind(x_vals, y_vals)

data <- as_tibble(as.data.frame(data))

print(data)

data_outside <- data %>% filter((x_vals-mean(x_vals))^2 +
                                 (y_vals-mean(y_vals))^2 > 1.8^2)




data_within <- data %>% filter((x_vals-mean(x_vals))^2 +
                                 (y_vals-mean(y_vals))^2 < 1.6^2)

#Assigna labels och merga
data_outside$label <- 1
data_within$label <- 0
all_data <- rbind(data_outside, data_within)
#Gör om till factors för att få schyssta labels
all_data$label <- factor(all_data$label)
sc <- ggplot(all_data, aes(x_vals, y_vals)) + geom_point(aes(color = label))
sc

#Vi gör en spännande support vector machine fit på det!
#Vi kan kalla på svm-paketet
svmfit = svm(label ~ x_vals + y_vals, data = all_data,
             kernel = "radial", cost = 1000, scale = FALSE)

plot(svmfit, all_data)
print(svmfit)


#Centrerar - visar också vad som händer om vi inte gör det
all_data <- all_data %>% mutate(radius = sqrt((x_vals-mean(x_vals))^2
                                + (y_vals-mean(y_vals))^2),angle = atan2((y_vals - mean(all_data$y_vals)),
                                                                         (x_vals- mean(all_data$x_vals))))

all_data <- all_data %>% mutate(radius = sqrt((x_vals)^2
                                             + (y_vals-mean(y_vals))^2),angle = atan2((y_vals - mean(all_data$y_vals)),
                                                                                      (x_vals- mean(all_data$x_vals))))

print(all_data)

sc <- ggplot(all_data, aes(radius, angle)) + geom_point(aes(color = label))
sc

all_data$x_vals <- NULL
all_data$y_vals <- NULL

svmfit = svm(label ~ angle + radius, data = all_data,
             kernel = "linear", cost = 1000, scale = FALSE)
print(svmfit)

print(all_data)
plot(svmfit, all_data)

