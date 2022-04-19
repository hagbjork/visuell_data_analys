#install.packages('lubridate')
#install.packages('plotly')
#install.packages('tidyverse')

library(tidyverse)
library(plotly)
library(lubridate)

data_daywise <- read_csv("daywise.csv")
data_daywise$Date <- ymd(data_daywise$Date)

head(data_daywise)

#Sortera på Date istället för land
data_daywise <- arrange(data_daywise, Date)


head(data_daywise)


#Gör en line plot av confirmed cases över tid.

#Facit:
plot_ly(data_daywise, x = ~Date, y = ~Confirmed, 
        type = 'scatter',mode = 'lines')


#Lägg med pipe operator till 3 lines med add_trace till 
#fig - confirmed, recovered och deaths. 
#Ser någonting konstigt ut?
#Kan du spekulera om någon förklaring?

fig <- plot_ly(data_daywise, x=~ Date)
#Facit: (Källan slutade bara att rapportera recovered cases 
#är förklaringen)
fig <- fig %>% add_trace(y = ~Confirmed, name = 'Confirmed', 
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Recovered, name = 'Recovered', 
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Deaths, name = 'Deaths', 
                         mode = 'lines', type = 'scatter')
fig

#Add_trace tar också in line som argument 
#- en lista där vi kan inkludera färg och storlek.
#Justera linjernas form och färg genom att göra 3 listor 
#och lägg till i figuren.

#Facit: 
cnfrm.line <- list(color = 'blue', width = 4)
death.line <- list(color = 'red', width = 6)
recovered.line <- list(color = 'green', width =2)

fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y =~ Confirmed, name = 'Confirmed', 
                         mode = 'lines', type = 'scatter', 
                         line = cnfrm.line)
fig <- fig %>% add_trace(y =~ Recovered, name = 'Recovered', 
                         mode = 'lines', type = 'scatter', 
                         line = recovered.line)
fig <- fig %>% add_trace(y =~ Deaths, name = 'Deaths', 
                         mode = 'lines', type = 'scatter', 
                         line = death.line)
fig

#Lägg till ett layoutargument med pipe operator som ger en 
#titel och xaxis/yaxis titlar
#Facit:
fig <- fig %>% layout(title = 'Total Cases World Wide', 
                      xaxis = list(title = 'Date'), 
                      yaxis = list(title = 'Total Cases'))
fig

#Ändra mode i confirmed till lines + markers och ge 
cnfrm.marker <- list(color='orange', size = 1, opacity = 1, 
                     line = list(color = 'orange', width = 2))

fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y =~ Confirmed, name = 'Confirmed', 
                         mode = 'lines+markers', 
                         type = 'scatter', 
                         line = cnfrm.line, 
                         marker = cnfrm.marker)
fig <- fig %>% add_trace(y =~ Recovered, name = 'Recovered', 
                         mode = 'lines', type = 'scatter', 
                         line = recovered.line)
fig <- fig %>% add_trace(y =~ Deaths, name = 'Deaths', 
                         mode = 'lines', type = 'scatter', 
                         line = death.line)
fig

#Ladda in country daywise och filtrera bort alla datum som 
#inte är det senaste datumet. Sortera i fallande ordning
#(störst först, lägst sist) baserat på dödsratio. 
#Lägg även till dödsratio som en kolumn.
#Du som har läst statistik - finns det något att kommentera 
#om ordningen?

#Facit: Det går givetvis inte med statistisk signifikans 
#säga att MS Zaandam 
#eller Vanuatu har högst dödsratio i världen.
data_countrywise <- read_csv("country_daywise.csv")
head(data_countrywise)
latest <- data_countrywise %>% 
  filter(Date == max(Date)) %>% 
  arrange(desc(Deaths/Confirmed))
latest$death_rate <- round(latest$Deaths/latest$Confirmed, 
                           digits = 3)
head(latest)

#Sortera nu istället på confirmed cases och välj de 10 länder
#med högst antal confirmed cases.
#Gör en bar plot i plot_ly med valfri med hjälp av layout.

