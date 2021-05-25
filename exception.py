class OutOfRangeError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)

class PlaceNotFoundError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)

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


def inputs():
    data=[]
    data.append( input("Nome: "))
    data.append( input("Cognome: "))
    data.append(input("Sesso (M/F): "))
    data.append(input("Anno di nascita: "))
    data.append(int(input("Mese di nascita (numero 1-12): ")))
    data.append(input("Giorno di nascita: "))
    pob = input("Stato in cui sei nato/a: ")
    if (pob.lower()=="italia"):
        pob = input("Città di nascita: ")
    data.append(pob)

    if (data[2]!=('M'or'F')):
        raise OutOfRangeError("Invalid gender!")

    if (int(data[3])>2021 or int(data[3])<1900):
        raise OutOfRangeError("Invalid year of birth!")

    if (int(data[4]) not in range(1,13)):
        raise OutOfRangeError("Invalid month!")

    if (int(data[5]) not in range(1,32)):
        raise OutOfRangeError("Invalid day of birth!")


    return data

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
    for j in range(len(odds)):
        score += OddD[odds[j]]
    _ = int(score)%26
    return str(Rem[_])


def separateString(word, get_even=True):
    lw=list(word)
    if (get_even==True):
        del lw[::2]
    elif(get_even==False):
        del lw[1::2]
    return ''.join(lw)