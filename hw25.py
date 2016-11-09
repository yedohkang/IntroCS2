# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #25


def cheer (string):
    position = 0
    outcome = ' '
    while position < len (string):
        if string [position] == " ":
            outcome = outcome + "Gimme a space, the final frontier" + "\n"
        elif string [position] == "\n":
            outcome = outcome + "Gimme a new line, please" + "\n"
        else:
            outcome = outcome + "Gimme a " + string [position] + "\n"
        position = position + 1
    return outcome
    
print cheer ("CS")
# ... should be Gimme a C \n Gimme a S
print cheer ("CS  \n")
# ... should be Gimme a C \n Gimme a S \n Gimme a space, the final frontier \n Gimme a space, the final frontier \n Gimme a new line, please
print cheer ('ABC \n')
# ... should be Gimme an A \n Gimme a B \n Gimme a C \n Gimme a space, the final frontier \n Gimme a new line, please
            
            