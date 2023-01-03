import pandas as pd
import matplotlib as plt

import os
import re

import crear_carpetas
import nube_palabras
import emojis

# Buscar y cargar ruta del archivo
ruta_bases = './bases'
archivo = os.listdir(ruta_bases)[0]
ruta_archivo = ruta_bases + '/' + archivo

# Crea las carpetas si no existen
crear_carpetas

# Cargar base en dataframe
df = pd.read_csv(ruta_archivo, encoding='utf8')

# Cargamos los conectores
conectores = pd.read_csv('conectores.csv')

# Crea el string para usar en la nube de palabras
palabras = ""

# Crear y guardar la nube de palabras
for texto in df['text']:
    # texto = re.sub("[^\x30-\x7f]", "", texto)
    lista_palabras = texto.split(' ')

    for palabra in lista_palabras:
        conector = conectores.isin([palabra]).any().any()

        if not conector:
            # palabra = emojis.deEmojify(palabra)
            palabras += palabra
    
imagen = nube_palabras.nube(palabras)
imagen.save('./resultados/determinantes_semanticos/nube/nube_palabras.png')

