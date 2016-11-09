# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #31

# created a file

dest = open ('heidi.txt' , 'w' , 0)

content = dest.write ('my name is \n')
content = dest.write ('heidi wong')
print content

dest.close()
print dest

# reads the file

source = open ('heidi.txt' , 'rU')

heidi = source.read ()
print heidi

source.close()
print source

# rewrites

dest = open ('heidi.txt' , 'w' , 0)

content = dest.write ('raindrops \n')
content = dest.write ('shatter \n')
content = dest.write ('when they land \n')
content = dest.write ('on the silver fly screen')
print content

dest.close()
print dest

# reshows

source = open ('heidi.txt' , 'rU')

heidi = source.read ()
print heidi

source.close()
print source
