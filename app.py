import tkinter
from tkinter import font
import engine


class App:
    #dictionary koji biljezi zapise u paru youtube.title:youtube objekt
    mainDict = {}


    def __init__(self, storePath):
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
        self.delOneButton.grid(column = 0, row = 1, sticky = "w")
        ### tipka za brisanje svih
        self.delAllButton = tkinter.Button(self.listFrame, text="Obriši sve", command=lambda:engine.brisi(self, 'svi'))
        self.delAllButton.grid(column = 0, ipadx = 10, row = 1, sticky = "e")
        ### tipka za download svih
        self.downAllButton = tkinter.Button(self.listFrame, text = "Skini sve", command = lambda:engine.skiniSve(self, storePath))
        self.downAllButton.grid(column = 3, ipadx = 20, row = 1, sticky = "e")
        ### frame za statusnu traku
        self.statusFrame = tkinter.Frame(self.win, height=10, width=200, highlightbackground="#9e9aa7", highlightthickness=1)
        self.statusFrame.grid(row = 2, column = 0)
        ### status text (label)
        self.statusLabel = tkinter.Label(self.statusFrame, text = "Idle", width = 50)
        self.statusLabel.grid(column = 0, pady = 2, row = 0)

        self.win.mainloop()


