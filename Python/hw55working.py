#! /usr/bin/python

#import cgitb
#cgitb.enable()

print 'content-type: text/html\n\r'

def readFile(filename):
    source = open(filename, "rU")
    data = source.read()
    source.close()
    data = data.split('\n')
    meme = []
    for line in data:
        meme.append(line.split(','))
    return meme

#print readFile('hw55_data.csv')

listOfLines = readFile('hw55.csv')
#print listOfLines
del listOfLines[0]
#print listOfLines

def csvToDict(meme):
    dictionary = {}
    for line in meme:
        dictionary[line[0]] = line[1:]
    return dictionary

#print csvToDict(listOfLines)
mememachine = csvToDict(listOfLines)

def floatify(listmeme):
    result = []
    for element in listmeme:
        try:
            result.append(float(element))
        except:
            pass
    return result

def averageMaker(data):
    for key in data:
        try:
            average = sum(floatify(data[key])) / len(data[key])
            data[key] = average
        except:
            pass
    return data

#print averageMaker(mememachine)
stuff = averageMaker(mememachine)
del stuff['']
print stuff

def htmlTableMaker(dream):
    string = ''
    for key in dream:
        string += '<tr>' + '<td>' + key + '</td>' + '<td>' + str(dream[key]) + '</td>' + '</tr>'
    string = "<!DOCTYPE html> <html> <head> <title> Average </title> </head> <body> <table border = '1'>" + string + "</table> </body> </html>"
    return string

print htmlTableMaker(stuff)