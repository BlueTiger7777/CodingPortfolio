'''
=====To Do=====
-Fixed, I think, Well it worked perfectly for The Soul of Eternity on 08/12/2023 at 21:01
-Forgot that the item count is not added to the tree so FileItem did what previous Item did and Item also hold count, 8/12/2023 at 22:29
-Fixed the edge-case of the Celebration Mk2, well looks like it worked, 17/01/2024 at 20:40
-Add list of active mods to the tree, 23/04/2024 at 17:33
-R.E.K. 3000 needs to be fixed, added an edge-case as it looks the same as a normal item, 23/04/2024 at 18:25
===============
'''

#Imports
from ete3 import Tree, TreeStyle, faces
import os
import PIL.Image
from PIL import ImageDraw
from PIL import ImageFont
import json

#Varables
x=1
file=open("CraftingTree.txt")
d=file.readlines()
ImageForm=".webp"
Item=str(d[x])
ImagePath="<path\\to\\items>"
Image=ImagePath+Item[:-1]+ImageForm
alt=100
prevItem=Item
y=[]
ModPath="<path\\to\\enabled\\mods>"
with open(ModPath, "r+") as m:
    Mods=json.load(m)

#Tree Generation
t=Tree()
ch=[]
ach=0
ch.append(t.add_child())

RootGen=True
while RootGen==True:
    pres=os.path.exists(Image)
    if pres==True:
        ch[ach].add_face(face=faces.TextFace(Item[:-1]), column=0)
        ch[ach].add_face(face=faces.ImgFace(Image), column=1)
        RootGen=False
    else:
        input(f'{Item[:-1]} is not present in image folder. Please add it and press ENTER')

#CraftingTree.txt traversal logic
TreeGen=True
while TreeGen==True:
    x+=2
    #check if at end of file or an alternate recipe and how many children deep
    try:
        ItemLoop=True
        while ItemLoop==True:
            LineLoop=True
            ach=d[x].count("|")
            if ach<alt:
                alt=100
            while LineLoop==True:
                if str(d[x]).find(" - Alternate Recipe") != -1 and alt==100:
                    x+=2
                    alt=ach
                    break
                    #print("[!]")
                elif str(d[x]).find(" - Alternate Recipe") != -1 and alt!=100:
                    x+=2
                    #alt=ach
                    break
                    #print("[!]")
                elif d[x-1].count("|")<alt and alt!=100:
                    x+=2
                    break
                else:
                    LineLoop=False

            #print(ach)
            Item=str(d[x])
            for i in range(1,ach):
                Item=Item[5:]
            equ=Item[2]
            Item=Item[6:-1]
            FileItem=Item

            #Check if there is a number after a space
            for i in FileItem[::-1]:
                try:
                    int(i)
                except ValueError:
                    if i==" ":
                        Count=True
                        break
                    else:
                        Count=False
                        break

            Item = Item.replace(".", "")
            FileItem = FileItem.replace(".", "")
            if Count == True and FileItem !="REK 3000": #FileItem!="Celebration Mk2":
                try:
                    int(FileItem[-1])
                    FileItem=''.join([i for i in Item if not i.isdigit()])
                    FileItem=FileItem[:-1]
                except (ValueError, KeyboardInterrupt):
                    pass
                
            #print(alt)
            if ach>alt and d[x-1].count("|")>alt or FileItem[0]=="=" or FileItem==prevItem:#ach+1>alt or Item[0]=="=" or Item==prevItem or equ!="="
                x+=2
                #print("[!]", Item)
            ##elif ach<str(d[x]).count("|"):
            ##    x+=2

            #elif ach==alt and ach+1>d[x-2].count("|") and d[x].count("=")!=-1:#3152 shows and nothing beyond 2652
                #x+=2
                
                #ItemLoop=False
                #alt=100
                #print("[!]", Item)
            elif ach!=alt:
                ItemLoop=False
                alt=100
                #print("[!]",Item)
            else:
                ItemLoop=False
                alt=100

        prevItem=FileItem
        
        try:
            ch[ach]=0
        except IndexError:
            ch.append(0)
        ch[ach]=ch[ach-1].add_child()
        
        Image=ImagePath+FileItem+ImageForm
        
        #loops if item image not found
        NodeGen=True
        while NodeGen==True:
            #check if image exists
            pres=os.path.exists(Image)
            if pres==True:
                print(f'Item: {FileItem}, Line: {x+1}') #, ach: {ach}, alt: {alt}
                ch[ach].add_face(face=faces.TextFace(Item), column=0)
                ch[ach].add_face(face=faces.ImgFace(Image), column=1)
                Item=Item+"\n"
                y.append(Item)
                NodeGen=False
            else:
                input(f'{FileItem} is not present in image folder. Please add it and press ENTER')
    except (IndexError, KeyboardInterrupt):
        print("End of file")
        TreeGen=False


#Export

###Sets an image and text for a node
##ch[0].add_face(face=faces.ImgFace(Image), column=0)
##ch[0].add_face(face=faces.TextFace(Item[:-1]), column=1)

#ch1=ch1.add_child(name="a")
#ch1=ch1.add_sister(name="b")

#Creates the tree image
print("Rendering Tree...")
z=open("CraftingTreeOut.txt", "w")
z.writelines(y)
z.close()
t.render("<path\\to\\output>")
print("Tree Rendered")

print("Adding Mods...")
img=PIL.Image.open("Crafting.png")
I1=ImageDraw.Draw(img)
ModFont=ImageFont.truetype("arial.ttf", 10)
ModY=5
for i in Mods:
    I1.text((10, ModY), i, font=ModFont, fill=(0, 0, 0))
    ModY+=10
img.save("Crafting.png")
print("Mods Added")

file.close()
m.close()
