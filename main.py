#Aluno: Gabriel Francisco Monteiro Amaral
#RA: 1T1.846767
#Matéria: Sistemas distribuídos e Programação Paralela


#Importações
import threading
import time

#----------------------------------------------------------

#Fazendo uso de apenas uma thread

def listar_primos():
    lista_primos = []
    with open('Entrada01.txt', 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            numero = int(linha)

            if numero<2:
                continue

            primo = True
            for i in range(2, int(numero**0.5) + 1): 
                if numero % i == 0:
                    primo = False
                    break
            if primo:
                lista_primos.append(numero)

    print(f'Lista de primos: {lista_primos}')
    
    with open ('output/Saida_01.txt', 'w') as saida:
        for numero in lista_primos:
            str_num = str(numero)
            saida.write(f"{str_num}\n")       

def solo_thread():
    thread = threading.Thread(target=listar_primos)
    thread.start()
    tempo_inicial = time.time()
    thread.join()
    tempo_final = time.time()
    duracao = tempo_final - tempo_inicial
    print(f'Arquivo lido com sucesso, sua duração em segundos foi de:{round(duracao,2)}')

solo_thread()
