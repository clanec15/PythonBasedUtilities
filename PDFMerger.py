from PyPDF2 import PdfFileMerger
import os


print("Introduce los nombres de los pdfs")
pdfs = list(map(str, input("").split()))


if len(pdfs) <= 1:
    print("Se necesitan al menos dos archivos")
    exit()
    


print("Introduce la ruta en donde los archivos estan ubicados")
path = input('')


if os.getcwd() != path:
    os.chdir(path)

else:
    None
    
if os.path.isfile(pdfs[0]) == True:
    merger = PdfFileMerger()
    
    for pdf in pdfs:
        merger.append(pdf)
    
    print("Coloca el nombre del nuevo archivo")
    result = input('')
    
    if os.path.isfile(result + ".pdf") == True:
        print("El archivo ya existe, por favor, cambia el nombre del archivo")
        exit()
    
    merger.write(result + ".pdf")
    merger.close()
    print("Documentos unidos... \nCon pegamento pritt :D")
    exit()

else:
    print("El/Los documentos no fueron encontrados, verifique los nombres e intente de nuevo")
    exit()
