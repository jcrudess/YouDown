import tkinter
from tkinter import font
import engine
from tkinter import filedialog
import configparser

class App:
    #dictionary koji biljezi zapise u paru youtube.title:youtube objekt
    mainDict = {}
    storePath = ''
    appSet = None


    def __init__(self, storePath, threadLimit):
        self.storePath = storePath
        self.threadLimit = threadLimit
        print(self.storePath)
        self.win = tkinter.Tk()
        self.win.title("YouDown v0.1.1")
        self.win.resizable(False, False)
        ### input frame
        self.inputFrame = tkinter.Frame(self.win, height = 50, width = 400)
        self.inputFrame.grid(column=0, columnspan = 2, padx=7, pady = 2, row = 0)
        ### input linija
        self.inp = tkinter.Entry(self.inputFrame, width = 75)
        self.inp.grid(column = 0, pady = 1, row = 0)
        self.inp.bind("<Return>", lambda event:engine.dodaj(self, self.inp.get()))
        ### input tipka
        self.addButton = tkinter.Button(self.inputFrame, text = "Dodaj", command=lambda: engine.dodaj(self, self.inp.get()))
        self.addButton.grid(row = 0, column=1, ipadx = 5, padx=10)

        ### lista frame
        self.listFrame = tkinter.Frame(self.win, height = 200, width = 400)
        self.listFrame.grid(column = 0, row = 1, rowspan = 1)
        ### lista listbox
        list_font = font.Font(size = 11, family = "Arial")
        self.lista = tkinter.Listbox(self.listFrame, selectmode = "extended", width = 65, font = list_font, height = 30)
        self.lista.grid(column = 0, columnspan = 4, pady = 2, row = 0)
        self.scroll = tkinter.Scrollbar(self.listFrame, orient = "vertical", command = self.lista.yview)
        self.scroll.grid(column = 4, row = 0, rowspan = 1, sticky = "ns")
        ### tipka za brisanje označenog
        self.delOneButton = tkinter.Button(self.listFrame, text="Obriši odabrane", command=lambda:engine.brisi(self, 'oznaceni'))
        self.delOneButton.grid(column = 0, row = 1, sticky = "w", ipadx = 10)
        ### tipka za brisanje svih
        self.delAllButton = tkinter.Button(self.listFrame, text="Obriši sve", command=lambda:engine.brisi(self, 'svi'))
        self.delAllButton.grid(column = 0, ipadx = 8, row = 1, sticky = "e")
        ### tipka za postavke
        self.delAllButton = tkinter.Button(self.listFrame, text="Postavke", command=self.pokreniPostavke)
        self.delAllButton.grid(column=3,sticky='w', row=1, ipadx = 12)
        ### tipka za download svih
        self.downAllButton = tkinter.Button(self.listFrame, text = "Skini sve", command = lambda:engine.skiniSve(self,))
        self.downAllButton.grid(column = 3, ipadx = 15, row = 1, sticky = "e")
        ### frame za statusnu traku
        self.statusFrame = tkinter.Frame(self.win, height=10, width=200, highlightbackground="#9e9aa7", highlightthickness=1)
        self.statusFrame.grid(row = 2, column = 0)
        ### status text (label)
        self.statusLabel = tkinter.Label(self.statusFrame, text = "Idle", width = 50)
        self.statusLabel.grid(column = 0, pady = 2, row = 0)

        self.win.mainloop()
    def pokreniPostavke(self):
        #self.appSet = AppSettings(self)
        self.winSet = tkinter.Toplevel(self.win)
        self.winSet.title("Postavke")
        self.winSet.master = self.win
        self.winSet.resizable(False, False)
        self.dirLabel = tkinter.Label(self.winSet, text="Lokacija spremanja:")
        self.dirLabel.grid(column=0, row=0, padx=1)
        self.dirInput = tkinter.Label(self.winSet, text=self.storePath)
        self.dirInput.grid(column=1, row=0, padx=5)
        self.dirButton = tkinter.Button(self.winSet, text="Odaberi...", command=self.loadDir)
        self.dirButton.grid(column=2, row=0, padx=10)

    def loadDir(self):
        fileDialog = filedialog.askdirectory()
        self.dirInput.config(text = fileDialog)
        self.storePath = fileDialog + '/'

        config = configparser.RawConfigParser()
        config.read('settings.cfg')
        config.set('Postavke', 'SAVE_LOKACIJA', self.storePath)

        with open('settings.cfg', 'w') as cfgfile:
            config.write(cfgfile)




