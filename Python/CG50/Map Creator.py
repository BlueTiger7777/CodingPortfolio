import random
from pprint import pprint

#0=empty, 1=entrence, 2=coridoor, 3=room, 4=undifined
CellTypes=[2,3]

while True:
    Cords=[3,3]
    Map=[
    [0,0,0,0,0,0,0],#[0][0-6]
    [0,0,0,0,0,0,0],#[1][0-6]
    [0,0,0,0,0,0,0],#[2][0-6]
    [0,0,0,1,0,0,0],#[3][0-6]
    [0,0,0,0,0,0,0],#[4][0-6]
    [0,0,0,0,0,0,0],#[5][0-6]
    [0,0,0,0,0,0,0],#[6][0-6]
    ]
    Rooms=random.randint(5,10)
    print(Rooms)
    while Rooms>0:
        NewRoom=True
        while NewRoom==True:
            Compass=random.randint(0,3)
            try:
                if Compass==0 and Map[Cords[0]+1][Cords[1]]==0:
                    Map[Cords[0]+1][Cords[1]]=random.choice(CellTypes)
                    Cords[0]+=1
                    NewRoom=False
                elif Compass==1 and Map[Cords[0]][Cords[1]+1]==0:
                    Map[Cords[0]][Cords[1]+1]=random.choice(CellTypes)
                    Cords[1]+=1
                    NewRoom=False
                elif Compass==2 and Map[Cords[0]-1][Cords[1]]==0:
                    Map[Cords[0]-1][Cords[1]]=random.choice(CellTypes)
                    Cords[0]-=1
                    NewRoom=False
                elif Compass==3 and Map[Cords[0]][Cords[1]-1]==0:
                    Map[Cords[0]][Cords[1]-1]=random.choice(CellTypes)
                    Cords[1]-=1
                    NewRoom=False
            except:
                print("IndexError reroll")
        Rooms-=1
    pprint(Map)
    input("Press ENTER for a new map")
