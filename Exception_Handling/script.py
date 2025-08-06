try:
    arquivo = open('blablabla.txt', 'r')
    for item in arquivo:
        print(item)
except FileNotFoundError:
    print('Arquivo não encontrado.')        