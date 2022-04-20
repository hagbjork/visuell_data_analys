#install.packages('lubridate')
#install.packages('plotly')
#install.packages('tidyverse')

library(tidyverse)
library(plotly)
library(lubridate)

data_daywise <- read_csv("daywise.csv")
data_daywise$Date <- ymd(data_daywise$Date)

head(data_daywise)

#Sortera p� Date ist�llet f�r land
data_daywise <- arrange(data_daywise, Date)


head(data_daywise)


#G�r en line plot av confirmed cases �ver tid.

#Facit:
plot_ly(data_daywise, x = ~Date, y = ~Confirmed, 
        type = 'scatter',mode = 'lines')


#L�gg med pipe operator till 3 lines med add_trace till 
#fig - confirmed, recovered och deaths. 
#Ser n�gonting konstigt ut?
#Kan du spekulera om n�gon f�rklaring?

fig <- plot_ly(data_daywise, x=~ Date)
#Facit: (K�llan slutade bara att rapportera recovered cases 
#�r f�rklaringen)
fig <- fig %>% add_trace(y = ~Confirmed, name = 'Confirmed', 
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Recovered, name = 'Recovered', 
                         mode = 'lines', type = 'scatter')
fig <- fig %>% add_trace(y = ~Deaths, name = 'Deaths', 
                         mode = 'lines', type = 'scatter')
fig

#Add_trace tar ocks� in line som argument 
#- en lista d�r vi kan inkludera f�rg och storlek.
#Justera linjernas form och f�rg genom att g�ra 3 listor 
#och l�gg till i figuren.

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

#L�gg till ett layoutargument med pipe operator som ger en 
#titel och xaxis/yaxis titlar
#Facit:
fig <- fig %>% layout(title = 'Total Cases World Wide', 
                      xaxis = list(title = 'Date'), 
                      yaxis = list(title = 'Total Cases'))
fig

#�ndra mode i confirmed till lines + markers och ge 
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
#inte �r det senaste datumet. Sortera i fallande ordning
#(st�rst f�rst, l�gst sist) baserat p� d�dsratio. 
#L�gg �ven till d�dsratio som en kolumn.
#Du som har l�st statistik - finns det n�got att kommentera 
#om ordningen?

#Facit: Det g�r givetvis inte med statistisk signifikans 
#s�ga att MS Zaandam 
#eller Vanuatu har h�gst d�dsratio i v�rlden.
data_countrywise <- read_csv("country_daywise.csv")
head(data_countrywise)
latest <- data_countrywise %>% 
  filter(Date == max(Date)) %>% 
  arrange(desc(Deaths/Confirmed))
latest$death_rate <- round(latest$Deaths/latest$Confirmed, 
                           digits = 3)
head(latest)

#Sortera nu ist�llet p� confirmed cases och v�lj de 10 l�nder
#med h�gst antal confirmed cases.
#G�r en bar plot i plot_ly med valfri med hj�lp av layout.

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

#Vi vill ha sorteringen gjord i bar plotten baserat p� 
#antal cases snarare �n alfabetisk ordning p� l�nder.
#Kan �tg�rdas genom att g�ra factors av Country. 
#Anv�nd detta tillsammans med f�rgkodning baserat p� death rate
#BONUS! Ordna s� att legend syns ordentligt f�r 
#f�rgkodningen! Finns ej i facit.

#Facit - saknar dock legend!
latest$Country <- factor(latest$Country, 
                         levels = c(as.character(latest$Country)))
p <- plot_ly(latest, x =~Country, y =~Confirmed, 
             text =~death_rate, 
             type = 'bar', 
             name = 'Confirmed Cases', 
             marker = list(color =~death_rate))
p


#Subplots! L�s in dig p� ?subplot och g�r upp 3 olika line plots.
#Datan som ska visualiseras �r fr�n country_daywise. 
#Filtrera ut endast Indien och arrangera baserat p� Date.
#G�r s� att de 3 olika subplottarna avser Confirmed, 
#recovered och deaths �ver tid.

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
#Utg� fr�n confirmed f�r att g�ra en scatter plot f�r de 10 
#l�nder med flest confirmed cases.
#

plot_ly(data = latest, x =~Confirmed, y=~Deaths, 
        type = 'scatter', 
        mode = 'markers', 
        color =~Country, 
        colors = heat.colors(n=10), 
        size =~Confirmed, 
        marker = list(size =~1.5e3*death_rate))

#Skippa att anv�nda storlek eller f�rg - 
#anv�nd ist�llet alla l�nders data (inte bara top 10) 
#i en scatter plot.
#Se till att inte visa legends s� att det inte blir plottrigt. 
#utnyttja plotlys interaktivitet f�r att hovra �ver n�gra l�nder
#med l�g respektive h�g d�dlighet. 
#T�nk p� att det g�r att zooma in smidigt!

#Facit:
data <- read_csv("country_daywise.csv") %>% 
  filter(Date == max(Date))
plot_ly(data = data, x =~Confirmed, y=~Deaths, 
        type = 'scatter', 
        mode = 'markers', 
        name =~Country, 
        showlegend = F)


#Pie chart -  G�r tv� pie charts - en f�r antal confirmed och 
#en f�r antal deaths f�r de top 10 l�nderna.

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

#Slutligen - g�r en pie chart med values =~death_rate. 
#Finns det n�gonting missvisande med valet av visual n�r
#du utreder detta med en pie chart? 
#Tips - f�rs�k att f�rklara vad storleken f�r varje land betyder.
fig3 <- plot_ly(latest, labels =~Country, 
                values =~death_rate, 
                type = 'pie', 
                textinfo = 'label')
fig3

