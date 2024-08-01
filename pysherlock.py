import requests
import argparse
from bs4 import BeautifulSoup
import os
import hashlib

# Dicionário com as redes sociais e seus URLs base para busca de usernames
print("*****************************")
print("* instagram: @rafael_cyber1 *")
print("*****************************")
social_media_urls = {
    'Instagram': 'https://www.instagram.com/{}',
    'Twitter': 'https://twitter.com/{}',
    'Discord': 'https://discord.com/users/{}',
    'Reddit': 'https://www.reddit.com/user/{}',
    'Medium': 'https://medium.com/@{}',
    'Facebook': 'https://www.facebook.com/{}',
    'GitHub': 'https://github.com/{}',
    'Snapchat': 'https://www.snapchat.com/add/{}',
    'WeChat': 'https://weixin.qq.com/u/{}',
    'LinkedIn': 'https://www.linkedin.com/in/{}',
    'Skype': 'https://join.skype.com/invite/{}',
    'Spotify': 'https://open.spotify.com/user/{}',
    'Pinterest': 'https://www.pinterest.com/{}/',
    'YouTube': 'https://www.youtube.com/{}',
    'Twitch': 'https://www.twitch.tv/{}',
    'TikTok': 'https://www.tiktok.com/@{}',
    'Xvideos': 'https://www.xvideos.com/profiles/{}',
    'Xnxx': 'https://www.xnxx.com/profile/{}',
    'Pornhub': 'https://www.pornhub.com/users/{}',
    'FreeCodeCamp': 'https://www.freecodecamp.org/{}',
    'TryHackMe': 'https://tryhackme.com/p/{}',
    'Freelancer': 'https://www.freelancer.com/u/{}',
    'FreelancerBR': 'https://www.freelancer.com.br/u/{}',
    'Privacy': 'https://privacy.com/{}',
    'OnlyFans': 'https://onlyfans.com/{}',
    'GitLab': 'https://gitlab.com/{}',
    'Archive.org': 'https://archive.org/details/@{}',
    'Pr0gramm': 'https://pr0gramm.com/user/{}',
    'Fandom': 'https://www.fandom.com/wiki/User:{}',
    'Interpals': 'https://www.interpals.net/{}',
    'PSNProfiles': 'https://psnprofiles.com/{}',
    'About.me': 'https://about.me/{}',
    'PyPI': 'https://pypi.org/user/{}',
    'Tumblr': 'https://{}.tumblr.com/',
    '9GAG': 'https://9gag.com/u/{}',
    'VK': 'https://vk.com/{}',
    'Flickr': 'https://www.flickr.com/people/{}',
    'YouPic': 'https://youpic.com/photographer/{}',
    'MyAnimeList': 'https://myanimelist.net/profile/{}',
    'Wattpad': 'https://www.wattpad.com/user/{}',
    'MySpace': 'https://myspace.com/{}',
    'Passes': 'https://passes.com/{}',
    'Disqus': 'https://disqus.com/by/{}',
    'Threads': 'https://threads.net/{}',
    'XHamester': 'https://xhamster.com/users/{}',
    'Sharesome': 'https://sharesome.com/{}',
    'YouPorn': 'https://youporn.com/users/{}',
    'Chaturbate': 'https://chaturbate.com/{}',
    'BongaCams': 'https://pt.bongacams.com/profile/{}',
    'Tinder': 'https://tinder.com/@{}',
    'LiveJasmin': 'https://livejasmin.com/{}',
    '7 Cups': 'https://www.7cups.com/{}',
    'Apclips': 'https://apclips.com/{}',
    'AdmireMe': 'https://admireme.vip/{}',
    'Airbit': 'https://airbit.com/{}',
    'AllMyLinks': 'https://allmylinks.com/{}',
    'AllThingsWorn': 'https://www.allthingsworn.com/{}',
    'AniWorld': 'https://aniworld.to/{}',
    'AniList': 'https://anilist.co/{}',
    'ArtStation': 'https://www.artstation.com/{}',
    'Blipfoto': 'https://www.blipfoto.com/{}',
    'Blogger': 'https://www.blogger.com/{}',
    'RedTube': 'https://www.redtube.com.br/{}',
    'RoyalCams': 'https://pt.royalcams.com/{}',
    'Shpock': 'https://www.shpock.com/{}',
    'Scribd': 'https://pt.scribd.com/{}',
    'Scratch': 'https://scratch.mit.edu/{}',
    'ImgSrc': 'https://imgsrc.ru/{}',
    'MercadoLivre': 'https://www.mercadolivre.com.br/{}',
    'Note': 'https://note.com/{}',
    'PicsArt': 'https://picsart.com/{}',
    'Dailymotion': 'https://www.dailymotion.com/br/{}'
}

# Cache simples para armazenar respostas de páginas
cache_dir = 'cache'

def get_page_content(url):
    """Função para obter o conteúdo de uma página, com cache."""
    cache_filename = hashlib.md5(url.encode()).hexdigest() + '.html'
    cache_path = os.path.join(cache_dir, cache_filename)

    if os.path.exists(cache_path):
        with open(cache_path, 'r', encoding='utf-8') as f:
            return f.read()

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.999 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code == 200:
            content = response.text
            # Salvar no cache
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return content
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f'[!] Erro ao acessar {url}: {e}')
        return None

def check_social_media(username):
    results_found = False
    for social_media, url_template in social_media_urls.items():
        base_url = url_template.format(username)
        try:
            content = get_page_content(base_url)
            if content:
                soup = BeautifulSoup(content, 'html.parser')
                # Exemplo de verificação específica para Instagram
                if social_media == 'Instagram':
                    if soup.find('meta', property='og:title', content=f'@{username} • Instagram photos and videos'):
                        print(f'[+] Username encontrado no {social_media}: {base_url}')
                        results_found = True
                # Exemplo genérico de verificação
                elif username in soup.get_text():
                    print(f'[+] Username encontrado no {social_media}: {base_url}')
                    results_found = True
        except Exception as e:
            print(f'[!] Erro de requisição para {social_media}: {e}')

    if not results_found:
        print(f'[-] Nenhum resultado encontrado para o username "{username}"')

def sherlock(username):
    print(f'[+] Iniciando busca por "{username}"...\n')
    check_social_media(username)

def main():
    parser = argparse.ArgumentParser(description='Sherlock em Python - Busca de usernames em redes sociais')
    parser.add_argument('username', help='Username a ser buscado')
    args = parser.parse_args()

    sherlock(args.username)

if __name__ == "__main__":
    main()
