"""
Faça um programa que peça a idade de pessoas de uma turma. Caso seja digitada uma idade
negativa, pare de receber idades. Após parar de receber idades, o programa deverá verificar se a
média de idade está entre 0 e 25, 26 e 60 ou é maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada.
"""

def main():
    contador_idade = 0
    idade = 0
    soma_idade = 0
    
    while idade >= 0:
        try:
            idade = int(input('Digite o número, caso deseje parar digite uma idade negativa:  '))
            if idade > 0:
                soma_idade += idade
                contador_idade += 1
        except ValueError:
            print('Idade inválida.')
    if contador_idade == 0:
        print('Nenhuma idade foi inserida corretamente.')
    else:
        media = soma_idade / contador_idade
        
        if 0 <= media <= 25:
            print('Turma jovem')
        elif 26 <= media <= 60:
            print('Turma adulta')
        else:
            print('Turma idosa')
            
if __name__ == "__main__":
    main()





