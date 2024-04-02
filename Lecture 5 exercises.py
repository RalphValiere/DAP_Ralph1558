# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 00:52:56 2024

@author: valie
"""

# Lecture 5 Exercise

# Function with arguments
def my_first_function(chif):
    rezilta = chif ** 5 - 2024
    final = print(f'Kantite lajan w ka espere genyen nan loto sa se {rezilta}')
    return final


my_first_function(5)
str
int
int()
my_first_function(10)


# Function with key arguments

def second_function(chif, peyi = "Ayiti", to_chanj = 150):
    rezilta = chif ** 5 - 2024
    rezilta_goud = rezilta * to_chanj
    final = print(f'Kantite lajan w ka espere genyen nan loto sa se {rezilta} dola ameriken. Pou {peyi}, sa reprezante {rezilta_goud}')
    return final

second_function(10, peyi = 'Dominik')


x = [2, 2, 4, 5, 12, 2, 7, 6, 21, 2, 1, 5, 10, 10]

ab = []

for i in x:
    if i == 2:
        rez = i ** 2
    elif i == 1:
        rez = i + 3 
    else:
        rez = i - 2
    ab.append(rez)
print(ab)

# Exercise from the lecture


names_2021 = [' jeff', 'molly', 'YIJIA', 'Jon', 'RaHuL', 'noah ', 'Bob']

names_2020 = ['JEFF', ' sarah', 'Simo n', 'Sawyer']


def name_fixer(n):
    n = n.strip().capitalize()
    if n == 'Jon':
        result = 'John'
    elif n == 'Bob':
        result = 'Bob does not work here any more!'
    elif n == 'Simo n':
        result = 'Simon'
    else:
        result = n
    return result

fixed_names = [name_fixer(n) for n in names_2021]
print(fixed_names)

new_fixed_names = [name_fixer(n) for n in names_2020]
print(new_fixed_names)


def name_fixer_prime(namelist):
    list_change = []
    for n in namelist:
        n = n.strip().capitalize()
        if n == 'Jon':
            result = 'John'
        elif n == 'Bob':
            result = 'Bob does not work here any more!'
        elif n == 'Simo n':
            result = 'Simon'
        else:
            result = n
        list_change.append(result)
    return print(list_change)


name_fixer_prime(names_2020)
name_fixer_prime(names_2021)


