### 📁 Estrutura de pastas sugerida

```plaintext
conversao-videos/
│
├── src/                          # Código-fonte principal
│   └── converter.py              # Seu script de conversão
│
├── tests/                        # Arquivos de teste (para testes manuais ou automáticos)
│   ├── teste_ffmpeg.py           # Scripts de teste unitário ou funcional
│   └── videos_teste/             # Vídeos .dav e .avi de exemplo
│
├── docs/                         # Documentação (opcional, para tutoriais ou prints)
│   └── exemplo_interface.png     # Imagem explicando o uso da interface
│
├── README.md                     # Documentação principal do projeto
├── .gitignore                    # Arquivos e pastas que não devem ir para o Git
└── requirements.txt              # Dependências do projeto
```

---

# 🎥 Conversor de Vídeos .DAV/.AVI para MP4

Este projeto permite converter vídeos no formato `.dav` e `.avi` para `.mp4` usando o FFmpeg com interface gráfica via Tkinter. Útil para equipes de monitoramento que lidam com vídeos de sinistros e precisam de um formato mais acessível.

## 🚀 Como usar

1. **Instale as dependências**:

   pip install -r requirements.txt


2. **Baixe e configure o FFmpeg**:

   * Baixe o FFmpeg: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   * Extraia e copie o caminho completo do `ffmpeg.exe`
   * Altere o caminho no código `converter.py` na linha do comando

3. **Execute o script**:

   
   python src/converter.py
   

4. **Passos via interface**:

   * Selecione o vídeo `.dav` ou `.avi`
   * Escolha a pasta de saída
   * Digite o nome do novo arquivo `.mp4`

## 📂 Estrutura de diretórios

* `src/` – Código principal
* `tests/` – Vídeos e scripts de teste
* `docs/` – Prints da interface ou tutoriais

## ✅ Requisitos

* Python 3.7+
* FFmpeg instalado
* Tkinter (já incluso no Python padrão)

## 🛠 Exemplo de comando FFmpeg usado


ffmpeg -fflags +genpts -avoid_negative_ts make_zero -i "entrada.avi" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -movflags +faststart "saida.mp4"


## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
