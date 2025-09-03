validacao = 0
soma = 0.0

while validacao < 2:
    notas = float(input())
    if 0<= notas <=10:
        soma+=notas
        validacao+=1
    else:
        print("nota invalida")


media = soma /2
print(f"media = {media:.2f}")
