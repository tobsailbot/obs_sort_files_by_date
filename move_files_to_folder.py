import os
import os.path
import shutil

#os.chdir('D:\\TOBI-PC\\Descargas\\recordings test\\origen')
#print(os.getcwd())

# Indicate the recordings output directory, must be the SAME as in OBS settings
srcdir = 'D:\\TOBI-PC\\Descargas\\recordings test\\origen\\'

# List of all the files in the source directory
files = os.listdir(srcdir)

# For every element into the "files" list do the follow:
def createFolder():
    for file in files: 
        if not os.path.exists(srcdir+'OBS VIDEOS\\'+file[0:10]):  # Checks if a folder with the name of the date already exists
            os.makedirs(srcdir+'OBS VIDEOS\\'+file[0:10]) # Creates a folder with the first 11 characters of the file name

# Moves the files to the destiny folder that matches with the name of the files
def moveFiles ():
    for file in files:
        print(srcdir+file)
        shutil.move(srcdir+file,'D:\\TOBI-PC\\Descargas\\recordings test\\origen\\OBS VIDEOS\\'+file[0:10])


createFolder()
moveFiles()



