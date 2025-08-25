#"""
# Imports
import subprocess
import time
import datetime
import os
import pprint
import shutil
from webdav3.client import Client

# Setup
# List of allowed SSIDs and current state of syncthing
updateT = 20
maxSecDif = 10
allowedSSIDs = [""]
running = False
# webDAV Setup
localHome = "/home/cosmic/"
remoteHome = "/home/cosmic/nextcloud/"
#remoteHome = "run/user/1000/gvfs/dav:host=nextcloud.fracturedstar.net,ssl=true,user=8b2218d2951e2df0030ebfec82c3850951f13753bf468fd0dab7b75e52bed645,prefix=%2Fremote.php%2Fdav%2Ffiles%2F8b2218d2951e2df0030ebfec82c3850951f1375et,ssl=true,user=8b2218d2951e2df0030ebfec82c3850951f13753bf468fd0dab7b75e52bed645,prefix=%2Fremote.php%2Fdav%2Ffiles%2F8b2218d2951e2df0030ebfec82c3850951f13753bf468fd0dab7b75e52bed645"
paths = ['Notes/']
remotePath, remoteMod = [], [] 
localPath, localMod = [], []
localPop, remotePop = [], []
#print(client.list("Notes", get_info=True)[0]['isdir'])

# Functions
# Gets list of all file locations on the nextcloud
def remoteFileList(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if entry[0] != ".":
            if os.path.isdir(full_path):
                remoteFileList(full_path)
            else:
                remotePath.append(full_path.replace(remoteHome, ''))
                remoteMod.append(os.path.getmtime(full_path))

# Gets list of all file locations localy stored
def localFileList(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if entry[0] != ".":
            if os.path.isdir(full_path):
                localFileList(full_path)
            else:
                localPath.append(full_path.replace(localHome, ''))
                localMod.append(os.path.getmtime(full_path))

def newDirPath(path):
    while True:
        rmChar = path[-1]
        if rmChar == "/":
            return path[:-1]
        else:
            path = path[:-1]

# Main
while True:
    # Gets the SSID of the connected network
    result = subprocess.run('iwgetid -r', capture_output=True, text=True, shell=True)
    ssid = result.stdout.strip()

    # Checks to see if it is in the whitelist and not already running
    if ssid in allowedSSIDs and not running:
        # Launches syncthing as a subprocess
        p = subprocess.Popen('syncthing')
        running = True
    # If syncthing is running and not on a whitelist SSID terminate syncthing
    elif ssid not in allowedSSIDs and running:
        p.terminate()
        p.wait()
        running = False

    # Compares the modification date and existance of files in the nextcloud aginst the local
    if ssid != "":
        print(f'{datetime.datetime.now()} - Began nextcloud sync')
        remoteFiles = []
        localFiles = []
        for path in paths:
            remoteFileList(remoteHome+path)
            localFileList(localHome+path)
            #lT = datetime.datetime.fromtimestamp(localMod[localPath.index(i)], datetime.timezone.utc)
            #lT = datetime.datetime.fromtimestamp(localMod[0], datetime.timezone.utc)
            #rT = datetime.datetime.fromtimestamp(remoteMod[7], datetime.timezone.utc)
            #print(lT)
            #print(rT)
            #print(lT >= rT-datetime.timedelta(hours=1))
            
            for i in localPath:
                if i not in remotePath:
                    try:
                        shutil.copy2(localHome+i, remoteHome+i)
                    except:
                        os.makedirs(newDirPath(remoteHome+i))
                        shutil.copy2(localHome+i, remoteHome+i)
                    print(f'{i} not in remote')
                    localPop.append(i)
                else:
                    lT = datetime.datetime.fromtimestamp(localMod[localPath.index(i)], datetime.timezone.utc)
                    rT = datetime.datetime.fromtimestamp(remoteMod[remotePath.index(i)], datetime.timezone.utc)
                    if lT+datetime.timedelta(seconds=maxSecDif) >= rT and lT-datetime.timedelta(seconds=maxSecDif) <= rT:
                        print(f'{i} already synced')
                    elif lT+datetime.timedelta(seconds=maxSecDif) < rT:
                        shutil.copy2(remoteHome+i, localHome+i)
                        print(f'Remote has newer {i}')
                    elif lT-datetime.timedelta(seconds-maxSecDif) > rT:
                        shutil.copy2(localHome+i, remoteHome+i)
                        print(f'Local has newer {i}')
                    else:
                        print("Something has gone wrong")
                    localPop.append(i)
                    remotePop.append(i)
            
            for i in localPop:
                localMod.pop(localPath.index(i))
                localPath.remove(i)
            if remotePop != []:
                for i in remotePop:
                    remoteMod.pop(remotePath.index(i))
                    remotePath.remove(i)
            localPop, remotePop = [], []
                    
            if remotePath != []:
                for i in remotePath:    
                    try:
                        shutil.copy2(remoteHome+i, localHome+i)
                    except:
                        os.makedirs(newDirPath(localHome+i))
                        shutil.copy2(remoteHome+i, localHome+i)
                    print(f'{i} not in local')
            
            #pprint.pp(localMod)
            #pprint.pp(remoteMod)
    
    print(f'{datetime.datetime.now()} - Nextcloud sync done, waiting {updateT} seconds till next sync')

    time.sleep(updateT)
#"""
#print("WIP")
