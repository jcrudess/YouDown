import requests
from bs4 import BeautifulSoup

def izradiListu(url):
    lista = []
    r = requests.get(url)
    data = r.text
    br = 0

    soup = BeautifulSoup(data, "html.parser")

    for i in soup.find_all("td", {"class":"pl-video-title"}):
        lista.append("http://www.youtube.com"+i.a.get('href').split('&')[0])
    return lista

def provjeriURL (url):
    if 'youtube' in url:
        if 'list=' in url:
            if 'watch' in url:
                return 'playlist_dorada'
            else:
                return 'playlist'
        elif 'watch?v=' in url:
            return 'video'
        else:
            return 'greska'
    else:
        return 'greska'

def dohvatiTitle(url):
    r = requests.get(url)
    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    title = soup.find("title").string.split(' - YouTube')[0]

    return title