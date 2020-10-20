from tkinter import *

class interpretationOfList:
    def __init__(self,master,canvas):
        self.master = master
        self.canvas = canvas
        self.lista = []
        self.entry = Entry(self.canvas)
        self.entry.pack()
        self.entry.insert(0, "Dodaj")

    def add(self):
        index = self.add_i.get()
        self.wartosc = self.entry.get()
        if (len(self.lista)<10 and index == ' '):
            self.lista.append(self.wartosc)
            self.wypisz()
            self.canvas.create_text(80, 110, text='Dodano: '+self.wartosc, fill='green')
        elif (len(self.lista)<10):
            self.lista.insert(int(index),self.wartosc)
            self.wypisz()
            self.add_i.set(index)
            self.canvas.create_text(115, 110, text='Dodano: '+self.wartosc+" na pozycji: "+index, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 110, text='Lista jest pełna', fill='red')

    def change(self):
        index = self.change_i.get()
        self.wartosc = self.entry.get()
        if (index != ' '):
            self.lista[int(index)] = self.wartosc
            self.wypisz()
            self.change_i.set(index)
            self.canvas.create_text(95, 155, text='Zmieniono pozycję: '+index, fill='green')
        elif(index == ' '):
            self.wartosc = self.entry.get()
            self.lista[len(self.lista) -1] = self.wartosc
            self.wypisz()
            self.canvas.create_text(95, 155, text='Zmieniono pozycję: ' +str(len(self.lista)-1), fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 155, text='Lista jest pusta', fill='red')

    def usun(self):
        index = self.del_i.get()
        self.wartosc = self.entry.get()
        if len(self.lista) > 0 and index == ' ':
            self.canvas.delete('all')
            item = self.lista.pop()
            self.wypisz()
            self.canvas.create_text(80, 200, text='Usunięto: '+item, fill='green')
        elif len(self.lista) > 0:
            self.canvas.delete('all')
            self.lista.pop(int(index))
            self.wypisz()
            self.canvas.create_text(95, 200, text='Usunięto pozycję: ' + index, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 200, text='Lista jest pusta', fill='red')

    def clearInput(self,e):
        self.entry.delete(0, END)

    def pobierz(self):
        index = self.get_i.get()
        if index == ' ': index = len(self.lista) - 1
        if len(self.lista)>0:
            self.wypisz()
            self.get_i.set(index)
            self.canvas.create_text(80, 420, text='Pobrano: '+self.lista[int(index)], fill='green')

        else:
            self.wypisz()
            self.canvas.create_text(80, 420, text='Lista jest pusta', fill='red')

    def pobierz_usun(self):
        index = self.get_n_del_i.get()
        if index == ' ': index = len(self.lista) - 1
        if len(self.lista)>0:
            item = 'Pobrano i usunięto: '+self.lista.pop(int(index))
            self.wypisz()
            self.canvas.create_text(110, 420, text=item, fill='green')
        else:
            self.wypisz()
            self.canvas.create_text(80, 420, text='Lista jest pusta', fill='red')

    def wypisz(self):
        self.canvas.delete('all')
        opcje = [' ']
        j = 10
        for i in range(len(self.lista)):
            j = j-1
            x = 450
            y = (j * 50) + 60
            width = 550
            height =(j * 50) + 100
            self.canvas.create_rectangle(x, y, width, height, fill='lightgrey')
            self.canvas.create_text((x + width) / 2, (y + height) / 2, text=self.lista[i])
            opcje.append(int(i))

        self.add_i = StringVar(self.master)
        self.del_i = StringVar(self.master)
        self.change_i = StringVar(self.master)
        self.get_i = StringVar(self.master)
        self.get_n_del_i = StringVar(self.master)

        self.add_i.set(opcje[0])
        self.del_i.set(opcje[0])
        self.change_i.set(opcje[0])
        self.get_i.set(opcje[0])
        self.get_n_del_i.set(opcje[0])

        index_add = OptionMenu(self.master, self.add_i, *opcje)
        index_add.place(x=230, y=72)

        index_delete = OptionMenu(self.master, self.del_i, *opcje)
        index_delete.place(x=230, y=164)

        index_change = OptionMenu(self.master, self.change_i, *opcje)
        index_change.place(x=230, y=118)

        index_get = OptionMenu(self.master, self.get_i, *opcje)
        index_get.place(x=230, y=316)

        index_get_n_del = OptionMenu(self.master, self.get_n_del_i, *opcje)
        index_get_n_del.place(x=230, y=356)

        self.canvas.create_window(40, 50, window=self.entry, anchor=NW,width=235)
        self.entry.bind("<Button-1>",self.clearInput)

        dodaj = Button(self.master, text="Dodaj do listy na pozycji", command=self.add, anchor="center")
        dodaj.configure(width=25, activebackground="lightgrey")
        self.canvas.create_window(40, 75, anchor=NW, window=dodaj)

        zamien = Button(self.master, text="Zmien wartosc na pozycji", command=self.change, anchor="center")
        zamien.configure(width=25, activebackground="lightgrey")
        self.canvas.create_window(40, 120, anchor=NW, window=zamien)

        usun = Button(self.master, text="Usuń z listy na pozycji", command=self.usun, anchor='center')
        usun.configure(width=25,activebackground = 'lightgrey')
        self.canvas.create_window(40, 166, anchor=NW, window=usun)

        pobierz = Button(self.master, text='Pobierz z listy pozycję', command=self.pobierz, anchor='center')
        pobierz.configure(width=25, activebackground='lightgrey')
        self.canvas.create_window(40, 320, anchor=NW, window=pobierz)

        pobierz_usun = Button(self.master, text='Pobierz i usuń z listy pozycję', command=self.pobierz_usun, anchor='center')
        pobierz_usun.configure(width=25, activebackground='lightgrey')
        self.canvas.create_window(40, 360, anchor=NW, window=pobierz_usun)