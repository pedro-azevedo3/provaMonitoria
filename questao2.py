"""
Crie um programa que lê N números (N digitado pelo usuário). Imprima o menor número, o
maior número, a soma de todos os números, o produto de todos os números, a soma do menor
com o maior e o produto do menor com o maior.
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
        
    num_min = min(numeros)
    num_max = max(numeros)
    soma_numeros = sum(numeros)
    num_produto = 1
    
    for numero in numeros:
        num_produto *= numero

    soma_minimo_maximo = num_min + num_max
    produto_minimo_maximo = num_min * num_max
    
    print(f'O menor número é: {num_min}')
    print(f'O maior número é: {num_max}')
    print(f'A soma dos números é: {soma_numeros}')
    print(f'Soma do maior número com o menor: {soma_minimo_maximo}')
    print(f'O produto do número minimo com o máximo: {produto_minimo_maximo}')
    
if __name__ == '__main__':
    main()