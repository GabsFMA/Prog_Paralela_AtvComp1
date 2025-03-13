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

    #print(f'Lista de primos: {lista_primos}')
    
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
    print(f'Processo concluído com sucessso, usando 1 Thread sua duração em segundos foi de:{round(duracao,2)}')

#solo_thread()

#----------------------------------------------------------

#Fazendo uso de cinco threads

def listar_primos_5_v1(numeros, resultado, lock):
    lista_primos = []

    for numero in numeros:
        if numero < 2:
            continue

        primo = True  

        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break

        if primo:
            lista_primos.append(numero)

   
    with lock:
        resultado.extend(lista_primos)

def multi_thread_5_v1():
    qnt_threads = 5
    tempo_inicial = time.time()

    with open('Entrada01.txt', 'r') as arquivo:
        numeros = [int(linha.strip()) for linha in arquivo]

    qnt_por_thread = len(numeros) // qnt_threads

    partes = [numeros[i * qnt_por_thread: (i + 1) * qnt_por_thread] for i in range(qnt_threads)]

    partes[-1].extend(numeros[qnt_threads * qnt_por_thread:])  

    lista_primos_compartilhada = []
    lock = threading.Lock()  
    lista_threads = []

    for i in range(qnt_threads):
        thread = threading.Thread(target=listar_primos_5_v1, args=(partes[i], lista_primos_compartilhada, lock))
        lista_threads.append(thread)
        thread.start()

    for thread in lista_threads:
        thread.join()

    with open('output/Saida_05_v1.txt', 'w') as saida:
        for primo in sorted(lista_primos_compartilhada):
            saida.write(f"{primo}\n")

    tempo_final = time.time()
    duracao = tempo_final - tempo_inicial
    print(f'Processo concluído com sucessso, usando 5 Threads sua duração em segundos foi de:{round(duracao,2)}')

#multi_thread_5_v1()




