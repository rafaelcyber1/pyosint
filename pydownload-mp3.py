import yt_dlp
import shutil
import os

def download_audio_from_youtube(video_url, output_path='audio.mp3'):
    # Configuração do yt-dlp para baixar apenas o áudio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=True)
        # O arquivo baixado terá a extensão do melhor formato de áudio disponível
        audio_file_path = 'temp_audio.' + info_dict.get('ext', 'webm')
       
        # Verificar se o arquivo foi baixado corretamente
        if not os.path.isfile(audio_file_path):
            raise FileNotFoundError(f'Arquivo de áudio {audio_file_path} não encontrado.')

        # Copiar o arquivo de áudio para MP3
        shutil.copy(audio_file_path, output_path)
       
        # Remover o arquivo temporário
        os.remove(audio_file_path)
       
        print(f'Áudio salvo em {output_path}')

# Solicitar URL do usuário
print("****************************")
print("* Instagram: rafael_cyber1 *")
print("****************************")
video_url = input('Digite a URL do vídeo do YouTube: ')
download_audio_from_youtube(video_url)
