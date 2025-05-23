import subprocess
import tkinter as tk
from tkinter import filedialog
import os

# Oculta a janela principal
root = tk.Tk()
root.withdraw()

print('🔍 Selecione um ou mais arquivos de entrada (.dav ou .avi)...')
entradas = filedialog.askopenfilenames(
    title='Selecione os arquivos de entrada',
    filetypes=[('Arquivos de vídeo', '*.dav *.avi'), ('Todos os arquivos', '*.*')]
)

if not entradas:
    print('❌ Nenhum arquivo de entrada selecionado.')
    exit()

print('📁 Selecione a pasta onde deseja salvar os vídeos convertidos...')
saida_diretorio = filedialog.askdirectory(title='Selecione a pasta de saída')

if not saida_diretorio:
    print('❌ Nenhuma pasta de saída selecionada.')
    exit()

for entrada in entradas:
    nome_original = os.path.splitext(os.path.basename(entrada))[0]
    print(f'\n📄 Arquivo selecionado: {nome_original}')

    saida_nome = input('✍️ Digite o nome do arquivo convertido (sem .mp4) ou pressione Enter para usar o nome original: ').strip()

    # Se o usuário não digitar nada, usa o nome original
    if not saida_nome:
        saida_nome = nome_original

    # Garante que o nome termina com .mp4
    if not saida_nome.lower().endswith('.mp4'):
        saida_nome += '.mp4'

    saida = os.path.join(saida_diretorio, saida_nome)

    entrada_aspas = f'"{entrada}"'
    saida_aspas = f'"{saida}"'

    comando = (
        f'C:\\ffmpeg\\bin\\ffmpeg.exe -fflags +genpts -avoid_negative_ts make_zero '
        f'-i {entrada_aspas} -c:v libx264 -preset fast -crf 23 '
        f'-c:a aac -b:a 128k -movflags +faststart {saida_aspas}'
    )

    print(f'🚀 Convertendo: {entrada}\n👉 Novo nome: {saida_nome}')
    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        if os.path.exists(saida) and os.path.getsize(saida) > 10_000:
            print(f'✅ Sucesso: {saida_nome}')
        else:
            print(f'⚠️ Arquivo convertido parece vazio ou inválido: {saida_nome}')
            print('📄 Saída do FFmpeg:\n', resultado.stderr)

    except subprocess.CalledProcessError as e:
        print(f'❌ Erro ao converter: {entrada}')
        print('📄 Erro do FFmpeg:\n', e.stderr)

print('\n🏁 Conversão de todos os arquivos finalizada.')
