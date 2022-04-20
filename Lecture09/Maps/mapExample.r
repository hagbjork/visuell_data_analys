#install.packages('rjson')
library(rjson)
library(jsonlite)

#Exempel - geografisk data 
#Ladda in json data
data <- fromJSON(file="https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json")
data$features[[1]]

#Ladda in CSV - ska matcha FIPS
df = read.csv("unemployed.csv", header = T, colClasses = c(fips="character"))
head(df)

#G�r en fig att plotta
fig <- plot_ly()

#Kan byggas p� med add_trace
fig <- fig %>% add_trace(
  type="choropleth",
  geojson=data,
  locations=df$fips,
  z=df$unemp,
  colorscale="Viridis"
)

fig <- fig %>% colorbar(title = "Unemployment Rate (%)")
fig <- fig %>% layout(
  title = "2016 US Unemployment by County"
)

fig <- fig %>% layout(
  geo = list(
    scope = 'usa'
  )
)

fig

