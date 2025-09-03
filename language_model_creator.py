from sklearn.feature_extraction.text import CountVectorizer
import csv
#Primer parte para obtener el vocabulario y su frecuencia
corpus = []
with open("ChatsNormalizado.txt", mode='r', encoding='utf-8') as archivo:
    contenido = archivo.readlines()
    for c in contenido:
        corpus.append(c)
vectorizador = CountVectorizer(token_pattern= r'<s>|</s>|https?://\S+|[\.¿?\!\(\)]|\$?\d+(?:\.\d+)?|\w+|[\U0001F000-\U0001FFFF]',ngram_range = (1,1))
X = vectorizador.fit_transform(corpus)
X_ARRAY = X.toarray()
print(X_ARRAY[0][0])
vocab = vectorizador.get_feature_names_out()
print(vocab)
vocabulario = []
for i in range(vocab.size):
    elemento = vocab[i]
    suma = 0
    for item in X_ARRAY:
        suma += item[i]
    vocabulario.append((elemento,suma))
vocabulario.sort(key=lambda x: x[1], reverse=True)        
with open('Vocabulario.csv', mode='w', newline='', encoding='utf-8') as archivocsv:
    escritor = csv.writer(archivocsv, delimiter=',')
    for item1, item2 in vocabulario:
        escritor.writerow([item1, item2])
#Obtención de bigramas
corpus = []
with open("ChatsNormalizado.txt", mode='r', encoding='utf-8') as archivo:
    contenido = archivo.readlines()
    for c in contenido:
        corpus.append(c)
vectorizador = CountVectorizer(token_pattern= r'<s>|</s>|https?://\S+|[\.¿?\!\(\)]|\$?\d+(?:\.\d+)?|\w+|[\U0001F000-\U0001FFFF]',ngram_range = (2,2))
X = vectorizador.fit_transform(corpus)
X_ARRAY = X.toarray()
print(X)
vocab = vectorizador.get_feature_names_out()
vocabulario = []
diccionario = {}
with open("Vocabulario.csv", mode='r', encoding='utf-8') as vocabulario_unigrama:
    lector = csv.reader(vocabulario_unigrama)
    for termino, valor in lector:
        diccionario[termino]=int(valor)
for i in range(vocab.size):
    elemento = vocab[i]
    suma = 0
    for item in X_ARRAY:
        suma += item[i]
    div = elemento.split()
    if div[0] in diccionario:
        frecuencia_contexto = diccionario[div[0]]
    else:
        frecuencia_contexto = 1
    probabilidad_condicional = suma/frecuencia_contexto
    vocabulario.append((div[0],div[1],suma,frecuencia_contexto,probabilidad_condicional))
vocabulario.sort(key=lambda x: x[2], reverse=True)        
with open('FrecuenciaBigramas.csv', mode='w', newline='', encoding='utf-8') as archivocsv:
    escritor = csv.writer(archivocsv, delimiter=',')
    for item1, item2, item3, item4, item5 in vocabulario:
        escritor.writerow([item1, item2, item3, item4, item5])
#Obtención de trigramas
corpus = []
with open("ChatsNormalizado.txt", mode='r', encoding='utf-8') as archivo:
    contenido = archivo.readlines()
    for c in contenido:
        corpus.append(c)
vectorizador = CountVectorizer(token_pattern= r'<s>|</s>|https?://\S+|[\.¿?\!\(\)]|\$?\d+(?:\.\d+)?|\w+|[\U0001F000-\U0001FFFF]',ngram_range = (3,3))
X = vectorizador.fit_transform(corpus)
X_ARRAY = X.toarray()
print(X)
vocab = vectorizador.get_feature_names_out()
vocabulario = []
diccionario = {}
with open("FrecuenciaBigramas.csv", mode='r', encoding='utf-8') as vocabulario_bigrama:
    lector = csv.reader(vocabulario_bigrama)
    for termino1,termino2,frecuencia,contexto,probabilidad in lector:
        diccionario[termino1+" "+termino2]=int(frecuencia)
for i in range(vocab.size):
    elemento = vocab[i]
    suma = 0
    for item in X_ARRAY:
        suma += item[i]
    div = elemento.split()
    elemento_encontrar = div[0]+" "+div[1]
    if elemento_encontrar in diccionario:
        frecuencia_contexto = diccionario[elemento_encontrar]
    else:
        frecuencia_contexto = 1
    probabilidad_condicional = suma/frecuencia_contexto
    vocabulario.append((div[0],div[1],div[2],suma,frecuencia_contexto,probabilidad_condicional))
vocabulario.sort(key=lambda x: x[3], reverse=True)        
with open('FrecuenciaTrigramas.csv', mode='w', newline='', encoding='utf-8') as archivocsv:
    escritor = csv.writer(archivocsv, delimiter=',')
    for item1, item2, item3, item4, item5, item6 in vocabulario:
        escritor.writerow([item1, item2, item3, item4, item5, item6])