import pandas as pd
import numpy as np


vowels = "Aeiou"
MtoN = {1: "A", 2: "B", 3:"C", 4:'D', 5:'E', 6:'H', 7:'L', 8:'M', 9:'P', 10:'R', 11:'S', 12:'T'}
#MtoN={'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'H':6, 'L':'7', 'M':8, 'P':9, 'R':10, 'S':11, 'T':12}

def getCF():
    CF=''
    name = input("Enter first name: ")
    surname = input("Enter last name: ")
    yob = input("Enter year of birth: ")
    mob = int(input("Enter month of birth (in number): "))
    dob = input("Enter day of birth: ")
    pob = input("Enter nation of birth:")
    if (pob.lower()=="italy"):
        pob = input("Enter city of birth:")

    CF += extractName(surname) + extractName(name)
    CF += ''.join(list(yob)[-2:])

    if(len(dob)==1):
        dob += '0'
        dob = dob[::-1]

    CF += str(MtoN[mob]) + dob

    df = pd.read_csv("Codici_ITA.csv", sep=';')

    df.head()

  #  with open('Codici_EXT.csv', mode='r') as infile:
      #  reader = csv.reader(infile)
      #  mydict.update( {rows[0].lower():rows[1] for rows in reader})

   # CF += str(mydict[pob])

    print(CF)


    return 0


def extractName(name):

    if(len(name)<=3):
        while(len(name)<3):
          name += 'X'
        return name.upper()

    cons = [letter.upper() for letter in list(name) if letter.upper() not in vowels.upper()]

    #print ("Cons: ", cons)
    if (len(cons)>3):
        return ''.join([cons[0],cons[2],cons[3]])
    elif(len(cons)==3):
        return ''.join(cons)
    else:
        voc = [letter.upper() for letter in list(name) if letter.upper() in vowels.upper()]
        cons += voc
        return ''.join(cons[:3])        

if __name__ == "__main__":
    getCF()