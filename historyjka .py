from tkinter import *
from tkinter import filedialog
from funkcje import *
from graph_h2 import *
import numpy as np
from graph_h1 import *

calls = []
calls_counter = 0
functionsInFiles = {}
modulesRelations = {}
dane_graf_his2 = []
path = []

def open_file():
    global path
    path = filedialog.askopenfilenames(initialdir="F:\VS Python\PythonApplication1", title="wybierz plik")
    #print(path)
    for lines in path:
        file_path = lines
        result = open(file_path)
        file_postion1 = file_path.index(".py")
        file_postion2 = file_path.rindex("/")
        file_name = file_path[file_postion2+1 : file_postion1+3]
        for c in result:
            safe_tab = c.split()
            is_quotation = 0
            for i in safe_tab:
                if '"' in (i) and is_quotation == 0:
                    is_quotation = 1
                elif '"' in (i) and is_quotation == 1:
                    is_quotation = 0
                if is_quotation == 0:
                    if i == "import" or i == "import*":
                        global calls_counter
                        if "from" in c:
                            position1 = c.find(i)
                            position2 = c.find("from")
                            for file in path:
                                filePostion1 = file.index(".py")
                                filePostion2 = file.rindex("/")
                                fileName = file[filePostion2 + 1: filePostion1 + 3]
                                if fileName == c[position2 + len("from "):position1 - 1] + ".py":
                                    calls.append([file_name, c[position2 + len("from "):position1 - 1]])  # dodanie nazwy pliku to tablicy
                                    calls_counter = calls_counter + 1
                        else:
                            position1 = c.find(i)
                            position2 = len(c)
                            for file in path:
                                filePostion1 = file.index(".py")
                                filePostion2 = file.rindex("/")
                                fileName = file[filePostion2 + 1: filePostion1 + 3]
                                if fileName == c[position1 + len(i) + 1:position2 - 1] + ".py":
                                    calls.append(
                                        [file_name,
                                         c[position1 + len(i) + 1:position2 - 1]])  # dodanie nazwy pliku to tablicy
                                    calls_counter = calls_counter + 1
                    if i == "using" or i == "include" or i == "open" or "open(" in i:
                        # global calls_counter
                        position1 = c.find(i)
                        position2 = len(c)
                        for file in path:
                            filePostion1 = file.index(".py")
                            filePostion2 = file.rindex("/")
                            fileName = file[filePostion2 + 1: filePostion1 + 3]
                            if fileName == c[position1 + len(i) + 1:position2 - 1] + ".py":
                                calls.append([file_name, c[position1 + len(i) + 1:position2 - 1]])  # dodanie nazwy pliku to tablicy
                                calls_counter = calls_counter + 1
                    if "#" in (i):
                        break
        #for i in range(0, calls_counter):
        #    print("wywolanie numer ", i + 1, "zawiera: ", calls[i])      # dałem w komentarz bo troche zbugowane
        #    pass

def convert(calls):         #zamiana listy w tuple
    return tuple(calls)
def dep():              #wypisanie danych pod graf
    #print(convert(calls))
    rysuj_graf(convert(calls))
def Graph():
    data_to_graph=convert(calls)
def func():
    global path
    files = path
    for file in files:
        functionsInFiles[file] = findFunctions(file)
    return files
def data_container():
    function_list=list(functionsInFiles.values())
    function_list=np.concatenate(function_list)
    #container=[]      #bedzie w formacie [funkcja, ile razy wystepuje]
    #for x in wystapienia
        #container.append(function_list[x],zmienna_odpowiadajaca_liczbie_wystapien[x])
    print("W plikach wystepuja takie funkcje: : \n {}".format(function_list))
    print("Funkcja ({}) wystepuje ({}) ".format('tu bedzie nazwa funkcji','tu bedzie ile razu wystepuje funkcja'))
def wage_graph_h():
    #listatupli do testu
    global dane_graf_his2
    slownik= {}
    for wyrazy in dane_graf_his2:
        slownik[wyrazy] = slownik.get(wyrazy, 0) + 1

    listafunkcji=[]
    listawag=[]
    for x in slownik.keys():
        listafunkcji.append(x)
    for x in slownik.values():
        listawag.append(x)

    listafunkcjiwtuple=tuple(listafunkcji)
    wage_graph(listafunkcji, listawag)
def modules_relations():
    global modulesRelations
    files = func()
    modulesRelations = findFunctionCalls(functionsInFiles, files)

    slownik= {}
    for wyrazy in modulesRelations:
        slownik[wyrazy] = slownik.get(wyrazy, 0) + 1

    listafunkcji=[]
    listawag=[]
    for x in slownik.keys():
        listafunkcji.append(x)
    for x in slownik.values():
        listawag.append(x)

    listafunkcjiwtuple=tuple(listafunkcji)
    graph3(listafunkcji, listawag) #Tu wołamy graph 3 jak już będzie
    
    #print(modulesRelations)
def dane_graph_2():
    global dane_graf_his2
    dane = []
    pliki = func()
    function_list = list(functionsInFiles.values())
    function_list = np.concatenate(function_list)
    for plik in pliki:
        tresc_pliku = open(plik)
        aktualna_funkcja = ""
        for linia in tresc_pliku:
            if linia.find("def") == 0:
                aktualna_funkcja = linia.replace("def ", "")
                aktualna_funkcja = aktualna_funkcja[:aktualna_funkcja.find("(")]
                continue
            for funkcja in function_list:
                pozycja = linia.find(funkcja + "(")
                if pozycja != -1 and (linia[pozycja-1] == "(" or linia[pozycja-1] == " "):
                    dane.append((aktualna_funkcja, funkcja))
    dane_graf_his2 = dane
def exit() :
    sys.exit()
root = Tk()
button = Button(root, text="wczytaj plik", command=open_file)
button1= Button(root, text="koniec", command=exit)
button2= Button(root,text="pokaz zaleznosci",command=dep)
#button3= Button(root,text="szukaj funkcji",command=func)
button4= Button(root,text="Rysuj graph 3",command=data_container)
button5= Button(root,text="Graf his_2",command=wage_graph_h)
button6= Button(root,text="Relacje między modułami",command=modules_relations)
button7= Button(root,text="Dane do grafu his2",command=dane_graph_2)
button.pack()
button1.pack()
button2.pack()
#button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
root.mainloop()
