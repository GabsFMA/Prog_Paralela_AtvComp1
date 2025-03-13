# import threading

# def teste_thread():
#     with open ('Entrada01.txt', 'r') as arquivo: 
#         for linha in arquivo:
#             print(linha.strip())
# thread = threading.Thread(target=teste_thread)
# thread.start()
# thread.join()
# print('Arquivo lido com sucesso')

#----------------------------------------------------------

import threading
import time

def teste_solo_thread():
    lista_primos = []
    with open('Entrada01.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            numero = int(linha)
            primo = True
            for i in range(2, int(numero**0.5) + 1): 
                if numero % i == 0:
                    #print(f'{numero}: Não é primo')
                    primo = False
                    break
            if primo:
                #print(f'{numero}: É primo')
                lista_primos.append(numero)
    print(f'Lista de primos: {lista_primos}')
                

thread = threading.Thread(target=teste_solo_thread)
thread.start()
tempo_inicial = time.time()
thread.join()
tempo_final = time.time()
duracao = tempo_final - tempo_inicial
print(f'Arquivo lido com sucesso, sua duração em segundos foi de:{round(duracao,2)}')


#----------------------------------------------------------

# def determina_primo():
#     numero = int(input('Digite um número: '))
#     if numero < 2:
#         print('Número não é primo')
#         return
#     for i in range(2, numero):
#         if numero % i == 0:
#             print('Número não é primo')
#             return
#     print('Número é primo')


# determina_primo()