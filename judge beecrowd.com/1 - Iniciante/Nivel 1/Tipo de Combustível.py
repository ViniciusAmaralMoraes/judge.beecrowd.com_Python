alcool = 0
gasolina = 0
diesel = 0

while True:
    escolha= int(input())
    if escolha == 1:
        alcool+=1
    elif escolha == 2:
        gasolina+=1
    elif escolha == 3:
        diesel+=1
    elif escolha ==4:
        break
    else:
        continue

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")