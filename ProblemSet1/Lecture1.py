__author__ = 'vnellore'

import pylab


def plotPrincipalTrend():
    principal = 10000
    interestRate = 0.05
    years = 20
    values = []

    for i in range(years + 1):
        values.append(principal)
        principal += principal * interestRate

    pylab.plot(values)
    pylab.title('5% growth, compounded annually')
    pylab.xlabel('Years of compounding')
    pylab.ylabel('Principal')
    pylab.show()

def readJulyTemps():

    try:
        lines = [line.strip('\n') for line in open('julyTemps.txt')]
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)
        lines.pop(0)


    except IOError:
        raise IOError

    return lines

from decimal import *

def plotJulyTempDiff():
    fileContent = readJulyTemps()

    highTemps = []
    lowTemps = []
    diff = []

    for currentLine in fileContent:
        line = currentLine.split(' ')

        highDecimal = Decimal(line[1])
        lowDecimal = Decimal(line[2])

        highTemps.append(highDecimal)
        lowTemps.append(lowDecimal)
        diff.append(abs(highDecimal - lowDecimal))



    print highTemps
    print lowTemps
    print diff
    pylab.plot(diff)
    pylab.show()

plotJulyTempDiff()