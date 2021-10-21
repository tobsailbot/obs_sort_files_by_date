import os
import os.path
import shutil


srcdir = 'F:\\VIDEO MEDIA\\OBS\\ORIGEN\\'


# for filename in os.listdir(srcdir):

#shutil.move(srcdir+'\\2021-dec-18 11-05-01.txt',srcdir+'\\origen')

archivos = os.listdir(srcdir)

def crearCarpeta():
    for archivo in archivos: #por cada elemento de la lista archivos hacer lo siguiente
        if not os.path.exists('F:\\VIDEO MEDIA\\OBS\\OBS VIDEOS\\'+archivo[0:11]):  # checkear si existe una carpeta con el nombre de cada archivo
            os.makedirs('F:\\VIDEO MEDIA\\OBS\\OBS VIDEOS\\'+archivo[0:11]) #crear la carpeta con los primeros 11 caracteres del string

 #  else:
   #     shutil.move(srcdir+archivo,'D:\\TOBI-PC\\Escritorio\\Nueva carpeta\\destino\\'+archivo[0:11])

def moverArchivos ():
    for archivo in archivos:
        shutil.move(srcdir+archivo,'F:\\VIDEO MEDIA\\OBS\\OBS VIDEOS\\'+archivo[0:11])

crearCarpeta()
moverArchivos()
     

            



#archivoTest = archivos[1]

#element = archivoTest[0:11]

#if not os.path.exists(srcdir+'\\'+element):
#    os.makedirs(srcdir+'\\'+element)

