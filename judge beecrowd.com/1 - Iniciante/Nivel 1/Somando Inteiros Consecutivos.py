valores = list(map(int, input().split()))

a = valores[0]
n = valores[1]
cont= 2
while n <= 0:
    n = valores[cont]
    cont+=1
soma = 0
for i in range(n):
    soma+=(a + i)

print(soma)