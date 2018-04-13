import pytube
from pomocni import *
class Video:
    def __init__(self, url):
        self.url = url
        self.title = dohvatiTitle(url)
        #TODO doraditi da uzme stream najveće dostupne kvalitete

    def download(self,storePath):
        yt = pytube.YouTube(self.url)
        self.stream = yt.streams.filter(only_audio=True).first()
        self.stream.download("C:/Users/Vjekoslav/Documents/test")
        #TODO doraditi slanje lokacije spremanja iz config filea


