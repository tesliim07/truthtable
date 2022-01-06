def getInputs():
    variables=[]
    inputAmount=input("Enter all the variables in the equation: ").upper()
    for i in range(len(inputAmount)):
        if inputAmount[i] in variables:
            continue
        else:
            variables.append(inputAmount[i])
    variables.sort()
    return variables

def truthTable():
    letters=getInputs()
    if len(letters)==1:
        string=''
        for i in range(len(letters)):
            string=string+letters[i]+'|'
        print(string)
        for a in range(0,2):
            print(a)

    elif len(letters)==2:
        string=''
        for i in range(len(letters)):
            string=string+letters[i]+'|'
        print(string)
        for a in range(0,2):
            for b in range(0,2):
                print(a,b)

    elif len(letters)==3:
        string=''
        for i in range(len(letters)):
            string=string+letters[i]+'|'
        print(string)
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    print(a,b,c)

    elif len(letters)==4:
        string=''
        for i in range(len(letters)):
            string=string+letters[i]+'|'
        print(string)
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    for d in range(0,2):
                        print(a,b,c,d)       

    
truthTable()

    




