
print("="* 5, "Programa que da factores :)" , "="* 5)

numero = int(input("Digita un numero para sacar el factor: "))

#sacar la mitad del numero, y lo casteamos a int para redondear en caso de que sea mitad
mitad_numero = int(numero / 2)

print("==> Los factores son: ")
for x in range(1, mitad_numero + 1):
    #determinamos si el dividirse entre el numero, de como residuo 0
    if numero % x == 0:
        print("->",x)
#como elfactor de un numero es si mismo, entonces imprimos ese valor:   
print("->", numero)