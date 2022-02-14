import os
import subprocess

currentdir = os.getcwd()

print("Se estara utilizando una USB o un lecto de DVD's? [USB/CD]")
device = input('')

if device.lower() == 'usb':
    def MountDetector():
        print("Comprobando si el disco esta montado")
        mountpoint = subprocess.check_output("findmnt -S /dev/sda | grep /media", shell=True)
        mountpointconf = subprocess.check_output("lsblk | grep /media", shell=True)
        if bool(mountpoint) and bool(mountpointconf) == True:
            print("El disco esta montado!")
            ismounted = True
            return ismounted
        elif bool(mountpoint) or bool(mountpointconf) == False:
            
            ismounted = False
            print("El disco no ha sido detectado correctamente, proceda con precaucion")
            return ismounted
else:
    def MountDetector():
        print("Comprobando si el disco esta montado")
        mountpoint = subprocess.check_output("findmnt -S /dev/sr0 | grep /media", shell=True)
        mountpointconf = subprocess.check_output("lsblk | grep /media", shell=True)
        
            
        if bool(mountpoint) and bool(mountpointconf) == True:
            
            ismounted = True
            print("El disco esta montado!")
            return ismounted
        elif bool(mountpoint) or bool(mountpointconf) == False:
            
            ismounted = False
            print("El disco no ha sido detectado correctamente, proceda con precaucion")
            return ismounted

    

print("Cual sera el nombre del archvio ISO?")
isoname = input('')

print("Deseas que el archivo iso este en la carpeta actual o en otra carpeta [A/o] A = Carpeta Actual / o = Otra Carpeta")
selectionname = input('')

if selectionname.lower() == 'a':
    if MountDetector() == True:
        print("El mountpoint del disco esta en " + str(subprocess.check_output("lsblk | sed -n -e 's/^.*rom //p'", shell=True)))
        print("Comenzando el copiado...")
        os.system('dd if=/dev/sr0 of=' + currentdir + "/" + isoname + '.iso'+ " " "status=progress")
        print("Confirmando que el archivo existe en el lugar designado")
        newfile = currentdir + "/" + isoname + '.iso'
        
        if os.path.isfile(newfile) == True:
            print("El archivo existe!, el copiado ha sido exitoso!")
            print("Finalizando...")
            exit()
        else:
            print("El archivo no se a encontrado, intente de nuevo")
            exit()
    
    elif MountDetector() == False:
        print("El disco ha sido detectado por solo uno de los dos comandos dados, confirme que el disco ha sido montado correctamente para evitar perdida de datos")
        exit()

else:
    print("Introduzca la ruta para el archivo, si el directorio aun no existe, sera creado...")
    mkdir = input('')
    
    if isdir(mkdir) == True:
        print("El directorio ya existe y sera usado")
        if MountDetector() == True:
            print("El disco fue encontrado de manera exitosa")
            print("Comenzando el copiado")
            os.system('dd if=/dev/sr0 of=' + mkdir + "/" + isoname + '.iso'+ " " "status=progress")
            print("Detectando la presencia del archivo en el lugar de destino...")
            filedetection = mkdir + "/" + isoname + ".iso"
            
            if os.path.isfile(filedetection) == True:
                print("El archivo ha sido detectado correctamente, el copiado fue exitoso, finalizando")
                exit()
            else:
                print("El archivo no fue detectado, el copiado no se ha realizado con exito, intente de nuevo...")
                exit()
                
                
    elif mkdir.isdir == False:
        print("El directorio no ha sido detectado, Creando...")
        os.system('mkdir ' + mkdir)
        print("Confirmando si el disco esta montado...")
        MountDetector()
        
        if MountDetector() == True:
            print("Comenzando el copiado")
            os.system('dd if=/dev/sr0 of=' + mkdir + "/" + isoname + '.iso'+ " " "status=progress")
            print("Detectando la presencia del archivo en el lugar de destino...")
            filedetection = mkdir + "/" + isoname + '.iso'
            
            if os.path.isfile(filedetection) == True:
                print("El archivo ha sido detectado correctamente, el copiado fue exitoso, finalizando")
                exit()
            else:
                print("El archivo no fue detectado, el copiado no se ha realizado con exito, intente de nuevo...")
                exit()
            
        


        
        
        
