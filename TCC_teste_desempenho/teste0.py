import timeit

valor_a_ser_procurado = "valor2"


def retorna_valor_com_ifs(valor_procurado):
    if "valor0" == valor_procurado:
        return 0
    if "valor1" == valor_procurado:
        return 1
    if "valor2" == valor_procurado:
        return 2
    if "valor3" == valor_procurado:
        return 3
    if "valor4" == valor_procurado:
        return 4
    if "valor5" == valor_procurado:
        return 5


def retorna_valor_com_dict(valor_procurado):
    dict_de_retornos = {
        "valor0": 0,
        "valor1": 1,
        "valor2": 2,
        "valor3": 3,
        "valor4": 4,
        "valor5": 5
    }
    return dict_de_retornos.get(valor_procurado)


tempo_ifs = timeit.timeit(lambda: retorna_valor_com_ifs(valor_a_ser_procurado), number=1000000)

tempo_dict = timeit.timeit(lambda: retorna_valor_com_dict(valor_a_ser_procurado), number=1000000)

print("Tempo usando ifs:", tempo_ifs)
print("Tempo usando dict:", tempo_dict)
