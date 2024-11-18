from flask import Flask

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return {"status": "auth_service running"}, 200

if __name__ == '__main__':
    app.run(port=5001)
