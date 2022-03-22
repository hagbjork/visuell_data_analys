source("circle.r")
source("cluster_methods.r")


params <- list(x_min = - 3, x_max = 3, y_min = -3, y_max = 3, n_vals = 10000, tol = 0.2, r_min = 1.5, r_max = 2.2)
return_list <- data_generator(params)

df <- return_list$df
plot <- return_list$plot
plot


dbscan.out <- dbscan(df, eps = 0.13, minPts = 7)

sample_df <- df %>%
  mutate(
    dbscan.cluster = dbscan.out$cluster
  )

print(sample_df)
print(sample_df$dbscan.cluster)