# Imports
import os
import random as r
import time
from tinytag import TinyTag
from pygame import mixer as s

# Vars
drive = "E:"
formats = ['.mp3']

# Funcs
# Finds the file based of the track number of total tracks
def trackLookup(track):
    for dirs in tracks:
        if track - dirs[1] <= 0:
            name = dirs[0].replace(":", "-")
            while True:
                if name.replace("\\", "_") == name:
                    break
                else:
                    name = name.replace("\\", "_")
            if os.path.isfile(name+".txt"):
                with open(name+".txt", "r") as f:
                    fLine = f.readlines()
                    f.close()
                return dirs[0].replace(drive, drive+"\\")+"\\"+fLine[track-1][:-1]
            else:
                fLine = cacheMusic(dirs[0], name)
                return dirs[0].replace(drive, drive+"\\")+"\\"+fLine[track-1]
        else:
            track -= dirs[1]

# Caches the files in the folder in track order for faster lookup
def cacheMusic(path, name):
    files = []
    for file in os.scandir(path):
        if os.path.splitext(file)[1] in formats:
            fPath = os.path.join(drive, file)
            files.append(fPath.replace(path+"\\", ""))
    # Bubble sort cache
    trackInt = []
    for i in files:
        trackInt.append(TinyTag.get(path+"\\"+i).track)
    n = len(files)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if trackInt[j] > trackInt[j+1]:
                trackInt[j], trackInt[j+1] = trackInt[j+1], trackInt[j]
                files[j], files[j+1] = files[j+1], files[j]
                swapped = True
        if swapped == False:
            break
    # Writes the cache
    with open(name+".txt", "w") as f:
        for i in files:
            f.write(f'{i}\n')
        f.close()
    return files


tag = TinyTag.get('E:\\MultiGameOST\\Calamity\\Infernum - Storm Before Dawn.mp3')
print(f'Title: {tag.title}, Album: {tag.album}, Track: {tag.track}, Duration: {tag.duration}')


# Looks for playable media and get total tracks
tracks = []
newDir = False
for subdir, dirs, files in os.walk(drive):
    for file in files:
        x = os.path.join(subdir, file)
        if os.path.splitext(x)[1] in formats and len(tracks) == 0:
            tracks.append([subdir, sum(1 for entry in os.scandir(subdir) if os.path.splitext(entry)[1] in formats)])
        else:
            for i in tracks:
                if subdir not in tracks[tracks.index(i)][0]:
                    newDir = True
                else:
                    newDir = False
                    break
            if os.path.splitext(x)[1] in formats and newDir:
                newDir = False
                tracks.append([subdir, sum(1 for entry in os.scandir(subdir) if os.path.splitext(entry)[1] in formats)])

count = 0
for dirs in tracks:
    count += dirs[1]

# Music player
s.init()

song = trackLookup(r.randrange(1, count+1))
print(song)
s.music.load(song)
s.music.play()
while True:
    song = trackLookup(r.randrange(1, count+1))
    print(song)
    while s.music.get_busy():
        time.sleep(1)
    s.music.unload()
    s.music.load(song)
    s.music.play()

##s.music.load('E:\\MultiGameOST\\Calamity\\Infernum - Storm Before Dawn.mp3')
##s.music.play()

## tag = TinyTag.get(x)
## print(f'Title: {tag.title}, Album: {tag.album}, Track: {tag.track}')
