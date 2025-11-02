def cifra_cesar(texto, chave, operacao='criptografar'):
    if operacao == 'descriptografar':
        chave = -chave

    alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    for letra in texto:
        if letra in alfabeto_maiusculo:
            indice = alfabeto_maiusculo.index(letra)
            novo_indice = (indice + chave) % 26
            resultado += alfabeto_maiusculo[novo_indice]

        elif letra in alfabeto_minusculo:
            indice = alfabeto_minusculo.index(letra)
            novo_indice = (indice + chave) % 26
            resultado += alfabeto_minusculo[novo_indice]

        else:
            resultado += letra

    return resultado


def main():
    print("===--- CIFRA DE CÉSAR ---===")
    print("1. Criptografar")
    print("2. Descriptografar")

    while True:
        try:
            opcao = input("\nEscolha uma opção (1-3): ").strip()

            if opcao == '3':
                print("Saindo do programa...")
                break

            if opcao not in ['1', '2']:
                print("Opção inválida! Escolha 1, 2 ou 3.")
                continue

            texto = input("Digite o texto: ")

            while True:
                try:
                    chave = int(input("Digite a chave (número inteiro): "))
                    break
                except ValueError:
                    print("Por favor, digite um número inteiro válido!")

            if opcao == '1':
                resultado = cifra_cesar(texto, chave, 'criptografar')
                print(f"\n Texto criptografado: {resultado}")
            else:
                resultado = cifra_cesar(texto, chave, 'descriptografar')
                print(f"\n Texto descriptografado: {resultado}")

            continuar = input("\nDeseja fazer outra operação? (sim/nao): ").strip().lower()
            if continuar != 'sim':
                print("Saindo do programa...")
                break

        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")