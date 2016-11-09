#! /usr/bin/python
print 'content-type: text/html\n'

import random

def choiceHomeCooked (list):
    n = len (list)
    return list [int (random.random() * n)]
    
def replaceholder (holder):
    weather = ["rainy", "sunny", "cloudy", "snowy", "stormy", "windy", "humid", "foggy"]
    if holder == "weather":
        return choiceHomeCooked (weather)
    
def weather ():
    source = open ("weather.txt" , 'rU')
    content = source.read ()
    source.close ()
    content = content.replace ('weather', replaceholder ('weather'))
    dest = open ('hw42_weather.py', 'w', 0)
    dest.write (content)
    return content
    dest.close ()
    
print weather ()
    