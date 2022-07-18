import numpy
import json

with open('words_dictionary.json') as f:
    dict = json.load(f)
    list = dict.keys()
    sList = sorted(list)
def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2 - 1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1
    return distances[len(token1)][len(token2)]


def callDictDist(word, numWords):

    dictWordDist = []
    wordIdx = 0

    for key in sList:
        wordDistance = levenshteinDistanceDP(word, key)
        if wordDistance >= 10:
            wordDistance = 9
        dictWordDist.append(str(int(wordDistance)) + "-" + key)
        wordIdx = wordIdx + 1

    closestWords = []
    wordDetails = []
    currWordDist = 0
    dictWordDist.sort()
    for i in range(numWords):
        currWordDist = dictWordDist[i]
        wordDetails = currWordDist.split("-")
        closestWords.append(wordDetails[1])
    print(word + ' not found. Suggestions:', end= ' ')
    for i in closestWords[:-1]:
        print(i,end=', ')
    print(closestWords[-1])


inpline = input('Type word you want to check: ')
for words in inpline:
    words = inpline.split()
for word in words:
    if word in sList:
        print(word + ' is spelled correctly')
    else:
        callDictDist(word, 8)