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

def computeMean(inputs):

    if len(inputs) == 0:
        return float("NaN")

    total = 0
    for i in inputs:
        total += i

    mean = float(total) / float(len(inputs))

    return mean

def computeVariance(inputs):

    mean = computeMean(inputs)
    variance = 0
    for i in inputs:
        variance += (i - mean) ** 2

    return variance

def stdDeviation(inputs):

    total = 0
    for i in inputs:
        total += i

    mean = computeMean(inputs)

    variance = computeVariance(inputs)

    standardDeviation = (variance / len(inputs))  ** 0.5

    return standardDeviation

def coefficientOfVariation(inputs):

    mean = computeMean(inputs)
    standardDeviation = stdDeviation(inputs)

    return float(standardDeviation) / float(mean)

L = ['apples', 'oranges', 'kiwis', 'pineapples']

#print stdDeviation([10, 4, 12, 15, 20, 5])
print "Coefficient of Variation - ", coefficientOfVariation([10, 4, 12, 15, 20, 5])

