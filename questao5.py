"""
Crie uma classe que simule um Aluno. A classe Aluno deve ter os atributos “nome”,
“matricula” e “notas”. A classe deve ter os métodos “adicionaNota” (que recebe uma nota) e
“calculaMedia” (que calcula e retorna a média do aluno). Imagine que o aluno pode ter diversas
notas, não só duas ou três. Para testar sua classe, crie diversos alunos, adicione notas e imprima
suas médias, informando o nome do aluno, sua matrícula e sua média.
"""

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionarNotas(self, nota):
        self.notas.append(nota)

    def media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
def teste():
    aluno1 = Aluno('Pedro', '3080006')
    aluno1.adicionarNotas(10)
    aluno1.adicionarNotas(9)
    aluno1.adicionarNotas(8)

    aluno2 = Aluno('Armando', '30800043')
    aluno2.adicionarNotas(5)
    aluno2.adicionarNotas(6)
    aluno2.adicionarNotas(7)
    aluno2.adicionarNotas(10)

    aluno3 = Aluno('Rafaela', '30800054')
    aluno3.adicionarNotas(6)
    aluno3.adicionarNotas(6)
    aluno3.adicionarNotas(6)
    aluno3.adicionarNotas(5)
    
    aluno4 = Aluno('José', '3080042')

    alunos = [aluno1, aluno2, aluno3, aluno4]

    for aluno in alunos:
        media = aluno.media()
        print(f'Aluno: {aluno.nome} Matrícula: {aluno.matricula} Média: {media:.2f}')

if __name__ == '__main__':
    teste()




