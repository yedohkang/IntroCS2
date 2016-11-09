# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #14

# 1. triangleArea
def triangleArea (base, height):
    return 0.5 * base * height
    
print triangleArea (4, 4)
# ...should be 8
print triangleArea (5, 2)
# ...should be 5
print triangleArea (3, 4)
# ...should be 6

# 2. 2 triangles
print triangleArea (3, 4) + triangleArea (4, 3)
# ...should be 12

# 3. distance
def distance (x0, y0, x1, y1):
    return (((x0 - y0) ** 2) + ((x1 - y1) ** 2)) ** 0.5

print distance (0, 0, 5, 3)
# ...should be 2
print distance (2, 2, 2, 2)
# ...should be 0
print distance (3, 3, 5, 9)
# ...should be 4

# 4. onLine
def onLine (x, y, slope, yintercept):
    return y == slope * x + yintercept
    
print onLine (0, 0, 2, 0)
# ...should be True
print onLine (0, 1, 2, 0)
# ...should be False
print onLine (1, 1, 2, 0)
# ...should be False    
    
# 5. onX
def onX (x, y):
    return y == x or y == -x

print onX (1, 1)
# ...should be True
print onX (1, -1)
# ...should be True
print onX (3, 4)
#... should be False

