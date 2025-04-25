#Navegadores
import re
from collections import Counter
regex = r"(Chrome|Firefox|Edg|Edge|OPR|Opera|MSIE|Trident|Safari)"

def extract(regex,data):
    if data:
        return re.findall(regex,data)
    return None
ruta=r"C:\\Users\\julid\Downloads\\acces.log"

nav = []

with open(ruta, "rt") as file:
    for line in file:
        resultado = extract(regex, line)
        
        if resultado:
            nav.extend(resultado)


contador = Counter(nav)
for navegador, count in contador.items():
    print(f"Navegador: {navegador} cantidad: {count}")