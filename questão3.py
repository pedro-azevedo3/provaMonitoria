"""
Crie um programa que lê N números (N digitado pelo usuário). Imprima a soma de todos os
números pares e a soma de todos os números ímpares.
"""

def main():
    try:
        n_numeros = int(input('Digite a quantidade de números que você deseja inserir: '))
        numeros = []
    
        for i in range(n_numeros):
            numero = float(input(f'Digite o número {i+1}: '))
            numeros.append(numero)
    
    except ValueError:
        print('Não consegui entender')
        
    soma_par = 0
    soma_impar = 0
    
    for numero in numeros:
        if numero % 2 == 0:  # Verifica se o número é par
            soma_par += numero
        else:
            soma_impar += numero
    
    print(f'Soma dos números pares é: {soma_par}')
    print(f'Soma dos números ímpares é: {soma_impar}')
    
if __name__ == '__main__':
    main()