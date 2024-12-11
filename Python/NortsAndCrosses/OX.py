# Imports
import random

# Setup
COM = True
b = [
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " ",
]
player = 1
with open ("OXAI.txt", "r") as f:
    AI = f.readlines()
    f.close()
playedStates = []
AIMoves = []
AIPlayer = 1
TeachAI = True
NewAI = []

# Funcs
def updateAI():
    with open ("OXAI.txt", "r") as f:
        AI = f.readlines()
        f.close()
    state = b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]
    state = state.replace(" ", "-")
    playedStates.append(state)
    probs = ""
    for i in AI:
        AIline = i.split()
        if AIline[0] == state:
            for j in range(1, 10):
                probs += AIline[j]
                if j != 9:
                    probs += " "
            break
    if probs == "":
        probs = "1 1 1 1 1 1 1 1 1"
        out = state + " " + probs + "\n"
        with open("OXAI.txt", 'a') as f:
            f.write(out)
            f.close()
        with open("OXAI.txt", 'r') as f:
            AI = f.readlines()
            f.close()
    return AI

def AILearn(Reward):
    for i in AI:
        NewAI.append(i)
    for i in playedStates:
        for j in AI:
            AIline = j.split()
            if AIline[0] == i:
                for n in range(1, 10):
                    if n == AIMoves[playedStates.index(i)]:
                        AIline[n] = str(int(AIline[n]) + Reward)
                        if abs(int(AIline[n])) != int(AIline[n]) or int(AIline[n]) == 0:
                            AIline[n] = "0"
                NewAI[NewAI.index(j)] = AIline
    with open("OXAI.txt", 'w') as f:
        for i in NewAI:
            if type(i) == type([]):
                out = i[0] + " " + i[1] + " " + i[2] + " " + i[3] + " " + i[4] + " " + i[5] + " " + i[6] + " " + i[7] + " " + i[8] + " " + i[9] + "\n"
            else:
                out = i
            f.write(out)
        f.close()


def player1Win():
    if COM and AIPlayer == 1 and TeachAI:
        AILearn(3)
    elif COM and AIPlayer == 2 and TeachAI:
        AILearn(-1)

def player2Win():
    if COM and AIPlayer == 1 and TeachAI:
        AILearn(-1)
    elif COM and AIPlayer == 2 and TeachAI:
        AILearn(3)
      
def draw():
    if COM and TeachAI:
        AILearn(1)
    
def reset():
    b = [
        " ", " ", " ",
        " ", " ", " ",
        " ", " ", " ",
    ]
    player = 1
    with open ("OXAI.txt", "r") as f:
        AI = f.readlines()
        f.close()
    playedStates = []
    AIMoves = []
    NewAI = []