#Facit:
latest <- arrange(latest, desc(Confirmed))
latest <- latest[1:10, ]


new_fig <- plot_ly(latest, x =~Country, y =~Confirmed, 
                   type = 'bar') %>% 
  layout(title = 'Confirmed Cases by Country',
         plot_bgcolor='#e5ecf6',
         xaxis = list(title = 'Count'),
         yaxis = list(title = 'Country'))
new_fig

#Vi vill ha sorteringen gjord i bar plotten baserat på 
#antal cases snarare än alfabetisk ordning på länder.
#Kan åtgärdas genom att göra factors av Country. 
#Använd detta tillsammans med färgkodning baserat på death rate
#BONUS! Ordna så att legend syns ordentligt för 
#färgkodningen! Finns ej i facit.

#Facit - saknar dock legend!
latest$Country <- factor(latest$Country, 
                         levels = c(as.character(latest$Country)))
p <- plot_ly(latest, x =~Country, y =~Confirmed, 
             text =~death_rate, 
             type = 'bar', 
             name = 'Confirmed Cases', 
             marker = list(color =~death_rate))
p


#Subplots! Läs in dig på ?subplot och gör upp 3 olika line plots.
#Datan som ska visualiseras är från country_daywise. 
#Filtrera ut endast Indien och arrangera baserat på Date.
#Gör så att de 3 olika subplottarna avser Confirmed, 
#recovered och deaths över tid.

#Facit:

data <- read_csv("country_daywise.csv") %>% 
  filter(Country == 'India') %>% arrange(Date)

fig1 <- plot_ly(data, x =~Date, y =~Confirmed, 
                type = 'scatter', 
                mode = 'lines', 
                name = 'Confirmed Cases')

fig2 <- plot_ly(data, x =~Date, y =~Recovered, 
                type = 'scatter', 
                mode = 'lines', 
                name = 'Recovered Cases')

fig3 <- plot_ly(data, x =~Date, y =~Deaths, 
                type = 'scatter', 
                mode = 'lines', 
                name = 'Deaths Cases')

subplot(fig1, fig2, fig3, shareX = FALSE, nrows = 2)
head(data)

#Scatter plot
#Utgå från confirmed för att göra en scatter plot för de 10 
#länder med flest confirmed cases.
#

plot_ly(data = latest, x =~Confirmed, y=~Deaths, 
        type = 'scatter', 
        mode = 'markers', 
        color =~Country, 
        colors = heat.colors(n=10), 
        size =~Confirmed, 
        marker = list(size =~1.5e3*death_rate))

#Skippa att använda storlek eller färg - 
#använd istället alla länders data (inte bara top 10) 
#i en scatter plot.
#Se till att inte visa legends så att det inte blir plottrigt. 
#utnyttja plotlys interaktivitet för att hovra över några länder
#med låg respektive hög dödlighet. 
#Tänk på att det går att zooma in smidigt!

#Facit:
data <- read_csv("country_daywise.csv") %>% 
  filter(Date == max(Date))
plot_ly(data = data, x =~Confirmed, y=~Deaths, 
        type = 'scatter', 
        mode = 'markers', 
        name =~Country, 
        showlegend = F)


#Pie chart -  Gör två pie charts - en för antal confirmed och 
#en för antal deaths för de top 10 länderna.

#Facit:
fig1 <- plot_ly(latest, labels =~Country, 
                values =~Confirmed, 
                type = 'pie', 
                textinfo = 'label+percent')
fig1

fig2 <- plot_ly(latest, labels =~Country, 
                values =~Deaths, 
                type = 'pie', 
                textinfo = 'label+percent')
fig2

#Slutligen - gör en pie chart med values =~death_rate. 
#Finns det någonting missvisande med valet av visual när
#du utreder detta med en pie chart? 
#Tips - försök att förklara vad storleken för varje land betyder.
fig3 <- plot_ly(latest, labels =~Country, 
                values =~death_rate, 
                type = 'pie', 
                textinfo = 'label')
fig3

