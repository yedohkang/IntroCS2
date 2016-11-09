#! /usr/bin/python
print "content-type: text/html\n"

def getStringsOfLines(fileName):
    source = open(fileName, 'rU')
    content = source.read()
    source.close()
    newList = content.split('\n')
    return newList

def csvToDict(filename):
    listOfLines = getStringsOfLines(filename)
    metaData = listOfLines.pop(0)
    titles = metaData.split(',')
    dOL = {}
    for line in listOfLines:
        fieldList = line.split(',')
        nonIdFields = {}
        curField = 1
        while curField < len(fieldList):
            try:
                float(fieldList[curField])
                nonIdFields[titles[curField]] = float(fieldList[curField])
            except ValueError: 
                nonIdFields[titles[curField]] = fieldList[curField]
            curField += 1
        dOL[fieldList[0]] = nonIdFields
    return dOL

#print csvToDict (filename)

'''{'2016-05-17': {'lap_2': 16.0, 'lap_1': 15.0, 'lap_0': 14.0}, 
    '2016-05-16': {'lap_2': 19.0, 'lap_1': 18.0, 'lap_0': 11.0}, 
    '2016-05-20': {'lap_2': 'about 15', 'lap_1': 20.0, 'lap_0': 10.5}, 
    '2016-05-19': {'lap_2': 35.0, 'lap_1': '', 'lap_0': 12.0}, 
    '2016-05-18': {'lap_2': 17.0, 'lap_1': 18.0, 'lap_0': 12.5}}'''

datadictionary = csvToDict ("hw55.csv")

#Thanks Othman!

def floatify (listgiven):
    result = []
    for element in listgiven:
        try:
            result.append(float(element))
        except:
            pass
    return result
    
def averagemaker(data):
    for key in data:
        try:
            average = sum(floatify(data[key])) / len (data[key])
            data[key] = average
        except:
            pass
    return data
    
content = averagemaker (datadictionary)
print content


#def isfloat (value):
#    try:
#        if float (value) == True:
#            return value
#    except ValueError:
#        return 0
#
#valuenumber = 0
#summ = 0
#for value in datadictionary:
#    for value in datadictionary[value]:
#        isfloat (value)
#        summ += int(value)
#        print summ / 3
#    valuenumber += 1
    
def htmlTableMaker(content):
    string = ''
    for key in content:
        string += '<tr>' + '<td>' + key + '</td>' + '<td>' + str(content[key]) + '</td>' + '</tr>'
    string = "<!DOCTYPE html> <html> <head> <title> Average </title> </head> <body> <table border = '1'>" + string + "</table> </body> </html>"
    return string

print htmlTableMaker(content)