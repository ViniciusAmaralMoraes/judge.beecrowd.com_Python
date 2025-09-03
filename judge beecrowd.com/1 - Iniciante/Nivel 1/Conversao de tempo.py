N = int(input())

segundos = N % 60
minutos = N // 60
horas = minutos // 60
minutos = minutos % 60

print(f"{horas}:{minutos}:{segundos}")


