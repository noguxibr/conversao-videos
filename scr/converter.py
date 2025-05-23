import subprocess
import tkinter as tk
from tkinter import filedialog
import os

# Oculta a janela principal
root = tk.Tk()
root.withdraw()

print('🔍 Selecione o arquivo de entrada (.dav ou .avi)...')
entrada = filedialog.askopenfilename(
    title='Selecione o arquivo de entrada',
    filetypes=[('Arquivos de vídeo', '*.dav *.avi'), ('Todos os arquivos', '*.*')]
)

if not entrada:
    print('❌ Nenhum arquivo de entrada selecionado.')
    exit()

print('📁 Selecione a pasta onde deseja salvar o vídeo convertido...')
saida_diretorio = filedialog.askdirectory(title='Selecione a pasta de saída')

if not saida_diretorio:
    print('❌ Nenhuma pasta de saída selecionada.')
    exit()

saida_nome = input('✍️ Digite o nome do arquivo de saída (ex: video_convertido.mp4): ').strip()
if not saida_nome.lower().endswith('.mp4'):
    saida_nome += '.mp4'

saida = os.path.join(saida_diretorio, saida_nome)

entrada_aspas = f'"{entrada}"'
saida_aspas = f'"{saida}"'

# Flag extra para corrigir problemas de tempo e leitura
comando = f'C:\\ffmpeg\\bin\\ffmpeg.exe -fflags +genpts -avoid_negative_ts make_zero -i {entrada_aspas} -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -movflags +faststart {saida_aspas}'

print(f'🚀 Executando comando:\n{comando}')

try:
    resultado = subprocess.run(
        comando,
        shell=True,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True
    )

    # Verifica se o arquivo foi criado com sucesso e tem conteúdo
    if os.path.exists(saida) and os.path.getsize(saida) > 10_000:  # mínimo 10 KB
        print(f'✅ Conversão concluída com sucesso!\n📁 Arquivo salvo em: {saida}')
    else:
        print('⚠️ Conversão finalizada, mas o arquivo parece vazio ou inválido.')
        print('📄 Saída do FFmpeg:\n', resultado.stderr)

except subprocess.CalledProcessError as e:
    print('❌ Ocorreu um erro durante a conversão.')
    print('📄 Erro do FFmpeg:\n', e.stderr)
