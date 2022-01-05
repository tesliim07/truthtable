def getInputs():
    amount_of_inputs=int(input("Enter the amount of inputs:"))
    variables=[]
    while len(variables)<amount_of_inputs:
        variable=str(input("Enter the variable:")).upper()[0]
        while variable.isalpha()==False:
            variable=str(input("Enter the variable:")).upper()[0]
            continue
        variables.append(variable)
    return amount_of_inputs

getInputs()