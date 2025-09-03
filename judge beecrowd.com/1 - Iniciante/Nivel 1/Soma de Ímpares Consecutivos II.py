N = int(input())

for i in range(N):
    X,Y = map(int,input().split())
    if Y > X :
       X , Y =  Y , X

    soma = 0
    for i in range(Y+1, X):
        if i % 2 != 0:
            soma += i
    print(soma)