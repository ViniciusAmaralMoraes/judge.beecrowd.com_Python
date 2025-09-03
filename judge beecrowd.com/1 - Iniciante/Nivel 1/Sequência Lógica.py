try:
    N= int(input())
    if 1 < N < 1000:
        for i in range(1,N+1):
            print(f"{i} {i**2} {i**3}")
            print(f"{i} {i ** 2+1} {i ** 3+1}")
    else:
        print("O valor de N deve ser um número inteiro entre 2 e 999.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")


