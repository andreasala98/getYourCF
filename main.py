import numpy as np



vowels = "Aeiou"
MtoN = {1: "A", 2: "B", 3:"C", 4:'D', 5:'E', 6:'H', 7:'L', 8:'M', 9:'P', 10:'R', 11:'S', 12:'T'}

def getCF():
    CF=''
    name = input("Enter first name: ")
    surname = input("Enter last name: ")
    sex = input("Enter F if you are female, otherwise any other letter:")
    yob = input("Enter year of birth: ")
    mob = int(input("Enter month of birth (in number): "))
    dob = input("Enter day of birth: ")
    pob = input("Enter nation of birth: ")
    if (pob.lower()=="italy"):
        pob = input("Enter city of birth: ")

    CF += extractName(surname) + extractName(name)
    CF += ''.join(list(yob)[-2:])

    if(len(dob)==1):
        dob += '0'
        dob = dob[::-1]

    doB = int(dob)

    CF += str(MtoN[mob])
    if(sex=='F'): doB += 40

    CF+=doB
  
    key_value = np.loadtxt("Codici_ITA.csv", delimiter=";", dtype=str)
    d = { k.upper():v for k,v in key_value }

    print(d)

    CF += str(d[pob.upper()])


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