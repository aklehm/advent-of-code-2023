# -*- coding: utf-8 -*-

def main() -> None:

    rawlines = list()

    with open('./day_1/input.txt', 'r') as f:
        rawlines = f.readlines()

    numberStrings = list()

    for line in rawlines:
        numString = ''
        for i in range(len(line)):
            try:
                a = int(line[i])
                numString = numString + str(a)
            except Exception as e:
                pass
        if numString != '':
            numString = numString[0] + numString[-1]
            numberStrings.append(numString)
        

    numbers = list()

    if len(numberStrings) == 1000:
        for number in numberStrings:
            numbers.append(int(number))
    else:
        print(f'Länge falsch: {len(numberStrings)}')

    result = 0

    for i in numbers:
        result = result + i

    print(result)


if __name__ == "__main__":
    main()
