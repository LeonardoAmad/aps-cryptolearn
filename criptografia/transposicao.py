def cifra_transposicao(texto, chave, operacao='criptografar'):
    resultado = ''
    tamanho_chave = len(chave)

    if operacao == 'criptografar':
        num_linhas = (len(texto) + tamanho_chave - 1) // tamanho_chave
        matriz = []

        for i in range(num_linhas):
            inicio = i * tamanho_chave
            fim = inicio + tamanho_chave
            linha = list(texto[inicio:fim].ljust(tamanho_chave, 'X'))
            matriz.append(linha)

        for coluna in chave:
            for linha in matriz:
                resultado += linha[coluna]

    else:
        num_linhas = len(texto) // tamanho_chave
        matriz = [[''] * tamanho_chave for _ in range(num_linhas)]

        posicao = 0
        for coluna in chave:
            for linha in range(num_linhas):
                matriz[linha][coluna] = texto[posicao]
                posicao += 1

        for linha in matriz:
            resultado += ''.join(linha)

    return resultado


def validar_chave(chave_str):
    try:
        chave = [int(x) for x in chave_str.split(',')]
        tamanho = len(chave)

        if sorted(chave) != list(range(tamanho)):
            return None, f"Use números de 0 a {tamanho - 1} sem repetir"

        return chave, None

    except ValueError:
        return None, "Use formato: 2,0,1"


def main():
    print("===-- CIFRA DE TRANSPOSIÇÃO --===")

    while True:
        opcao = input(" 1.Criptografar \n 2.Descriptografar \n 3.Sair\nOpção: ").strip()

        if opcao == '3':
            print("Até logo!")
            break
        if opcao not in ['1', '2']:
            continue

        texto = input("Texto: ")

        while True:
            chave_str = input("Chave (ex: 2,0,1): ").strip()
            chave, erro = validar_chave(chave_str)
            if not erro:
                break
            print(erro)

        if opcao == '1':
            resultado = cifra_transposicao(texto, chave, 'criptografar')
            print(f"\nCriptografado: {resultado}")
        else:
            resultado = cifra_transposicao(texto, chave, 'descriptografar')
            print(f"\nDescriptografado: {resultado}")

        if input("\nContinuar? (sim/nao): ").lower() != 'sim':
            print("saindo do programa...")
            break


if __name__ == '__main__':
    main()
