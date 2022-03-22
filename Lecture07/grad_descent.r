#Gör egen gradient descent för rät linje
library(ggplot2)
samples <- 423
x_vals <- sample(40:200, size = samples, replace = TRUE)

x_vals <- x_vals + rnorm(samples, mean = 4, sd = 6)


y_vals <- 3*x_vals + rnorm(samples, mean = 4, sd = 100) - 40


data <- as.data.frame(cbind(x_vals,y_vals))


plt <- ggplot(data, aes(x_vals, y_vals)) + geom_point()
plt

#grad_descent <- function(values, max_iterations, )

