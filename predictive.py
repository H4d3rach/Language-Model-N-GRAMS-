import csv
import os
import random
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
modelo = []
palabra = None
def seleccionar_modelo():
    archivo = filedialog.askopenfilename(title="Seleccionar Modelo")
    if archivo:
        with open(archivo, 'r', encoding="utf-8") as file:
            global modelo
            modelo = []
            lectura = csv.reader(file)
            primer_fila = next(lectura)
            determinante = len(primer_fila)
            if determinante == 5:
                for termino1,termino2,frecuencia,contexto,probabilidad in lectura:
                    modelo.append([termino1,termino2,probabilidad])
            else:
                for termino1,termino2,termino3,frecuencia,contexto,probabilidad in lectura:
                    modelo.append([termino1+" "+termino2,termino3,probabilidad])
            nombre_archivo = os.path.basename(archivo)
            lbl2.config(text=nombre_archivo)
def seleccionar_palabra():
    terminos_probables = []
    probables = []
    combo.set("3 most probable words")
    opc = textarea1.get("1.0", "end-1c")
    if opc == '.':
        raiz.quit()
    for elemento in modelo:
        if elemento[0] == opc:
            terminos_probables.append((elemento[1],elemento[2]))
    terminos_probables.sort(key=lambda x: x[1], reverse=True)
    print("Términos probables: ")
    for i in range (len(terminos_probables)):
        
        print(terminos_probables[i][0]+ " "+terminos_probables[i][1])
        probables.append(terminos_probables[i][0])
        if i==2:
            break
    combo.config(values = probables)
def añadir_palabra():
    texto_lbl = lbl5.cget('text')
    texto_ta =  textarea1.get("1.0", "end-1c")
    division = texto_ta.split()
    if len(division) != 1:
        if texto_lbl == "":
            texto = division[0] + " " + division[1]
        else:
            texto = texto_lbl+" "+division[1]
        word = division[1] + " "+combo.get()
    else:
        word = combo.get()
        texto = texto_lbl +" "+ texto_ta
    lbl5.config(text=texto)
    textarea1.delete("1.0", tk.END)
    textarea1.insert("1.0", word)
if __name__ == '__main__':
    raiz = Tk()
    raiz.title("Texto predictivo")
    raiz.geometry("750x650")

    lbl1 = Label(raiz, text="Load language model", font=("Courier New", 14), bg="yellow")
    lbl1.place(x=10, y=10, width=350, height=20)
    selector_modelo = Button(raiz, text="Select Model", command=seleccionar_modelo)
    selector_modelo.place(x=20, y=40)
    lbl2 = Label(raiz, text="", font=("Courier New", 12), bg="white")
    lbl2.place(x=200, y=40, width=300, height=25)

    lbl3 = Label(raiz, text="Write a word (or two words to start a sentence)", font=("Courier New", 14), bg="yellow")
    lbl3.place(x=10, y=105, width=550, height=20)
    textarea1 = Text(raiz, font=("Courier New",12), bg="white", borderwidth=2, relief="solid", border=1)
    textarea1.place(x=20, y=135, width=200, height=25)
    next_word = Button(raiz, text="Next Word", command=seleccionar_palabra)
    next_word.place(x=300, y=130, width=80, height=30)
    combo = Combobox(raiz, textvariable=palabra, font=("Courier New",12))
    combo.place(x=450, y=130, width=250, height=30)
    combo.set("3 most probable words")

    add_word = Button(raiz, text="Add Word", command=añadir_palabra)
    add_word.place(x=515, y=175, width=80, height=30)

    lbl4 = Label(raiz, text="Generated Text", font=("Courier New", 14), bg="yellow")
    lbl4.place(x=10, y=235, width=250, height=20)
    lbl5 = Label(raiz, text="", font=("Courier New", 14), bg="white")
    lbl5.place(x=20,y=275, width=650, height=300)
    raiz.mainloop()