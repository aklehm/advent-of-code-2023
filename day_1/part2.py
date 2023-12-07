# -*- coding: utf-8 -*-

def replaceNumberstrings(numberString: str) -> str:
    numstr = numberString
    result = ''
    strings = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for i in range(len(numberString)):
        a = numstr[i:]
        if a[0].isnumeric():
            result = result + a[0]
        for b in strings.keys():
            if a.startswith(b):
                result = result + strings[b]
    return result


def main() -> None:
    rawlines = list()

    with open('./day_1/input.txt', 'r') as f:
        rawlines = f.readlines()

    numberStrings = list()
    cnt =0

    for line in rawlines:
        cnt += 1
        numString = ''
        numline = replaceNumberstrings(line)
        for i in range(len(numline)):
            try:
                a = int(numline[i])
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
        print(f'Error: wrong length: {len(numberStrings)}')

    result = 0

    for i in numbers:
        result = result + i

    print(result)

if __name__ == "__main__":
    main()