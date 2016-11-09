#! /usr/bin/python
print "content-type: text/html\n"

#http://bart.stuy.edu/~yedoh.kang/hw44_welcomeTo.py/?person=yedoh&place=Stuy

import cgi
fromQS = cgi.FieldStorage ()
person = fromQS ['person'].value
place = fromQS ['place'].value

html = ''' 
<table border="1" cellpadding="2" cellspacing="2">
    <tbody>
        <tr>
            <td>
                <center>
                <h1> Hello, <i> person </i> ! </h1>
                <br> <h3> Welcome </h3> <h4> to <i> place </i> ! </h4>
            </td>
        </tr>
    </tbody>
</table>
'''

htmlFinal = html.replace('person', person).replace('place', place)
print htmlFinal
