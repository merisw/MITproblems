import pylab
import string

def getWords():
    wordFile = open('words.txt', 'r', 0)
    line = wordFile.readline()
    wordlist = string.split(line)
    freq = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
            'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
            'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
            'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    for word in wordlist:
        freq[word[0]] += 1
    print freq
    
    freqList = []
    for letter in freq:
        freqList += freq[letter]
    print freqList
    return freqList
    
def wordPlot(freqList):   
    pylab.plot(range(1, 27), freqList)
    pylab.title('Problem 3 Wordlist: Frequency of Words by First Letter')
    pylab.xlabel('Letter in the Alphabet, ex: a=1')
    pylab.ylabel('Number of Words in Wordlist 3 beginning with Letter')
    pylab.show()

freq = [3344, 3610, 5203, 3422, 2279, 2645, 2042, 1977, 1729, 586, 454, 1858, 2821, 989, 1317, 4259, 288, 3185, 6795, 2952, 1326, 980, 1510, 17, 179, 133]

wordPlot(freq)
    
