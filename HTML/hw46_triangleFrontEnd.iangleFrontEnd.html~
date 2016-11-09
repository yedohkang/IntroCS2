#! /usr/bin/python
print "content-type: text/html\n"

import cgitb
cgitb.enable()

import cgi
fromQS = cgi.FieldStorage ()
leg0 = float (fromQS['leg0'].value)
leg1 = float (fromQS['leg1'].value)
leg2 = float (fromQS['leg2'].value)

S = (leg0 + leg1 + leg2) / 2
P = leg0 + leg1 + leg2
A = (S * (S - leg0) * (S - leg1) * (S - leg2)) ** 0.5

html = ''' 
<center>
<table border="1" cellpadding="2" cellspacing="2">
    <tbody>
        <tr>
            <td>
                <center>
                <h3> leg 0 : leg0 <br> leg 1 : leg1 <br> leg 2 : leg2 </h3> <h2> perimeter: P <br>
                area: A
                </h2>
                </center>
            </td>
        </tr>
    </tbody>
</table>
</center>
'''

htmlFinal = html.replace('leg0', str (leg0))
htmlFinal = htmlFinal.replace('leg1', str (leg1))
htmlFinal = htmlFinal.replace('leg2', str (leg2))
htmlFinal = htmlFinal.replace('P', str (P))
htmlFinal = htmlFinal.replace('A', str (A))
print htmlFinal