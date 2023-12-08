# -*- coding: utf-8 -*-

def main():
    rawPartNumbers = list()
    positions = list()
    partNumbers = list()
    gearPositions = list()

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
    foundPositions = list()

    # print(gearPositions)



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

            # if i == (len(position[1])-1):
        if trailingGearPos != None:
            if upperGearPos:
                upperGearPos[1].append(trailingGearPos[1])
                possibleNumPos.append([gear[0]-1, trailingGearPos[1]])
            if lowerGearPos:
                lowerGearPos[1].append(trailingGearPos[1])
                possibleNumPos.append([gear[0]+1, trailingGearPos[1]])
        
        print(possibleNumPos)

        foundnumbers = 0
        for numPos in possibleNumPos:
            if rawPartNumbers[numPos[0]][numPos[1]].isnumeric():
                foundnumbers += 1
        
        print(foundnumbers)

        

        # if leadingGearPos != None:
        #     if rawPartNumbers[leadingGearPos[0]][leadingGearPos[1]] != '.' and not rawPartNumbers[leadingGearPos[0]][leadingGearPos[1]].isnumeric():
        #         foundPositions.append(gear)
        #         pnum = ''
        #         for i in gear[1]:
        #             pnum = pnum + rawPartNumbers[position[0]][i]
        #         partNumbers.append(int(pnum))
        # if trailingGearPos != None:
        #     if rawPartNumbers[trailingGearPos[0]][trailingGearPos[1]] != '.' and not rawPartNumbers[trailingGearPos[0]][trailingGearPos[1]].isnumeric():
        #         foundPositions.append(gear)
        #         pnum = ''
        #         for i in position[1]:
        #             pnum = pnum + rawPartNumbers[position[0]][i]
        #         partNumbers.append(int(pnum))
        # if upperPos:
        #     for i in upperPos[1]:
        #         pnum = ''
        #         if rawPartNumbers[upperPos[0]][i] != '.' and not rawPartNumbers[upperPos[0]][i].isnumeric():
        #             foundPositions.append(position)
        #             for j in position[1]:
        #                 pnum = pnum + rawPartNumbers[position[0]][j]
        #         if pnum != '':
        #             partNumbers.append(int(pnum))
        # if lowerPos:
        #     for i in lowerPos[1]:
        #         pnum = ''
        #         if rawPartNumbers[lowerPos[0]][i] != '.' and not rawPartNumbers[lowerPos[0]][i].isnumeric():
        #             foundPositions.append(position)
        #             for j in position[1]:
        #                 pnum = pnum + rawPartNumbers[position[0]][j]
        #         if pnum != '':
        #             partNumbers.append(int(pnum))

    # print(sum(partNumbers))


if __name__ == "__main__":
    main()
