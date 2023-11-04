while True:
    q = input("+ | - | * | / | % | ^ | Выйти из цикла - 1|: ")

    if q == '1':
        break
    else:
        pass

    a = float((input("Первое щисло: ")))
    b = float(input("Второе щисло: "))

    if q == "+":
        print(a+b)
    elif q == '-':
        print(a-b)
    elif q == '*':
        print(a*b)
    elif q == '/':
        print(q/b)
    elif q == '%':
        print(a%b)
    elif q == '^':
        print(a**b)
