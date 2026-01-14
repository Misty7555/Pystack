def interest():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))
    ch = int(input("1.Simple Interest  2.Compound Interest: "))
    if ch == 1:
        si = (p * r * t) / 100
        print("Simple Interest =", si)
    elif ch == 2:
        ci = p * (1 + r/100) ** t - p
        print("Compound Interest =", ci)

interest()
