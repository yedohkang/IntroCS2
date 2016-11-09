# Yedoh Kang <kang.yedoh@gmail.com> Period 06
# HW #33

'''
0. the literal representation of a list: [] and commas separating the different elements ; an empty list is just [] ; for a list that is an element of a list: [ element, [element]]

1. i do not know. I just thought that all indexes are legitimate, but usually the max is n, and the minimum is -(n+1).

2. g [0] --> a --> string
   g [1] --> 0 --> integer
   g [2] --> [7] --> list
   g [3] --> a string literal of characters that represent the file
   g [4] --> [0] --> list
   
3. g [0:] --> ['a', 0, [7], open('pirateTalk.txt', 'rU'), [0]] --> list
   g [17:] --> [] --> empty list
   g [2:2] --> [] --> empty list
   
4. print g.index(42) --> integer literal
list.index (value) returns the element number of the first appearance of the parameter found in the list

5. print g.remove(42) --> removes 42 from the list and returns None
print g prints the resulting list
list.remove(value) removes the first appearance of value from the list and returns none. printing the list returns the list with the value taken out.

6. print g.append(42) --> adds the number 42 as the last element of the list
print g prints the list with the added value.
list.append (value) adds the value to the end of the list as the last element, and then returns none. printing the list returns the list with the added element at the end of the list. 
'''