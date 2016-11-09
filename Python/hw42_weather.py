#! /usr/bin/python
print "content-type: text/html\n"

import random

weathers = ["rainy", "sunny", "cloudy", "snowy", "stormy", "windy", "humid", "foggy"]
print weathers [int(random.random () * len (weathers))]