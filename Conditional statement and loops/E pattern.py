
for row in range(7):
    for column in range(5):
            if column==0 or row==0 or (row==3 and column!=3)or row==6:
                print("*",end=" ")
    print( )