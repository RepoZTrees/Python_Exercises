#-----*****-----

#Numeric Types:
#Integers, Floats, complext numbers
#e.g. 10, 54, 2.5, 3.0, 3+4j, 6-2j
#Operations: +, -, *, /, %, //, **, abs()

# x and y are complex numbers

x = 3+4j
print (x + 2) # 5+4j
print (x.real, x.imag) # 3.0, 4.0
print (x.conjugate()) # 3-4j
print (abs(x)) # 5
print (5/2, 5//2) # 2.5. 2
print (5**2) #25
print (abs(-5)) #5

#-----*****-----

# Strings
# ''Example'', 'example'
# """ Multiline string """
# Operations: +, *, len()

x = "hello there"

print (x.upper()) # 'HELLO THERE'
print (x.split()) # ['hello', 'there']
print (x.center(20)) # '  hello there  '
print (x.endswith("e")) # True
print (x.endswith("x")) # False

t = "{} in {}"
print(t.format("python", 2016)) # 'python in 2016'

#-----*****-----

#List
#[1,2,3] or list(1,2,3)
#Operations: +, *, len()

l = [3,2]
l.append(5) # l is [3,2,5]
l.extend(["a", "b"]) #l is now [3,2,5, 'a','b']
#l.sort() # l is [2,3,5,'a','b']
#l.reverse() # l is ['b','a',5,2,3]
a = [1,2] + [3,4] #[1,2,3,4]
print(a)
a = [1,2] * 2 # [1,2,1,2]
print(a)
print(5 in l) # True
print(100 in l) # False

#-----*****------

#Dictionaries
#{"name:"Turing", "age":30} OR
#dict(name="Turing", age = 30)
# Operations: [], del

d = dict(x=1, y=2)
print(list(d)) #['x', 'y']
print(list(d.items())) #[('x', 1) ('y', 2)]
print(list(d.values())) #[1, 2]
print('x' in d) #True
print('a' in d) #False
print(d['x']) # 1
#d['t'] # it'll raise KeyError
d['t'] = 10 # Adds a new key
print(d['t']) # 10
#del d['t'] # Deletes key
#print(d['t']) # raises KeyError

#-----*****-----

# Sets
# set([1,2,3]) or {1,2,3}
# Operations: -, &, |, ∧, len

u = {1,2}
v = {2,3}
w = {2}
print(u.union(v)) #{1, 2, 3}
print (u | v) # {1, 2, 3}
print (u & v) # {2}
print(u.intersection(v)) # {2}
print(u - v) # {1}
print(u.isdisjoint(v)) # False
print(u.issuperset(w)) # True

#-----*****-----

# Tuples
# Tuples are similar to lists but it can't be modified(it's immutable)
# Tuples are often used to group related data together rather than iterating
# (e.g.(r,g,b)for color triplets.)

l = (1,2,3)
#l[2] = '0' # Raise TypeError

#-----*****-----

# Control Structures

#Python statem blocks are marked by indentation(unlike in languages like 
#C which use curly braces). Statement headers end with a : and all statements 
#in the body are indented.

# def
# is used to create functions. They function body is indented

def add(x, y):
    return x + y
t = add(5, 6)
print (t) # 11

#-----*****-----

# For 
# Used for definite loops. The body of the for loops is indented

l = []
for i in [1,2,3]:
    l.append(i*2)
    print(l)
# l is [2,4,6]

m = []
for i in "ace":
    m.append(i)
    print(m)
#m is ['a','b','c']

s = 0
for i in range(1,20):
    s += i #is shorthand for a = a+b 
    print(s)
#s is 190

#-----*****-----

# While
# Used for indefinite loops. They body of the while is indented.

l = []
c = 10
while c > 0:
    l.append(c)
    c -= 2
    print(l)
# l will be [10, 8, 6, 4, 2]

#-----*****-----

# if
# Used for conditionals. The bodies of the if, elif and else clauses are
#indented

x = 10
if x%2 == 0:
    print (f"{x} is even.")
# Will print "10 is even"

gwords = ["Axe.", "Axe", "axe"]
for t in gwords:
    if t[0].isupper() and t.endswith("."):
        print("Good")
    elif t[0].isupper() or t.endswith("."):
        print ("Okay")
    else:
        print("Bad")
# Will print Good Okay Bad

#-----*****-----

# exceptions
# Used for error handling

"""
l = ["a", "b", "c"]
print(l[5]) # Raises an IndexErro exception

try:
    print(l[5])
except IndexError as e:
    # We can handle the exception here.
    print("Out of bounds")
except (TypeError, AttributeError) as e:
    # Handle TypeError and AttributeError here
except Exception:
    # Handle everything else here.
"""

#-----*****-----

# class
# Used to define classes. The body of the class is indented and the bodies
# of all the methods are indented again.

class Person:
    def __init__(self, name, age):
        # Initialiser method
        self.name = name
        self.age = age

    def update_age(self, new_age):
        self.age = new_age


    def __str__(self):
        # Magic method is used for str()
        return "{} of age {}".format(self.name, self.age)

n = Person("Shams", 30)
print (str(n)) # Will print Shams of age 30
n.update_age(32)
print(str(n)) # Will print Shams of age 32

#-----*****-----

# Program Files
# You can type a python program into a file (e.g. python3refcard.py).
# You can import and run functions inside them
# For e.g.:
# Filename is: python3refcard.py
# def add(x,y):
#    return x + y

# To import and run the above function:

# >>> python3
# >>> import python3refcard #filename.py
# >>> python3refcard.add #function name
