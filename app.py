from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/post', methods=['POST'])
def post():
    data = request.form.get('data')
    eval(data)  # Vulnérabilité de sécurité
    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
