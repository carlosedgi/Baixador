import yt_dlp
import os
import platform
from datetime import datetime



def clear_screen():
    # Verifica o sistema operacional e executa o comando de limpeza da tela
    os_system = platform.system().lower()
    if os_system == "windows":
        os.system("cls")  # Para Windows
    else:
        os.system("clear")  # Para Linux/macOS

def download_video(video_url, platform):
    try:
        # Caminho para a pasta 'downloads' no mesmo diretório do script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        downloads_folder = os.path.join(script_dir, "downloads")
        
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)
        
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_id = "video"
        if "youtube" in video_url or "youtu.be" in video_url:
            platform = "YouTube"
            if "v=" in video_url:
                video_id = video_url.split("v=")[1].split("&")[0]
            elif "youtu.be/" in video_url:
                video_id = video_url.split("youtu.be/")[1]
        
        file_name = f"{platform}_{current_time}.%(ext)s"
        
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(downloads_folder, file_name),
        }

        # Adiciona cookies do navegador se a plataforma for Instagram
        if platform.lower() == "instagram":
            ydl_opts['cookiesfrombrowser'] = ("chrome",)  # ou "firefox" se preferir

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            print(f"Vídeo baixado: {info_dict['title']}")
            print(f"Salvo em: {os.path.join(downloads_folder, f'{platform}_{current_time}.mp4')}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")


def download_youtube(video_url):
    download_video(video_url, "YouTube")

def download_twitter(video_url):
    download_video(video_url, "Twitter")

def download_facebook(video_url):
    download_video(video_url, "Facebook")

def download_instagram(video_url):
    download_video(video_url, "Instagram")

def download_tiktok(video_url):
    download_video(video_url, "TikTok")

def download_reddit(video_url):
    download_video(video_url, "Reddit")

if __name__ == "__main__":
    while True:

        #clear_screen()  # Limpa a tela antes de exibir o menu
        
        print("\nEscolha a plataforma para baixar vídeos:")
        print("1 - YouTube")
        print("2 - Twitter")
        print("3 - Facebook")
        print("4 - Instagram")
        print("5 - TikTok")
        print("6 - Reddit")
        print("7 - Sair")
        
        opcao = input("Digite o número da opção desejada: ").strip()
        
        plataformas = {"1": "YouTube", "2": "Twitter", "3": "Facebook", "4": "Instagram", "5": "TikTok", "6": "Reddit"}
        
        if opcao == "7":
            print("Saindo...")
            break
        elif opcao in plataformas:
            video_url = input(f"Digite o URL do vídeo do {plataformas[opcao]}: ").strip()
            if opcao == "1":
                download_youtube(video_url)
            elif opcao == "2":
                download_twitter(video_url)
            elif opcao == "3":
                download_facebook(video_url)
            elif opcao == "4":
                download_instagram(video_url)
            elif opcao == "5":
                download_tiktok(video_url)
            elif opcao == "6":
                download_reddit(video_url)
        else:
            print("Opção inválida. Tente novamente.")
