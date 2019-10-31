from tkinter import *
from tkinter import filedialog
def wczytaj_plik():
   result =  filedialog.askopenfile(initialdir="/", title="wybierz plik", filetypes=(("text files", ".txt"), ("all files", "*.*")))
   print(result)
   for c in result:
       print(c)
def koniec() :
    sys.exit()
root = Tk()
przycisk = Button(root, text="wczytaj plik", command=wczytaj_plik)
przycisk1= Button(root, text="koniec", command=koniec)
przycisk.pack()
przycisk1.pack()
root.mainloop()
