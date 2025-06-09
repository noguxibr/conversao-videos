import subprocess
import os

def converter_video(caminho_entrada, caminho_saida):
    comando = [
        'C:\\ffmpeg\\bin\\ffmpeg.exe',
        '-fflags', '+genpts',
        '-avoid_negative_ts', 'make_zero',
        '-i', caminho_entrada,
        '-c:v', 'libx264',
        '-preset', 'fast',
        '-crf', '23',
        '-c:a', 'aac',
        '-b:a', '128k',
        '-movflags', '+faststart',
        caminho_saida
    ]
    
    try:
        subprocess.run(comando, check=True)
        return True, f'Arquivo convertido com sucesso: {caminho_saida}'
    except subprocess.CalledProcessError as e:
        return False, f'Erro na conversão: {e.stderr}'
