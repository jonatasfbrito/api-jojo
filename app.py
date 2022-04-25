from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route('/apk')
def baixar_apk():
    path = "acerto.apk"
    return send_file(path, as_attachment=True)

@app.route('/')
def index():
    return "O diretório correto é: /apk"

if __name__ == '__main__':
    app.run(port=5000)