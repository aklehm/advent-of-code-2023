# -*- coding: utf-8 -*-

def main():
    rawPartNumbers = list()
    positions = list()
    gearPositions = list()
    gearRatios = list()

    with open('./day_3/input.txt', 'r') as f:
        rawPartNumbers = f.readlines()

    for i in range(len(rawPartNumbers)):
        foundNumber = False
        for j in range(len(rawPartNumbers[i])):
            if rawPartNumbers[i][j] == '*':
                gearPositions.append([i, j])
            if rawPartNumbers[i][j].isnumeric():
                if foundNumber:
                    positions[-1][1].append(j)
                else:
                    positions.append([i, [j]])
                    foundNumber = True
            else:
                foundNumber = False
    

    for i in range(len(positions)):
        pnum = ''
        for j in positions[i][1]:
            pnum = pnum + rawPartNumbers[positions[i][0]][j]
        positions[i].append(pnum)
    

    for gear in gearPositions:
        leadingGearPos = None
        trailingGearPos = None
        upperGearPos = None
        lowerGearPos = None
        possibleNumPos = list()

        if gear[1]-1 >= 0:
            leadingGearPos = [gear[0], gear[1]-1]
            possibleNumPos.append(leadingGearPos)
        if gear[1]+1 <= len(rawPartNumbers[0])-2:
            trailingGearPos = [gear[0], gear[1]+1]
            possibleNumPos.append(trailingGearPos)
        if gear[0]-1 >= 0:
            upperGearPos = [gear[0]-1, []]

        if gear[0]+1 < len(rawPartNumbers):
            lowerGearPos = [gear[0]+1, []]

        if leadingGearPos != None and upperGearPos:
            upperGearPos[1].append(leadingGearPos[1])
            possibleNumPos.append([gear[0]-1, leadingGearPos[1]])
        if leadingGearPos and lowerGearPos:
            lowerGearPos[1].append(leadingGearPos[1])
            possibleNumPos.append([gear[0]+1, leadingGearPos[1]])

        if upperGearPos:
            upperGearPos[1].append(gear[1])
            possibleNumPos.append([gear[0]-1, gear[1]])
        if lowerGearPos:
            lowerGearPos[1].append(gear[1])
            possibleNumPos.append([gear[0]+1, gear[1]])

        if trailingGearPos != None:
            if upperGearPos:
                upperGearPos[1].append(trailingGearPos[1])
                possibleNumPos.append([gear[0]-1, trailingGearPos[1]])
            if lowerGearPos:
                lowerGearPos[1].append(trailingGearPos[1])
                possibleNumPos.append([gear[0]+1, trailingGearPos[1]])
        
        foundcounter = 0
        foundNumbers = list()


        if leadingGearPos:
            if  rawPartNumbers[leadingGearPos[0]][leadingGearPos[1]].isnumeric():
                foundcounter += 1
                for pos in positions:
                    if leadingGearPos[0] == pos[0] and leadingGearPos[1] == pos[1][-1]:
                        foundNumbers.append(pos[2])
        
        if trailingGearPos:
            if rawPartNumbers[trailingGearPos[0]][trailingGearPos[1]].isnumeric():
                foundcounter += 1
                for pos in positions:
                    if trailingGearPos[0] == pos[0] and trailingGearPos[1] == pos[1][0]:
                        foundNumbers.append(pos[2])
        
        foundUpper = list()
        if upperGearPos:
            for u in upperGearPos[1]:
                if rawPartNumbers[upperGearPos[0]][u].isnumeric():
                    for pos in positions:
                        if upperGearPos[0] == pos[0]:
                            for i in pos[1]:
                                if u == i and pos[2] not in foundUpper:
                                    foundUpper.append(pos[2])

        foundLower = list()
        if lowerGearPos:
            for l in lowerGearPos[1]:
                if rawPartNumbers[lowerGearPos[0]][l].isnumeric():
                    for pos in positions:
                        if lowerGearPos[0] == pos[0]:
                            for i in pos[1]:
                                if l == i and pos[2] not in foundLower:
                                    foundLower.append(pos[2])
        
        
        for i in foundUpper:
            foundNumbers.append(i)

        for i in foundLower:
            foundNumbers.append(i)
        

        if len(foundNumbers) == 2:
            gearRatios.append(int(foundNumbers[0]) * int(foundNumbers[1]))
    
    print(sum(gearRatios))


if __name__ == "__main__":
    main()
