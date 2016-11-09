# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #26
# Help from Benjamin Shen and Piazza

def wordsVertically (string):
    result = ''
    while string.find (' ') != -1: # while there is a space in the string
        result += string [:string.find (' ')] + "\n"
        string = string [string.find (' ') + 1:] # update the string to the new string
    return result [:len (result) - 1]
    
print wordsVertically ('ab cd e ')
# ... should be
#ab
#cd
#e
print wordsVertically ('a b')
# ... should be
#a
print wordsVertically ('\n   ')
# ... should be
#
#
#