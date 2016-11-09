# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #33 html part

'''
0. open the template
1. read it and bind it to a variable
2. replace the title
3. open the text i want to change
4. read it and bind it to a variable
5. import hw33
6. replace body with the changed landlubber text
7. create a new html file
8. write the html
'''

template = open ('hw33_template.html' , 'rU')
html = template.read ()
template.close ()

print html 
print

html = html.replace ('titleGoesHere' , 'Pirafy!')
print html
print

source = open ('hw32_landlubberTalk.txt' , 'rU')
landlubberTalk = source.read ()
source.close ()

import hw33_prateLikeAPirate_module
html = html.replace ('bodyGoesHere' , hw33_prateLikeAPirate_module.prateLikeAPirate (landlubberTalk))

dest = open ('hw33_piratesOnTheWeb.html' , 'w' , 0)
dest.write (html)
dest.close ()

