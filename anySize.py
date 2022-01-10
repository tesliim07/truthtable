

def test(size):
    dim_columns = 2**size
    dim_rows = size
    arr = [[0 for x in range(dim_columns)] for i in range(dim_rows)]

    for var in range(1,size+1):
        for row in range(2**size):
            rowSplit = 2**size/(2**var)
            if (row//rowSplit)%2==1:
                arr[var-1][row]=1
    
        
    print(arr)


test(5)


