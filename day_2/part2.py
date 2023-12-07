# -*- coding: utf-8 -*-

maxCubes = {'red': 12, 'green': 13, 'blue': 14}

def main():
    games = list()
    result = 0

    with open('./day_2/input.txt', 'r') as f:
        games = f.readlines()

    for i in range(len(games)):
        result = result + checkGame(game=games[i].strip().split(':')[1])
    print(result)


def checkGame(game: str) -> int:
    global maxCubes
    red = list()
    green = list()
    blue = list()

    
    gameSets = game.strip().split(';')
    for set in gameSets:
        hand = set.strip().split(',')
        for cubes in hand:
            cube = cubes.strip().split(' ')
            if cube[1].strip() == 'red':
                red.append(int(cube[0].strip()))
            if cube[1].strip() == 'green':
                green.append(int(cube[0].strip()))
            if cube[1].strip() == 'blue':
                blue.append(int(cube[0].strip()))

    return max(red) * max(green) * max(blue)


if __name__ == "__main__":
    main()
