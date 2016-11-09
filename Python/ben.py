# Benjamin Shen <bshen@stuy.edu> pd10
# hw15_if
# started 12:01

#1. onX reprise (copied from hw14)
def onLine(x,y,a,b): # for point(x,y) and line y=ax+b
    return y == a*x + b
#tests omitted
def onX(x,y): # for point(x,y)
    return onLine(x,y,1,0) or onLine(x,y,-1,0)
#tests
print onX(5,5), ' ...expecting True'
print onX(-10,10), ' ...expecting True'
print onX(9,-8), ' ...expecting False'

#2. autotip
def autotip(n_of_people): # should produce number, in percent
    if n_of_people >= 8:
        return 18
	else: 
        return 0
#tests
print autotip(1), ' ...expecting 0'
print autotip(10), ' ...expecting 18'
print autotip(8), ' ...expecting 18'

#3. absHomeCooked
def absHomeCooked(n): # should produce |n|
    if n >= 0:
	    return n
	else:
	     return -n
#tests
print absHomeCooked(3), ' ...expecting 3'
print absHomeCooked(-2), ' ...expecting 2'
print absHomeCooked(0), ' ...expecting 0'

#4. autotip_4way
def autotip_4way(n_of_people): # should produce number, in percent
    if n_of_people >= 12:
	    return 25
	elif n_of_people >= 8:
	    return 18
	elif n_of_people >= 4:
	    return 15
	else:
	    return 0
#tests
print autotip_4way(12), ' ...expecting 25'
print autotip_4way(8), ' ...expecting 18'
print autotip_4way(7), ' ...expecting 15'
print autotip_4way(1), ' ...expecting 0'
		
# ended 12:23