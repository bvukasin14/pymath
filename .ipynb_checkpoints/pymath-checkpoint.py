PI = 3.141592653589793
class perimeter():
    def square(a):
        o = 4 * a
        return o
    def rectangle(a, b):
        o = 2 * a + 2 * b
        return o
    def circle(r):
        u = 2 * r * PI
        return u
class area():
    def square(a):
        p = a * a
        return p
    def rectangle(a, b):
        p = a * b
        return p
    def circle(r):
        A = (r ** 2) * PI
        return A
class convert():
    def size(fromr, tor, a):
        units = {
            "1" : "mm",
            "2" : "cm",
            "3" : "dm",
            "4" : "m",
            "7" : "km"
        }
        for key, value in units.items():
            if value == fromr:
                fromrkey = key
        for key, value in units.items():
            if value == tor:
                torkey = key
        multiplier = 1
        divider = 1
        if fromrkey > torkey:
            biggerA = True
        else:
            biggerA = False
        bigger = int(max(fromrkey, torkey))
        smaller = int(min(fromrkey, torkey))
        if biggerA:
            zeroMultiplier = bigger - smaller
            for i in range(zeroMultiplier):
                multiplier = multiplier * 10
            a = a * multiplier
        else:
            zeroDivider = bigger - smaller
            for i in range(zeroDivider):
                divider = divider * 10
            a = a / divider
        return a
    def area(fromr, tor, a):
        units = {
            "1" : "mm2",
            "2" : "cm2",
            "3" : "dm2",
            "4" : "m2",
            "7" : "km2"
        }
        for key, value in units.items():
            if value == fromr:
                fromrkey = key
        for key, value in units.items():
            if value == tor:
                torkey = key
        multiplier = 1
        divider = 1
        if fromrkey > torkey:
            biggerA = True
        else:
            biggerA = False
        bigger = int(max(fromrkey, torkey))
        smaller = int(min(fromrkey, torkey))
        if biggerA:
            zeroMultiplier = bigger - smaller
            for i in range(zeroMultiplier):
                multiplier = multiplier * 100
            a = a * multiplier
        else:
            zeroDivider = bigger - smaller
            for i in range(zeroDivider):
                divider = divider * 100
            a = a / divider
        return a
    def volume(fromr, tor, a):
        units = {
            "1" : "mm3",
            "2" : "cm3",
            "3" : "dm3",
            "4" : "m3",
            "7" : "km3"
        }
        for key, value in units.items():
            if value == fromr:
                fromrkey = key
        for key, value in units.items():
            if value == tor:
                torkey = key
        multiplier = 1
        divider = 1
        if fromrkey > torkey:
            biggerA = True
        else:
            biggerA = False
        bigger = int(max(fromrkey, torkey))
        smaller = int(min(fromrkey, torkey))
        if biggerA:
            zeroMultiplier = bigger - smaller
            for i in range(zeroMultiplier):
                multiplier = multiplier * 1000
            a = a * multiplier
        else:
            zeroDivider = bigger - smaller
            for i in range(zeroDivider):
                divider = divider * 1000
            a = a / divider
        return a
def squared(a, b):
    c = a ** b
    return c