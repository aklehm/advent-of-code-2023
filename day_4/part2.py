# -*- coding: utf-8 -*-

def main():
    rawCards = list()
    winningcounter = list()
    with open('./day_4/input.txt', 'r') as f:
        rawCards = f.readlines()

    for card in rawCards:
        winningNumbers = list()
        cardNumbers = list()
        counter = 0

        for wNum in card.split(':')[1].strip().split('|')[0].strip().split(' '):
            if wNum.strip() != '':
                winningNumbers.append(wNum.strip())
        for cNum in card.split(':')[1].strip().split('|')[1].strip().split(' '):
            if cNum.strip() != '':
                cardNumbers.append(cNum.strip())

        # print(winningNumbers)
        # print(cardNumbers)

        for i in cardNumbers:
            if i in winningNumbers:
                counter += 1
        # print(f'C: {counter}')
        # print(f'P: {pow(2, counter-1)}')
        
        winningcounter.append(counter)

    totalCards = [0]

    for i in range(len(winningcounter)):
        if winningcounter[i] > 0:
            for j in range(1, winningcounter[i]+1, 1):
                if (i+j < len(totalCards)):
                    totalCards[i+j] += 1
                else:
                    totalCards.append(1)
    print(sum(totalCards))
    print(sum(winningcounter))
    # print(totalwinning)

    summe = 0
    for i in range(len(winningcounter)):
        summe = summe + winningcounter[i] + winningcounter[i] * totalCards[i]

    print(summe)

if __name__ == '__main__':
    main()
