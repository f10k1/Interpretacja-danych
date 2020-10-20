from tkinter import *

class interpretationOfDeque:
    def __init__(self,master,canvas):
        self.master = master
        self.canvas = canvas
        self.lista = []
        self.entry = Entry(self.canvas)
        self.entry.pack()
        self.entry.insert(0, "Dodaj")

    def add_p(self):
        if (len(self.lista)<10):
            self.wartosc = self.entry.get()
            self.lista.insert(0,self.wartosc)
            self.wypisz()
            self.canvas.create_text(90, 240, text='Dodano na początek: '+self.wartosc, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 240, text='Kolejka jest pełna', fill='red')
    def add_k(self):
        if (len(self.lista)<10):
            self.wartosc = self.entry.get()
            self.lista.append(self.wartosc)
            self.wypisz()
            self.canvas.create_text(90, 240, text='Dodano na koniec: '+self.wartosc, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 240, text='Kolejka jest pełna', fill='red')

    def usun_p(self):
        if len(self.lista) > 0:
            self.canvas.delete('all')
            item = self.lista.pop(0)
            self.wypisz()
            self.canvas.create_text(90, 240, text='Usunięto z początku: '+item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 240, text='Kolejka jest pusta', fill='red')
    def usun_k(self):
        if len(self.lista) > 0:
            self.canvas.delete('all')
            item = self.lista.pop()
            self.wypisz()
            self.canvas.create_text(90, 240, text='Usunięto z końca: ' + item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 240, text='Kolejka jest pusta', fill='red')

    def clearInput(self,e):
        self.entry.delete(0, END)

    def pobierz_p(self):
        if len(self.lista)>0:
            self.wypisz()
            self.canvas.create_text(90, 480, text='Pobrano z początku: '+self.lista[0], fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 480, text='Kolejka jest pusta', fill='red')
    def pobierz_k(self):
        if len(self.lista)>0:
            self.wypisz()
            self.canvas.create_text(90, 480, text='Pobrano z końca: '+self.lista[len(self.lista)-1], fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 480, text='Kolejka jest pusta', fill='red')

    def pobierz_usun_p(self):
        if len(self.lista)>0:
            item = 'Pobrano i usunięto z początku: '+self.lista.pop(0)
            self.wypisz()
            self.canvas.create_text(90, 480, text=item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 480, text='Kolejka jest pusta', fill='red')
    def pobierz_usun_k(self):
        if len(self.lista)>0:
            item = 'Pobrano i usunięto z końca: '+self.lista.pop()
            self.wypisz()
            self.canvas.create_text(90, 480, text=item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(90, 480, text='Kolejka jest pusta', fill='red')

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

        self.canvas.create_window(50, 40, window=self.entry, anchor=NW,width=100)
        self.entry.bind("<Button-1>",self.clearInput)

        dodaj_p = Button(self.master, text="Dodaj na początek", command=self.add_p, anchor="center")
        dodaj_p.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(40, 70, anchor=NW, window=dodaj_p)
        dodaj_k = Button(self.master, text="Dodaj na koniec", command=self.add_k, anchor="center")
        dodaj_k.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(40, 150, anchor=NW, window=dodaj_k)

        usun_p = Button(self.master, text="Usuń z początku", command=self.usun_p, anchor='center')
        usun_p.configure(width=15,activebackground = 'lightgrey')
        self.canvas.create_window(40, 110, anchor=NW, window=usun_p)
        usun_k = Button(self.master, text="Usuń z końca", command=self.usun_k, anchor='center')
        usun_k.configure(width=15, activebackground='lightgrey')
        self.canvas.create_window(40, 190, anchor=NW, window=usun_k)

        pobierz_p = Button(self.master, text='Pobierz z początku', command=self.pobierz_p, anchor='center')
        pobierz_p.configure(width=15, activebackground='lightgrey')
        self.canvas.create_window(40, 320, anchor=NW, window=pobierz_p)
        pobierz_usun_p = Button(self.master, text='Pobierz i usuń z początku', command=self.pobierz_usun_p, anchor='center')
        pobierz_usun_p.configure(width=20, activebackground='lightgrey')
        self.canvas.create_window(40, 355, anchor=NW, window=pobierz_usun_p)

        pobierz_k = Button(self.master, text='Pobierz z końca', command=self.pobierz_k, anchor='center')
        pobierz_k.configure(width=15, activebackground='lightgrey')
        self.canvas.create_window(40, 395, anchor=NW, window=pobierz_k)
        pobierz_usun_k = Button(self.master, text='Pobierz i usuń z końca', command=self.pobierz_usun_k, anchor='center')
        pobierz_usun_k.configure(width=20, activebackground='lightgrey')
        self.canvas.create_window(40, 430, anchor=NW, window=pobierz_usun_k)