n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    try:
        divisao = x / y
        print(f"{divisao:.1f}")
    except ZeroDivisionError:
        print("divisao impossivel")
