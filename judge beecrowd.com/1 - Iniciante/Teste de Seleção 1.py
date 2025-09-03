a, b, c, d = map(int, input().split())

if (
    a % 2 == 0 and
    b > c and
    d > a and
    (c+d) > (a+b)and
    (c+d) > 0 and
    (a+b) >0 ):
        print("Valores aceitos")
else:
    print("Valores nao aceitos")
