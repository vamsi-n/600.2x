__author__ = 'vnellore'

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    LSize = len(L)
    sumOfLengths = 0
    stringLengths = []

    for i in L:
        stringLength = len(i)
        sumOfLengths += stringLength
        stringLengths.append(stringLength)

    print sumOfLengths

    mean = sumOfLengths / float(LSize)

    print mean
    print stringLengths

    total = 0
    for j in stringLengths:
        total += (j - mean) ** 2

    total = total / len(stringLengths)

    stdDev = total ** 0.5
    return stdDev

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print stdDevOfLengths(L)
