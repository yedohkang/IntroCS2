# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #27
# Worked with Gabi Newman and help from Piazza & Ben Shen

# 1. rfind, home-cooked

def rfind (letter, string):
    last = string[::-1].find(letter)
    return len (string) - 1 - last

print rfind ('o', 'hello world')
# ... should be 7
print rfind ('b', 'bubble')
# ... should be 3

# 2. replaceOne

def replaceOne (text, lookFor, replaceWith):
    start = text.find (lookFor)
    if start != -1:
        end = start + len (lookFor)
        text = text [:start] + replaceWith + text [end:]
    return text 
    
print replaceOne ('I love comp sci', 'love', 'dislike')
# ... should be I dislike comp sci. 
# on a side note, I like comp sci!

# 3. replaceAll

def replaceAll (text, lookFor, replaceWith):
    while text.find (lookFor) != -1:
        text = replaceOne (text, lookFor, replaceWith)
    return text
    
print replaceAll ('bubble','b','p')
# ... should be pupple

