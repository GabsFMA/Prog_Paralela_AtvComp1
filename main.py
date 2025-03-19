# Alunos: Gabriel Francisco Monteiro Amaral, Yago Bastos dos Santos e Julia Batista Iervese
# RA: 1T1.846767, 1T1.844186 e 1T1.833991
# Matéria: Sistemas distribuídos e Programação Paralela

# Importações
import multiprocessing
import time

# ----------------------------------------------------------

# Função para verificar se um número é primo
def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Função para calcular números primos em uma lista
def calcular_primos_com_indices(numeros_com_indices):

    return [(indice, numero) for indice, numero in numeros_com_indices if verificar_primo(numero)]

# ----------------------------------------------------------

# Função para processar números primos usando 1 processo
def solo_process():
    tempo_inicial = time.time()

    with open('Entrada01.txt', 'r') as arquivo:
        numeros = [(indice, int(linha.strip())) for indice, linha in enumerate(arquivo)]

    lista_primos = calcular_primos_com_indices(numeros)

    with open('output/Saida_01.txt', 'w') as saida:
        for _, numero in sorted(lista_primos):
            saida.write(f"{numero}\n")

    tempo_final = time.time()
    duracao = tempo_final - tempo_inicial
    print(f'Processo concluído com sucesso, usando 1 processo. Duração: {round(duracao, 2)} segundos.')

# ----------------------------------------------------------

# Função para processar números primos usando múltiplos processos
def multi_process(qnt_processos, output_file):
    tempo_inicial = time.time()

    with open('Entrada01.txt', 'r') as arquivo:
        numeros = [(indice, int(linha.strip())) for indice, linha in enumerate(arquivo)]

   
    qnt_por_processo = len(numeros) // qnt_processos
    partes = [numeros[i * qnt_por_processo: (i + 1) * qnt_por_processo] for i in range(qnt_processos)]
    partes[-1].extend(numeros[qnt_processos * qnt_por_processo:])  

  
    with multiprocessing.Pool(processes=qnt_processos) as pool:
        resultados = pool.map(calcular_primos_com_indices, partes)

 
    lista_primos = [primo for sublista in resultados for primo in sublista]

    
    lista_primos.sort(key=lambda x: x[0])

    
    with open(output_file, 'w') as saida:
        for _, numero in lista_primos:
            saida.write(f"{numero}\n")

    tempo_final = time.time()
    duracao = tempo_final - tempo_inicial
    print(f'Processo concluído com sucesso, usando {qnt_processos} processos. Duração: {round(duracao, 2)} segundos.')

# ----------------------------------------------------------

# Função principal para executar os testes
if __name__ == "__main__":
    # Teste com 1 processo
    print("Executando com 1 processo:")
    solo_process()

    # Teste com 5 processos
    print("\nExecutando com 5 processos:")
    multi_process(5, 'output/Saida_05.txt')

    # Teste com 10 processos
    print("\nExecutando com 10 processos:")
    multi_process(10, 'output/Saida_10.txt')