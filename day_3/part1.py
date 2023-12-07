# -*- coding: utf-8 -*-


def main():
    rawPartNumbers = list()
    positions = list()
    partNumbers = list()
    result = 0

    with open('./day_3/input.txt', 'r') as f:
        rawPartNumbers = f.readlines()
    
    print(len(rawPartNumbers[0]))

    
    for i in range(len(rawPartNumbers)):
        # print(i)
        foundNumber = False
        for j in range(len(rawPartNumbers[i])):
            # print(j)
            if rawPartNumbers[i][j].isnumeric():
                # print(f'isNumeric: {i}|{j}')
                if foundNumber:
                    positions[-1][1].append(j)
                else:
                    positions.append([i, [j]])
                    foundNumber = True
            else:
                foundNumber = False
        # print(positions)
    foundPositions = list()

    for position in positions:
        # print(position)
        leadingPos = None
        trailingPos = None
        upperPos = None
        lowerPos = None
        if position[1][0]-1 >= 0:
            leadingPos = [position[0],position[1][0]-1]
        # print(position[1][-1]+1)
        # print(len(rawPartNumbers[0]))
        if position[1][-1]+1 <= len(rawPartNumbers[0]):
            trailingPos = [position[0],position[1][-1]+1]
        if position[0]-1 >= 0:
            upperPos = [position[0]-1, []]
        if position[0]+1 < len(rawPartNumbers):
            lowerPos = [position[0]+1, []]

        if leadingPos != None and upperPos:
            upperPos[1].append(leadingPos[1])
        if leadingPos and lowerPos:
            lowerPos[1].append(leadingPos[1])

        for i in range(len(position[1])):
            if upperPos:
                upperPos[1].append(position[1][i])
            if lowerPos:
                lowerPos[1].append(position[1][i])

            # if i == (len(position[1])-1):
        if trailingPos != None:
            if upperPos:
                upperPos[1].append(trailingPos[1])
            if lowerPos:
                lowerPos[1].append(trailingPos[1])


        # print(leadingPos)
        # print(trailingPos)
        # print(upperPos)
        # print(lowerPos)
        # print('')
        

        if leadingPos != None:
            if rawPartNumbers[leadingPos[0]][leadingPos[1]] != '.' and not rawPartNumbers[leadingPos[0]][leadingPos[1]].isnumeric():
                foundPositions.append(position)
                # print('leading')
                pnum = ''
                for i in position[1]:
                    pnum = pnum + rawPartNumbers[position[0]][i]
                partNumbers.append(int(pnum))
                # break
        if trailingPos != None:
            if rawPartNumbers[trailingPos[0]][trailingPos[1]] != '.' and not rawPartNumbers[trailingPos[0]][trailingPos[1]].isnumeric():
                foundPositions.append(position)
                # print('trailing')
                pnum = ''
                for i in position[1]:
                    pnum = pnum + rawPartNumbers[position[0]][i]
                partNumbers.append(int(pnum))
                # break
        if upperPos:
            for i in upperPos[1]:
                pnum = ''
                if rawPartNumbers[upperPos[0]][i] != '.' and not rawPartNumbers[upperPos[0]][i].isnumeric():
                    foundPositions.append(position)
                    # print('upperpos')                    
                    for j in position[1]:
                        pnum = pnum + rawPartNumbers[position[0]][j]
                if pnum != '':
                    partNumbers.append(int(pnum))
                # break
        if lowerPos:
            for i in lowerPos[1]:
                pnum = ''
                if rawPartNumbers[lowerPos[0]][i] != '.' and not rawPartNumbers[lowerPos[0]][i].isnumeric():
                    foundPositions.append(position)
                    # print('lowerpos')
                    for j in position[1]:
                        pnum = pnum + rawPartNumbers[position[0]][j]
                if pnum != '':
                    partNumbers.append(int(pnum))
                # break
    # print(partNumbers)
    print(len(foundPositions))
    print(len(positions))
    
    for i in partNumbers:
        result = result + i
    print (sum(partNumbers))
    print(result)


        



if __name__ == "__main__":
    main()

