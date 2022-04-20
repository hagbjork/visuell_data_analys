library(plotly)
#Exempel för plotly med enkel line plot - 
data <- read.csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
head(data)
#Exempel på "bare bones" - det som krävs för att få en enkel visual
fig <- plot_ly(x = as.Date(data$AAPL_x), y = data$AAPL_y, type = 'scatter', mode = 'lines', color = I('red')
               , name = 'Share Prices (in USD)')

fig


#Vidareutveckling med layoutargument 

fig <- fig %>%  layout(title = 'Apple Share Prices over time (2014)',
         plot_bgcolor='#e5ecf6',  
         xaxis = list(  
           title = 'AAPL_x',
           zerolinecolor = '#ffff',  
           zerolinewidth = 2,  
           gridcolor = 'ffff'),  
         yaxis = list(  
           title = 'AAPL_y',
           zerolinecolor = '#ffff',  
           zerolinewidth = 2,  
           gridcolor = 'ffff'),
         showlegend = TRUE, width = 1100)
fig
