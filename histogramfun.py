import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList


def get_number_of_vowels(input):
    vowels = ['a','e','i','o','u']

    count = 0
    for i in input:
        if i in vowels:
            count += 1

    return count

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    print len(wordList)

    n = 0
    vowel_proportion = []
    for current_word in wordList:

        word_length = len(current_word)
        vowel_count = get_number_of_vowels(current_word)

        vowel_proportion.append(float(vowel_count) /float(word_length))

    plotHistogram(vowel_proportion)

def plotHistogram(values_to_plot):

    pylab.hist(values_to_plot, bins = 10)
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
