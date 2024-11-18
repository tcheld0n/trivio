from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')  # Rota inicial

@app.route('/game')  # Rota para o jogo
def game():
    try:
        # Faz requisição ao question_service
        response = requests.get('http://localhost:5003/get_question')
        response.raise_for_status()
        questions = response.json()  # Dados das perguntas
        return render_template('game.html', questions=questions)  # Renderiza o template com as perguntas
    except Exception as e:
        return f"Erro ao obter perguntas: {str(e)}", 500

if __name__ == '__main__':
    app.run(port=5000)
