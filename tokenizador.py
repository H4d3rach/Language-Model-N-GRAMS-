import spacy
import json

corpus = []
nlp = spacy.load("es_core_news_sm")
with open("./ChatW.txt",mode='r',encoding='utf-8') as archivo:
    contenido = archivo.readlines()
    for c in contenido:
        tokens = nlp(c)
        chats_tokenized = {"chats": []}
        line = "<s> "
        with open("./ChatsNormalizado.txt", mode='a' , encoding='utf-8') as newarchivo:
            newarchivo.write("<s> ")
            for token in tokens:
                if token.text.strip():
                    newarchivo.write(str(token)+" ")
                    line = line + str(token) + " "
            line = line + "</s>"
            newarchivo.write("</s>\n")
            corpus.append(line)
    with open("./chats.json", mode="w", encoding="utf-8") as file:
        chats_tokenized["chats"] = corpus
        json.dump(chats_tokenized, file, indent=1)