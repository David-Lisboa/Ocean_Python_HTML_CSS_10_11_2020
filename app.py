from flask import (
    Blueprint, render_template, request
)


from flask import Flask
app = Flask(__name__)

bp = Blueprint('app', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    
    nome_jogador = None
    premio = None
    premio_imagem = None

    if request.method == 'POST':
        nome_jogador = request.form['nome_jogador']
        escolha = request.form['escolha']

        if escolha == 'futurista':
            premio = 'Um sabre de luz'
            premio_imagem = 'https://media.indiedb.com/images/members/5/4384/4383197/profile/Knight.gif'
        elif escolha == 'medieval':
            premio = 'Uma espada'
            premio_imagem = 'https://i.pinimg.com/originals/f5/72/7b/f5727b17d6e3cb84596deb8f96cbe071.gif'

    return render_template('index.html', nome_jogador=nome_jogador, premio=premio, premio_imagem=premio_imagem)


app.register_blueprint(bp)


# http://127.0.0.1:5000/
