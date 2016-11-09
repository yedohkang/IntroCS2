# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #18

def sumOfSquares (howMany):
    i = 0
    while howMany > 0:
        i = i + (howMany ** 2)
        howMany = howMany - 1
        return i

print sumOfSquares (5)
