


class pilha:

    def __init__(self):
        self.dados = []


    def insere(self, elem):
        self.dados.append(elem)

    def remove(self):
        if not self.vazia():
            return self.dados.pop()

        else:
            print("Pilha vazia!")

    def tamanho(self):
        return len(self.dados)

    def vazia(self):
        return len(self.dados) == 0

    def topo(self):
        if not self.vazia():
            return self.dados[-1]

        else:
            print("Pilha vazia!")

    def print(self):
        while not self.vazia():
            print(self.topo())
            self.remove()