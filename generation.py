import csv
import random as rd

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import os

CSVS = ["FrecuenciaBigramas.csv", "FrecuenciaTrigramas.csv"]
BIGRAMS = 0
TRIGRAMS = 1

language_model = []
trigram_or_bigram = None

def get_CSV():
    archivo = filedialog.askopenfilename(title="Seleccionar Modelo")
    nombre_archivo = os.path.basename(archivo)
    lbl2.config(text=nombre_archivo) 
    with open(archivo, encoding="utf-8") as file:
        reader = csv.reader(file)
        lista = []
        for element in reader:
            lista.append(element)
        global trigram_or_bigram
        if len(lista[0]) == 5:
            trigram_or_bigram = BIGRAMS
        else:
            trigram_or_bigram = TRIGRAMS
        global language_model
        language_model = lista
        

def bigram_generation():
    actual = "<s>"
    string = "<s>"
    while not actual == "</s>":
        matches = [sublista for sublista in language_model if sublista[0] == actual]
        prob_acum = [] 
        p = 0
        for match in matches:
            p = p + float(match[4])
            prob_acum.append(p)
        prob_acum[len(prob_acum)-1] = 1.00
        rand = rd.random()
        index = None
        for i in range(0, len(prob_acum)):
            if rand < prob_acum[i]:
                index = i
                break
        string = string + " " + matches[index][1]
        actual = matches[index][1]
    return string

def trigram_init() -> str:
    matches = [sublista for sublista in language_model if sublista[0] == "<s>"]
    prob_acum = [] 
    p = 0
    for match in matches:
        p = p + float(match[5])
        prob_acum.append(p)
    prob_acum[len(prob_acum)-1] = 1.00
    rand = rd.random()
    index = None
    for i in range(0, len(prob_acum)):
        if rand < prob_acum[i]:
            index = i
            break
    string = matches[index][0] + " " + matches[index][1] + " " + matches[index][2]
    return string

def trigram_generation():
    string = trigram_init()
    actual = string.split()
    while not actual[2] == "</s>":
        matches = [sublista for sublista in language_model if sublista[0] == actual[1] and sublista[1] == actual[2]]
        prob_acum = [] 
        p = 0
        for match in matches:
            p = p + float(match[5])
            prob_acum.append(p)
        prob_acum[len(prob_acum)-1] = 1.00
        rand = rd.random()
        index = None
        for i in range(0, len(prob_acum)):
            if rand < prob_acum[i]:
                index = i
                break
        string = string + " " + matches[index][2]
        actual = [matches[index][0], matches[index][1], matches[index][2]]
    return string

# Codigo para la GUI

def generar_texto():
    if trigram_or_bigram == BIGRAMS:
        string = bigram_generation()
    else:
        string = trigram_generation()
    lbl5.config(text=string, wraplength=500)    

if __name__ == '__main__':
    raiz = Tk()
    raiz.title("Generador de texto")
    raiz.geometry("750x650")

    lbl1 = Label(raiz, text="Load language model", font=("Courier New", 14), bg="yellow")
    lbl1.place(x=10, y=10, width=350, height=20)
    selector_modelo = Button(raiz, text="Select corpus file", command=get_CSV)
    selector_modelo.place(x=20, y=40)
    lbl2 = Label(raiz, text="", font=("Courier New", 12), bg="white")
    lbl2.place(x=200, y=40, width=300, height=25)
    
    gen_text = Button(raiz, text="Generate Sentence", command=generar_texto)
    gen_text.place(x=20, y=100, width=120, height=30)

    lbl4 = Label(raiz, text="Generated Text", font=("Courier New", 14), bg="yellow")
    lbl4.place(x=10, y=235, width=250, height=20)
    lbl5 = Label(raiz, text="", font=("Courier New", 14), bg="white")
    lbl5.place(x=20,y=275, width=650, height=300)
    raiz.mainloop()