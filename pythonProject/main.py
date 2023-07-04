import csv


def separar_arquivo_csv(arquivo_origem, tamanho_lote):
    with open(arquivo_origem, 'r') as arquivo:
        leitor_csv = csv.reader(arquivo)
        cabecalho = next(leitor_csv)  # Lê o cabeçalho do arquivo original

        contador = 1
        lote = []
        for linha in leitor_csv:
            lote.append(linha)
            if len(lote) == tamanho_lote:
                criar_arquivo_lote(cabecalho, lote, contador)
                lote = []
                contador += 1

        # Cria o último arquivo com o restante das linhas (se houver)
        if lote:
            criar_arquivo_lote(cabecalho, lote, contador)


def criar_arquivo_lote(cabecalho, lote, contador):
    nome_arquivo = f'lote_{contador}.csv'
    with open(nome_arquivo, 'w', newline='') as arquivo_lote:
        escritor_csv = csv.writer(arquivo_lote)
        escritor_csv.writerow(cabecalho)
        escritor_csv.writerows(lote)
    print(f'Arquivo {nome_arquivo} criado com sucesso!')


# Exemplo de uso
arquivo_origem = 'modelo_pedido_venda.csv'
tamanho_lote = 500
separar_arquivo_csv(arquivo_origem, tamanho_lote)
