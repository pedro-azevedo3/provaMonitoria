"""
Crie um programa que lê a idade do usuário.
◆ Caso tenha entre 5 e 16 anos, imprima: “Espero que esteja indo bem na escola!”;
◆ Caso tenha entre 17 e 30 anos, imprima: “Vai se formar quando?”;
◆ Caso tenha mais que 30 anos, mas menos que 60, imprima: “Trabalhando pesado!”;
◆ Por fim, caso tenha 60 anos ou mais, imprima: “Hora de aposentar!”.

Cara, realmente eu vou fazer com Python, eu nem tenho o eclipse baixado no PC...
"""

idade = int(input('Insira a sua idade: '))

if idade >= 5 and idade < 16:
    print('Espero que esteja indo bem na escola!')
elif idade >= 17 and idade < 30:
    print('Vai se formar quando?')
elif idade >= 30 and idade < 60:
    print('Trabalhando pesado!')
elif idade >= 60:
    print('É hora de dar tchau!')
else:
    print('Idade inválida.')