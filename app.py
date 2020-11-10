from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        # Tira o espaço e coloca em minusculo
    estilo = input("Informe o seu estilo: ").strip().lower()

    if estilo == "medieval":
         return "espada"

    elif estilo == "futurista":
        return "sabre de luz"

    else:
        return "erro"

# http://127.0.0.1:5000/
