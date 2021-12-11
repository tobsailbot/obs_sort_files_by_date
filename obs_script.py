
import obspython as obs
import time
import pathlib
import os
import os.path
import shutil


# ----------- Sort files by folder script -----------

srcdir = None
files = None


# For every element into the "files" list do the follow:
def createFolder():
    for file in files:
        if not os.path.exists(srcdir+'\\OBS VIDEOS\\'+file[0:10]):  # Checks if a folder with the name of the date already exists
            os.makedirs(srcdir+'\\OBS VIDEOS\\'+file[0:10]) # Creates a folder with the first 11 characters of the file name

# Moves the files to the destiny folder that matches with the name of the files
def moveFiles():
    for file in files:
        shutil.move(srcdir+'/'+file,srcdir+'\\OBS VIDEOS\\'+file[0:10])



# ------------------- OBS script ------------------

class Data:
    OutputDir = None

def frontend_event_handler(data):
    if data == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        time.sleep(0.5)
        print('The recording stopped..')
        global files  # List of all the files in the source directory
        files = [f for f in os.listdir(srcdir)
                 if os.path.isfile(os.path.join(srcdir, f)) and f.endswith(
                (".flv", ".mp4", ".mov", ".mkv", ".ts", ".m3u8"))]
        createFolder()
        moveFiles()
        print('Files were moved!')
        return True

def script_update(settings):
    Data.OutputDir = obs.obs_data_get_string(settings,"outputdir")
    global srcdir
    srcdir = Data.OutputDir


def script_description():
    return ("SORT RECORDINGS IN FOLDERS\n\n"
            "How it works:\n\n"
            "Choose the folder where recordings are saved below.\n"
            "It must be THE SAME as you have in the OBS settings."
            " When the recording stops, the most recent file "
            " will be moved to a folder with the name of the date."
            " You should change the date format in recording settings"
            " -> %CCYY-%MM-%DD")

# Properties inside the OBS script GUI
def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_path(props, "outputdir", "Recordings folder", obs.OBS_PATH_DIRECTORY,None, str(pathlib.Path.home()))
    return props

obs.obs_frontend_add_event_callback(frontend_event_handler)










