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


def validar_chave_cesar(chave):
    try:
        chave = int(chave)
        return chave, None
    except ValueError:
        return None, "A chave deve ser um número inteiro."