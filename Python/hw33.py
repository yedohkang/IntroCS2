# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #33

# module and function
#import hw32_filePirating
#print hw32_filePirating.prateLikeAPirate ('you are me asfdkj bye . sdf. df.')

def translatetopirate (file):
    source = open (file, 'rU') # opens the file, bound to source
    text = source.read () # reads the file and binds content to 'text'
    source.close() # closes the file
    dest = open (file, 'w', 0) # file is opened, but bound to dest
    import hw32_filePirating
    result = dest.write (hw32_filePirating.prateLikeAPirate (text))
    dest.close()
    source = open (file, 'rU')
    text = source.read()
    source.close()
    return text
    
#print translatetopirate ('jkrowling.txt')

