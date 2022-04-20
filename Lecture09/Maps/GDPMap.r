library(plotly)
#Ladda in GDP2014 och tolka datan. Använd sedan ISO-koden som argument till locations för att visualisera hur GDP
#såg ut runtom i världen 2014.

#Använd hover text som i https://plotly.com/r/hover-text-and-formatting/ så att ISO-kod för varje land
#blir synligt då man håller över landet


######################
######################
#Facit:

df <- read.csv("gdp2014.csv")
head(df)
df$idx <- 1:222


df$hover <- with(df, paste(COUNTRY, 'Code:', CODE, 'Index:', idx))

fig <- plot_geo(df)

# 

fig <- fig %>% add_trace(
  z = ~GDP..BILLIONS., locations = ~CODE, text = ~hover,
  color = ~GDP..BILLIONS., colors = 'Purples'
)
fig <- fig %>% colorbar(title = "Millions USD")
fig <- fig %>% layout(
  title = '2011 US Agriculture Exports by State<br>(Hover for breakdown)'
)

fig
######################
######################

#Uppgift (inget facit) - Hitta egen data med ISO-kod och utforska med map visualizations!
#Uppgift (inget facit) - Ladda in countries by population och lägg till GDP per capita som hover text istället för.
#Hantera 
