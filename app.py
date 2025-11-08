from flask import Flask, render_template, request
from criptografia.cesar import cifra_cesar
from criptografia.substituicao import cifra_substituicao, gerar_chave_aleatoria
from criptografia.transposicao import cifra_transposicao, validar_chave

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/cesar', methods=['GET','POST'])
def cesar():
    if request.method == 'POST':
        mensagem = request.form.get('mensagem', '')
        chave = int(request.form.get('chave', 0))
        operacao = request.form.get('operacao', 'criptografar')

        resultado = cifra_cesar(mensagem, chave, operacao)

        return render_template(
            'cesar.html',
            resultado=resultado,
            mensagem=mensagem,
            chave=chave,
            operacao=operacao
        )

    return render_template('cesar.html')

@app.route('/substituicao', methods=['GET','POST'])
def substituicao():
    if request.method == 'POST':
        mensagem = request.form.get('mensagem', '')
        chave = request.form.get('chave', '').strip().upper()
        operacao = request.form.get('operacao', 'criptografar')

        # Se o usuário não fornecer chave, gera uma automaticamente
        if not chave:
            chave = gerar_chave_aleatoria()

        resultado = cifra_substituicao(mensagem, chave, operacao)

        return render_template(
            'substituicao.html',
            resultado=resultado,
            mensagem=mensagem,
            chave=chave,
            operacao=operacao
        )

    return render_template('substituicao.html')

@app.route('/transposicao', methods=['GET', 'POST'])
def transposicao():
    if request.method == 'POST':
        mensagem = request.form.get('mensagem', '')
        chave_str = request.form.get('chave', '').strip()
        operacao = request.form.get('operacao', 'criptografar')

        chave, erro = validar_chave(chave_str)
        if erro:
            resultado = f"Erro na chave: {erro}"
        else:
            resultado = cifra_transposicao(mensagem, chave, operacao)

        return render_template(
            'transposicao.html',
            resultado=resultado,
            mensagem=mensagem,
            chave=chave_str,
            operacao=operacao
        )

    return render_template('transposicao.html')

app.run()