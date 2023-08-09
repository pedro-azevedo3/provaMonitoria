"""
Explique Herança e coloque em prática numa classe qualquer.

Veja o código abaixo:
"""

class Cachorro:
    def __init__(self):
        self.nome = None
        self.idade = None

    def comer(self):
        print('Comeu')

    def dormir(self):
        print('Dormiu')

    def latir(self):
        print('Latiu!')

class Gato:
    def __init__(self):
        self.nome = None
        self.idade = None

    def comer(self):
        print('Comeu')

    def dormir(self):
        print('Dormiu')

    def miar(self):
        print('Miou!')
        
"""
Notou que os 2 códigos são bastante parecidos com a exceção dos métodos miar e latir, mas será que eu preciso 
mesmo ficar digitando por extenso todos esses métodos a mão? Bom, para isso que existem as heranças.

Observe as mudanças no código:
"""

class Animal:
    def comer(self):
        print('Comeu')

    def dormir(self):
        print('Dormiu')

class Cachorro(Animal):
    def __init__(self):
        self.nome = None
        self.idade = None

    def latir(self):
        print('Latiu!')

class Gato(Animal):
    def __init__(self):
        self.nome = None
        self.idade = None

    def miar(self):
        print('Miou!')
        
#Veja que passamos (Animal) como parâmetro, que serve para dizer que a classe Gato e a classe Cachorro 
# está herdando a classe Animal.

class Animal:
    def __init__(self):
        self.nome = None
        self.idade = None

    def comer(self):
        print('Comeu')

    def dormir(self):
        print('Dormiu')

class Cachorro(Animal):
    def latir(self):
        print('Latiu!')

class Gato(Animal):
    def miar(self):
        print('Miou!')

def main():
    cachorro1 = Cachorro()
    cachorro1.nome = 'Dori'
    cachorro1.idade = 1
    cachorro1.comer()
    cachorro1.latir()
    cachorro1.dormir()

    print('')

    gato1 = Gato()
    gato1.nome = 'Ori'
    gato1.idade = 2
    gato1.comer()
    gato1.miar()
    gato1.dormir()

if __name__ == "__main__":
    main()

