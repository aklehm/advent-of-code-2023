# -*- coding: utf-8 -*-


def main():
    rawPartNumbers = list()
    positions = list()
    partNumbers = list()
    result = 0

    with open('./day_3/input.txt', 'r') as f:
        rawPartNumbers = f.readlines()
    
    for i in range(len(rawPartNumbers)):
        foundNumber = False
        for j in range(len(rawPartNumbers[i])):
            if rawPartNumbers[i][j].isnumeric():
                if foundNumber:
                    positions[-1][1].append(j)
                else:
                    positions.append([i, [j]])
                    foundNumber = True
            else:
                foundNumber = False

    for position in positions:
        print(position)
        leadingPos = None
        trailingPos = None
        upperPos = None
        lowerPos = None
        if position[1][0]-1 >= 0:
            leadingPos = [position[0],position[1][0]-1]
        if position[1][-1]+1 < len(rawPartNumbers[0]):
            trailingPos = [position[0],position[1][-1]+1]
        if position[0]-1 >= 0:
            upperPos = [position[0]-1, []]
        if position[0]+1 < len(rawPartNumbers):
            lowerPos = [position[0]+1, []]

        if leadingPos != None and upperPos:
            upperPos[1].append(leadingPos[1])

        for i in range(len(position[1])):
            if upperPos:
                upperPos[1].append(position[1][i])
            if lowerPos:
                lowerPos[1].append(position[1][i])

            if i == (len(position[1])-1):
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

        print(rawPartNumbers[leadingPos[0]][leadingPos[1]])
    #     if rawPartNumbers[leadingPos[0]][leadingPos[1]] != '.':
    #         pnum = ''
    #         for i in position[1]:
    #             pnum = pnum + rawPartNumbers[position[0]][i]
    #         partNumbers.append(int(pnum))
    #         break

    #     for i in upperPos[1]:
    #         if rawPartNumbers[upperPos[0]][i] != '.':
    #             pnum = ''
    #             pnum = pnum + rawPartNumbers[upperPos[0]][i]
    #         partNumbers.append(int(pnum))
    #         break

    #     for i in lowerPos[1]:
    #         if rawPartNumbers[lowerPos[0]][i] != '.':
    #             pnum = ''
    #             pnum = pnum + rawPartNumbers[lowerPos[0]][i]
    #         partNumbers.append(int(pnum))
    #         break

    # for i in partNumbers:
    #     result = result + i
    
    # print(result)


        



if __name__ == "__main__":
    main()

