x = "compsci"

print repr (x [-3])
print repr (x[1:5])
# print repr (x[7])
# error because string index is out of range

x = "abcde"
# x -= x[0] 
# error because operand not associated with strings

x = "abcde"
x += x[::-1]
print x

def function (text, letter):
    newstring = ""
    position = 0
    while position < len (text):
        if ord (text [position]) < ord (letter):
            newstring += text [position]
            position += 1
        else:
            position += 1
    return newstring
        
print function ("abcde","d")
    
name = ("Jim, John, Jack,")

print name [:name.find(",")]
print name [name.find(",") + 1:]

print repr ("'\n")