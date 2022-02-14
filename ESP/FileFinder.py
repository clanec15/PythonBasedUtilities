import os
import time
import platform
import subprocess, sys


currentos=platform.system()

print("Cual es el archivo que quieres encontrar?")
name=input('')
print("Quieres buscar en la carpeta actual o en otra carpeta? \n A.- Carpeta Actual O.- Otra Carpeta")
directorio=input("")
if directorio == ("A"):
    path=os.getcwd()

else:
    print("Introduce la direccion del directorio, P.E= C:/Directorio/De/Prueba.txt")
    path=input("")


def find(name, path):
    try:
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
            else:
                raise FileNotFoundError
    except FileNotFoundError:
        print("El documento no se ha encontrado, Vuelva abrir el buscador he intente de nuevo")
        print("Terminando Programa...")
        time.sleep(5)
        exit()


file=find(name, path)

print("Archivo Encontrado!, Directorio: "+ file)


print("Abriendo archivo...")

if currentos == ("Linux"):
    os.system("xdg-open "+ file)

elif currentos == ("Windows"):
    os.startfile(file)

elif currentos == ("Darwin"):
    print("Lo sentimos, el script actual no soporta Mac...")

time.sleep(2)
exit()
        
    
    
