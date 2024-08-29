import yt_dlp
import shutil
import os

def download_video_from_youtube(video_url, output_path='video.mp4'):
    print("Iniciando o download do vídeo...")

    # Configuração do yt-dlp para baixar o vídeo e o áudio em um único arquivo
    ydl_opts = {
        'format': 'best',  # Baixa o melhor formato de vídeo e áudio disponível combinado
        'outtmpl': 'temp_video.%(ext)s',  # Define o template para o nome do arquivo temporário
        'noplaylist': True,  # Evita baixar playlists
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Extraindo informações do vídeo: {video_url}")
        info_dict = ydl.extract_info(video_url, download=True)
        video_file_path = 'temp_video.' + info_dict.get('ext', 'mp4')
        print(f"Arquivo baixado temporariamente como: {video_file_path}")

        # Verificar se o arquivo foi baixado corretamente
        if not os.path.isfile(video_file_path):
            raise FileNotFoundError(f'Arquivo de vídeo {video_file_path} não encontrado.')

        # Copiar o arquivo de vídeo para o destino final
        shutil.copy(video_file_path, output_path)
        print(f'Arquivo de vídeo copiado para: {output_path}')

        # Remover o arquivo temporário
        os.remove(video_file_path)
        print(f'Arquivo temporário {video_file_path} removido.')

        print(f'Vídeo salvo em {output_path}')

# Solicitar URL do usuário
print("****************************")
print("* Instagram: rafael_cyber1 *")
print("****************************")
video_url = input('Digite a URL do vídeo do YouTube: ')
download_video_from_youtube(video_url)
