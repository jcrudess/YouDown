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
            br+=1
            dodajT(app, i, 'video')
            if br >= 5:
                break

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
    _thread.start_new_thread(skiniSveT, (app,))
    #TODO testirati skidanje u vise threadova

def skiniSveT(app):
    c1 = datetime.datetime.now()
    for i in app.mainDict:
        c1 = datetime.datetime.now()
        print(i + ' počinjem ' + str(c1))
        updateStatus(app, 'Skidam '+i+'..).....')
        app.mainDict[i].download(app.storePath)
        c2 = datetime.datetime.now()
        print(i + ' počinjem ' + str(c2))
    updateStatus(app, 'Skidanje završeno')
