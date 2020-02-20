import logging
from api import PixabayAPI
import threading

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'computadoras'
api = PixabayAPI('15336424-3010f778fbb10add8cf653c86', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 5)


#no se usar el main
for u in urls:
  
  logging.info(f'Descargando {u}')
  #api.descargar_imagen(u)
  threading.Thread(target=api.descargar_imagen, args=[u]).start()
  #target= lo que ejecuta
  #args= parametro con una lista de una sola u ->(url)
