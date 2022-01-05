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

def truthTableDesign():
    amount_of_inputs=(getInputs())
    number_in_inputs=2**amount_of_inputs
    half_number_in_inputs=number_in_inputs/2
    integer=int(half_number_in_inputs)
    
    if amount_of_inputs==1:
        print("A")
        for a in range(0,2):
            str_a=str(a)
            print(a)

    elif amount_of_inputs==2:
        print("A|B")
        for a in range(0,2):
            for b in range(0,2):
                str_a,str_b=str(a),str(b)
                print(a,b)

    elif amount_of_inputs==3:
        print("A|B|C")
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    str_a,str_b,str_c=str(a),str(b),str(c)
                    print(a,b,c)

    elif amount_of_inputs==4:
        print("A|B|C|D")
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):   
                    for d in range(0,2):
                        str_a,str_b,str_c,str_d=str(a),str(b),str(c),str(d)
                        print(a,b,c,d)

    elif amount_of_inputs==5:
        print("A|B|C|D|E")
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):   
                    for d in range(0,2):
                        for e in range(0,2):
                            str_a,str_b,str_c,str_d,str_e=str(a),str(b),str(c),str(d),str(e)
                            print(a,b,c,d,e)

    elif amount_of_inputs==6:
        print("A|B|C|D|E|F")
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):   
                    for d in range(0,2):
                        for e in range(0,2):
                            for f in range(0,2):   
                                str_a,str_b,str_c,str_d,str_e=str(a),str(b),str(c),str(d),str(e)
                                print(a,b,c,d,e,f)



getInputs()
