# -*- coding: utf-8 -*-

def main():
    rawCards = list()
    points = 0
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
        
        print(winningNumbers)
        print(cardNumbers)
        
        for i in cardNumbers:
            if i in winningNumbers:
                counter += 1
        print(f'C: {counter}')
        print(f'P: {pow(2, counter-1)}')
        
        if counter > 0:
            points = points + pow(2, counter-1)
    
    print(points)
    

if __name__ == '__main__':
    main()