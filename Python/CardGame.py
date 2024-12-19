# Imports
import random
import itertools

# Constants
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

# Functions
# Generates the deck based of presets
def createDeck(preset):
    deck = []
    match preset:
        case "Standard52": # A-K CDHS
            for i in ranks:
                for j in suits:
                    deck.append([i,j])
        case "Standard104": # A-K CDHS 2x
            for i in range(0, 2):
                for j in ranks:
                    for n in suits:
                        deck.append([j,n])
        case "SingleSuit52": # A-K C 4x
            for i in range(0, 4):
                for j in ranks:
                    deck.append([j,"Clubs"])
    return deck
    
# Uses the bubble sort algorithum to sort cards by rank
def sortCards(cards):
    n = len(cards)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if ranks.index(cards[j][0]) > ranks.index(cards[j+1][0]):
                cards[j], cards[j+1] = cards[j+1], cards[j]
                swapped = True
        if swapped == False:
            break
    return cards
    
def cardCombos(list1, list2, n):
    combo = []
    for i in range(len(list1)):
        combo.append(list1[i])
    for i in range(len(list2)):
        combo.append(list2[i])
    return list(itertools.combinations(combo, n))

# Texes Hold'em
playerCount = int(input("Number of players: "))
players = []
community = []
stack = createDeck("Standard52")
# Generates player and community hands
for i in range(0, 2):
    for j in range(0, playerCount):
        if i == 0:
            players.append([])
        x = random.choice(stack)
        players[j].append(x)
        stack.remove(x)
        players[j] = sortCards(players[j])
for i in range(0, 5):
    x = random.choice(stack)
    community.append(x)
    stack.remove(x)
community = sortCards(community)
# Hand output
for i in players:
    print(f'Player {players.index(i)+1}: {i[0][0]} of {i[0][1]}, {i[1][0]} of {i[1][1]}')
