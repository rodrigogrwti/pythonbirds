class Pessoa:
    def __init__(self, *filhos,nome = None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rodrigo = Pessoa(nome='Rodrigo')
    ana = Pessoa(rodrigo, nome='Ana')
    print(Pessoa.cumprimentar(rodrigo))
    print(id(rodrigo))
    print(rodrigo.cumprimentar())
    print(rodrigo.nome)
    print(rodrigo.idade)
    for filho in ana.filhos:
        print(filho.nome)
