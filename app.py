from flask import Flask, request, send_file, render_template, jsonify
from src.converter import converter_video
import os
import uuid

app = Flask(__name__, static_folder='static', template_folder='templates')

UPLOAD_DIR = 'uploads'
OUTPUT_DIR = 'convertidos'
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    arquivo = request.files.get('video')
    if not arquivo:
        return 'Nenhum arquivo enviado!', 400

    nome_original = arquivo.filename
    nome_base = str(uuid.uuid4())
    caminho_entrada = os.path.join(UPLOAD_DIR, f'{nome_base}_{nome_original}')
    caminho_saida = os.path.join(OUTPUT_DIR, f'{nome_base}.mp4')

    arquivo.save(caminho_entrada)

    sucesso, mensagem = converter_video(caminho_entrada, caminho_saida)

    if sucesso:
        return send_file(caminho_saida, as_attachment=True)
    else:
        return jsonify({'erro': mensagem}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
