count_of_first_names = {}
my_cool_list = [["Test", "Testsson"], ["Test2", "Testsson2"], ["Test", "Testsson"]]



for sublist in my_cool_list:
    #Så vi går över varje index
    print(sublist)
    #Vi kollar förnamn - ifall det inte finns där, lägger vi till det
    if sublist[0] not in count_of_first_names:
        count_of_first_names[sublist[0]] = 1
    else:
        count_of_first_names[sublist[0]] += 1
print(count_of_first_names.items())

print(count_of_first_names)

final_list =[]

for sublist in my_cool_list:
    #Kollar om value för varje förnamn i vår dictionary är större än 1 - fattar beslut om vad vi skickar vidare
    #baserat på det 

    #.....
    final_list.append(result)
