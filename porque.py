import csv
import json

# Esto es un edit de el archivo
with open('listadoPersonasEdad.csv', 'r') as archivo_csv:
    
    lector_csv = csv.DictReader(archivo_csv)
    
    
    datos = list(lector_csv)
# Esto es un edit de el archivo

for dato in datos:
    
    edad = int(dato['edad'])
    
    
    if edad < 18:
        dato['clasificacionEdad'] = 'Menor edad'
    elif 18 <= edad <= 30:
        dato['clasificacionEdad'] = 'Persona Joven'
    elif 31 <= edad <= 60:
        dato['clasificacionEdad'] = 'Persona Adulta'
    else:
        dato['clasificacionEdad'] = 'Adulto mayor'

# Esto es un edit de el archivo
with open('ClasificacionEdades.json', 'w') as archivo_json:
    
    json.dump(datos, archivo_json, ensure_ascii=False, indent=4)