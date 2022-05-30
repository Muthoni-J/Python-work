x = range(20)
for y in x:
    if y%2==0 and y%3==0:
        print(f'{y} is divisible by 2 and 3')
    elif y%2==0:
        print(f"{y} is divivisible by 2")
    elif y%3==0:
        print(f"{y} is divivisible by 3")
    else:
        print(f'{y} is not divivsible by 2 or 3')

z = range(0,100)
for a in z:
    if a%5==0 and a%6==0 and a%7==0 and a%9==0:
        print(f"{a} is divisible by 5, 6, 7 and 9")
    elif a%5==0:
        print(f"{a} is divisible by 5")
    elif a%6==0:
        print(f"{a} is divisible by 6")
    elif a%7==0:
        print(f"{a} is divisible by 7")
    elif a%9==0:
        print(f"{a} is divisible by 9")
    else:
        print(a)