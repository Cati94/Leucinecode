# Catarina Costa 12-07-2023 #
# Calcular par ou impar de numero #

numero = int(input("Digite um valor: "))
if (numero == 0):
    print("Zero é nulo")
elif (numero % 2 == 0):
    print("O número ",numero," é par")
elif (numero % 2 != 0):
    print("O número ",numero," é ímpar")
# calcular quadrado e o cubo #
if  (numero % 2 == 0):
    print("O quadrado do numero e", numero*numero)
elif ( numero %2 != 0):
    print ("O cubo do numero e ", numero*numero*numero)