# En este programa vamos a descargar todas las imagenes de articulos
# que se encuentren en la primera pestaña de Mercado Libre (ML)
# Por ejemplo:
# Si buscamos 'iphone 12' en ML obtenemos un link como el siguiente:
# https://listado.mercadolibre.com.mx/iphone-12_DisplayType_LF
# vamos a descargar la imagen asociada a cada articulo, y las
# almacenaremos en una carpeta 'imagenes'.

import requests
from bs4 import BeautifulSoup
import urllib.request as rqt
import shutil, os
import webbrowser


def status_URL(request):
    """
    Aqui vamos a obtener el status de la pagina,
    
    Parámetros
    -----------
    request: objeto Request.get(), en donde tenemos la solicitud que hicimos
    a la URL
    
    Regresa
    -----------
    bool
        True: si se obtiene un status de 200

        False: si se obtiene un status diferente de 200.
    """
    if request.status_code == 200:
        print("Acceso concedido.")
        return True
    else:
        print("Acceso denegado")
        return False

def descargar_imagenes(items):
    """
    Utilizamos esta función para descargar las imagenes que tengamos
    en nuestra 'soup' de ML.
    
    Parámetros
    ----------
    items: objeto BeautifulSoup.soup() en el que 
    tenemos el HTML en donde estan localizados los items
    que queremos descargar. 
    """
    
    print("Descargando imagenes...")
    for number, element in enumerate(items):
        print(f"Descargando imagen {number + 1}, de {len(items)}")
        url_imagen = element.find("img")["data-src"]
        file = opener.retrieve(url_imagen, f'imagen_{number}.jpg')
    print("Listo!")

def ruta_imagenes(ruta: str):
    """
    En esta función vamos a crear la carpeta 'imagenes'
    en la que vamos a guardar la imagen de cada articulo de ML.
        
    Parámetros
    ----------
    ruta: cadena de caracteres en la cual le vamos a indicar
    en que ruta tenemos nuestro archivo .py, ruta en la que
    se generara una carpeta con las imagenes.
    """
    
    os.chdir(ruta)
    if "imagenes" in os.listdir():
        shutil.rmtree("imagenes")
    os.mkdir("imagenes")
    os.chdir(ruta + '/imagenes')
    

# Le damos formato a la URL para que ML la reconozca.
objeto_buscador = str(input('Introduce el objeto del que quieres sus imagenes: '))
objeto_buscador = objeto_buscador.split(" ")
objeto_buscador = "-".join(objeto_buscador)

URL = f'https://listado.mercadolibre.com.mx/{objeto_buscador}_DisplayType_LF'
    
# Hacemos un Request a la URL.
request = requests.get(URL)

# Verificamos si tenemos un status de 200.
if status_URL(request):
    # Cargamos el HTML a nuestra un 'soup'.
    soup = BeautifulSoup(request.text, "html.parser")

    # Hacemos una lista que contenga info de cada publicacion.
    items = soup.select(".ui-search-layout__item")

    # Cargamos HEADERS, y creamos nuestro opnener para descargar las imagenes.
    opener = rqt.URLopener()
    opener.addheader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36")

    # Le damos la ruta en donde tengamos guardado este archivo.
    ruta = 'C:/Users/masan/ENGINEER/Mercado_Libre'
    ruta_imagenes(ruta)
    
    # Navegamos en cada pedazo del HTML, extrayendo la imagene pura.
    descargar_imagenes(items)
    
    # Nos auxiliamos de la libreria webbroserver para al final abrir
    # la carpeta en la que se guardan nuestras imagenes.
    webbrowser.open('C:/Users/masan/ENGINEER/Mercado_Libre/imagenes')
else:
    print("La URL no es valida.")