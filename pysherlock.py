import requests
import whois
import dns.resolver
import os
import hashlib
from datetime import datetime
from bs4 import BeautifulSoup

# Dicionário com as redes sociais e seus URLs base para busca de usernames
print("*****************************")
print("* instagram: @rafael_cyber1 *")
print("*****************************")
social_media_urls = {
    'Instagram': 'https://www.instagram.com/{}',
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
    'XHamster': 'https://xhamster.com/users/{}',
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
    'Dailymotion': 'https://www.dailymotion.com/br/{}',
    'Cont.ws': 'https://cont.ws/@{}',
    'Estante Virtual': 'https://www.estantevirtual.com.br/busca?editora={}',
    'Kwai': 'https://www.kwai.com/@{}',
    'Disqus': 'https://disqus.com/by/{}/?',
    'Hack This Site': 'https://www.hackthissite.org/user/view/{}',
    'Telegram': 'https://t.me/{}',
    'Duolingo': 'https://www.duolingo.com/profile/{}',
    'Hentai City': 'https://www.hentaicity.com/profile/{}',
    'Strip Chat': 'https://stripchat.com/user/{}',
    'Ifunnny': 'https://br.ifunny.co/user/{}',
    'Itch': 'https://itch.io/profile/{}',
    'Etsy': 'https://www.etsy.com/pt/people/{}?ref=l_review',
    'Ludopedia': 'https://ludopedia.com.br/usuario/{}',
    'Viva o Linux': 'https://www.vivaolinux.com.br/~{}',
    'Cursos Alura': 'https://cursos.alura.com.br/user/{}',
    'Guj': 'https://www.guj.com.br/u/{}/summary',
    'Mk Auth': 'https://mk-auth.com.br/members/{}',
    'Forum Elipse': 'https://forum.elipse.com.br/u/{}/summary',
    'Home Assistent': 'https://homeassistantbrasil.com.br/u/{}/summary',
    'Endian Eth0': 'https://endian.eth0.com.br/forums/profile/{}',
    'Vakinha': 'https://www.vakinha.com.br/usuario/{}'
        'Mastodon': 'https://mastodon.social/@{}',
    'Anime Planet': 'https://www.anime-planet.com/users/{}',
    'Bsky': 'https://bsky.app/profile/{}.bsky.social',
    'Live Journal': 'https://{}.livejournal.com/',
    'Deviantart': 'https://www.deviantart.com/{}/gallery',
    'Soundcloud': 'https://soundcloud.com/{}',
    'Last': 'https://www.last.fm/pt/user/{}',
    'Veoh': 'https://www.veoh.com/users/{}',
    'Behance': 'https://www.behance.net/{}',
    'Tripadvisor': 'https://www.tripadvisor.com.br/Profile/{}',
    'Polyvore': 'https://polyvore.ch/author/{}/',
    'Kongregate': 'https://www.kongregate.com/accounts/{}',
    'Beebom': 'https://beebom.com/author/{}/',
    'Wikihow': 'https://www.wikihow.com/Author/{}',
    'Laptopmag': 'https://www.laptopmag.com/uk/author/{}',
    'Flip Board': 'https://flipboard.com/@{}',
    'Hackr': 'https://hackr.io/blog/author/{}',
    'Clean': 'https://clean.email/authors/{}',
    'Gravatar': 'https://gravatar.com/{}',
    'Dio': 'https://www.dio.me/users/{}',
    'Sex HD': 'https://www.sexhd.pics/mobile/{}/',
    'Blog Bang': 'https://blog.bang.com/author/{}/',
    'Bang': 'https://www.bang.com/videos?term={}',
    'Eplay': 'https://www.eplay.com/{}',
    'Eporner': 'https://www.eporner.com/profile/{}/',
    'Eyeem': 'https://www.eyeem.com/u/{}',
    'Dribbble': 'https://dribbble.com/{}',
    'Members Fotki': 'https://members.fotki.com/{}/about/',
    'Bebee': 'https://br.bebee.com/bee/{}',
    'Daily Motion': 'https://www.dailymotion.com/{}',
    'Sound Cloud': 'https://soundcloud.com/{}',
    'Weibo': 'https://www.weibo.com/{}',
    'Kiwi Box': 'https://www.kiwibox.com/author/{}/',
    'Forums Opera': 'https://forums.opera.com/user/{}',
    'Revista Forum': 'https://revistaforum.com.br/autor/{}.html',
    'Viex Americanas': 'https://www.viex-americas.com/{}/',
    'Community Kobotoolbox': 'https://community.kobotoolbox.org/u/{}/summary',
    'Forum Asana': 'https://forum.asana.com/u/{}/summary'
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

def consulta_dns_whois_ip(domain):
    print(f'\nConsultando registros DNS para o domínio: {domain}')
    
    try:
        # Consultar registros DNS
        a_records = [r.address for r in dns.resolver.resolve(domain, 'A')]
        aaaa_records = [r.address for r in dns.resolver.resolve(domain, 'AAAA')]
        
        if a_records:
            print(f'\nEndereços IPv4 para {domain}:')
            for ip in a_records:
                print(f'  {ip}')
        else:
            print(f'Nenhum registro A encontrado para {domain}')
        
        if aaaa_records:
            print(f'\nEndereços IPv6 para {domain}:')
            for ip in aaaa_records:
                print(f'  {ip}')
        else:
            print(f'Nenhum registro AAAA encontrado para {domain}')
    
    except Exception as e:
        print(f'[!] Erro ao consultar DNS: {e}')
    
    print(f'\nConsultando informações WHOIS para o domínio: {domain}')
    try:
        whois_info = whois.whois(domain)
        
        print('Dados brutos do WHOIS:')
        for key, value in whois_info.items():
            if isinstance(value, list):
                value = ', '.join([v.strftime('%Y-%m-%d %H:%M:%S') if isinstance(v, datetime) else str(v) for v in value])
            elif isinstance(value, datetime):
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            print(f'  {key:<20}: {value}')
    
    except Exception as e:
        print(f'[!] Erro ao buscar informações WHOIS: {e}')
    
    print(f'\nConsultando informações IPs')
    try:
        # Verificar IPs obtidos
        all_ips = a_records + aaaa_records
        for ip in all_ips:
            print(f'\nConsultando IP: {ip}')
            response = requests.get(f'http://ip-api.com/json/{ip}')
            if response.status_code == 200:
                data = response.json()
                print(f'Localização do IP {ip}:')
                print(f'  País: {data.get("country", "Desconhecido")}')
                print(f'  Região: {data.get("regionName", "Desconhecido")}')
                print(f'  Cidade: {data.get("city", "Desconhecido")}')
                print(f'  CEP: {data.get("zip", "Desconhecido")}')
                print(f'  ISP: {data.get("isp", "Desconhecido")}')
            else:
                print(f'[!] Erro ao consultar IP {ip}')
    
    except Exception as e:
        print(f'[!] Erro ao consultar IPs: {e}')
def menu():
    while True:
        print("\nMenu:")
        print("1. Verificar Usernames")
        print("2. DNS, WHOIS, IP")
        print("3. Sair")

        choice = input("Escolha uma opção (1/2/3): ")

        if choice == '1':
            username = input("Digite o username a ser pesquisado: ")
            sherlock(username)
        elif choice == '2':
            domain = input("Digite o domínio (ex: exemplo.com): ")
            consulta_dns_whois_ip(domain)
        elif choice == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
