# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #47

#0 5 and -6

#1 comp

#2 [0]

#3 [17, 'comp']

#4 []

#5 []

#6 Error because 42 is not in the list

#7 Error because 42 is not in the list

#8 None
# [1.618, [0], 'Stuy', 'comp', 'sci', 17, 42]

#9 h.append([42])
# print h

#10 h[1:2] = (7, 8)
# print h

#11
'''
def hush (file):
    source = open (file, 'rU')
    content = source.read()
    source.close()
    content = content.replace(".", "!")
    dest = open ((str ("hushed_" + file)), 'w', 0)
    dest.write(content)
    dest.close()
'''

#12
'''
One change that is required is the URL. There is the folder public_html written
as part of the URL, and with Apache, it is not supposed to be written because it automatically
looks in the public_html folder. Therefore, the correct URL should be
http://bart.stuy.edu/~dholmes/today/t1.py. Also, one other thing that should be 
fixed is the carriage return. Instead of tr '\n' '\r' < t0.py >t1.py it should be 
tr -d '\r' < t0.py > t1.py. Simply, the '\n' should be replaced by a -d. Lastly,
execution commands should be allowed, so in order for the browser to execute the 
file, you should do chmod +x t0.py because fixing the carriage return.
'''

#13 yes

#ec Edouard Lalo's Symphonie Espagnole Op. 21 Mvmts. 1 & 3
























