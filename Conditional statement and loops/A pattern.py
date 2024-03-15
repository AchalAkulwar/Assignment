for row in range(5):
    for column in range(7):
        if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row ==3 )and (column > 1 and column < 5))):
            print("*",end="")
print( )