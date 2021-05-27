import numpy as np
from exception import *
import tkinter as tk

def getCF( inputData):

    name = inputData[0]
    surname = inputData[1]
    sex = inputData[2]
    yob = inputData[3]
    mob = inputData[4]
    dob = inputData[5]
    pob = inputData[6]


    CF = extractName(surname) + extractName(name)
    CF += ''.join(list(yob)[-2:])
    CF += str(MtoN[mob])

    if(len(dob)==1):
        dob += '0'
        dob = dob[::-1]

    dobN = int(dob)

    if(sex=='F'): dobN += 40

    CF+=str(dobN)
  
    key_value = np.loadtxt("Codici_ITA.csv", delimiter=";", dtype=str)
    d = { k.upper():v for k,v in key_value }

    key_value2 = np.loadtxt("Codici_EXT.csv", delimiter=";", dtype=str)
    d.update ({ k.upper():v for k,v in key_value2 })

    if not(pob.upper() in d):
        em = "Luogo di nascita non valido. Non posso generare il codice."
        raise PlaceNotFoundError(em)
    else:
        bp = d[pob.upper()]
    
    CF += bp
  

    CF+= controlDigit(CF)
   
    return CF



if __name__ == "__main__":

    print("Fiscal code calculator")
    inpData = inputs()
  
    CF = getCF(inpData)

    if (CF==""):
        print("") 
    else:
        print ("Your fiscal code is " + CF)
    #window = tk.Tk()
    #greeting = tk.Label(text="Hello, Tkinter")
    #greeting.pack()