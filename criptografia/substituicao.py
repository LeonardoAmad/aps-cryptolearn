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

def validar_chave_substituicao(chave):
    chave = chave.upper()
    if len(chave) != 26:
        return None, "A chave deve ter exatamente 26 letras."
    if not chave.isalpha():
        return None, "A chave deve conter apenas letras."
    if len(set(chave)) != 26:
        return None, "A chave não pode ter letras repetidas."
    return chave, None