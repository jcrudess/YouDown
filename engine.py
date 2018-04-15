from Video import *
import _thread
from pomocni import *
import threading
import os

def dodaj(app, url):
    updateStatus(app, 'Dodajem..........')
    _thread.start_new_thread(dodajT, (app, url,))


def dodajT(app, url, value = None):

    if value == None:
        provjera = provjeriURL(url)
    else:
        provjera = value

    br = 0

    if provjera=='video':
        video = Video(url)

        tekst = video.title

        app.lista.insert(app.lista.size(), tekst)
        app.inp.delete(0, "end")
        ##updateaj status
        updateStatus(app, tekst)
        ##dodaj u dictionary
        app.mainDict[tekst] = video
    elif provjera == 'playlist':
        lista = izradiListu(url) ##parsiraj html i za svaki link pokreni proceduru za dodavanje
        for i in lista:
            dodajT(app, i, 'video')

    elif provjera=='playlist_dorada':    ##doradi link i pokreni rekurzivno kao da se poslao originalni playlist link
        dodajT(app, "http://www.youtube.com/playlist?"+url.split('&')[1], 'playlist')
    else:
        updateStatus(app, 'Uneseni URL nije validan!')
        app.inp.delete(0, "end")

def brisi(app, opcija):
    pos = 0
    if app.lista.curselection() or opcija == 'svi':
        if opcija == 'oznaceni':
            selekt = app.lista.curselection()
            updateStatus(app, 'Označeni zapisi su obrisani!')
        else:
            selekt = range(app.lista.size())
            updateStatus(app, 'Svi zapisi su obrisani!')
        for i in selekt:
            index = i - pos
            naziv = app.lista.get(index)
            del app.mainDict[naziv]
            app.lista.delete(index)
            pos+=1
    else:
        pass

def updateStatus(app, tekst):
    app.statusLabel.config(text = tekst)


def skiniSve(app):
    t = threading.Thread(target = skiniSveT, args = (app,))
    t.start()
    #_thread.start_new_thread(skiniSveT, (app,))



def skiniSveT(app):
    threadovi = []
    br = 0
    for i in app.mainDict:
        thr = threading.Thread(target = downThread, args = (app, i))
        threadovi.append(thr)

    while True:
        if br==len(threadovi):
            print("break petlje")
            break

        if len(threading.enumerate())==int(app.threadLimit) + 2:
        #plus 2 jer računam main thread + pozivajući master thread
            pass
        else:
            threadovi[br].start()
            br+=1


def downThread(app, title):
    print("Počinjem "+title)
    app.mainDict[title].download(app.storePath)
    print("Završavam "+title)
    print("Počinjem konverziju "+title)
    MP3Convert(app.storePath, title)
    print("Završavam konverziju "+title)

def MP3Convert(storepath, title):
    mp4 = '.mp4'
    mp3 = '.mp3'
    fpath = storepath+'"'+title+mp4+'"'
    newfpath = storepath+'"'+title+mp3+'"'
    ffmpegPath = "C:/Users/Vjekoslav/Desktop/KOD/Python/YouDown/ffmpeg.exe"
    os.system(ffmpegPath+' -i '+fpath+' '+newfpath)
    print("unutar konverzija gotova")
    str = 'del '+'"'+storepath+title+mp4+'"'
    os.system(str.replace('/', '\\'))





