# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #38
# Worked with Terry Guan and help from Levi Olevsky

#0 choiceHomeCooked

import random

def choiceHomeCooked (list):
    n = len (list)
    return list [int(random.random() * n)]

print choiceHomeCooked ([1, 2, 4, 5, 6])

#1 model flipping a coin

from fractions import Fraction

def flipsFraction (numberofflips):
    return Fraction ((1 / 2.0) ** numberofflips)

print flipsFraction (4)

#2 madLib

def replaceholder (holder):
    feeling = ["tired", "excited", "happy", "sad", "angry"]
    noun = ["school", "the mall", "the beach", "camp", "the city"]
    weather = ["snowing", "raining", "sunny", "drizzling", "hailing"]
    city = ["New York City", "Phoenix", "Boston", "Hanover", "Pittsburgh"]
    holiday = ["Christmas", "Thanksgiving", "Easter" , "Memorial Day", "birthday"]
    if holder == "FEELING":
        return choiceHomeCooked (feeling)
    if holder == "NOUN":
        return choiceHomeCooked (noun)
    if holder == "WEATHER":
        return choiceHomeCooked (weather)
    if holder == "CITY":
        return choiceHomeCooked (city)
    if holder == "HOLIDAY":
        return choiceHomeCooked (holiday)

def madLib ():
    source = open ("madlib.txt" , 'rU')
    content = source.read ()
    source.close ()
    print content
    content = content.replace ('FEELING', replaceholder ('FEELING'))
    content = content.replace ('NOUN', replaceholder ('NOUN'))
    content = content.replace ('WEATHER', replaceholder ('WEATHER'))
    content = content.replace ('CITY', replaceholder ('CITY'))
    content = content.replace ('HOLIDAY', replaceholder ('HOLIDAY'))
    dest = open ("MADLIBS.txt", 'w', 0)
    dest.write (content)
    return content
    dest.close ()
    
print madLib ()

    
    