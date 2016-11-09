source = open ("macbeth.txt", "rU")
book = source.read().lower()
source.close()

tempbook = book.split()

book = []
for word in tempbook:
    book.append(word.strip("~`!@#$%^&*()_-+=|\}]{['""<,>.?/;:]}"))
    
count = {}
for word in book:
    count[word] = 0

for word in book:
    count[word] = count[word] + 1
    
countcopy = count
    
topwords = {}
for each in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    topword = 0
    for element in count:
        if countcopy [element] > topword:
            topword = countcopy[element]
            currentword = element
    topwords[each] = {currentword:topword}
    countcopy[currentword] = 0
    
for each in topwords:
    print each, ":", topwords[each]

