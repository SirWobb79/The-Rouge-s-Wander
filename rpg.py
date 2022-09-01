import os
import numpy as np

# The world
map = [
    ["#","#","#","#","#"," ","#","#","#","#","#","#","#","#","#"," "," "," "," "," ","#","#","#","#","#",],
    ["#",".",".",".","#"," ","#",".","1",".","1",".",".",".","#"," "," "," "," "," ","#","m","h","m","#",],
    ["#",".",".",".","#"," ","#",".","#","#","#","#","#",".","#"," "," "," "," "," ","#","@","@","@","#",],
    ["#",".",".",".","#"," ","#",".","#"," "," "," ","#",".","#"," "," "," "," "," ","#","#","&","#","#",],
    ["#",".",".",".","#"," ","#","2","#"," "," "," ","#","3","#","#","#","#","#","#","#",".",".",".","#",],
    ["#",".","@",".","#","#","#",".","#","#","#","#","#",".","#",".",".",".",".",".","#",".",".",".","#",],
    ["#",".",".",".",".",".","#",".","#","H","@","@","&",".","&",".",".",".",".",".","&",".",".",".","&",],
    ["#","#","#","#","#",".","#",".","#","#","#","#","#","#","#",".",".",".",".",".","#",".",".",".","#",],
    [" ","#","1","1","&",".","#","1","#"," "," "," ","#","m","#","#","#","#","#","#","#",".",".",".","#",],
    [" ","#","1","1","#",".","#",".","#"," "," "," ","#","m","#",".",".","#",".",".","#","#","&","#","#",],
    [" ","#","2","1","#",".","#",".","#"," "," "," ","#","h","#",".",".","#",".",".","#",".",".",".","#",],
    ["#","#","2","#","#",".","#",".","#","#","#","#","#","@","#",".",".","4",".",".","&",".",".",".","#",],
    ["#","m","@","h","#",".",".",".","&","1","2","2","3","@","#",".",".","#",".",".","#",".",".",".","#",],
    ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#",],
]

# Spawn position. Remember that the 'y' is inverted but the 'x' isn't
player = {'y': 1, 'x': 2}

# Moving the player
moves = {"W": {'y': -1, 'x': 0},
         "A": {'y': 0, 'x': -1},
         "S": {'y': 1, 'x': 0},
         "D": {'y': 0, 'x': 1},
         "I": {'y': 0, 'x': 0}
        }
        
# Changes the 2D list of 'map' to be a numpy array
map = np.array(map)

# Your player character
map[player['y']][player['x']] = "$"

# Stats
health = 30

xp = 0
levelup = 100

level = 1

gold = 0

temp = 37

meat = 0
hide = 0

timer = 76

# Keeping the shape of the map when moving (as a function)
def print_map(map):
    
    for row in map:
        print(" ".join(str(n) for n in row))

print("<The Rouge's Wander>\n\nYou find yourself in a dungeon which makes you cold very slowly.\nThe only way out is to fight, collect, and level up right to the\nend. (Enemies are literally numbered as their level. Time is how\nmany game ticks until you lose heat.)\n\nThink you got what it takes? Then press S to start.")

#Prints the map
print_map(map)

game = True
while game:
    
    # Basic moving
    move = input("Move: WASD | Action: K | Inventory: I\n\n>")
    
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
    os.system("cls" if os.name == "nt" else "clear")

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
          
        health += 15
        xp += 2
        
    if map_pos == "@":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
        
        gold += 1
        xp += 2
    
    if map_pos == "m":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
        
        meat += 5
        xp += 3
        
    if map_pos == "h":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
        
        hide += 5
        xp += 3
        
    # Enemies ranging in levels (max is 6)
    if map_pos == "1":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health -= 5
        xp += 5
        meat += 1
        hide += 2

    if map_pos == "2":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health -= 15
        xp += 10
        meat += 3
        hide += 8
        
    if map_pos == "3":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health -= 50
        xp += 15
        meat += 8
        hide += 15

    if map_pos == "4":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health -= 100
        xp += 25
        meat += 15
        hide = 35
        
    if map_pos == "5":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health -= 200
        xp += 40
        meat += 25
        hide += 60
        
    if map_pos == "6":
        map[player['y']][player['x']] = "."
        map[y2][x2] = "$"
            
        player['x'] = x2
        player['y'] = y2
          
        health -= 400
        xp += 75
        meat += 50
        hide += 85

    # Leveling up (max level is 6)    
    if xp >= levelup:
        if level <= 6:
            xp = 0
            level += 1
            levelup *= 2
        if level == 6:
            xp = 0
            health *= 3
    # Inventory
    if move == "I":
        os.system("clear")
        print(f"Inventory:\n\nMeat - Eat to heal: {meat}\nHide - Use to be warmer: {hide}\n---------")
        
        use = input("Use an object by the first letter\n\n>")
        
        if use == "m":
            if meat > 0:
                meat -= 1
                health += 10
                xp += 1
        
        if use == "h":
            if hide > 0:
                hide -= 1
                temp += 0.5
        
        if use == "BACK":
            continue
        
        os.system("clear")
       
    # Game over if health is 0 or less
    if health <= 0:
        print(f"Game Over! You tried fighting a Lvl {map_pos}. Final stats were:\n")
        game = False
        
    timer -= 1
    
    if timer == 0:
        temp -= 1
        timer = 75
        
        if temp < 20 or temp > 50:
            print(f"Game Over! You died from abnormal tempratures. Final stats were:\n")
            game = False
        
    # Prints stats
    if level != 6:
        print(f"Level:  {level}/6\nHealth: {health}\nXP:     {xp}/{levelup}\nGold:   {gold}\nTemp:   {temp}°C/50°C\nTime:   {timer}\n---------")
    
    if level == 6:
        print(f"Level:  {level}/6\nHealth: {health}\nXP:     {xp}\nGold:   {gold}\nTemp: {temp}°C/50°C\n---------")
    
    if game == True:
        # Camera screen
        print_map(map[max(y2-2,0) : y2+3, max(x2-2,0) : x2+3])
