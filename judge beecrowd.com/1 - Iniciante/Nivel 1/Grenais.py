escolha=0
grenais = 0
vInter = 0
vGremio = 0
empates = 0

while escolha != 2:
    inter, gremio = map(int, input().split())
    grenais += 1
    if inter > gremio:
        vInter+=1
    elif gremio > inter:
        vGremio+=1
    else:
        empates+=1
    escolha = int(input("Novo grenal (1-sim 2-nao)\n"))

print(f"{grenais} grenais")
print(f"Inter:{vInter}")
print(f"Gremio:{vGremio}")
print(f"Empates:{empates}")

if vInter > vGremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")