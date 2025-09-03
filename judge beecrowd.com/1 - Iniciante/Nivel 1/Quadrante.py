while True:
    y , x = map(int, input().split())
    if y > 0 and x > 0:
        print("primeiro")
    elif y < 0 and x > 0:
        print("segundo")
    elif y < 0 and x < 0:
        print("terceiro")
    elif y > 0 and x < 0:
        print("quarto")
    else:
        break