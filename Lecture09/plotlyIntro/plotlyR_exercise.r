#install.packages('lubridate')
#install.packages('plotly')
#install.packages('tidyverse')

library(tidyverse)
library(plotly)
library(tidyverse)
library(lubridate)

data_daywise <- read_csv("daywise.csv")
data_daywise$Date <- ymd(data_daywise$Date)
head(data_daywise)

#Sortera på Date istället för land
data_daywise <- arrange(data_daywise, Date)
head(data_daywise)


#Gör en line plot av confirmed cases över tid.
fig <- plot_ly(x = as.Date(data_daywise$Date), y = data_daywise$Confirmed, 
               type = 'scatter',
               mode = 'lines',
               color = 'red')
fig

fig <- fig %>%  layout(title = 'Confirmed covid cases by date', 
                       yaxis = list(title = 'Number of confirmed cases'), 
                       xaxis = list(title = 'Date'))
fig


#Lägg med pipe operator till 3 lines med add_trace till fig - confirmed, recovered och deaths. Ser någonting konstigt ut?
#Kan du spekulera om någon förklaring?
fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y = ~Confirmed, name = 'Confirmed',
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Recovered, name = 'Recovered',
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Deaths, name = 'Deaths',
                         mode = 'lines', type = 'scatter')
fig

#Aug 4 2021 så går recovered från 130.899milj till 0. 


#Add_trace tar också in line som argument - en lista där vi kan inkludera färg och storlek.
#Justera linjernas form och färg genom att göra 3 listor och lägg till i figuren.
conf.list <- list(color ='green', width = 2)
rec.list <- list(color = 'blue', width = 2)
deaths.list <- list(color = 'red', width = 2)

fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y =~ Confirmed, name = 'Confirmed', 
                         mode = 'lines', type = 'scatter', 
                         line = conf.list)
fig <- fig %>% add_trace(y =~ Recovered, name = 'Recovered', 
                         mode = 'lines', type = 'scatter', 
                         line = rec.list)
fig <- fig %>% add_trace(y =~ Deaths, name = 'Deaths', 
                         mode = 'lines', type = 'scatter', 
                         line = deaths.list)
fig

#Lägg till ett layoutargument med pipe operator som ger en titel och xaxis/yaxis titlar



#Ändra mode i confirmed till lines + markers och ge 
cnfrm.marker <- list(color='orange', size = 1, opacity = 1, line = list(color = 'orange', width = 2))

fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y =~ Confirmed, name = 'Confirmed', mode = 'lines+markers', type = 'scatter', line = cnfrm.line, marker = cnfrm.marker)
fig <- fig %>% add_trace(y =~ Recovered, name = 'Recovered', mode = 'lines', type = 'scatter', line = recovered.line)
fig <- fig %>% add_trace(y =~ Deaths, name = 'Deaths', mode = 'lines', type = 'scatter', line = death.line)
fig

#Ladda in country daywise och filtrera bort alla datum som inte är det senaste datumet. Sortera i fallande ordning
#(störst först, lägst sist) baserat på dödsratio. Lägg även till dödsratio som en kolumn.
#Du som har läst statistik - finns det något att kommentera om ordningen?




#Sortera nu istället på confirmed cases och välj de 10 länder med högst antal confirmed cases.
#Gör en bar plot i plot_ly med valfri med hjälp av layout.





#Vi vill ha sorteringen gjord i bar plotten baserat på antal cases snarare än alfabetisk ordning på länder.
#Kan åtgärdas genom att göra factors av Country. Använd detta tillsammans med färgkodning baserat på death rate
#BONUS! Ordna så att legend syns ordentligt för färgkodningen! Finns ej i facit.

''


#Subplots! Läs in dig på ?subplot och gör upp 3 olika line plots.
#Datan som ska visualiseras är från country_daywise. Filtrera ut endast Indien och arrangera baserat på Date.
#Gör så att de 3 olika subplottarna avser Confirmed, recovered och deaths över tid.




#Scatter plot
#Utgå från confirmed för att göra en scatter plot för de 10 länder med flest confirmed cases.
#

plot_ly(data = latest, x =~Confirmed, y=~Deaths, type = 'scatter', mode = 'markers', color =~Country, colors = heat.colors(n=10), size =~Confirmed, marker = list(size =~1e-4*Deaths))

#Skippa att använda storlek eller färg - använd istället alla länders data (inte bara top 10) i en scatter plot.
#Se till att inte visa legends så att det inte blir plottrigt. utnyttja plotlys interaktivitet för att hovra över några länder
#med låg respektive hög dödlighet. Tänk på att det går att zooma in smidigt!




#Pie chart -  Gör två pie charts - en för antal confirmed och en för antal deaths för de top 10 länderna.




#Slutligen - gör en pie chart med values =~death_rate. Finns det någonting missvisande med valet av visual när
#du utreder detta med en pie chart? Tips - försök att förklara vad storleken för varje land betyder.


