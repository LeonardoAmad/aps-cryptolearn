from flask import Flask, render_template, request
from criptografia.cesar import cifra_cesar
from criptografia.substituicao import cifra_substituicao, gerar_chave_aleatoria

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
        # Pega os dados do formulário
        mensagem = request.form.get('mensagem', '')
        chave = int(request.form.get('chave', 0))
        operacao = request.form.get('operacao', 'criptografar')

        # Chama a função de criptografia
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

@app.route('/transformacao')
def transformacao():
    return render_template('transformacao.html')

app.run()