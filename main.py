import numpy as np
from exception import *
import tkinter as tk

def getCF():
    try:
        [name, surname, sex, yob, mob, dob, pob] = inputs()
    except ValueError:
        raise OutOfRangeError("Some parameters were out of range!")
  

    CF = extractName(surname) + extractName(name)
    CF += ''.join(list(yob)[-2:])
    CF += str(MtoN[mob])

    if(len(dob)==1):
        dob += '0'
        dob = dob[::-1]

    if(sex=='F'): dob += 40

    CF+=str(dob)
  
    key_value = np.loadtxt("Codici_ITA.csv", delimiter=";", dtype=str)
    d = { k.upper():v for k,v in key_value }

    key_value2 = np.loadtxt("Codici_EXT.csv", delimiter=";", dtype=str)
    d.update ({ k.upper():v for k,v in key_value2 })

    if not(pob in d):
        bp='0000'
    else:
        bp = d[pob.upper()]
    
    CF += bp
  

    CF+= controlDigit(CF)
   
    return CF



if __name__ == "__main__":
    print("Hi, your fiscal code is")
    print(getCF())
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()