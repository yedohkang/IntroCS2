d = {}
print 'initialized:', d

d[0] = 'some letters'
d[-11] = 17
print 'after some assignments:', d
print 'just one:', d[-11]

d['a string!'] = 17
v = 'another'
d[v] = ['hello', 'world']
print 'after more assignments:', d

#1
print d[-11] # 17
print d['a string!'] # 17
print d[v] # ['hello', 'world]
print d[v][0] # hello
print d[0][0:4] # some

#2
valuenumber = 0
for value in d:
    print d[value]
    valuenumber += 1
    
#3
def keys (dictionary):
    final = []
    for keys in dictionary:
        final.append(keys)
    return final
    
print keys (d)




