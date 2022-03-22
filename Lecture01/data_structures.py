from ast import Return
from typing import *
import numpy as np


def list_comprehension_squares(max_value: int) -> List:
    '''
    Returns a list of squared values in a range specified by max_value.

    Args in: max_value denoting the value of the last number to be squared.

    Returns: List of squared values starting at 0 incremented by 1 at each step.
    '''
    #TODO - gör en funktion med list comprehension som ger tillbaks listan av kvadrerade värden upp till och med 
    # max_value ([0, 1, 4, 9, 16... max_value**2])
    list = []
    for i in range(max_value):
        li = i**2
        list.append(li)
    return list

def filtered_list_comprehension(max_value: int) -> List:
    '''
    Returns a list of even, squared values in a range specified by max_value.

    Args in: max_value denoting the value of the last number to be squared.

    Returns: List of squared values starting at 0 incremented by 1 at each step.
    '''

    #TODO - Samma som ovan, men filtrera bort alla kvadrater med udda värden!
    list = []
    for i in range(max_value):
        li = i**2
        if li % 2 == 0:
                list.append(li)
    return list

def squared_tuples(max_value: int) -> List:
    '''
    Returns a list of tuples with (x, x**2) from a range specified by max_value

    Args in: max_value denoting the value of the last number to be squared.

    Returns: List of tuples 
    '''
    #TODO - gör en lista med tuples där index 0 i varje tuple är det ursprungliga värdet och index 1 är det kvadrerade värdet.
    return [(x,x**2) for x in range(max_value)]



def recursion(input_iterable: List, index: int) -> float:
    '''
    Recursively computes the sum of an input iterable starting from a specified index.

    Args in: input_iterable - iterable to be summed recursively
             index - index to start the summation from.
    '''

    #TODO - Gör en funktion som rekursivt beräknar summan utav en lista eller array med start i specificerat index.
    #T.ex. - input recursion([1,2,3,4,5], 3) ska ge tillbaks 4+5
    #Hard mode - gör detta med en rad kod!
    pass


def matrix_to_dict(matrix:np.ndarray)->dict:
    '''
    Returns a dictionary of matrix rows where each key is the number of the row and the value 
    is the sum of products row times the row in reverse.
    
    Args in: matrix - 2d array of float values
    
    Returns: dictionary of {int:int}
    '''

    #TODO - Gör en funktion som tar in en matris och för varje rad summerar produkten av raden och lägger 
    #Exempel: [1,2,3,4] -> 1*4 + 2*3 + 3*2 + 4*1, returnerar {0:20}
    #Hard mode - gör detta med en rad kod (inklusive return statement)
    pass


def dict_generator(max_value:int)->dict:
    #TODO - Gör en funktion som ger tillbaks dictionaryt {"0":0, "1":1, "2":2... "max_value":max_value} om max_value är över 40
    #annars {"0":max_value, "1":max_value - 1}.
    #Hard mode: gör detta med en rad kod (inklusive return statement)
    pass

def args_n_kwargs(*args, **kwargs):
    #TODO - Gör en funktion som kan ta in hur många positional arguments som helst och därefter hur många key word arguments som helst.
    #Funktionen behöver bara printa varje arg och kwarg.
    pass

def function_calling_function(func1, func2, max_value):
    #TODO- Gör en funktion som tar in 2 funktioner och ett maxvärde.
    #Skicka in my_dict_generator och args_n_kwargs och max_value

    pass

print(list_comprehension_squares(5))
print(filtered_list_comprehension(20))
print(squared_tuples(5))