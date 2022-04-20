#Programa que permite ir para um menu principal #
# Tarefa 2 - Catarina Costa 20-4-2022 #

# Menu principal  - Mostra as opcoes e pedido ao utilizador de selecao de opcao #

menu_options = {
    1: 'Vogal count',
    2: 'Palíndrome',
    3: 'Extense Date',
    4: 'Exit',
}


def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

# --------------------------------------------------------------------------------------------#


# Contar vogais - Parte do codigo para a opcao 1 conta vogais da palavra pedida ao utilizador #

def conta_vogais(string):
    string = string.lower() # para que a comparação não seja sensível a maiuscula/minuscula
    vogais = 'aeiou'
    print(conta_vogais(""))
    return {i: string.count(i) for i in vogais if i in string}

# --------------------------------------------------------------------------------------------# 

# Palindromo - Parte do codigo para opcao 2 - diz se a palavra é Palindromo ou nao # 


def option2(): 
    word = input("Write a word: ")
    if str(word) == str(word)[::-1] :
        print("Palindrome")
    else:
        print("Not Palindrome")


# -------------------------------------------------------------------------------------#
#data por extenso - Parte do codigo para opcao 3 - pede a data de nascimento ao utilizador e converte por extenso # 


def retorna_data_extenso(data_string):
    import locale
    from datetime import datetime
    locale.setlocale(locale.LC_ALL, 'pt_PT')
    data = input("Write your born date in DD/MM/AAAA:")
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de data inválido, deve ser DD/MM/AAAA")
        return None
    if data_extenso is not None:
        print(data_extenso) 
    else:
        data_datetime = datetime.strptime(data_string, '%d/%m/%Y')
        # return datetime.strftime(data_datetime, '%d de %B de %Y')
        dia = datetime.strftime(data_datetime, '%d')
        mes = datetime.strftime(data_datetime, '%B')
        ano = datetime.strftime(data_datetime, '%Y')
        return dia + " de " + mes[0].upper() + mes[1:] + " de " + ano
    data_extenso = retorna_data_extenso(data)
#-----------------------------------------------------------------------------------------------------------------#

# Sair - Parte do código para a opção 4 - co3nvida o utilizador a abandonar o programa # 


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Insira uma opcao: '))
        except:
            print('Opcao errada, insira um numero ...')
        if option == 1:
           conta_vogais()
        elif option == 2:
            option2()
        elif option == 3:
            retorna_data_extenso ()
        elif option == 4:
            print('Obrigado por usar este  programa!')
            exit()
        else:
            print('Opcao errada, insira um numero entre 1 e 4')

# ------------------------------------------------------------------------------------#