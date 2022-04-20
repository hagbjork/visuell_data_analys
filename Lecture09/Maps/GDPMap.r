library(plotly)
#Ladda in GDP2014 och tolka datan. Anv�nd sedan ISO-koden som argument till locations f�r att visualisera hur GDP
#s�g ut runtom i v�rlden 2014.

#Anv�nd hover text som i https://plotly.com/r/hover-text-and-formatting/ s� att ISO-kod f�r varje land
#blir synligt d� man h�ller �ver landet


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
#Uppgift (inget facit) - Ladda in countries by population och l�gg till GDP per capita som hover text ist�llet f�r.
#Hantera 
