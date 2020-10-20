from tkinter import *
from stack import *
from queue import *
from deque import *
from list import *

class program:
    def __init__(self):
        self.master = Tk()
        self.menubar = Menu(self.master)
        self.menubar.add_command(label="Stos", command=self.callStack)
        self.menubar.add_command(label="Kolejka", command=self.callQueue)
        self.menubar.add_command(label="Kolejka dwustronna", command=self.callDeque)
        self.menubar.add_command(label="Lista", command=self.callList)
        self.master.config(menu=self.menubar)
        self.canvas = Canvas(self.master, width='650', height='600')
        self.canvas.pack()

    def start(self):
        self.canvas.create_text(650/2,200,text='Wybierz strukturę danych: ',anchor="center")
        stos = Button(self.master, text="Stos", command=self.callStack, anchor="center")
        stos.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(650/2, 250, anchor="center", window=stos)
        kolejka = Button(self.master, text="Kolejka", command=self.callQueue, anchor="center")
        kolejka.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(650/2, 300, anchor="center", window=kolejka)
        kolejka_ds = Button(self.master, text="Kolejka dwustronna", command=self.callDeque, anchor="center")
        kolejka_ds.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(650 / 2, 350, anchor="center", window=kolejka_ds)
        lista = Button(self.master, text="Lista", command=self.callList, anchor="center")
        lista.configure(width=15, activebackground="lightgrey")
        self.canvas.create_window(650 / 2, 400, anchor="center", window=lista)

    def callStack(self):
        start = interpretationOfStack(master=self.master,canvas=self.canvas)
        start.wypisz()

    def callQueue(self):
        start = interpretationOfQueue(master=self.master,canvas=self.canvas)
        start.wypisz()

    def callDeque(self):
        start = interpretationOfDeque(master=self.master, canvas=self.canvas)
        start.wypisz()

    def callList(self):
        start = interpretationOfList(master=self.master, canvas=self.canvas)
        start.wypisz()


zaliczenie = program()
zaliczenie.start()

mainloop()