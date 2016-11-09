# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #24

# 1. encrypt and decrypt longer strings

sequence = 'abcdefghijklmnopqrstuvwxyz'
 
def encryptCaesar (plaintext):
    plainAt = sequence.find (plaintext)
    if plainAt == -1:
        return plaintext
    else:
        cipherAt = (plainAt - 3) % len (sequence)
        return sequence [cipherAt]
    
def decryptCaesar (ciphertext):
    cipherAt = sequence.find (ciphertext)
    if cipherAt == -1:
        return ciphertext
    else:
        plainAt = (cipherAt + 3) % len (sequence)
        return sequence [plainAt]

def encryptMany (string):
    ords = ''
    position = 0
    while position < len (string):
        ords = ords + str (encryptCaesar (string [position]))
        position = position + 1
    return ords
    
print encryptMany ('abcde')
# ... should be xyzab

def decryptMany (string):
    ords = ''
    position = 0
    while position < len (string):
        ords = ords + str (decryptCaesar (string [position]))
        position = position + 1
    return ords

print decryptMany ('abcde')
# ... should be defgh
    


# 2. revisit test 1

# 1

def cupOunces (character):
    if character == 'Hal':
        drinkOz = 8
    elif character == 'Poins':
        drinkOz = 12
    elif character == 'Falstaff':
        drinkOz = 16
    else:
        return -1
    return drinkOz + 2

print cupOunces ('Hal')
# ... should be 10
print cupOunces ('Bardolf')
# ... should be -1

# 4

def foot (numofdashes, text):
    return '-' * numofdashes + ' ' + text + ' '+ '-' * numofdashes
    
print foot (10, 'comp sci intro 2')
# ... should be ---------- comp sci intro 2 ----------
