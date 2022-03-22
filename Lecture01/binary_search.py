import time
import numpy as np
import random

#Låt n variera lite - den styr hur många element vi har i vår array
n = 100
#Antal försök vi gör
k = 100
#Vi sätter upp en array att leta i 
arr = np.arange(n)
value_list = [val for val in range(n)]

start_time = time.time()
for i in range(k):
    #Binärsökning med numpy för sorterad array: Vid varje sökning halverar vi mängden element vi betraktar.
    value = random.randint(0, n-1)
    #I vilket index finns värdet vi har slumpat?
    index_of_value = np.searchsorted(arr, value)
    #TODO - Your code here: Leta efter indexet i listan för det slumpade valuet
    #Stega genom listan, jämför värdet i varje index mot ditt slumpade value. Är de samma -> fortsätt loopa över k (förtydligande)
    for value in value_list:
        if value == index_of_value:
         print(value, 'är talet vi letar efter')
    
    ''' for x in range(index_of_value):
        if x == value: break '''

stop_time = time.time()
time_elapsed = stop_time - start_time

print(f'Total time elapsed: {time_elapsed}')