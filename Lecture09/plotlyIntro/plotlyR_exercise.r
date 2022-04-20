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

#Sortera p� Date ist�llet f�r land
data_daywise <- arrange(data_daywise, Date)
head(data_daywise)


#G�r en line plot av confirmed cases �ver tid.
fig <- plot_ly(x = as.Date(data_daywise$Date), y = data_daywise$Confirmed, 
               type = 'scatter',
               mode = 'lines',
               color = 'red')
fig

fig <- fig %>%  layout(title = 'Confirmed covid cases by date', 
                       yaxis = list(title = 'Number of confirmed cases'), 
                       xaxis = list(title = 'Date'))
fig


#L�gg med pipe operator till 3 lines med add_trace till fig - confirmed, recovered och deaths. Ser n�gonting konstigt ut?
#Kan du spekulera om n�gon f�rklaring?
fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y = ~Confirmed, name = 'Confirmed',
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Recovered, name = 'Recovered',
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Deaths, name = 'Deaths',
                         mode = 'lines', type = 'scatter')
fig

#Aug 4 2021 s� g�r recovered fr�n 130.899milj till 0. 


#Add_trace tar ocks� in line som argument - en lista d�r vi kan inkludera f�rg och storlek.
#Justera linjernas form och f�rg genom att g�ra 3 listor och l�gg till i figuren.
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

#L�gg till ett layoutargument med pipe operator som ger en titel och xaxis/yaxis titlar



#�ndra mode i confirmed till lines + markers och ge 
cnfrm.marker <- list(color='orange', size = 1, opacity = 1, line = list(color = 'orange', width = 2))

fig <- plot_ly(data_daywise, x=~ Date)
fig <- fig %>% add_trace(y =~ Confirmed, name = 'Confirmed', mode = 'lines+markers', type = 'scatter', line = cnfrm.line, marker = cnfrm.marker)
fig <- fig %>% add_trace(y =~ Recovered, name = 'Recovered', mode = 'lines', type = 'scatter', line = recovered.line)
fig <- fig %>% add_trace(y =~ Deaths, name = 'Deaths', mode = 'lines', type = 'scatter', line = death.line)
fig

#Ladda in country daywise och filtrera bort alla datum som inte �r det senaste datumet. Sortera i fallande ordning
#(st�rst f�rst, l�gst sist) baserat p� d�dsratio. L�gg �ven till d�dsratio som en kolumn.
#Du som har l�st statistik - finns det n�got att kommentera om ordningen?




#Sortera nu ist�llet p� confirmed cases och v�lj de 10 l�nder med h�gst antal confirmed cases.
#G�r en bar plot i plot_ly med valfri med hj�lp av layout.





#Vi vill ha sorteringen gjord i bar plotten baserat p� antal cases snarare �n alfabetisk ordning p� l�nder.
#Kan �tg�rdas genom att g�ra factors av Country. Anv�nd detta tillsammans med f�rgkodning baserat p� death rate
#BONUS! Ordna s� att legend syns ordentligt f�r f�rgkodningen! Finns ej i facit.

''


#Subplots! L�s in dig p� ?subplot och g�r upp 3 olika line plots.
#Datan som ska visualiseras �r fr�n country_daywise. Filtrera ut endast Indien och arrangera baserat p� Date.
#G�r s� att de 3 olika subplottarna avser Confirmed, recovered och deaths �ver tid.




#Scatter plot
#Utg� fr�n confirmed f�r att g�ra en scatter plot f�r de 10 l�nder med flest confirmed cases.
#

plot_ly(data = latest, x =~Confirmed, y=~Deaths, type = 'scatter', mode = 'markers', color =~Country, colors = heat.colors(n=10), size =~Confirmed, marker = list(size =~1e-4*Deaths))

#Skippa att anv�nda storlek eller f�rg - anv�nd ist�llet alla l�nders data (inte bara top 10) i en scatter plot.
#Se till att inte visa legends s� att det inte blir plottrigt. utnyttja plotlys interaktivitet f�r att hovra �ver n�gra l�nder
#med l�g respektive h�g d�dlighet. T�nk p� att det g�r att zooma in smidigt!




#Pie chart -  G�r tv� pie charts - en f�r antal confirmed och en f�r antal deaths f�r de top 10 l�nderna.




#Slutligen - g�r en pie chart med values =~death_rate. Finns det n�gonting missvisande med valet av visual n�r
#du utreder detta med en pie chart? Tips - f�rs�k att f�rklara vad storleken f�r varje land betyder.


