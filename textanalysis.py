import requests, re, csv
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt


#DESCARGAR INFORMACION DE LA WEB
###############################################################
###############################################################
###############################################################
#WEB A ANALIZAR
link = 'https://www.skyscrapercity.com/categories/proyectos.1008/'
res = requests.get(link)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
set([t.parent.name for t in text])


###############################################################
###############################################################
###############################################################

#LIMPIEZA DEL TEXTO
texto = ''
blacklist = [
    '[document]','noscript', 'header', 'html','meta','head', 'input','script',
]
for t in text:
    if t.parent.name not in blacklist:
        texto += '{} '.format(t)
#BANEO DE PALABAS PARA LIMPIAR LOS RESULTADOS

#dic = [ 'Registrarse','inicio','Visitas','div', 'class', 'Visitas', 'Respuestas', 'Buscar', 'mensajes', 'Hoy', 'Ayer', 'Foros',"Siguiente","Hace","Economia","Última","Hora",]
b = {'Respuestas': '', 'Inicio': '', 'Visitas': '', 'Hoy': '', 'Ayer': '', 'Última': '','Temas': '','Mensaje': '','sesión': '','mensajes': '','siguiente': '','Hora': '','Foros': '',
'página': '','AM': '','PM': '','Visitas': '','Visitas': '','Foros': '','Economía': '','Buscar': '', 'Siguiente': '','Bolsa': '', 'Hace': '','minutos': '','Último': '','Hace': '',
'Buscar': '','Adherido': '','Nuevos': '','Adherido': '','JavaScript': '','Trending': '','Foros': '','Menú': '','Miembros': '','Registrarse': '','foros': '','Foro': '','Navegador': '',
'Xenforo': '','2022': '','Burbuja.info': '','by': '','Iniciar': '','navegador': '','foro': '','momento': '','hace': '',':': '','Lunes': '','Martes': '','Miércoles': '','Jueves': '',
'Viernes': '','Sábado': '','Domingo': '','solo': '','Hilo': '','ahora': '','-': '','ahora': '','sólo': '','para': '','como': '','|': '','%': '','.': '','members': '','Join': '',
'forums': '','forum': '','Home': '','Forums': '','Forum': '','with': '','Search': '','Replies': '','this': '','browser': '','LatinAmerican': '','Provincias': '','Advanced': '','&': '',
'American': '','Caribbean': '','Área': '','moment': '','Business': '','Moderator': '','Latin': '','Community': '','SkyscraperCity': '','Grow': '','Your': '','View': '','Threads': '',}
for x,y in b.items():
    texto = texto.replace(x, y)

#QUITAR LOS NUMEROS

texto2 = ''.join([i for i in texto if not i.isdigit()])
texto = texto2

#QUITAR MONOSILABOS
shortword = re.compile(r'\W*\b\w{1,3}\b')
texto = shortword.sub('', texto)

######

limpieza = texto

#DETECTAR PALABRAS MAS REPETIDAS

split_it = limpieza.split()
Counter = Counter(split_it)
most_occur = Counter.most_common(20)
print("######")
diccionariodepalabras = dict(most_occur)
print(diccionariodepalabras)


###############################################################
###############################################################
###############################################################

#ALMACENAR EN UN ARCHIVO

import csv
new_path = open("data.csv", "w")
z = csv.writer(new_path)
for new_k, new_v in diccionariodepalabras.items():
    z.writerow([new_k, new_v])

new_path.close()

#GRAFICO
###############################################################
###############################################################
###############################################################

keys = diccionariodepalabras.keys()
values = diccionariodepalabras.values()
plt.bar(keys, values)
plt.show()
