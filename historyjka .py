from tkinter import *
from tkinter import filedialog
def open_file():
   result =  filedialog.askopenfile(initialdir="/", title="wybierz plik", filetypes=(("text files", ".txt"), ("all files", "*.*")))
   print(result)
   for c in result:
       print(c)
def exit():
    sys.exit()
root = Tk()
Button = Button(root, text="wczytaj plik", command=open_file)
Button1= Button(root, text="koniec", command=exit)
Button.pack()
Button1.pack()
root.mainloop()
