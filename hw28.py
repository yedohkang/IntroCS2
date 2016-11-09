# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #28
# Worked with Maddie Wong

# 1. replace

oldThink = "It's a long, long way to Tipperary"
oldThink = oldThink.replace ('long', 'LONG')
print oldThink 

# 2. Pirates of SCS

def your (string):
    string = string.replace (' your ',' yers ')
    return string
def you (string):
    string = string.replace (' you ',' ye ')
    string = string.replace (" you'",' ye')
    return string
def the (string):
    string = string.replace (' the '," t' ")
    return string
def ing (string):
    string = string.replace ('ing ',"in' ")
    return string
def I (string):
    string = string.replace (' I ',' me ')
    return string
def my (string):
    string = string.replace (' my ',' me ')
    return string
def mine (string):
    string = string.replace (' mine ',' me ')
    return string
def am (string):
    string = string.replace (' am ',' be ')
    return string
def iss (string):
    string = string.replace (' is ',' be ')
    return string
def are (string):
    string = string.replace (' are ',' be ')
    return string
def re (string):
    string = string.replace (" re ",' be ')
    return string
def myself (string):
    string = string.replace (' myself',' meself')
    return string
def forr (string):
    string = string.replace (' for ',' fer ')
    return string   
    
#Helper Function for endofSentence for Arrr!:
def endofSentenceArrr(string):
    string = string.replace("." , "!" , 1)
    return string
    
#For Arrr! after every other sentence (Thanks to Adeebur Rahman)
def Arrr(string):
    i = 0
    arrr = 0
    while string.find(".") != -1:
        i = string.find(".") + 1
        string = endofSentenceArrr(string)
        arrr += 1
        if arrr % 2 == 0:
            string = string[:i:] + " Arrr!" + string[i::]
    return string
     
def translatetopirate (string):
    string = your (string)
    string = you (string)
    string = the (string)
    string = ing (string)
    string = I (string)
    string = my (string)
    string = mine (string)
    string = am (string)
    string = iss (string)
    string = are (string)
    string = re (string)
    string = myself (string)
    string = forr (string)
    string = Arrr (string)
    return string
    
print translatetopirate ("Sorry to disappoint you and all that, but the greatest wizard in the world is Albus Dumbledore. Everyone says so. Even when you were strong, you didn't dare try and take over at Hogwarts. Dumbledore saw through you when you were at school and he still frightens you now, wherever you're hiding these days.")
# ... should be Sorry to disappoint ye and all that, but t' greatest wizard in t' world be Albus Dumbledore! Everyone says so! Arrr! Even when ye were strong, ye didn't dare try and take over at Hogwarts! Dumbledore saw through ye when ye were at school and he still frightens ye now, wherever ye be hidin'these days! Arrr!
print translatetopirate (" Hello, it's me I was wondering if after all these years you'd like to meet To go over everything They say that time's supposed to heal ya But I ain't done much healing Hello, can you hear me? I'm in California dreaming about who we used to be When we were younger and free I've forgotten how it felt before the world fell at our feet There's such a difference between us And a million miles Hello from the other side I must have called a thousand times To tell you I'm sorry for everything that I've done But when I call you never seem to be home Hello from the outside At least I can say that I've tried To tell you I'm sorry for breaking your heart But it don't matter. It clearly doesn't tear you apart anymore")

