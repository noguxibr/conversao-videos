# 🧠 Conversor de Vídeos .DAV/.AVI para .MP4

Este projeto converte arquivos `.dav` e `.avi` para `.mp4` utilizando o FFmpeg via Python. Agora com interface web feita em Flask para facilitar o uso na rede corporativa.

---

## 🔧 Tecnologias utilizadas

- Python 3
- Flask
- FFmpeg
- HTML5 + CSS3

---

## 🚀 Como rodar localmente

### Pré-requisitos:
- Python instalado
- FFmpeg instalado no sistema e disponível no PATH
- Pip para instalar dependências

### Instalação:

```bash
git clone https://github.com/noguxibr/conversao-videos.git
cd conversao-videos
pip install -r requirements.txt

Crie requirements.txt com:

Flask

Executar o servidor Flask

python app.py

Acesse em http://127.0.0.1:5000

🗂️ Estrutura do Projeto

conversao-videos/
├── app.py                  # App principal Flask
├── src/conversor.py        # Função de conversão com FFmpeg
├── static/css/estilo.css   # Estilo visual da interface
├── templates/index.html    # Página HTML com formulário
├── uploads/                # Uploads temporários
├── convertidos/            # Arquivos convertidos
├── .gitignore
└── README.md

✍️ Autor

Feito por Lucas Emanuel Miranda de Oliveira

## ✅ Passo 5: Comitar o README.md

Após atualizar o `README.md`, rode:

```bash
git add README.md
git commit -m "docs: atualiza README com nova estrutura web"
git push origin main
