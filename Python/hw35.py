# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW 35

# 1 accumulate a list

def splitStringIntoList (string):        
    newlist = []
    while string.find (' ') != -1:
        newlist.append (string [:string.find (' ')])
        string = string [string.find (' ') + 1:]
    return newlist
    
print splitStringIntoList ('Swaboda Jones Agee Grote Harrelson ')
# should be ['Swaboda', 'Jones', 'Agee', 'Grote', 'Harrelson']

def zip (integerlist, list1):
    finalstring = ''
    position = 0
    while position < len (list1):
        finalstring += str (integerlist [position]) + " " + str (list1 [position]) + "\n"
        position += 1
    return finalstring
    
print zip ([1, 2, 3] , ['james', 'bob', 'ben'])
        
    
    