````markdown
# 🎥 Conversor de Vídeos .DAV/.AVI para MP4

Este projeto permite converter vídeos no formato `.dav` e `.avi` para `.mp4` usando o FFmpeg com interface gráfica via Tkinter. Útil para equipes de monitoramento que lidam com vídeos de sinistros e precisam de um formato mais acessível e compatível com players comuns.

## 🚀 Como usar

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
````

2. **Baixe e configure o FFmpeg**:

   * Baixe o FFmpeg: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
   * Extraia e copie o caminho completo do `ffmpeg.exe`
   * Altere o caminho no código `converter.py` na linha onde o comando FFmpeg é construído

3. **Execute o script**:

   ```bash
   python src/converter.py
   ```

4. **Passos via interface**:

   * Selecione **um ou mais arquivos** `.dav` ou `.avi`
   * Escolha a pasta de saída
   * Para cada arquivo selecionado, digite um nome para o arquivo `.mp4` gerado (ou pressione Enter para usar o nome original)

## 📂 Estrutura de diretórios

```plaintext
conversao-videos/
├── src/                # Código-fonte principal
│   └── converter.py
├── tests/              # Arquivos de teste
│   ├── teste_ffmpeg.py
│   └── videos_teste/
├── docs/               # Documentação opcional
│   └── exemplo_interface.png
├── README.md
├── .gitignore
└── requirements.txt
```

## ✅ Requisitos

* Python 3.7+
* FFmpeg instalado
* Tkinter (incluso no Python por padrão)

## 🛠 Exemplo de comando FFmpeg usado

```bash
ffmpeg -fflags +genpts -avoid_negative_ts make_zero -i "entrada.avi" -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -movflags +faststart "saida.mp4"
```

## 🔁 Suporte a múltiplos arquivos

O script oferece suporte à **seleção e conversão em lote** de múltiplos arquivos `.dav` ou `.avi` de uma só vez. Para cada vídeo selecionado, o sistema solicitará um nome personalizado (ou usará o nome original se você pressionar Enter). Isso facilita o trabalho com grandes volumes de vídeos de monitoramento.
