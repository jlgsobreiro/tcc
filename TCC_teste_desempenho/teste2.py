import timeit

dict_de_retornos = {
    "valor0": 0,
    "valor1": 1,
    "valor2": 2,
    "valor3": 3,
    "valor4": 4,
    "valor5": 5
}


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

    return dict_de_retornos.get(valor_procurado)


tempo_ifs_valor0 = timeit.timeit(lambda: retorna_valor_com_ifs("valor0"), number=1000000)
tempo_ifs_valor1 = timeit.timeit(lambda: retorna_valor_com_ifs("valor1"), number=1000000)
tempo_ifs_valor2 = timeit.timeit(lambda: retorna_valor_com_ifs("valor2"), number=1000000)
tempo_ifs_valor3 = timeit.timeit(lambda: retorna_valor_com_ifs("valor3"), number=1000000)
tempo_ifs_valor4 = timeit.timeit(lambda: retorna_valor_com_ifs("valor4"), number=1000000)
tempo_ifs_valor5 = timeit.timeit(lambda: retorna_valor_com_ifs("valor5"), number=1000000)
tempo_ifs_total = tempo_ifs_valor0 + tempo_ifs_valor1 + tempo_ifs_valor2 + tempo_ifs_valor3 + tempo_ifs_valor4 + tempo_ifs_valor5

tempo_dict_valor0 = timeit.timeit(lambda: retorna_valor_com_dict("valor0"), number=1000000)
tempo_dict_valor1 = timeit.timeit(lambda: retorna_valor_com_dict("valor1"), number=1000000)
tempo_dict_valor2 = timeit.timeit(lambda: retorna_valor_com_dict("valor2"), number=1000000)
tempo_dict_valor3 = timeit.timeit(lambda: retorna_valor_com_dict("valor3"), number=1000000)
tempo_dict_valor4 = timeit.timeit(lambda: retorna_valor_com_dict("valor4"), number=1000000)
tempo_dict_valor5 = timeit.timeit(lambda: retorna_valor_com_dict("valor5"), number=1000000)
tempo_dict_total = tempo_dict_valor0 + tempo_dict_valor1 + tempo_dict_valor2 + tempo_dict_valor3 + tempo_dict_valor4 + tempo_dict_valor5

print("Tempo usando ifs [valor0]:", tempo_ifs_valor0)
print("Tempo usando ifs [valor1]:", tempo_ifs_valor1)
print("Tempo usando ifs [valor2]:", tempo_ifs_valor2)
print("Tempo usando ifs [valor3]:", tempo_ifs_valor3)
print("Tempo usando ifs [valor4]:", tempo_ifs_valor4)
print("Tempo usando ifs [valor5]:", tempo_ifs_valor5)

print("Tempo usando dict [valor0]:", tempo_dict_valor0)
print("Tempo usando dict [valor1]:", tempo_dict_valor1)
print("Tempo usando dict [valor2]:", tempo_dict_valor2)
print("Tempo usando dict [valor3]:", tempo_dict_valor3)
print("Tempo usando dict [valor4]:", tempo_dict_valor4)
print("Tempo usando dict [valor5]:", tempo_dict_valor5)

print("Tempo usando ifs:", tempo_ifs_total)
print("Tempo usando dict:", tempo_dict_total)
