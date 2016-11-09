# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #15

# 1. onX reprise

def onLine (x, y, slope, yintercept):
    return y == slope * x + yintercept
    
# tests ommitted

def onXreprise (x, y):
    return onLine (x, y, 1, 0) or onLine (x, y, -1, 0)
    
print onXreprise (0, 0)
# ...should be True
print onXreprise (1, 1)
# ...should be True
print onXreprise (-1, 1)
# ...should be True
    
    
# 2. autotip

def autotip (people):
    if people >= 8:
        return 0.18
    else:
        return 0
        
print autotip (8)
# ...should be 0.18
print autotip (4)
# ...should be 0
print autotip (16)
# ...should be 0.18

# 3. absolute value

def absHomeCooked (number):
    if number >= 0:
        return number
    else:
        return -number
        
print absHomeCooked (5)
# ...should be 5
print absHomeCooked (-5)
# ...should be 5
print absHomeCooked (0)
# ...should be 0

# 4. autotip_4way

def autotip_4way (people):
    if people >= 12:
        return 0.25
    elif people >= 8:
        return 0.18
    elif people >= 4:
        return 0.15
    else:
        return 0

print autotip_4way (12)
# ...should be 0.25
print autotip_4way (8)
# ...should be 0.18
print autotip_4way (4)
# ...should be 0.15
print autotip_4way (2)
# ...should be 0