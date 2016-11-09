def sumOfSquares (howMany):
    acc = 0
    count = 0
    while count < howMany:
        acc = acc + count * count
        print acc
        count = count + 1

print sumOfSquares (5)
    