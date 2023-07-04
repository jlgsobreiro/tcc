import timeit


class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        self.arvore_dict = {}

    def insere(self, dado):
        if self.raiz is None:
            self.raiz = No(dado)
        else:
            self._insere_recursivo(dado, self.raiz)

    def _insere_recursivo(self, dado, no):
        if dado < no.dado:
            if no.left is None:
                no.left = No(dado)
            else:
                self._insere_recursivo(dado, no.esquerda)
        else:
            if no.right is None:
                no.right = No(dado)
            else:
                self._insere_recursivo(dado, no.direita)

    def procura(self, dado):
        return self._procura_recursiva(dado, self.raiz)

    def _procura_recursiva(self, dado, no):
        if no is None or no.dado == dado:
            return no
        if dado < no.dado:
            return self._procura_recursiva(dado, no.esquerda)
        return self._procura_recursiva(dado, no.direita)


dict_de_retornos = {
    "valor0": 0,
    "valor1": 1,
    "valor2": 2,
    "valor3": 3,
    "valor4": 4,
    "valor5": 5
}
lista_chaves = [
    "valor0",
    "valor1",
    "valor2",
    "valor3",
    "valor4",
    "valor5"
]
lista_valores = [0, 1, 2, 3, 4, 5]


def retorna_valor_com_listas(valor_procurado):
    return lista_valores[lista_chaves.index(valor_procurado)]


def retorna_valor_com_dict(valor_procurado):
    return dict_de_retornos.get(valor_procurado)


tempo_listas_valor0 = timeit.timeit(lambda: retorna_valor_com_listas("valor0"), number=1000000)
tempo_listas_valor1 = timeit.timeit(lambda: retorna_valor_com_listas("valor1"), number=1000000)
tempo_listas_valor2 = timeit.timeit(lambda: retorna_valor_com_listas("valor2"), number=1000000)
tempo_listas_valor3 = timeit.timeit(lambda: retorna_valor_com_listas("valor3"), number=1000000)
tempo_listas_valor4 = timeit.timeit(lambda: retorna_valor_com_listas("valor4"), number=1000000)
tempo_listas_valor5 = timeit.timeit(lambda: retorna_valor_com_listas("valor5"), number=1000000)
tempo_listas_total = tempo_listas_valor0 + tempo_listas_valor1 + tempo_listas_valor2 + tempo_listas_valor3 + tempo_listas_valor4 + tempo_listas_valor5

tempo_dict_valor0 = timeit.timeit(lambda: retorna_valor_com_dict("valor0"), number=1000000)
tempo_dict_valor1 = timeit.timeit(lambda: retorna_valor_com_dict("valor1"), number=1000000)
tempo_dict_valor2 = timeit.timeit(lambda: retorna_valor_com_dict("valor2"), number=1000000)
tempo_dict_valor3 = timeit.timeit(lambda: retorna_valor_com_dict("valor3"), number=1000000)
tempo_dict_valor4 = timeit.timeit(lambda: retorna_valor_com_dict("valor4"), number=1000000)
tempo_dict_valor5 = timeit.timeit(lambda: retorna_valor_com_dict("valor5"), number=1000000)
tempo_dict_total = tempo_dict_valor0 + tempo_dict_valor1 + tempo_dict_valor2 + tempo_dict_valor3 + tempo_dict_valor4 + tempo_dict_valor5

print("Tempo usando listas [valor0]:", tempo_listas_valor0)
print("Tempo usando listas [valor1]:", tempo_listas_valor1)
print("Tempo usando listas [valor2]:", tempo_listas_valor2)
print("Tempo usando listas [valor3]:", tempo_listas_valor3)
print("Tempo usando listas [valor4]:", tempo_listas_valor4)
print("Tempo usando listas [valor5]:", tempo_listas_valor5)

print("Tempo usando dict [valor0]:", tempo_dict_valor0)
print("Tempo usando dict [valor1]:", tempo_dict_valor1)
print("Tempo usando dict [valor2]:", tempo_dict_valor2)
print("Tempo usando dict [valor3]:", tempo_dict_valor3)
print("Tempo usando dict [valor4]:", tempo_dict_valor4)
print("Tempo usando dict [valor5]:", tempo_dict_valor5)

print("Tempo usando listas:", tempo_listas_total)
print("Tempo usando dict:", tempo_dict_total)
