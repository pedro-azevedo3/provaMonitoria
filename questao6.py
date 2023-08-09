"""
Explique Encapsulamento e coloque em prática numa classe qualquer.
"""

"""
Encapsulamento é um dos pilares da programação orientada a objetos, segundo o qual procuramos esconder
de clientes (usuários da classe) todas as informações que não são necessárias ao uso da classe.

Por exemplo, suponha que precisássemos criar uma classe para armazenar informações de funcionários
de uma empresa...
"""
class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome
        self.cargo
        self.valor_hora_trabalhada
        self.horas_trabalhadas = 0
        self.salario = 0
    def registra_hora_trabalhada(self):
        self.horas_trabalhadas += 1
    def calcula_salario(self):
        self.salario = self.horas_trabalhadas * self.valor_hora_trabalhada
        
"""
Essa classe possui alguns problemas. Informações de funcionários como salário, são expostas para clientes comuns,
o que não é desejável. Além disso podemos adicionar valores e editar salários e horas trabalhadas.
Ou seja, o encapsulamento serve para esconder as informações. Existe a palavra-chave "private" para indicar que 
um dado ou método não é visível fora da classe.

Além disso, o encapsulamento permite que a implementação das funcionalidades da classe seja alterada sem que 
o código que usa a classe precise mudar. Ou seja, dado que a interface da classe (o que é exposto aos clientes) não mude, o programador tem liberdade de mudar a implementação da funcionalidade que a classe
oferece. Por exemplo, caso a forma de cálculo do salário mude, basta que o programador altere a implementação
do método "calcula_salario()" e clientes da classe continuarão a usar o método precisar sofrer alterações.

Como posso impedir a alteração de salário para pessoas que tem acesso ao código fonte?

Na linguagem que eu estou usando (e que domino), o Python, usamos o decorador @property, que nos permite restringir
o acesso a variáveis de uma classe, semelhante ao private class do Java.
"""

class Funcionario:
    def __init__(self, nome, cargo, valor_hora_trabalhada):
        self.nome = nome
        self.cargo = cargo
        self.valor_hora_trabalhada = valor_hora_trabalhada
        self.__salario = 0
        self.__horas_trabalhadas = 0

    @property
    def salario(self): 
        return self.__salario

    @salario.setter
    def salario(self, novo_salario): 
        raise ValueError("Impossivel alterar salario diretamente. Use a funcao calcula_salario().")

    def registra_hora_trabalhada(self):
        self.__horas_trabalhadas += 1

    def calcula_salario(self):
        self.__salario = self.__horas_trabalhadas * self.valor_hora_trabalhada
        
pedro = Funcionario('Pedro', 'Desenvolvedor', 50)
pedro.salario = 100000 

