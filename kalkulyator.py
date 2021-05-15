"""Bu dasdur bilan matematik amallreni bajaramiz"""

a = float(input('son-->'))

while True:
    c = input("amal kiriting->>")
    if c != '=':
        b = float(input('son-->'))
        if c == '+':
            a = a + b
        elif c == '-':
            a = a - b
        elif c == '*':
            a = a * b
        elif c == '/':
            a = a / b
        elif c == '//':
            a = a // b
        elif c == '**':
            a = a ** b
        elif c == 'i':
            a = a ** (1 / b)
        # print(a)
    elif c == '=':
        print(a)
        break
    #     print(a)
    # elif not (c != '=') or not (c != '='):
    #     print("bunaqa amal dasturda mavjud emas")
