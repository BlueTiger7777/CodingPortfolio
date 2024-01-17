'''
=====To Do=====
-Fixed, I think, Well it worked perfectly for The Soul of Eternity on 08/12/2023 at 21:01
-Forgot that the item count is not added to the tree so FileItem did what pervious Item did and Item also hold count, 8/12/2023 at 22:29
===============
'''

#Imports
from ete3 import Tree, TreeStyle, faces
import os

#Varables
x=1
file=open("CraftingTree.txt")
d=file.readlines()
ImageForm=".webp"
Item=str(d[x])
ImagePath="C:\\Users\\alex\\Documents\\Terraria Crafting Tree Gen\\Items\\"
Image=ImagePath+Item[:-1]+ImageForm
alt=100
prevItem=Item
y=[]

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
            if FileItem!="Celebration Mk2":
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
                input(f'{Item} is not present in image folder. Please add it and press ENTER')
    except (IndexError, KeyboardInterrupt):
        print("End of file")
        TreeGen=False


#Export

###Sets a image and text for a node
##ch[0].add_face(face=faces.ImgFace(Image), column=0)
##ch[0].add_face(face=faces.TextFace(Item[:-1]), column=1)

#ch1=ch1.add_child(name="a")
#ch1=ch1.add_sister(name="b")

#Creates the tree image
print("Rendering Tree...")
z=open("CraftingTreeOut.txt", "w")
z.writelines(y)
z.close()
t.render("Crafting.png")
print("Tree Rendered")
file.close()