print(f'\nCommunity: {community[0][0]} of {community[0][1]}, {community[1][0]} of {community[1][1]}, {community[2][0]} of {community[2][1]}, {community[3][0]} of {community[3][1]}, {community[4][0]} of {community[4][1]}\n')
# Hand checker
for i in players:
    players[players.index(i)].append(0)
    for j in range(0,2):
        players[players.index(i)].append(None)
    combos = cardCombos(community[0:5], players[players.index(i)][0:2], 5)
    for j in combos:
        sortedJ = sortCards(list(j))
        if sortedJ[0][1] == sortedJ[1][1] and sortedJ[1][1] == sortedJ[2][1] and sortedJ[2][1] == sortedJ[3][1] and sortedJ[3][1] == sortedJ[4][1]:
            # Royal Flush
            if sortedJ[0][0] == "Ace" and sortedJ[1][0] == "10" and sortedJ[2][0] == "Jack" and sortedJ[3][0] == "Queen" and sortedJ[4][0] == "King":
                if players[players.index(i)][2] <= 9:
                    players[players.index(i)][2], players[players.index(i)][3] = 9, "Ace"
            # Stright Flush
            elif ranks.index(sortedJ[0][0])+1 == ranks.index(sortedJ[1][0]) and ranks.index(sortedJ[1][0])+1 == ranks.index(sortedJ[2][0]) and ranks.index(sortedJ[2][0])+1 == ranks.index(sortedJ[3][0]) and ranks.index(sortedJ[3][0])+1 == ranks.index(sortedJ[4][0]):
                if players[players.index(i)][2] <= 8:
                    winCombo = cardCombos(sortedJ, [], 5)
                    for n in winCombo:
                        if players[players.index(i)][3] == None and ranks.index(n[0][0])+1 == ranks.index(n[1][0]) and ranks.index(n[1][0])+1 == ranks.index(n[2][0]) and ranks.index(n[2][0])+1 == ranks.index(n[3][0]) and ranks.index(n[3][0])+1 == ranks.index(n[4][0]) and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1] or players[players.index(i)][2] < 8 and ranks.index(n[0][0])+1 == ranks.index(n[1][0]) and ranks.index(n[1][0])+1 == ranks.index(n[2][0]) and ranks.index(n[2][0])+1 == ranks.index(n[3][0]) and ranks.index(n[3][0])+1 == ranks.index(n[4][0]) and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1] or players[players.index(i)] == 8 and ranks.index(players[players.index(i)][3]) < ranks.index(n[4][0]) and n[0][0] != "Ace" and ranks.index(n[0][0])+1 == ranks.index(n[1][0]) and ranks.index(n[1][0])+1 == ranks.index(n[2][0]) and ranks.index(n[2][0])+1 == ranks.index(n[3][0]) and ranks.index(n[3][0])+1 == ranks.index(n[4][0]) and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1]:
                            players[players.index(i)][3] = n[4][0]
                    players[players.index(i)][2] = 8
            # Flush
            else:
                if players[players.index(i)][2] <= 5:
                    winCombo = cardCombos(sortedJ, [], 5)
                    for n in winCombo:
                        if players[players.index(i)][3] == None and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1] or players[players.index(i)][2] < 5 and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1] or players[players.index(i)][2] == 5 and ranks.index(players[players.index(i)][3]) < ranks.index(n[4][0]) and players[players.index(i)][3] != "Ace" and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1]:
                            players[players.index(i)][3] = n[4][0]
                        elif n[0][0] == "Ace" and n[0][1] == n[1][1] and n[1][1] == n[2][1] and n[2][1] == n[3][1] and n[3][1] == n[4][1]:
                            players[players.index(i)][3] = n[0][0]
                    players[players.index(i)][2] = 5
        # Four of a Kind
        elif sortedJ[0][0] == sortedJ[1][0] and sortedJ[1][0] == sortedJ[2][0] and sortedJ[2][0] == sortedJ[3][0] or sortedJ[1][0] == sortedJ[2][0] and sortedJ[2][0] == sortedJ[3][0] and sortedJ[3][0] == sortedJ[4][0]:
            if players[players.index(i)][2] <= 7:
                winCombo = cardCombos(sortedJ, [], 4)
                for n in winCombo:
                    if players[players.index(i)][3] == None and n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[2][0] == n[3][0] or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[2][0] == n[3][0] and players[players.index(i)][2] < 7 or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[2][0] == n[3][0] and players[players.index(i)][2] == 7 and ranks.index(players[players.index(i)][3]) < ranks.index(n[0][0]) and players[players.index(i)][3] != "Ace" or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[2][0] == n[3][0] and n[0][0] == "Ace":
                        players[players.index(i)][3] = n[0][0]
                players[players.index(i)][2] = 7
        # Full House
        elif sortedJ[0][0] == sortedJ[1][0] and sortedJ[2][0] == sortedJ[3][0] and sortedJ[3][0] == sortedJ[4][0] or sortedJ[0][0] == sortedJ[1][0] and sortedJ[1][0] == sortedJ[2][0] and sortedJ[3][0] == sortedJ[4][0]:
            if players[players.index(i)][2] <= 6:
                winCombo = cardCombos(sortedJ, [], 5)
                for n in winCombo:
                    if players[players.index(i)][3] == None and n[0][0] == n[1][0] and n[2][0] == n[3][0] and n[3][0] == n[4][0] or n[0][0] == n[1][0] and n[2][0] == n[3][0] and n[3][0] and n[4][0] and players[players.index(i)][2] < 6 or n[0][0] == n[1][0] and n[2][0] == n[3][0] and n[3][0] == n[4][0] and ranks.index(players[players.index(i)][4]) < ranks.index(n[2][0]) and players[players.index(i)][2] == 6 or n[0][0] == n[1][0] and n[2][0] == n[3][0] and n[3][0] == n[4][0] and ranks.index(players[players.index(i)][3]) < ranks.index(n[0][0]) and players[players.index(i)][2] and players[players.index(i)][3] != "Ace" or n[0][0] == n[1][0] and n[2][0] == n[3][0] and n[3][0] == n[4][0] and n[0][0] == "Ace":
                        players[players.index(i)][3], players[players.index(i)][4] = n[0][0], n[2][0]
                    elif players[players.index(i)][3] == None and n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[3][0] == n[4][0] or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[3][0] and n[4][0] and players[players.index(i)][2] < 6 or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[3][0] == n[4][0] and ranks.index(players[players.index(i)][4]) < ranks.index(n[3][0]) and players[players.index(i)][2] == 6 or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[3][0] == n[4][0] and ranks.index(players[players.index(i)][3]) < ranks.index(n[0][0]) and players[players.index(i)][2] == 6 and players[players.index(i)][3] != "Ace" or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[3][0] == n[4][0] and n[0][0] == "Ace":
                        players[players.index(i)][4], players[players.index(i)][3] = n[0][0], n[3][0]
                players[players.index(i)][2] = 6
        # Stright
        elif ranks.index(sortedJ[0][0])+1 == ranks.index(sortedJ[1][0]) and ranks.index(sortedJ[1][0])+1 == ranks.index(sortedJ[2][0]) and ranks.index(sortedJ[2][0])+1 == ranks.index(sortedJ[3][0]) and ranks.index(sortedJ[3][0])+1 == ranks.index(sortedJ[4][0]) or sortedJ[0][0] == "Ace" and sortedJ[1][0] == "10" and sortedJ[2][0] == "Jack" and sortedJ[3][0] == "Queen" and sortedJ[4][0] == "King":
            if players[players.index(i)][2] <= 4:
                winCombo = cardCombos(sortedJ, [], 5)
                for n in winCombo:
                    if players[players.index(i)][3] == None and ranks.index(n[0][0])+1 == ranks.index(n[1][0]) and ranks.index(n[1][0])+1 == ranks.index(n[2][0]) and ranks.index(n[2][0])+1 == ranks.index(n[3][0]) and ranks.index(n[3][0])+1 == ranks.index(n[4][0]) or ranks.index(n[0][0])+1 == ranks.index(n[1][0]) and ranks.index(n[1][0])+1 == ranks.index(n[2][0]) and ranks.index(n[2][0])+1 == ranks.index(n[3][0]) and ranks.index(n[3][0])+1 == ranks.index(n[4][0]) and players[players.index(i)][2] < 4 or ranks.index(n[0][0])+1 == ranks.index(n[1][0]) and ranks.index(n[1][0])+1 == ranks.index(n[2][0]) and ranks.index(n[2][0])+1 == ranks.index(n[3][0]) and ranks.index(n[3][0])+1 == ranks.index(n[4][0]) and ranks.index(players[players.index(i)][3]) < ranks.index(n[4][0]) and players[players.index(i)][2] == 4 and players[players.index(i)][3] != "Ace":
                        players[players.index(i)][3] = n[4][0]
                    elif n[0][0] == "Ace" and n[1][0] == "10" and n[2][0] == "Jack" and n[3][0] == "Queen" and n[4][0] == "King":
                        players[players.index(i)][3] = n[0][0]
                players[players.index(i)][2] = 4
        # Three of a Kind
        elif sortedJ[0][0] == sortedJ[1][0] and sortedJ[1][0] == sortedJ[2][0] or sortedJ[1][0] == sortedJ[2][0] and sortedJ[2][0] == sortedJ[3][0] or sortedJ[2][0] == sortedJ[3][0] and sortedJ[3][0] == sortedJ[4][0]:
            if players[players.index(i)][2] <= 3:
                winCombo = cardCombos(sortedJ, [], 3)
                for n in winCombo:
                    if players[players.index(i)][3] == None and n[0][0] == n[1][0] and n[1][0] == n[2][0] or n[0][0] == n[1][0] and n[1][0] == n[2][0] and players[players.index(i)][2] < 3 or n[0][0] == n[1][0] and n[1][0] == n[2][0] and ranks.index(players[players.index(i)][3]) < ranks.index(n[0][0]) and players[players.index(i)][2] == 3 and players[players.index(i)][3] != "Ace" or n[0][0] == n[1][0] and n[1][0] == n[2][0] and n[0][0] == "Ace":
                        players[players.index(i)][3] = n[0][0]
                players[players.index(i)][2] = 3
        # Two Pair
        elif sortedJ[0][0] == sortedJ[1][0] and sortedJ[2][0] == sortedJ[3][0] or sortedJ[0][0] == sortedJ[1][0] and sortedJ[3][0] == sortedJ[4][0] or sortedJ[1][0] == sortedJ[2][0] and sortedJ[3][0] == sortedJ[4][0]:
            if players[players.index(i)][2] <= 2:
                winCombo = cardCombos(sortedJ, [], 4)
                for n in winCombo:
                    if players[players.index(i)][3] == None and n[0][0] == n[1][0] and n[2][0] == n[3][0] or n[0][0] == n[1][0] and n[2][0] == n[3][0] and players[players.index(i)][2] < 2 or n[0][0] == n[1][0] and n[2][0] == n[3][0] and ranks.index(players[players.index(i)][4]) < ranks.index(n[2][0]) and players[players.index(i)][2] == 2 and players[players.index(i)] or n[0][0] == n[1][0] and n[2][0] == n[3][0] and ranks.index(players[players.index(i)][3]) < ranks.index(n[0][0]) and players[players.index(i)][2] == 2 and players[players.index(i)][3] != "Ace" or n[0][0] == n[1][0] and n[2][0] == n[3][0] and n[0][0] == "Ace":
                        players[players.index(i)][3], players[players.index(i)][4] = n[0][0], n[2][0]
                players[players.index(i)][2] = 2
        # Pair
        elif sortedJ[0][0] == sortedJ[1][0] or sortedJ[1][0] == sortedJ[2][0] or sortedJ[2][0] == sortedJ[3][0] or sortedJ[3][0] == sortedJ[4][0]:
            if players[players.index(i)][2] <= 1:
                winCombo = cardCombos(sortedJ, [], 2)
                for n in winCombo:
                    if players[players.index(i)][3] == None and n[0][0] == n[1][0] or n[0][0] == n[1][0] and players[players.index(i)][2] < 1 or n[0][0] == n[1][0] and ranks.index(players[players.index(i)][3]) < ranks.index(n[0][0]) and players[players.index(i)][2] == 1 and players[players.index(i)][3] != "Ace" or n[0][0] == n[1][0] and n[0][0] == "Ace":
                        players[players.index(i)][3] = n[0][0]
                players[players.index(i)][2] = 1
        # Highcard
        else:
            if players[players.index(i)][2] <= 0:
                players[players.index(i)][2] = 0
                for n in sortedJ:
                    if players[players.index(i)][3] == None or ranks.index(players[players.index(i)][3]) < ranks.index(n[0]) and players[players.index(i)][3] != "Ace" or n[0] == "Ace":
                        players[players.index(i)][3] = n[0]
    match players[players.index(i)][2]:
        case 0:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Highcard')
        case 1:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Pair')
        case 2:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]}, {players[players.index(i)][4]} Two Pair')
        case 3:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Three of a Kind')
        case 4:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Stright')
        case 5:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Flush')
        case 6:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]}, {players[players.index(i)][4]} Full House')
        case 7:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Four of a Kind')
        case 8:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Stright Flush')
        case 9:
            print(f'Player {players.index(i)+1} got {players[players.index(i)][3]} Royal Flush')
