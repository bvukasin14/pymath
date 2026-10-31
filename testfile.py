import pymath

myperimeters = pymath.perimeter.square(10)
myperimeterp = pymath.perimeter.rectangle(10, 5)
myareas = pymath.area.square(10)
myareap = pymath.area.rectangle(10, 5)
print(myperimeters)
print(myperimeterp)
print(myareas)
print(myareap)

######

myvalue = "m"
myvalue2 = "km"
converted = pymath.convert.size(myvalue, myvalue2, 10000)
print(converted)


######

"""
Task: One body has travelled 30000000mm and other 30km. Which one did travel more? (convert everything into decimeters)
"""

firstBody = 30000000
secondBody = 30
firstBodydm = pymath.convert.size("mm", "dm", firstBody)
secondBodydm = pymath.convert.size("km", "dm", secondBody)
if firstBodydm > secondBodydm:
    print("First body has travelled more!")
elif firstBodydm < secondBodydm:
    print("Second body has travelled more!")
else:
    print("They have travelled the same!")



#####

print(pymath.convert.area("km2", "m2", 10))
print(pymath.convert.volume("km3", "m3", 10))

#####

print(pymath.area.circle(5))
print(pymath.perimeter.circle(5))

###########

print(pymath.abs(12))
print(pymath.abs(-12))
print(pymath.abs(0))
print(pymath.abs(-0))

#######

print(pymath.perimeter.triangle(1, 2, 3))

##########

print(pymath.is_prime(2))
print(pymath.is_prime(5))

##########

print(pymath.average([1, 3, 5]))
print(pymath.average([]))

#########
