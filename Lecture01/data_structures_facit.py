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
    return [x**2 for x in range(max_value)]


def filtered_list_comprehension(max_value: int) -> List:
    '''
    Returns a list of even, squared values in a range specified by max_value.

    Args in: max_value denoting the value of the last number to be squared.

    Returns: List of squared values starting at 0 incremented by 1 at each step.
    '''

    #TODO - Samma som ovan, men filtrera bort alla kvadrater med udda värden!
    return [x**2 for x in range(max_value) if x%2 ==0]


def squared_tuples(max_value: int) -> List:
    '''
    Returns a list of tuples with (x, x**2) from a range specified by max_value

    Args in: max_value denoting the value of the last number to be squared.

    Returns: List of tuples 
    '''
    #TODO - gör en lista med tuples där index 0 i varje tuple är det ursprungliga värdet och index 1 är det kvadrerade värdet.
    return [(x,x**2) for x in range(max_value)]



def recursion(input_iterable, index):
    '''
    Recursively computes the sum of an input iterable starting from a specified index.

    Args in: input_iterable - iterable to be summed recursively
             index - 
    '''

    #TODO - Gör en funktion som rekursivt beräknar summan utav en lista eller array med start i specificerat index.
    #T.ex. - input recursion([1,2,3,4,5], 3) ska ge tillbaks 4+5
    #Hard mode - gör detta med en rad kod!
    return input_iterable[index] if index == len(input_iterable) - 1 else input_iterable[index] + recursion(input_iterable, index + 1)


def matrix_to_dict(matrix):
    '''
    Returns a dictionary of matrix rows where each row is 
    '''

    #TODO - Gör en funktion som tar in en matris och för varje rad summerar produkten av raden och lägger 
    #Exempel: [1,2,3,4] -> 1*4 + 2*3 + 3*2 + 4*1, returnerar {0:20}
    #Hard mode - gör detta med en rad kod (inklusive return statement)
    return {i:np.dot(row,np.flip(row)) for i, row in enumerate(matrix)}


def dict_generator(max_value):
    #TODO - Gör en funktion som ger tillbaks dictionaryt {"0":0, "1":1, "2":2... "max_value":max_value} om max_value är över 40
    #annars {"0":max_value, "1":max_value - 1}.
    #Hard mode: gör detta med en rad kod (inklusive return statement)
    return {str(i): max_value - i for i in range(max_value)} if max_value > 40 else {str(i): i for i in range(max_value)}

def args_n_kwargs(*args, **kwargs):
    #TODO - Gör en funktion som kan ta in hur många positional arguments som helst och därefter hur många key word arguments som helst.
    #Funktionen behöver bara printa varje arg och kwarg.
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

def function_calling_function(func1, func2, max_value):
    #TODO- Gör en funktion som tar in 2 funktioner och ett maxvärde.
    #Funktionen ska kunna ta in vilket antal positional arguments som helst och vilket antal key word arguments som helst.
    #Skicka in my_dict_generator och args_n_kwargs

    my_dict = func2(max_value)

    func1(1,2,3,4,5,6,1,**my_dict)


print('list_comprehension_squares:', list_comprehension_squares(6))
print('filtered_list_comprehension:', filtered_list_comprehension(10))
print('squared_tuples:', squared_tuples(3))
print('recursion:', recursion([1,2,3,4,5], 2))
print('matrix_to_dict:', matrix_to_dict([1,2,3,4]))
print('dict_generator:', dict_generator(5))