import pytube
from pomocni import *
class Video:
    def __init__(self, url):
        self.url = url
        self.title = dohvatiTitle(url)

    def download(self,storePath):
        yt = pytube.YouTube(self.url)
        self.stream = yt.streams.filter(only_audio=True).first()
        self.stream.download(storePath)


