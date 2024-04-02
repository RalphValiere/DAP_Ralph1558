# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 22:37:14 2024

@author: valie
"""

test = 2
type(test)

test_2 = 4

z = test ** 2 + test_2 / 7 

type(z)
print(type(z))

test += 2
print(test)

test == test_2

test == z

test != z

ab = True

ab != (test != z)

ab + test

ab + 0

title  = 'Manman'

print(title)


title_2 = 'M pa konprann sa k ap pase a"'

print(title)

title_final = title + ' ' + title_2

title_final += ' , a man of honor'

print(title_final)

print(title_final.upper())

uppertitle = title_final.capitalize()
print(uppertitle)


print(title_final)

titpam = " Ou lach anpil "

print(titpam.strip().upper())

kantite = 2
soutit = f'Kisa pou m ta di w la menm? Mwen vann {kantite} soulye depi m maten'
soutit_2 = 'Tante vann {} pou mwen'.format(kantite)
soutit_3 = 'Pa fe m bagay sa. Se %s plat mwen vann wi depi le m rive a.' % kantite
print(soutit)
print(soutit_2)
print(soutit_3)


pati = ['Pitit Desalin', 'Montana', 'RED']
lajan_pati = [1500, 2400, 3500]
type(pati)
type(lajan_pati)
print(pati)
print(lajan_pati)

len(lajan_pati)
print(lajan_pati[0], pati[0])

lajan_pati[2:]
lajan_pati[:2]

full_info = pati + lajan_pati
print(full_info)

full_info[::2]

lis_konple = [test, title_final, lajan_pati, pati, soutit]

print(lis_konple)

lis_konple[-2][-3]

my_tuple = (12, 21, 34, 35, 23, 21, 35)

my_first_set = {12, 21, 34, 35, 23, 21, 35}

print(my_first_set)

lis_konple[3][0][::-1]

my_first_dictionary = {pati[0]:2}
print(my_first_dictionary)
my_first_dictionary['Pitit Desalin']


import datetime

mydate = datetime.datetime(2024, 3, 6) 
print(mydate)
mydate.year
mydate.month
mydate.day
mydate.minute

mydatenow = datetime.datetime.now() - datetime.datetime(2024, 3, 6) 
print(mydatenow)
