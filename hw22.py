# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #23

#1 firstName

def firstName (name):
    i = 0
    fname = ''
    while i != name.find (' '):
        fname = fname + name [i]
        i = i + 1
    return fname


print firstName ('James Smith')
# ... should be James
print firstName ('blah blah')
# ... should be blah

#2 lastName

def lastName (name):
    i = len (name) - 1
    lname = ''
    while i > name.find (' '):
        lname = name [i] + lname
        i = i - 1
    return lname

print lastName ('Brian Kernighan')
# ... should be Kernighan
print lastName ('James Smith')
# ... should be Smith

#3 Bondify

def Bondify (name):
    print lastName (name),'.', name
    
print Bondify ('Brian Kernighan')