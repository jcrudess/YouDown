from Video import *
import _thread
from pomocni import *
import datetime

def dodaj(app, url):
    updateStatus(app, 'Dodajem..........')
    _thread.start_new_thread(dodajT, (app, url,))

def dodajT(app, url, value = None):

    if value == None:
        provjera = provjeriURL(url)
    else:
        provjera = value

    if provjera=='video':
        video = Video(url)

        tekst = video.title

        app.lista.insert(app.lista.size(), tekst)
        app.inp.delete(0, "end")
        ##updateaj status
        updateStatus(app, tekst)
        ##dodaj u dictionary
        #TODO kako složiti brisanje? dodati u tuple sa indeksom
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
    #TODO dodaj brisanje iz dictionarya
    if app.lista.curselection() or opcija == 'svi':
        if opcija == 'oznaceni':
            selekt = app.lista.curselection()
            updateStatus(app, 'Označeni zapisi su obrisani!')
        else:
            selekt = range(app.lista.size())
            updateStatus(app, 'Svi zapisi su obrisani!')
        for i in selekt:
            index = i - pos
            app.lista.delete(index)
            pos+=1
    else:
        pass

def updateStatus(app, tekst):
    app.statusLabel.config(text = tekst)


def skiniSve(app, storePath):
    _thread.start_new_thread(skiniSveT, (app,storePath,))
    #TODO testirati skidanje u vise threadova

def skiniSveT(app, storePath):
    c1 = datetime.datetime.now()
    print(c1)
    for i in app.mainDict:
        c1 = datetime.datetime.now()
        print(i + ' počinjem ' + str(c1))
        updateStatus(app, 'Skidam '+i+'..).....')
        app.mainDict[i].download(storePath)
        c2 = datetime.datetime.now()
        print(i + ' počinjem ' + str(c2))
    updateStatus(app, 'Skidanje završeno')
