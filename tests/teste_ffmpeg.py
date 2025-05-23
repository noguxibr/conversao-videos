import subprocess

def converter_video_ffmpeg(entrada, saida):
    comando = [r'C:\ffmpeg\bin\ffmpeg.exe', '-i', entrada, saida]
    subprocess.run(comando, check=True)