# Main
while True:
    print(f'\n{b[0]}|{b[1]}|{b[2]}\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n{b[6]}|{b[7]}|{b[8]}')
    if COM and player == AIPlayer:
        state = b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]+b[8]
        state = state.replace(" ", "-")
        playedStates.append(state)
        probs = ""
        for i in AI:
            AIline = i.split()
            if AIline[0] == state:
                for j in range(1,10):
                    probs += AIline[j]
                    if j != 9:
                        probs += " "
                break
        if probs == "":
            probs = "10 10 10 10 10 10 10 10 10"
            out = state + " " + probs + "\n"
            with open("OXAI.txt", 'a') as f:
                f.write(out)
                f.close()
            with open("OXAI.txt", 'r') as f:
                AI = f.readlines()
                f.close()
        loop = True
        while loop:
            try:
                probs = probs.split()
            except AttributeError:
                pass
            total = 0
            for i in probs:
                total += int(i)
            rand = random.randrange(1, total+2)
            x = 0
            for i in probs:
                rand -= int(i)
                x += 1
                if rand <= 0:
                    move = x - 1
                    if b[move] != " ":
                        break
                    else:
                        loop = False
                        AIMoves.append(move+1)
                        break
                elif x == 9:
                    move = x - 1
                    if b[move] != " ":
                        break
                    else:
                        loop = False
                        AIMoves.append(move+1)
                        break
    else:
        while True:
            try:
                move = int(input(f'\nPlayer {player}s move: ')) - 1
            except ValueError:
                print("Given a str wanted int")
            if b[move] != " ":
                print("Not a valied move")
            else:
                break
    if player == 1:
        b[move] = "O"
    else:
        b[move] = "X"
    player = (player % 2) + 1
    # Player 1 Win Check
    if b[0] == b[4] and b[4] == b[8] and b[8] == "O":
        print(f'\n\nPlayer 1 Wins\n\n\|{b[1]}|{b[2]}\n-\---\n{b[3]}|\|{b[5]}\n---\-\n{b[6]}|{b[7]}|\\')
        player1Win()
        break
    elif b[2] == b[4] and b[4] == b[6] and b[6] == "O":
        print(f'\n\nPlayer 1 Wins\n\n{b[0]}|{b[1]}|/\n---/-\n{b[3]}|/|{b[5]}\n-/---\n/|{b[7]}|{b[8]}')
        player1Win()
        break
    elif b[0] == b[1] and b[1] == b[2] and b[2] == "O":
        print(f'\n\nPlayer 1 Wins\n\n-----\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n{b[6]}|{b[7]}|{b[8]}')
        player1Win()
        break
    elif b[3] == b[4] and b[4] == b[5] and b[5] == "O":
        print(f'\n\nPlayer 1 Wins\n\n{b[0]}|{b[1]}|{b[2]}\n-----\n-----\n-----\n{b[6]}|{b[7]}|{b[8]}')
        player1Win()
        break
    elif b[6] == b[7] and b[7] == b[8] and b[8] == "O":
        print(f'\n\nPlayer 1 Wins\n\n{b[0]}|{b[1]}|{b[2]}\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n-----')
        player1Win()
        break
    elif b[0] == b[3] and b[3] == b[6] and b[6] == "O":
        print(f'\n\nPlayer 1 Wins\n\n||{b[1]}|{b[2]}\n-----\n||{b[4]}|{b[5]}\n-----\n||{b[7]}|{b[8]}')
        player1Win()
        break
    elif b[1] == b[4] and b[4] == b[7] and b[7] == "O":
        print(f'\n\nPlayer 1 Wins\n\n{b[0]}|||{b[2]}\n-----\n{b[3]}|||{b[5]}\n-----\n{b[6]}|||{b[8]}')
        player1Win()
        break
    elif b[2] == b[5] and b[5] == b[8] and b[8] == "O":
        print(f'\n\nPlayer 1 Wins\n\n{b[0]}|{b[1]}||\n-----\n{b[3]}|{b[4]}||\n-----\n{b[6]}|{b[7]}||')
        player1Win()
        break
            
    # Player 2 Win Check
    if b[0] == b[4] and b[4] == b[8] and b[8] == "X":
        print(f'\n\nPlayer 2 Wins\n\n\|{b[1]}|{b[2]}\n-\---\n{b[3]}|\|{b[5]}\n---\-\n{b[6]}|{b[7]}|\\')
        player2Win()
        break
    elif b[2] == b[4] and b[4] == b[6] and b[6] == "X":
        print(f'\n\nPlayer 2 Wins\n\n{b[0]}|{b[1]}|/\n---/-\n{b[3]}|/|{b[5]}\n-/---\n/|{b[7]}|{b[8]}')
        player2Win()
        break
    elif b[0] == b[1] and b[1] == b[2] and b[2] == "X":
        print(f'\n\nPlayer 2 Wins\n\n-----\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n{b[6]}|{b[7]}|{b[8]}')
        player2Win()
        break
    elif b[3] == b[4] and b[4] == b[5] and b[5] == "X":
        print(f'\n\nPlayer 2 Wins\n\n{b[0]}|{b[1]}|{b[2]}\n-----\n-----\n-----\n{b[6]}|{b[7]}|{b[8]}')
        player2Win()
        break
    elif b[6] == b[7] and b[7] == b[8] and b[8] == "X":
        print(f'\n\nPlayer 2 Wins\n\n{b[0]}|{b[1]}|{b[2]}\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n-----')
        player2Win()
        break
    elif b[0] == b[3] and b[3] == b[6] and b[6] == "X":
        print(f'\n\nPlayer 2 Wins\n\n||{b[1]}|{b[2]}\n-----\n||{b[4]}|{b[5]}\n-----\n||{b[7]}|{b[8]}')
        player2Win()
        break
    elif b[1] == b[4] and b[4] == b[7] and b[7] == "X":
        print(f'\n\nPlayer 2 Wins\n\n{b[0]}|||{b[2]}\n-----\n{b[3]}|||{b[5]}\n-----\n{b[6]}|||{b[8]}')
        player2Win()
        break
    elif b[2] == b[5] and b[5] == b[8] and b[8] == "X":
        print(f'\n\nPlayer 2 Wins\n\n{b[0]}|{b[1]}||\n-----\n{b[3]}|{b[4]}||\n-----\n{b[6]}|{b[7]}||')
        player2Win()
        break

    if b[0] != " " and b[1] != " " and b[2] != " " and b[3] != " " and b[4] != " " and b[5] != " " and b[6] != " " and b[7] != " " and b[8] != " ":
        print("Draw")
        draw()
        break
