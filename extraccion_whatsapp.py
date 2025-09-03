import re
import os

patron = re.compile(r'user_or_cellphone: (.*)') #You can change the user or cellphone what you want to extract
for firstdoc in os.listdir("./chats"):
    if firstdoc.endswith(".txt"):
        ruta = os.path.join("./chats",firstdoc)
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()
            for c in contenido:
                mensaje = patron.search(c)
                if mensaje:
                    contenido = mensaje.group(1)
                    if contenido != "<Multimedia omitido>":
                        with open("ChatW.txt", 'a', encoding='utf-8') as archivo:
                            archivo.write(contenido)
                            archivo.write("\n")
