source = open("macbeth.txt","rU")
book = source.read().lower()
source.close()

symbols = "!@#$%^&*()_-=+[]{}|:;'\",.<>?/`~\\"

tempBook = book.split()

book = []
for word in tempBook:
    book.append(word.strip(symbols))

wordDict = {}
for word in book:
   wordDict[word] = 0
    
for word in book:
   wordDict[word] = wordDict[word] + 1
    
wordDictCopy = wordDict

topWords = {}
for each in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    currentTop = 0
    for element in wordDict:
        if wordDictCopy[element] > currentTop:
            currentTop = wordDictCopy[element]
            currentWord = element
    topWords[each] = {currentWord:currentTop}
    wordDictCopy[currentWord] = 0

print "Words and Their Count"
print wordDict
print "\n\n\n\n"
print "Top 10 Words and Their Count from 0: most to 9: tenth most"
for each in topWords:
    print each, ":", topWords[each]