from tkinter import *
from tkinter import filedialog
from funkcje import findFunctions
from graph_h2 import wage_graph
calls = []
calls_counter = 0
functionsInFiles = {}
def open_file():
    path = filedialog.askopenfilenames(initialdir="/", title="wybierz plik")
    print(path)
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
def exit() :
    sys.exit()
def convert(calls):         #zamiana listy w tuple
    return tuple(calls)
def dep():              #wypisanie danych pod graf
    print(convert(calls))
def Graph():
    data_to_graph=convert(calls)
def func():
    files = filedialog.askopenfilenames(initialdir="/", title="wybierz plik")
    for file in files:
        functionsInFiles[file] = findFunctions(file)
def data_to_graph():
    function_list=list(functionsInFiles.values())
    function_list=np.concatenate(function_list)
    print("W plikach wystepuja takie funkcje: : \n {}".format(function_list))
    print("Funkcja ({}) wystepuje ({}) razy w funkcji ({})".format('tu bedzie nazwa funkcji','tu bedzie ile razu wystepuje funkcja','tu bedzie w jakiej funkcji wystepuje funkcja'))

root = Tk()
button = Button(root, text="wczytaj plik", command=open_file)
button1= Button(root, text="koniec", command=exit)
button2= Button(root,text="pokaz zaleznosci",command=dep)
button3= Button(root,text="szukaj funkcji",command=func)
button4=Button(root,text="Dane do grafu",command=data_to_graph)
button5= Button(root,text="Graf his_2",command=wage_graph)

button.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
root.mainloop()
