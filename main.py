Grau = int(input("Grau da Equação:\n"))
if Grau not in range (1,3):
        print("Grau inválido")
elif Grau == 1:
    print("A equação é do primeiro grau")
    a = int(input("Digite valor de A:\n"))
    if a == int(0):
        print("Valor de a inválido")
    b = int(input("Digite valor de B:\n"))
    r1 = -b/a 
    arredondado = round(r1, 2)
    print(arredondado)
    
elif Grau == 2:
    print("A equação é do segundo grau")
    a = int(input("Digite valor de A:\n"))
    if a == int(0):
        print("Valor de a inválido")
    b = int(input("Digite valor de B:\n"))
    c = int(input("Digite valor de C:\n"))
    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        x = -b / (2*a)
        print("A equação possui uma raiz real: {:.2f}".format(x))
    else:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        if x1 < x2:
            print("A equação possui duas raízes reais: {:.2f} e {:.2f}".format(x1, x2))
        else:
            print("A equação possui duas raízes reais: {:.2f} e {:.2f}".format(x2, x1))