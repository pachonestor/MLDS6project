from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import pandas as pd
import numpy as np
import re
from unidecode import unidecode
import spacy
import nltk
from nltk.stem.snowball import SnowballStemmer
snow_stemmer = SnowballStemmer('english')
from sklearn.feature_extraction.text import TfidfVectorizer
nlp = spacy.load("en_core_web_sm")
import joblib
import json
from tensorflow.keras import applications, models

# Preprocessing function
def preprocess(text,min_len=2, max_len=23):
    pat = re.compile(r"[^a-z ]")
    spaces = re.compile(r"\s{2,}")

    # Normalizamos el texto
    norm_text = unidecode(text)
    doc = nlp(norm_text)

    # Eliminamos stopwords
    filtered_tokens = filter(lambda token: not token.is_stop, doc )

    # Filtramos palabras por longitud
    filtered_tokens2 = filter(lambda token: len(token) >= min_len
                              and len(token) <= max_len, filtered_tokens)

    # Obtenemos los lemmas de cada token
    lemmas = map(lambda token: token.lemma_, filtered_tokens2 )
    stem = map( lambda token: snow_stemmer.stem(token), lemmas )
    lemma_text = " ".join(stem)

    # Quitamos grafía
    lower_text = lemma_text.lower()

    # Eliminamos caracteres especiales
    clean_text = re.sub(pat, "", lower_text)

    # Eliminamos espacios duplicados
    spaces_text = re.sub(spaces, " ", clean_text)
    return spaces_text.strip()



nn=models.load_model('best_weights.h5', compile=False)
emb = joblib.load("vect.joblib")


# Init App
app = FastAPI()

#Alive function
@app.get("/")
def alive():
    return ('Alive')

# Probabilities
@app.post("/proba") # creamos api que permita requests de tipo post.
async def proba(file: UploadFile= File(...)):
    contents = await file.read()
    #f=open(contents)
    features = json.loads(contents)
    plot = features['texts']

    clean_text=preprocess(plot)
    vect=emb.transform([clean_text]).toarray()
    resul=nn(vect).numpy()[0]
    salida=dict(zip(['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History',
       'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Short',
       'Sport', 'Thriller', 'War', 'Western'],resul.tolist()))
    return salida

#uvicorn deploymentAPIs:app --reload