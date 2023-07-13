# Catarina Costa 12-07-2023 #

# Palindromo - diz se a palavra e Palindromo ou nao # 
palavra = input("Escreva uma palavra: ")
if str(palavra) == str(palavra)[::-1] :
        print("Palindromo")
else:
        print("Nao e Palindromo")


