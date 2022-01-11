def getInputs():
    variables=[]
    inputAmount=input("Please enter all the variables in the equation: ").upper()
    for i in range(len(inputAmount)):
        if inputAmount[i] in variables:
            continue
        else:
            variables.append(inputAmount[i])
    variables.sort()
    return variables

def truthTable():
    letters=getInputs()
    size=len(letters)
    dim_columns = 2**size
    dim_rows = size
    arr = [[0 for x in range(dim_columns)] for i in range(dim_rows)]

    for var in range(1,size+1):
        for row in range(2**size):
            rowSplit = 2**size/(2**var)
            if (row//rowSplit)%2==1:
                arr[var-1][row]=1

    for j in range(len(letters)):
        for items in arr[j]:
            print(items)

    
        
    

truthTable()
    




