from tkinter import *

class interpretationOfStack:
    def __init__(self,master,canvas):
        self.master = master
        self.canvas = canvas
        self.lista = []
        self.entry = Entry(self.canvas)
        self.entry.pack()
        self.entry.insert(0, "Dodaj")

    def add(self):
        if (len(self.lista)<10):
            self.wartosc = self.entry.get()
            self.lista.append(self.wartosc)
            self.wypisz()
            self.canvas.create_text(80, 170, text='Dodano: '+self.wartosc, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 170, text='Stos jest pełny', fill='red')

    def usun(self):
        if len(self.lista) > 0:
            item = self.lista.pop()
            self.wypisz()
            self.canvas.create_text(80, 170, text='Usunięto: '+item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 170, text='Stos jest pusty', fill='red')

    def clearInput(self,e):
        self.entry.delete(0, END)

    def pobierz(self):
        if len(self.lista)>0:
            self.wypisz()
            self.canvas.create_text(80, 420, text='Pobrano: '+self.lista[len(self.lista) - 1], fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 420, text='Stos jest pusty', fill='red')

    def pobierz_usun(self):
        if len(self.lista)>0:
            item = 'Pobrano i usunięto: '+self.lista.pop()
            self.wypisz()
            self.canvas.create_text(110, 420, text=item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 420, text='Stos jest pusty', fill='red')

    def wypisz(self):
        self.canvas.delete('all')
        j = 10
        for i in range(len(self.lista)):
            j = j-1
            x = 450
            y = (j * 50) + 60
            width = 550
            height =(j * 50) + 100
            self.canvas.create_rectangle(x, y, width, height, fill='lightgrey')
            self.canvas.create_text((x + width) / 2, (y + height) / 2, text=self.lista[i])

        self.canvas.create_window(50, 50, window=self.entry, anchor=NW,width=100)
        self.entry.bind("<Button-1>",self.clearInput)

        dodaj = Button(self.master, text="Dodaj do stosu", command=self.add, anchor="center")
        dodaj.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(40, 75, anchor=NW, window=dodaj)

        usun = Button(self.master, text="Usuń ze stosu", command=self.usun, anchor='center')
        usun.configure(width=15,activebackground = 'lightgrey')
        self.canvas.create_window(40, 120, anchor=NW, window=usun)

        pobierz = Button(self.master, text='Pobierz ze stosu', command=self.pobierz, anchor='center')
        pobierz.configure(width=15, activebackground='lightgrey')
        self.canvas.create_window(40, 320, anchor=NW, window=pobierz)

        pobierz_usun = Button(self.master, text='Pobierz i usuń ze stosu', command=self.pobierz_usun, anchor='center')
        pobierz_usun.configure(width=20, activebackground='lightgrey')
        self.canvas.create_window(40, 360, anchor=NW, window=pobierz_usun)