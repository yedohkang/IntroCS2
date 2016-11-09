# Yedoh Kang <kang.yedoh@gmail.com> Period 6
# HW #29
# Help from Piazza

def arrrify (string, n):
    currentstring = string
    finalstring = ''
    i = 0
    while currentstring.find (".") != -1:
        finalstring = finalstring + currentstring [:currentstring.find(".") + 1]
        currentstring = currentstring [currentstring.find(".") + 1:]
        i += 1
        if i % n == 0:
            finalstring = finalstring + " Arrr!"
    return finalstring
    
print arrrify ('this is yedoh. yes. this is she. i can tell you.', 3)