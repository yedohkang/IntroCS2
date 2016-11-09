#! /usr/bin/python
print "content-type: text/html\n"
import cgitb
cgitb.enable()
print "<h1> hello yedoh </h1>"
print 1 / 0
