X = int(input())
Y = int(input())
if (Y > X):
  #X , Y  =  Y , X
    for i in range(X + 1, Y ):
        if (i%5==2) or (i%5==3):
            print(i)
elif (X > Y):
  #Y , X = X , Y
    for i in range(Y + 1, X ):
        if (i%5==3) or (i%5==2):
            print(i)