# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #23

# 1. encryptCaesar

sequence = 'abcdefghijklmnopqrstuvwxyz'

def encryptCaesar (plaintext):
        AtPlain = sequence.find (plaintext)
        if AtPlain == -1:
            return plaintext
        else:
            AtCipher = (AtPlain - 3) % len (sequence)
            return sequence [AtCipher]
    
print encryptCaesar( 'g'), '...should be "d"'
print encryptCaesar( 'z'), '...should be "w"'  
print encryptCaesar( 'a'), '...should be "x"'  
print encryptCaesar( 'p'), '...should be "m"'  
print 


# 2. decryptCaesar

def decryptCaesar (ciphertext):
        AtCipher = sequence.find (ciphertext)
        if AtCipher == -1:
            return ciphertext
        else:
            plainAt = (AtCipher + 3) % len (sequence)
            return sequence[ plainAt]
    
print decryptCaesar( 'a'), '...should be "d"' 
print decryptCaesar( 'w'), '...should be "z"' 
print decryptCaesar( 'p'), '...should be "s"' 
print decryptCaesar( 'z'), '...should be "c"'  
print

print repr ('hi')
print repr (2)
