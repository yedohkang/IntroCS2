def before (text, letter):
    early = ''
    for letters in text:
        if letters < letter:
            early += letters
    return early
    
print before ('abtp', 'm')
#should be ab

list = ['a', 'b', 42]
for elements in list:
    print elements

string = 'abcd'
for char in string:
    print char
    
source = open ("template.py", "rU")
linenumber = 0
for line in source:
    print line
    linenumber += 1