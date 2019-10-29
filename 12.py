from tkinter import*


def koniec() :
    sys.exit()

okno = Tk ()
etykieta= Label(okno, text= "Witaj  w panelu sterowania",fg="darkgreen")
etykieta.pack()
gornaramka=Frame(okno)
gornaramka.pack()

dolramka=Frame(okno)
dolramka.pack(side=BOTTOM)

przycisk1= Button(gornaramka,text="wprowadz dane ",fg="green")
przycisk2=Button(gornaramka,text="koniec",fg="blue", command= koniec)


przycisk1.pack(side=LEFT)
przycisk2.pack(side=RIGHT)

okno.mainloop()