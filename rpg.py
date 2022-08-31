import os
import numpy as np

# The world
map = [
    ["#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#",],
    ["#",".",".",".","#"," ","#",".",".",".",".",".",".",".","#",],
    ["#",".",".",".","#"," ","#",".","#","#","#","#","#",".","#",],
    ["#",".",".",".","#"," ","#",".","#"," "," "," ","#",".","#",],
    ["#",".",".",".","#"," ","#",".","#"," "," "," ","#",".","#",],
    ["#",".","@",".","#","#","#",".","#","#","#","#","#",".","#",],
    ["#",".",".",".",".",".","#",".","#","A",".",".","&",".","&",],
    ["#","#","#","#","#",".","#",".","#","#","#","#","#",".","#",],
    [" "," "," "," ","#",".","#",".","#"," "," "," ","#",".","#",],
    [" "," "," "," ","#",".","#",".","#"," "," "," ","#",".","#",],
    [" "," "," "," ","#",".","#",".","#"," "," "," ","#",".","#",],
    [" "," "," "," ","#",".","#",".","#","#","#","#","#",".","#",],
    [" "," "," "," ","#",".",".",".",".",".",".",".",".",".","#",],
    [" "," "," "," ","#","#","#","#","#","#","#","#","#","#","#",],
]

# Spawn position. Remember that the 'y' is inverted but the 'x' isn't
player = {'y': 1, 'x': 2}

# Moving the player
moves = {"W": {'y': -1, 'x': 0},
         "A": {'y': 0, 'x': -1},
         "S": {'y': 1, 'x': 0},
         "D": {'y': 0, 'x': 1}
        }
        
# Changes the 2D list of 'map' to be a numpy array
map = np.array(map)

# Your player character
map[player['y']][player['x']] = "$"

# Stats
health = 10

xp = 0
levelup = 100

level = 1

gold = 0

attack = 1

# Keeping the shape of the map when moving (as a function)
def print_map(map):
    
    for row in map:
        print(" ".join(str(n) for n in row))

print("Press S to start")

#Prints the map
print_map(map)

game = True 
while game:
    
    # Basic moving
    move = input("Move with WASD, action with K\n\n>")
    
    move = move.upper()
    
    try:
        pos = moves[move]
    except KeyError:
        print(f"{move} is an invalid action.\n")
        continue
   
    x2 = player['x'] + pos['x']
    y2 = player['y'] + pos['y']
    
    # If the player tries to leave the map and not crash the game
    try:
        map_pos = map[y2][x2]
    except IndexError:
        print("You cannot leave the map. That is probably in production\n")
        continue

    # Keeps the terminal clean
    os.system("clear")

    # Prints stats
    print(f"Level:  {level}\nHealth: {health}\nXP:     {xp}/{levelup}\nGold:   {gold}\n---------")
    
    # Collision, moving, and items
    if map_pos != "#":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
        
    if map_pos == "H":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health += 25
        xp += 5
        
    if map_pos == "@":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
        
        gold += 1
        xp += 2

    # Camera screen
    print_map(map[max(y2-2,0) : y2+3, max(x2-2,0) : x2+3])