import os
import pathlib
import numpy as np
from exception import *


class Extractor():
    def __init__(self,):
        self.CF = ''

    def parse_data(self,):
        self.name = input("Nome: ").replace(' ','')
        self.surname = input("Cognome: ").replace(' ','')
        self.sex = input("Sesso (M/F): ")
        self.yob = int(input("Anno di nascita: "))
        self.mob = int(input("Mese di nascita (numero 1-12): "))
        self.dob = int(input("Giorno di nascita: "))
        self.pob = input("Stato in cui sei nato/a: ")
        if (self.pob.lower()=="italia"):
            self.pob = input("Città di nascita: ")

        #checks 
        if self.sex not in ['M', 'F']:
            raise OutOfRangeError("Invalid gender!")
      
        if not (1900 <= self.yob <= 2022):
            raise OutOfRangeError("Invalid year of birth!")

        if not (1 <= self.mob <= 12):
            raise OutOfRangeError("Invalid month!")

        if not (1 <= self.dob <= 31):
            raise OutOfRangeError("Invalid day of birth!")


    def get_first_name(self,):
        if(len(self.name)<=3):
            while(len(self.name)<3):
              self.name += 'X'
            return self.name.upper()

        cons = [letter.upper() for letter in list(self.name) if letter.upper() not in vowels.upper()]

        if (len(cons)>3):
            return ''.join([cons[0],cons[2],cons[3]])
        elif(len(cons)==3):
            return ''.join(cons)
        else:
            voc = [letter.upper() for letter in list(self.name) if letter.upper() in vowels.upper()]
            cons += voc
            return ''.join(cons[:3])        
    

    def get_last_name(self,):
        if(len(self.surname)<=3):
            while(len(self.surname)<3):
              self.surname += 'X'
            return self.surname.upper()

        cons = [letter.upper() for letter in list(self.surname) if letter.upper() not in vowels.upper()]
        if (len(cons)>=3):
            return ''.join([cons[0],cons[1],cons[2]])
        else:
            voc = [letter.upper() for letter in list(self.surname) if letter.upper() in vowels.upper()]
            cons += voc
            return ''.join(cons[:3])  


    def get_birthdate(self,):
        date = ''.join(list(str(self.yob))[-2:]) 
        date += month_to_number[self.mob]
        if(len(str(self.dob))==1):
            self.dob += '0'
            self.dob = int(str(self.dob)[::-1])
        if self.sex=='F':
            self.dob += 40
        date += str(self.dob)
        return date


    def get_birthplace(self,):
        data_dir = os.path.join(pathlib.Path(__file__).parent.parent.parent, 'data')
        ita = np.loadtxt(os.path.join(data_dir, "Codici_ITA.csv"), delimiter=";", dtype=str)
        ext = np.loadtxt(os.path.join(data_dir, "Codici_EXT.csv"), delimiter=";", dtype=str)
        
        d = { k.upper():v for k,v in ita}
        d.update ({ k.upper():v for k,v in ext})

        if not(self.pob.upper() in d.keys()):
            err_msg = "Luogo di nascita non valido. Non posso generare il codice."
            raise PlaceNotFoundError(err_msg)
        
        return d[self.pob.upper()]


    def get_control_digit(self,):
        evens = list(self.__sep_str__(self.CF))
        odds = list(self.__sep_str__(self.CF, get_even=False))
        score = 0

        for i in range(len(evens)):
            score += even_digit[evens[i]]
        for j in range(len(odds)):
            score += odd_digit[odds[j]]
        score = int(score)%26
        return str(remainder[score])

    @staticmethod
    def __sep_str__(word, get_even=True):
        lw=list(word)
        if (get_even==True):
            del lw[::2]
        elif(get_even==False):
            del lw[1::2]
        return ''.join(lw)


    def run(self,):
        self.parse_data()
        self.CF = self.get_last_name() + self.get_first_name()
        self.CF += self.get_birthdate() + self.get_birthplace()
        self.CF += self.get_control_digit()

        return self.CF