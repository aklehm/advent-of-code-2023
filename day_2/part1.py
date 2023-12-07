# -*- coding: utf-8 -*-

maxCubes = {'red': 12, 'green': 13, 'blue': 14}

def main():
    games = list()
    result = 0


    with open('./day_2/input.txt', 'r') as f:
        games = f.readlines()
    
    for i in range(len(games)):
        # print(games[i].strip().split(':'))
        if checkGame(game=games[i].strip().split(':')[1]):
            result = result + (i+1)
    print(result)



def checkGame(game: str) -> bool:
    # print(game)
    global maxCubes
    gameSets = game.strip().split(';')
    for set in gameSets:
        hand = set.strip().split(',')
        for cubes in hand:
            cube = cubes.strip().split(' ')
            if int(cube[0].strip()) > maxCubes[cube[1].strip()]:
                return False
    return True
            

if __name__ == "__main__":
    main()

# 'Game 1: 2 green, 12 blue; 6 red, 6 blue; 8 blue, 5 green, 5 red; 5 green, 13 blue; 3 green, 7 red, 10 blue; 13 blue, 8 red'
