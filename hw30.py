# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #30

# create a file object
text = open ('heidi.txt','rU')
print text

# read contents
heidi = text.read()

# display contents
print heidi

# signal done!
text.close()
print text