#{ 
#  1922 : {'Tm' : 'NYY',  'PA' : 496 ...} ,
#  1914 : {'Tm' : 'BOS',  'PA' :  10 ...} ,
#  ...
#}

def getStringsOfLines (fileName):
    source = open (fileName, 'rU')
    content = source.read()
    source.close()
    newList = content.split('\n')
    return newList

stringsOfLines = getStringsOfLines("babe.csv")

metaData = stringsOfLines.pop(0)

def listToDict (listOfLines):
    dictOfStats = {}
    for yearlyStats in listOfLines:
        listOfStats = yearlyStats.split(',')
        dictOfStats[listOfStats[0]] = { 'Tm': listOfStats [1], 'PA' : listOfStats[2], 'AB' : listOfStats[3], 'R' : listOfStats[4], 'H' : listOfStats[5], '2B' : listOfStats[6], '3B' : listOfStats[7], 'HR' : listOfStats[8],}
    return dictOfStats

dictOfLines = listToDict (stringsOfLines)
print dictOfLines

def total(dict):
    newKey = {'PA' : 0, 'AB' : 0, 'R'  : 0, 'H'  : 0, '2B' : 0, '3B' : 0, 'HR' : 0,}
    for years in dict:
        newKey['PA'] += int(dict[years]['PA'])
        newKey['AB'] += int(dict[years]['AB'])
        newKey['R'] += int(dict[years]['R'])
        newKey['H'] += int(dict[years]['H'])
        newKey['2B'] += int(dict[years]['2B'])
        newKey['3B'] += int(dict[years]['3B'])
        newKey['HR'] += int(dict[years]['HR'])
    dict['total'] = newKey    
    return dict


print total(dictOfLines)['total']