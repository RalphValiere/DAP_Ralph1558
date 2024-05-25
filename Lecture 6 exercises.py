# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 23:14:51 2024

@author: valie
"""

class MyfirstClass():
    a = 20
    b = 40
    x = a + b


abot = MyfirstClass()

class MyfirstClass():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.x = a + b


abot = MyfirstClass(10, 20)
inta = abot.x

type(abot)

abot.x


class MyHouse():
    def __init__(self, bedr, bathr, sqrfoot):
        self.bedr = bedr
        self.bathr = bathr
        self.sqrfoot = sqrfoot     
    
    def esti_value(self, interest):
        premvalue = self.bedr * 10
        premsize = self.bathr * 10
        self.interest = interest
        self.value =  (self.sqrfoot * 3) * (premvalue * premsize) - interest * (premvalue * premsize)
        self.reduc = self.pick_city()
        self.total = self.value / self.reduc
        print(f'I estimate the price of this house will be {self.total} Mora')        
    
    def pick_city(self):        
        while True:
            self.region = input('Choose your city ID: ')
            if self.region != '1' and self.region != '0':
                print('You have to choose a valid ID. Insert a correct city ID')                
            elif self.region == '0':
                self.citypercent = 25
                print(f'The Dumbass law reduction rate is {self.citypercent}')
                break
            elif self.region == '1':
                self.citypercent = 17.5
                print(f'The Dumbass law reduction rate is {self.citypercent}')
                break
        return self.citypercent



abot = MyHouse(3, 2, 2110)

abot.esti_value(0.05)

