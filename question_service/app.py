from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Rota para verificar o funcionamento do serviço
@app.route('/health', methods=['GET'])
def health():
    return {"status": "question_service running"}, 200

# Rota para buscar perguntas
@app.route('/get_question', methods=['GET'])
def get_question():
    # URL da API externa
    api_url = "https://opentdb.com/api.php?amount=10"
    
    try:
        # Realiza a chamada para a API externa
        response = requests.get(api_url)
        response.raise_for_status()  # Levanta exceções para erros HTTP
        
        data = response.json()
        if data["response_code"] == 0:  # Código de sucesso da API externa
            # Retorna as perguntas no formato esperado
            questions = []
            for question_data in data["results"]:
                questions.append({
                    "question": question_data["question"],
                    "options": question_data["incorrect_answers"] + [question_data["correct_answer"]],
                    "answer": question_data["correct_answer"]
                })
            return jsonify(questions), 200
        else:
            return jsonify({"error": "Failed to fetch questions"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5003)
