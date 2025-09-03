import csv
import os
import spacy
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Treeview
modelos = {}
def seleccionar_modelo():
    contenido = {}
    archivo = filedialog.askopenfilename(title="Seleccionar Modelo")
    if archivo:
        with open(archivo, mode='r', encoding='utf-8') as file:
            lector = csv.reader(file)
            primer_fila = next(lector)
            determinante = len(primer_fila)
            if determinante == 5:
                for termino1,termino2,frecuencia,contexto,probabilidad in lector:
                    contenido[termino1+" "+termino2]=probabilidad
            else:
                for termino1,termino2,termino3,frecuencia,contexto,probabilidad in lector:
                    contenido[termino1+" "+termino2+" "+termino3]=probabilidad
        nombre_archivo = os.path.basename(archivo)
        nombre = os.path.splitext(nombre_archivo)[0]
        lbl2.config(text=nombre)
        tv.insert("",END,text=nombre)
        modelos[nombre] = contenido


def tokenizar(frase):
    nlp = spacy.load("es_core_news_sm")
    nueva_frase = None
    tokens = nlp(frase)
    for token in tokens:
        if token.text.strip():
            if nueva_frase == None:
                nueva_frase = str(token)
            else:
                nueva_frase = nueva_frase + " " + str(token)
    return nueva_frase

def probabilidad_condicional():
    probabilidad = []
    if tv2.get_children():
        for hijo in tv2.get_children():
            tv2.delete(hijo)
    frase = textarea1.get("1.0", "end-1c")
    nueva_frase = tokenizar(frase)
    print(nueva_frase)
    for nombre, contenido in modelos.items():
        divisor = next(iter(contenido)).split()
        determinante = len(divisor)
        tokens = nueva_frase.split()
        probabilidad_n_grama = 1
        for i in range(len(tokens)-determinante+1):
            if determinante == 2:
                n_grama = tokens[i] + " " + tokens[i+1]
            else:
                n_grama = tokens[i] + " " + tokens[i+1] + " " + tokens[i+2]
            n_grama_modelo = modelos[nombre].get(n_grama)
            print(n_grama_modelo)
            if n_grama_modelo is not None:
                probabilidad_n_grama = probabilidad_n_grama * float(n_grama_modelo)
            else:
                probabilidad_n_grama = probabilidad_n_grama * 0.0001
        print("N-grama: {} Del modelo: {} probabilidad: {}".format(n_grama,nombre,probabilidad_n_grama))  
        probabilidad.append((nombre,probabilidad_n_grama))
    probabilidad.sort(key=lambda x: x[1], reverse=True)
    for item in probabilidad:
        tv2.insert("",END,text=item[0], values=(item[1]))
if __name__ == '__main__':
    raiz = Tk()
    raiz.title("Conditional Probability")
    raiz.geometry("750x650")

    lbl1 = Label(raiz, text="Load Language Model", font=("Courier New", 14), bg="yellow")
    lbl1.place(x=10, y=10, width=350, height=20)
    selector_modelo = Button(raiz, text="Select Model", command=seleccionar_modelo)
    selector_modelo.place(x=20, y=40)
    lbl2 = Label(raiz, text="", font=("Courier New", 12), bg="white")
    lbl2.place(x=200, y=40, width=300, height=25)

    tv = Treeview(raiz)
    tv.column("#0", width=250)
    tv.heading("#0", text="Model", anchor=CENTER)
    tv.place(x=20, y=95, height=150)

    lbl3 = Label(raiz, text="Test sentence", font=("Courier New", 14), bg="yellow")
    lbl3.place(x=10, y=255, width=350, height=20)
    textarea1 = Text(raiz, font=("Courier New",12), bg="white", borderwidth=2, relief="solid", border=1)
    textarea1.place(x=20, y=285, width=450, height=25)
    join = Button(raiz, text="Determinate Join Probability", command=probabilidad_condicional)
    join.place(x=480, y=283, width=150, height=30)

    lbl4 = Label(raiz, text="Results", font=("Courier New", 14), bg="yellow")
    lbl4.place(x=10, y=335, width=350, height=20)
    tv2 = Treeview(raiz, columns="col1")
    tv2.column("#0",width=250, anchor=CENTER)
    tv2.column("col1", width=250, anchor=CENTER)
    tv2.heading("#0", text="Language Model", anchor=CENTER)
    tv2.heading("col1", text="Joinyt Probability", anchor=CENTER)
    tv2.place(x=20, y=375, height=200)
    raiz.mainloop()