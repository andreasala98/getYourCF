import numpy as np


vowels = "Aeiou"
MtoN = {1: "A", 2: "B", 3:"C", 4:'D', 5:'E', 6:'H', 7:'L', 8:'M', 9:'P', 10:'R', 11:'S', 12:'T'}
EvenD = {'0': 0, '1':1, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':0, 'B':1, 'C':2,
         'D':3, 'E':4, 'F':5,'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 
         'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25 }
OddD = {'0': 1, '1':0, '2': 5, '3':7, '4':9, '5':13, '6':15, '7':17, '8':19, '9':21, 'A':1, 'B':0, 'C':5,
         'D':7, 'E':9, 'F':13,'G':15, 'H':17, 'I':19, 'J':21, 'K':2, 'L':4, 'M':18, 'N':20, 'O':11, 'P':3, 
         'Q':6, 'R':8, 'S':12, 'T':14, 'U':16, 'V':10, 'W':22, 'X':25, 'Y':24, 'Z':23 }
Rem = {0: 'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L', 12:'M', 13:'N', 
14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y', 25:'Z'}

def getCF():
    CF=''
    name = input("Nome: ")
    surname = input("Cognome: ")
    sex = input("Inserisci F se sei donna, altrimenti qualsiasi altro carattere: ")
    yob = input("Anno di nascita: ")
    mob = int(input("Mese di nascita (numero 1-12): "))
    dob = input("Giorno di nascita: ")
    pob = input("Stato in cui sei nato/a: ")
    if (pob.lower()=="italy"):
        pob = input("Città di nascita: ")

    CF += extractName(surname) + extractName(name)
    CF += ''.join(list(yob)[-2:])

    if(len(dob)==1):
        dob += '0'
        dob = dob[::-1]

    doB = int(dob)

    CF += str(MtoN[mob])
    if(sex=='F'): doB += 40

    CF+=str(doB)
  
    key_value = np.loadtxt("Codici_ITA.csv", delimiter=";", dtype=str)
    d = { k.upper():v for k,v in key_value }

    key_value2 = np.loadtxt("Codici_EXT.csv", delimiter=";", dtype=str)
    d.update ({ k.upper():v for k,v in key_value2 })


    CF += str(d[pob.upper()])

    CF+= controlDigit(CF)

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


def controlDigit(pCF) ->str:
    evens = list(separateString(pCF))
    odds = list(separateString(pCF, get_even=False))
    score: int = 0.0
    for i in range(len(evens)):
        score += EvenD[evens[i]]
        print("Even character " + str(evens[i]) + ", score " + str(EvenD[evens[i]]))
    print("Total even score: ", str(score))
    for j in range(len(odds)):
        score += OddD[odds[j]]
        print("Odd character " + str(odds[j]) + ", score " + str(OddD[odds[j]]))
    print("Total score: ", str(score))
    _ = int(score)%26
    print("Remainder: " + str(_))
    print("Return character " + str(Rem[_]))
    
    return str(Rem[_])


def separateString(word, get_even=True):
    lw=list(word)
    if (get_even==True):
        del lw[::2]
    elif(get_even==False):
        del lw[1::2]
    return ''.join(lw)

if __name__ == "__main__":
    getCF()
