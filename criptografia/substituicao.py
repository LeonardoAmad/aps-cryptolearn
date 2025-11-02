import random

def cifra_substituicao(texto, chave, operacao='criptografar'):
    alfabeto_original = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
    resultado = ''

    for letra in texto:
        if letra in alfabeto_original:
            if operacao == 'criptografar':
                indice = alfabeto_original.index(letra)
                resultado += chave[indice]
            else:
                indice = chave.index(letra)
                resultado += alfabeto_original[indice]

        elif letra in alfabeto_minusculo:
            letra_chave_minuscula = chave.lower()
            if operacao == 'criptografar':
                indice = alfabeto_minusculo.index(letra)
                resultado += letra_chave_minuscula[indice]
            else:
                indice = letra_chave_minuscula.index(letra)
                resultado += alfabeto_minusculo[indice]

        else:
            resultado += letra

    return resultado

def gerar_chave_aleatoria():
    alfabeto = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    chave_aleatoria = alfabeto.copy()
    random.shuffle(chave_aleatoria)
    return ''.join(chave_aleatoria)

def main_substituicao():
    print("===--- CIFRA DE SUBSTITUIÇÃO ---===")
    print("1. Criptografar")
    print("2. Descriptografar")
    print("3. Sair")

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

            if opcao == '1':
                chave = gerar_chave_aleatoria()
                print(f"\n Chave gerada: {chave}")
                print("GUARDE ESTA CHAVE PARA DESCRIPTOGRAFAR!")

                resultado = cifra_substituicao(texto, chave, 'criptografar')
                print(f"\n Texto criptografado: {resultado}")

            else:
                print("\nPara descriptografar, digite a chave de 26 letras:")
                print("Exemplo: QWERTYUIOPASDFGHJKLZXCVBNM")

                while True:
                    chave = input("Digite a chave: ").strip().upper()

                    if len(chave) != 26:
                        print("A chave deve ter exatamente 26 letras!")
                        continue

                    if not chave.isalpha():
                        print("A chave deve conter apenas letras!")
                        continue

                    if len(set(chave)) != 26:
                        print("A chave não pode ter letras repetidas!")
                        continue
                    break

                resultado = cifra_substituicao(texto, chave, 'descriptografar')
                print(f"\n Texto descriptografado: {resultado}")

            continuar = input("\n Deseja fazer outra operação? (sim/nao): ").strip().lower()
            if continuar != 'sim':
                print("Saindo do programa...")
                break

        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    main_substituicao()