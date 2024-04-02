# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:42:21 2024

@author: valie
"""

# Lecture 4 Practice

var = 2 < 10
vartest = [1, 3, 5, 7]

2 in vartest

result = 5 in vartest

print(result)

count_result = 8 not in vartest

print(result)

spring = "Mwen renmen kou sa!"

prlet = spring.startswith("M")

prlet

not prlet

prlet2 = not spring.startswith("M")


prlet3 = spring.find("ren")

print(prlet3)

my_number = "12132a3"

my_number.isnumeric()

type(my_number)

spring == vartest or my_number.isnumeric() == True


datamom = [1, 17, 3, 4, 7, 15, 17, 21, 18, 4, 9, 20, 14, 3, 1]
datadad = [2, 7, 32, 4, 14, 5, 13, 4, 10, 12, 32, 5, 32]

datamom[0:2]


if datamom[1] > 5:
    print(f'Ou pa rantre bon chif la paske {datamom[1]} pi gwo ke 5')
elif datamom[1] == 5:
    print('Ou rantre bon chif la')
else:
    print(f"Chif ou mete a, {datamom[1]}, pi piti ke 5")

bb = range(0, 40, 2)

for i in bb:
    if i < max(datadad):
        print(f'{i} pi piti ke maksimom lis sila')
    elif i > max(datadad):
        print(f'{i} pi gwo ke maksimo lis sila')
    else:
        print(f'{i} se maksimom lis sa')

for i in range(101):
    if i == max(datamom):
        print(f'{i} se maksimom na lis ou genyen an')
        break
    else:
        print(f'{i} pa maksimom lan, kontinye chache toujou')


for i in range(101):
    if i == max(datamom):
        continue
    else:
        print(f'Nou fini ak iterasyon sa. {i} pa maksimom lan, nou pa oblije sote l')

x = 0
while x < max(datamom):
    print(f'{x} pa maksimom lan')
    x += 1


my_first_list_comprehension = [i == max(datamom) for i in range(53)]
my_first_list_comprehension


my_second_list_comprehension = [i for i in range(53) if i == max(datamom)]
my_second_list_comprehension 


my_dictio = {'prem':100, 'dez':200, 'twaz': 34}

for al in my_dictio.keys():
    print(al)

for al in my_dictio.values():
    print(al)

for al in my_dictio.items():
    print(al)

aa, bb, cc = ['No', 'Yes', 'Pa konnen']

aa, bb, cc = [list(al) for al in my_dictio.items()]

ccc = {al:val for al, val in my_dictio.items()}
ccc



start_list = ['a', 'b', 'c', 'd', 'e']
new_dict = {key.upper():None for key in start_list}
print(new_dict)


