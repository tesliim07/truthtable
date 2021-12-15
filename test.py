def getInputs():
    amount_of_inputs=int(input("Enter the amount of inputs:"))
    return amount_of_inputs
def truthTableDesign():
    amount_of_inputs=(getInputs())
    number_in_inputs=2**amount_of_inputs
    half_number_in_inputs=number_in_inputs/2
    integer=int(half_number_in_inputs)
    for a in range(0,2):
        if amount_of_inputs==1:
            print(a)
        for b in range(0,2):
            if amount_of_inputs==2:
                print(a,b)
            for c in range(0,2):
                if amount_of_inputs==3:
                    print(a,b,c)
                for d in range(0,2):
                    if amount_of_inputs==4:
                        print(a,b,c,d)
                    for e in range(0,2):
                        if amount_of_inputs==5:
                            print(a,b,c,d,e)
                        for f in range(0,2):
                            if amount_of_inputs==6:
                                print(a,b,c,d,e,f)

truthTableDesign()