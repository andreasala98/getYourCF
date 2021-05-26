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

    dob_num = int(dob)

    if(sex.upper()=='F'): dob_num += 40

    CF+=str(dob_num)
  
    key_value = np.loadtxt("Codici_ITA.csv", delimiter=";", dtype=str)
    d = { k.upper():v for k,v in key_value }

    key_value2 = np.loadtxt("Codici_EXT.csv", delimiter=";", dtype=str)
    d.update ({ k.upper():v for k,v in key_value2 })

    
    bp = d[pob.upper()]
    
    CF += bp
  
    CF += controlDigit(CF)
   
    return CF



if __name__ == "__main__":
    print("## Fiscal Code Calculator ##")
    print(getCF())