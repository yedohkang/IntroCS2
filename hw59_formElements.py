#! /usr/bin/python
# process a form that has 2 submit buttons

import cgitb
cgitb.enable()

import cgi
fromClient = cgi.FieldStorage()

print 'content-type: text/html\n'

# start a standards-conforming web page
import hw55_htmlFunctions
print hw55_htmlFunctions.htmlSetup()
print hw55_htmlFunctions.element( True, 0, 'h1', '',
                                  'FieldStorage data')

print hw55_htmlFunctions.element( True, 0, 'h2', '',
  'Show the parts of the FieldStorage structure')

for key in fromClient: # just like a dictionary
    print key + ': ' + fromClient[key].value + '<br>'
print '<br>'

print hw55_htmlFunctions.element( True, 0, 'h2', '',
  'Handle the selected button')
if 'login' in fromClient:
    print 'login button was pressed; authenticate'
else:
    print 'register button was pressed; <code> addAccount(...) </code>'

    
    
# end a standards-conforming web page
print hw55_htmlFunctions.html_end()