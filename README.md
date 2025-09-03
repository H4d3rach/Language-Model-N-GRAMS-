# Language-Model-N-GRAMS-
This project implements a language modeling system based on N-grams (unigrams, bigrams, trigrams) trained on WhatsApp chat data.  It allows you to preprocess conversations, build statistical models, generate text, and evaluate probabilities using graphical interfaces.

---

## Features

- **Chat Preprocessing**
  - Extract messages from WhatsApp `.txt` exports.
  - Tokenization and normalization using spaCy.
  - Adds sentence delimiters `<s>` and `</s>` for training.

- **N-gram Model Building**
  - Generates vocabulary frequencies (unigrams).
  - Builds **bigram** and **trigram** frequency/probability tables.
  - Exports results to CSV files:
    - `Vocabulario.csv`
    - `FrecuenciaBigramas.csv`
    - `FrecuenciaTrigramas.csv`

- **Predictive Text GUI**
  - Suggests the **3 most probable next words** given an input word or phrase.
  - Allows interactive sentence construction.

- **Text Generation GUI**
  - Automatically generates random sentences based on bigram or trigram models.
  - Starts with `<s>` and ends with `</s>`.

- **Conditional Probability Evaluator**
  - Load multiple models (bigram/trigram).
  - Enter a test sentence and compare its **joint probability** across models.

---

## Project Structure

- **Preprocessing**
  - Extract and clean WhatsApp chats → `ChatW.txt`
  - Normalize and tokenize → `ChatsNormalizado.txt`

- **Model Construction**
  - `Vocabulario.csv` → unigram frequencies
  - `FrecuenciaBigramas.csv` → bigram probabilities
  - `FrecuenciaTrigramas.csv` → trigram probabilities

- **Applications (Tkinter GUIs)**
  - **Predictive Text** → word suggestions
  - **Text Generator** → automatic sentence generation
  - **Probability Evaluator** → compare models

---

## Requirements

- Python 3.8+
- spacy
- scikit-learn
- tkinter
  ```bash
  python -m spacy download es_core_news_sm


---

## How to use it

- **Chat extraction**
  - First of all you need to export all the chats you want from Whatsapp `txt format`. Make sure you store them in the `chats` directory
  - Once you have all chats you want run  `extraccion_whatsapp.py` #You need to change the line 4 with the user or cellphone you want to extract chats
  ```bash
  python extraccion_whatsapp.py

- **Normalization**
  - Next step is normalize extracted chats, adding the special tokens <s> </s> at the begining and the end of each sentence from the chat. 
  ```bash
  python tokenizador.py

- **Normalization**
  - Last configuration step is to create the language model you want, the funny fact here is that all model you create will have the way to write from person you extracted the chat.
  - Need to run `language_model_creator.py` #If you want to create only bigrams or trigrams or only vocab, do not hesitate to modify or comment parts of the code you do not need.
  ```bash
  python language_model_creator.py

## Play with it
Once you have made the steps above, play with the GUI, in all of them you need to load the models you generated
- `predictive.py` Is developed to find the 3 most probable words in appear after you write one or two (Bigram or trigram)
- `generation.py` Is developed to generate random sentences
- `conditional_probability.py` Is developed to determine which model is most likely to belong to a sentence given
