library(dbscan)


params <- list( n_vals = 10000, x_min = - 3, x_max = 3, y_min = -3, y_max = 3, 
                r_min = 1.5, r_max = 2.2, tol = 0.2)
return_list <- data_generator(params)

df <- return_list$df
df
plot <- return_list$plot
plot


dbscan.out <- dbscan(df, eps = 0.13, minPts = 7)

sample_df <- df %>%
  mutate(
    dbscan.cluster = dbscan.out$cluster
  )

print(sample_df)
print(sample_df$dbscan.cluster)

sc <- ggplot(sample_df, aes(x_vals, y_vals, color=dbscan.cluster)) + geom_point()
sc