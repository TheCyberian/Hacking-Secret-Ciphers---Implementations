import pprint


def getWordPattern(word):
# Returns a string of the pattern form of the given word.
# e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'
    word = word.upper()
    nextNum = 0
    letterNums = {}
    wordPattern = []
    for letter in word:
        if letter not in letterNums:
            letterNums[letter] = str(nextNum)
            nextNum += 1
        wordPattern.append(letterNums[letter])
    return '.'.join(wordPattern)

"""
This seems like a straightforward way to do this. However, it is very inefficient for Python to concatenate strings.
The reasons are technical and beyond the scope of this book, but it is much faster to start with a blank list instead
of a blank string, and then use the append() list method instead of string concatenation. After you are done building
the list of strings, you can convert the list of strings to a single string value with the join() method.
"""

def main():
    allPatterns = {}
    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    fo.close()
    for word in wordList:
        pattern = getWordPattern(word)
        if pattern not in allPatterns:
            allPatterns[pattern] = [word]
        else:
            allPatterns[pattern].append(word)
# This is code that writes code. The wordPatterns.py file contains
# one very, very large assignment statement.
    fo = open('wordPatterns.py', 'w')
    fo.write('allPatterns = ')
    fo.write(pprint.pformat(allPatterns))
    fo.close()


if __name__ == '__main__':
    main()
