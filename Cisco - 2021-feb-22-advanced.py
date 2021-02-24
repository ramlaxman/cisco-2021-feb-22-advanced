#!/usr/bin/env python
# coding: utf-8

# In[2]:


print('Hello, world!')


# In[3]:


print('hello')                # enter == go down one line
print('hello again!')          # enter == go down one line
print('hello a third time!')   # shift+enter == execute the code in the cell


# In[4]:


x = 100


# In[5]:


x  # the final expression in a cell is returned


# In[6]:


10 + 10
20 + 20 
30 + 30


# # Different types of cells!
# 
# - Regular "code" cells
# - Markdown cells (like this one)

# # Different modes
# 
# - Edit mode -- green outline, you can type into the cell, and the text appears there.  Typically, for entering code and text.  You can enter "edit mode" by pressing Enter or clicking in a cell.
# 
# - Command mode -- blue outline, anything you type is interpreted as a Jupyter command. (Typically, one-character commands.)  Enter "command mode" by pressing ESC or clicking to the left of a cell.

# # A few useful Jupyter commands:
# 
# - `a` to add a new cell *above* the current one
# - `b` to add a new cell *below* the current one
# - `x` to cut a cell
# - `c` to copy a cell
# - `v` to paste a cell
# - `z` for undo (of deleting a cell, typically)
# - `m` to make a cell into Markdown mode
# - `y` to make a cell into code mode
# - `r` to put a cell into "raw" mode

# In[7]:


print('hello')


# In[8]:


x


# In[9]:


s = input('Enter a string: ')


# In[10]:


x


# In[11]:


get_ipython().run_line_magic('ls', '')


# In[12]:


get_ipython().run_line_magic('pwd', '')


# In[13]:


def hello(name):
    return f'Hello, {name}'


# In[14]:


get_ipython().run_line_magic('timeit', "hello('world')")


# # Agenda
# 
# 1. Data structures
#     - How do the built-in data structures work?
#     - More advanced data structures, especially from `collections`
# 2. Functions
#     - Different argument types (and thus parameter types)
#     - Function objects and bytecodes
#     - Variable scoping (LEGB rule)
#     - Enclosing functions and closures
#     - Treating functions as nouns, not just verbs
# 3. Functional programming 
#     - Comprehensions (list, set, dict, nested) 
#     - Sorting 
#     - `lambda`
#     - `operator` module
# 4. Modules and packages
# 5. Objects
#     - Classes, methods, instances
#     - Attributes -- what are they, why are they important, and the ICPO rule
#     - Inheritance
#     - Magic methods for customizing our objects
#     - Properties
#     - Descriptors
# 6. The iterator protocol
#     - Adding iteration to our classes
#     - Generator functions
#     - Coroutines and generators
#     - Generator expressions / generator comprehensions
# 7. Decorators
# 8. Threading and multiprocessing

# # `None` -- what is it?

# In[15]:


x = None

type(x)


# In[16]:


None == None


# In[17]:


if x == None:   # not Pythonic!
    print('Yes, x is None!')


# In[18]:


if x is None:
    print('Yes, x is None!')


# In[19]:


1 == 1.0


# In[20]:


x = 12345
y = 67890
z = 'hello out there'


# In[21]:


type(x)


# In[22]:


type(y)


# In[23]:


type(z)


# In[24]:


id(x)


# In[25]:


id(y)


# In[26]:


id(z)


# In[27]:


y = x    # the variable y should now refer to whatever the variable x is referring to


# In[28]:


id(x)


# In[29]:


id(y)


# In[30]:


x is y   # really asking: id(x) == id(y)


# In[31]:


x = None

if x is None:
    print('yes, x is None!')


# In[32]:


# PEP -- Python Enhancement Proposal


# In[33]:


x = 100
y = 100

x == y


# In[34]:


x is y


# In[35]:


x = 1000
y = 1000

x == y


# In[36]:


x is y


# In[39]:


x = type(None)()
y = type(None)()
z = type(None)()


# In[40]:


print(x)


# In[41]:


print(y)


# In[42]:


print(z)


# In[43]:


x is y


# In[44]:


y is z


# In[45]:


x = None

if x:
    print('x is True-ish')
else:
    print('x is False-ish')


# In[46]:


bool(None)


# # In a boolean context
# 
# Everything in Python is `True`!  Except for:
# 
# - `None`
# - `False`
# - 0 (of any type)
# - anything empty
#     - `''`
#     - `[]`
#     - `()`
#     - `{}`

# In[47]:


[] == False


# In[49]:


while True:
    s = input('Enter your name: ').strip()
    
    if not s:
        break
        
    print(f'Hello, {s}!')


# In[51]:


# as of Python 3.8, you can use the "assignment expression" operator
# aka "the walrus"
# looks like this:    :=

while s := input('Enter your name: ').strip():
    
    print(f'Hello, {s}!')


# In[52]:


# BDFL -- benevolent dictator for life


# In[53]:


True == True


# In[54]:


True == 1


# In[55]:


False == 0


# In[56]:


type(True)


# In[57]:


bool.__bases__


# In[58]:


x = 1


# In[59]:


import sys
sys.getsizeof(x)


# In[60]:


x = 1


# In[61]:


x = 1234567890
x = x ** 20


# In[65]:


x = x ** 20


# In[63]:


x


# In[66]:


sys.getsizeof(x)


# In[68]:


x = 100     # x refers to the int object 100
y = x       # y also refers to the int object 100 (same as x!)

x = 200     # x NOW refers to the int object 200 
y


# In[69]:


x = [10, 20, 30]
y = x

x[0] = '!!!'   # this is only possible because lists are mutable
x


# In[70]:


y


# In[71]:


x = 100
y = x

x += 10  # really this is: x = x + 10
x


# In[72]:


y


# In[73]:


# floats

0.1 + 0.2


# In[74]:


1/3


# In[75]:


x = 0.1
y = 0.2

z = x + y
z


# In[77]:


round(z, 20)


# In[78]:


# BCD -- binary coded decimals
# meaning: we will write the decimal digits using binary numbers, 
#  and the calculate using those decimal digits, like we did in school


# In[79]:


from decimal import Decimal 
x = Decimal('0.1')   # use a string to define!
y = Decimal('0.2')   # use a string to define!

x+y


# In[80]:


float(x+y)


# In[81]:


x = Decimal(0.1)
y = Decimal(0.2)


# In[82]:


x


# In[83]:


y


# In[84]:


x+y


# In[85]:


# strings are a "sequence"
# sequences: strings, lists, tuples


# In[86]:


# f-strings are as of Python 3.6

x = 'abcd'
y = 100
z = [10, 20, 30]

f'x = {x}, y = {y}, z = {z}'


# In[87]:


f'x = {x.upper()}, y = {y}, z = {z}'


# In[88]:


# as of Python 3.9, there's a new syntax for showing variables + values

f'{x=}, {y=}, {z=}'


# In[89]:


first = 'Reuven'
last = 'Lerner'

s = f'Hello, {first} {last}.'
print(s)


# In[90]:


s = f'Hello, {first:10} {last:15}.'
print(s)


# In[91]:


s = f'Hello, {first:^10} {last:>15}.'
print(s)


# In[92]:


s = f'Hello, {first:*^10} {last:_>15}.'
print(s)


# In[96]:


d = {'a':1000, 'bcd':2, 'efghi':3, 'jk':4567890}

for key, value in d.items():
    print(f'{key:.<8}{value:.>8}')


# In[97]:


x = 'abcd'
y = 'abcd'

x == y


# In[98]:


x is y


# In[99]:


x = 'abcd' * 5000
y = 'abcd' * 5000

x == y


# In[100]:


x is y


# In[101]:


x = 'ab.cd'
y = 'ab.cd'

x == y


# In[102]:


x is y


# In[103]:


x = 100


# In[104]:


# x is turned into a string ('x') and used a key in the globals dictionary
globals()  # this function returns that dictionary!


# In[105]:


print(x)


# In[106]:


'x' in globals()  # is it a key?


# In[107]:


globals()['x']


# In[108]:


globals()['x'] = 200


# In[109]:


x


# In[111]:


# Python uses "interning" on strings.  Meaning:
# - the first time it sees a string, it creates the string
# - any subsequent time, it just reuses that same string object


# In[114]:


x = sys.intern('ab.cd')
y = sys.intern('ab.cd')


# In[115]:


x is y


# In[116]:


s = 'abcd'
len(s)


# In[117]:


s[0]


# In[118]:


s[1]


# In[119]:


s[-1]


# In[120]:


s = ''
sys.getsizeof(s)


# In[121]:


s = 'a'
sys.getsizeof(s)


# In[122]:


s = 'ab'
sys.getsizeof(s)


# In[123]:


s = 'א'
sys.getsizeof(s)


# In[124]:


s = 'שלום'
len(s)


# In[125]:


s[0]


# In[126]:


s[1]


# In[127]:


# turn a string into bytes
s.encode()


# In[128]:


b = b'hello'


# In[129]:


b


# In[130]:


type(b)


# In[131]:


b[0]


# In[132]:


b[1]


# In[133]:


b.decode()


# In[134]:


mylist = [10, 20, 30, 40, 50]
type(mylist)


# In[135]:


mylist = [10, 20, 30]
mylist.append(40)  # this returns None!

mylist


# In[136]:


# mylist = mylist.append(50)  # don't do this!


# In[137]:


mylist = [10, 20, 30]
mylist.append(40)  # this returns None!

mylist


# In[140]:


mylist = []
for i in range(100):
    print(f'i = {i}, sys.getsizeof(mylist) = {sys.getsizeof(mylist)}')
    mylist.append(i)


# In[141]:


mylist = [10, 20, 30]

mylist.append('abcd')  # adds 'abcd' to the end of mylist
mylist


# In[142]:


mylist.extend('abcd')  # adds each element of 'abcd' to the end of mylist
mylist


# In[143]:


mylist += 'efgh'   # also adds each element of 'abcd' to the end of mylist
mylist


# In[144]:


mylist = [10, 20, 30]
biglist = [mylist, mylist, mylist]

len(biglist)


# In[145]:


biglist


# In[146]:


mylist[0] = '!!!'
mylist


# In[147]:


biglist


# # Sequences
# 
# What do they have in common?
# 
# - Indexing with `[i]`
# - Slices with `[start:end+1]` or `[start:end+1:step]`
# - Search with `in` (`LITTLE in BIG`)
# - Iterate with a `for` loop
# - Get the starting index of an element with the `.index` method
# - Find out how often something appears with the `.count` method

# In[148]:


s = 'abcabcaaabc'
s.count('a')

Comparison of sequences

              mutable/immutable  what are the elements?
string          immutable            strings
list              mutable            anything
tuple           immutable            anything
# In[149]:


t = (10, 20, 30)
type(t)


# In[150]:


t = (10, 20)
type(t)


# In[151]:


t = (10)
type(t)


# In[152]:


t = ()
type(t)


# In[153]:


4 + 5 * 6


# In[154]:


(4 + 5) * 6


# In[155]:


t = (10,)   #now it's a tuple!
type(t)


# In[156]:


(4 + 5,) * 6


# In[157]:


bool.__bases__  


# In[158]:


t = ([10, 20, 30],
     [100, 200, 300])


# In[159]:


t[0]


# In[160]:


t[1]


# In[161]:


t[0].append(40)


# In[162]:


t


# In[163]:


t[0] += [50, 60, 70]     # t[0].__iadd__([50, 60, 70])


# In[164]:


t


# In[165]:


t = 10, 20, 30, 40, 50
t


# In[168]:


def myfunc():
    return 10, 20, 30   # traditional not to use parentheses when returning values


# In[167]:


myfunc()


# In[169]:


# tuple unpacking == unpacking

mylist = [10, 20, 30]

x = mylist
x


# In[170]:


x,y,z = mylist


# In[171]:


x


# In[172]:


y


# In[173]:


z


# In[174]:


mylist = [10, 20, 30, 40 ,50, 60, 70]
x,y,z = mylist


# In[175]:


# Python 3 gives us some flexibility here
x,y,*z = mylist


# In[176]:


x


# In[177]:


y


# In[178]:


z


# In[179]:


x,*y,z = mylist
x


# In[180]:


y


# In[181]:


z


# In[182]:


mylist = [10, 20]
x,*y,z = mylist


# In[183]:


x


# In[184]:


y


# In[185]:


z


# In[186]:


mylist = [10, 20]
x,*y,*z = mylist


# In[187]:


def myfunc():
    return 'abcd', {'a':1, 'b':2, 'c':3}, [10, 20, 30]


# In[188]:


myfunc()


# In[189]:


s,d,mylist = myfunc()


# In[190]:


s


# In[191]:


d


# In[192]:


mylist


# In[193]:


p = ('Reuven', 'Lerner', 46)
p


# In[194]:


p[0]


# In[195]:


p[1]


# In[196]:


p[2]


# In[203]:


# named tuples

from collections import namedtuple

Person = namedtuple('something_else_entirely', ['first', 'last', 'shoesize'])


# In[204]:


type(Person)  # Person is actually a new class!  It was created via "namedtuple"


# In[205]:


str.__name__


# In[206]:


list.__name__


# In[207]:


Person.__name__


# In[208]:


Person = namedtuple('Person',
                    ['first', 'last', 'shoesize'])


# In[209]:


p = Person('Reuven', 'Lerner', 46)


# In[210]:


# printed representation
p


# In[211]:


p[0]


# In[212]:


p[1]


# In[213]:


p[2]


# In[214]:


p.first


# In[215]:


p.last


# In[216]:


p.shoesize


# In[217]:


Person.__bases__


# In[218]:


p[0] = 'asdfafa'


# In[219]:


p._replace(first='asdfafa')


# In[220]:


p


# # Exercise: Bookshop
# 
# 1. Define a new class, `Book`, using `namedtuple`, in which there are three field: `title`, `author`, `price`.
# 2. Define three books and put them into a list.
# 3. Ask the user repeatedly what book they want to buy. 
#     - If they give us an empty string, stop asking and print the total price.
#     - If they name a book title in our inventory, print all of the info, add the price to the total, and print the total.
#     - If they name a book title that is *not* in our inventory, then scold them.
# 4. When they're done asking, print the total price.

# In[226]:


from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'price'])

inventory = [Book('title1', 'author1', 100),
             Book('title2', 'author2', 120),
             Book('title3', 'author2', 120)]

total = 0

while look_for := input('Enter book title: ').strip():
    found_it = False
    for one_book in inventory:
        if one_book.title == look_for:
            print(f'Found {one_book}')
            total += one_book.price
            found_it = True
            break
            
    if not found_it:
        print(f'Did not find {look_for}')
            
print(f'{total=}')            
    


# In[222]:


inventory


# In[ ]:


from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'price'])

inventory = [Book('title1', 'author1', 100),
             Book('title2', 'author2', 120),
             Book('title3', 'author2', 120)]

total = 0

while look_for := input('Enter book title: ').strip():

    for one_book in inventory:
        if one_book.title == look_for:
            print(f'Found {one_book}')
            total += one_book.price
            break
            
    else:  # if we did not encounter a break, and got to the natural end of the loop
        print(f'Did not find {look_for}')
            
print(f'{total=}')        
    


# # Dictionaries
# 
# - Key-value pairs
#     - Key must be hashable (basically the same as immutable) -- typically ints and strings
#     - Value can be absolutely any Python object
# - Keys are unique -- this is enforced by the dict
# - Searching for a key is O(1) (constant time)
# 

# In[ ]:





# In[228]:


d = {'a':1, 'b':2, 'c':3}

d.keys()


# In[229]:


d.values()


# In[230]:


d.items()


# In[231]:


# Searching for keys
'a' in d.keys()  # this works -- but don't do it!


# In[232]:


# rather, use this:
'a' in d


# In[233]:


# searching for values
1 in d.values()  


# In[234]:


# unpacking
for key, value in d.items():
    print(f'{key}:{value}')


# In[235]:


d


# In[236]:


d['x'] = 100  # assignment adds a key-value pair to the dict!


# In[237]:


d


# In[238]:


d['x'] = 234  # assignment *ALSO* updates a value in the dict!


# In[239]:


d


# In[241]:


d['x']


# In[242]:


d['y']  # no such key


# In[243]:


# the dict.get method is like [], but more forgiving -- it returns None, not an exception

d.get('y')  # if 'y' in d, then return d['y'] else, None


# In[244]:


d.get('x')


# In[245]:


# the (optional) second argument to dict.get is returned if the key isn't there
d.get('x', 'hello')


# In[246]:


d.get('y', 'hello')


# In[247]:


# if I want to assign to a key-value pair in a dict, but I don't want 
# to overwrite an existing value, I can use dict.setdefault

d


# In[248]:


d.setdefault('y', 100)


# In[249]:


d


# In[250]:


d.setdefault('y', 999)


# In[251]:


d


# In[252]:


d = {'a':1, 'b':2, 'c':3}
others = {'b':200, 'c':300, 'd':400}

d.update(others)  # assign all key-value pairs in others to be in d, also
d


# In[254]:


# in Python 3.9, they added the | and |= operators to dicts!

d = {'a':1, 'b':2, 'c':3}
others = {'b':200, 'c':300, 'd':400}


d | others  # returns a new dict, doesn't modify either d or others


# In[255]:


d |= others  # same as dict.update

d


# # Exercise: `dictdiff`
# 
# 1. Write a function that takes two dicts as arguments, and returns a dict as its output.
# 2. The returned dict will represent the differences between the two arguments.
#     - If the two input dicts are identical, then the output dict will be empty.
#     - If the two input dicts have the same key and the same value, then for that key, there will be no output.
#     - For each key that has a different value in the different dicts, the output will contain a key-value pair -- the key will be the shared key, and the value will be a list of two elements, the value from the first dict and the value from the second dict.
#     - If a key exists in one dict but not the other, represent that with `None` in the two-element output list.
#     
# ```python
# d1 = {'a':1, 'b':2, 'c':3}
# d2 = {'a':100, 'b':2, 'd':4}
# 
# dictdiff(d1, d1)   # returns {}
# dictdiff(d1, d2)   # returns {'a':[1, 100], 'c':[3, None], 'd':[None, 4]}
# ```

# In[256]:


def dictdiff(first, second):
    output = {}
    
    for key in first.keys() | second.keys():
        v1 = first.get(key)
        v2 = second.get(key)
        
        if v1 != v2:
            output[key] = [v1, v2]
    
    return output


# In[257]:


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':100, 'b':2, 'd':4}


# In[258]:


dictdiff(d1, d1)


# In[259]:


dictdiff(d1, d2)

In Python 2, a new dict caused the creation of a table

index   key      value
0       'a'        1
1        'i'       4
2        'c'        3
3        'b'        2
4
5
6
7



# In[260]:


# PyPy -- JIT compiled version of Python

In Python 3, a new dict creates *two* data structures

(1) table with index-key-value with ZERO rows for starters
(2) an array at the C level of ints

index   key    value
0       'a'     1
1       'b'     2
2       'c'     3


[0,2,None,None,None,None,1,None]  # what row in the table should we go to?
# In[261]:


d = {}
d['a'] = 1


# In[262]:


hash('a') % 8  # what index in the array should we go to?


# In[263]:


'a' in d


# In[264]:


d['b'] = 2
d['c'] = 3


# In[265]:


hash('b')  % 8


# In[266]:


hash('c') % 8


# In[267]:


mylist = [10, 20, 30]

d[mylist] = 100


# # Next up
# 
# 1. Different `dict` types
# 2. Functions

# In[269]:


# defaultdict

from collections import defaultdict

d = defaultdict(0)


# In[270]:


callable(int)


# In[271]:


callable(5)


# # `defaultdict`
# 
# When we create a new `defaultdict`, we pass a callable. If we ask for a key's value, and the key does *not* exist, then the callable is invoked (with no arguments), and its return value is assigned to a new key-value pair.
# 
# If a key exists in the defaultdict, then the value is returned.

# In[272]:


int('5')


# In[273]:


int('    5       ')


# In[274]:


int('')


# In[275]:


int()   # int called with no arguments returns 0


# In[276]:


str()


# In[277]:


list()


# In[278]:


dict()


# In[279]:


d = defaultdict(int)

d['a']


# In[280]:


d['b']


# In[281]:


d['c'] += 5     # d['c'] = d['c'] + 5
d['d'] += 10
d


# In[282]:


def loud_int():
    print('Now running loud_int')
    return 0

d = defaultdict(loud_int)


# In[283]:


d['a']


# In[284]:


d['b'] += 5


# In[285]:


d['b']


# In[286]:


d['b']


# In[287]:


d['b']


# In[288]:


import time
time.time()


# In[289]:


d = defaultdict(time.time)


# In[290]:


d['a']


# In[291]:


d['b']


# In[292]:


d['c']


# In[293]:


d


# In[294]:


d = defaultdict(dict)

d['a']['b'] = 10
d['c']['d'] = 20
d['c']['x'] = 30


# In[295]:


d


# # Exercise: Travel
# 
# 1. Ask the user, repeatedly, to enter a city and country, separated by a comma. (e.g., 'Chicago, USA')
# 2. Use a defaultdict to create a dictionary in which the keys are country names and the values are lists of cities in each of those countries.
# 3. Don't worry about the same city appearing more than once.
# 4. If the user enters an empty string, then stop asking and print the countries, and each city in each country.  

# In[300]:


from collections import defaultdict

all_places = defaultdict(list)

while s := input('Enter city, country: ').strip():
    if ',' not in s:
        print('Use "city, country" format')
        continue
        
    city, country = s.split(',', 1)  # return a list whose highest index is 1
    
    all_places[country.strip()].append(city.strip())
    
    
for one_country, all_cities in all_places.items():
    print(one_country)
    for one_city in all_cities:
        print(f'\t{one_city}')


# In[299]:


all_places


# In[301]:


from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3


# In[302]:


od


# In[303]:


for key, value in od.items():
    print(f'{key}: {value}')


# In[304]:


# dict.pop removes a key-value pair (based on the key) and returns the value
od.pop('b')


# In[305]:


od.keys()


# In[309]:


od['b'] = 999
od


# In[310]:


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'b':2, 'a':1, 'c':3}


# In[311]:


d1 == d2


# In[312]:


od1 = OrderedDict(d1)
od2 = OrderedDict(d2)


# In[313]:


od1 == od2


# # `Counter`

# In[314]:


from collections import Counter

c = Counter()
c['a'] += 1
c['b'] += 10
c['c'] += 20

c


# In[315]:


# the real way to use Counter is to create a new Counter object based on 
# an existing iterable 

c = Counter('abcabcccbcbcba')


# In[316]:


c


# In[317]:


c = Counter([10, 20, 30, 20, 30, 40, 20, 30, 40, 50, 50, 20, 30, 40, 50])


# In[318]:


c


# In[319]:


c.most_common()


# In[320]:


c.most_common(3)  # show the 3 most common values, and their counts


# In[324]:


c2 = Counter([20, 30, 20, 20, 30, 40, 50,60])

c + c2  


# In[322]:


c


# In[323]:


c2


# # Exercise: Letter frequency
# 
# Use a `Counter` to go through the lines of a text file and count how many times each character appears. What are the 10 most common characters in the file?

# In[325]:


from collections import Counter

c = Counter()
for one_line in open('/etc/passwd'):
    c += Counter(one_line)


# In[327]:


c.most_common(10)


# In[328]:


def hello():
    return 'Hello!'


# In[329]:


hello()


# In[330]:


type(hello)


# In[331]:


hello = 5


# In[332]:


type(hello)


# In[333]:


hello()


# In[334]:


s = 'abcd'
x = s.upper() 


# In[335]:


type(x)


# In[336]:


x


# In[337]:


# here we're creating an alias, so that x and s.upper refer to the same object!

x = s.upper   # no parentheses!


# In[338]:


type(x)


# In[339]:


x


# In[340]:


x()


# In[341]:


while True:
    s = input('Enter something: ').strip()
    
    if not s:
        break
        
    print(s)


# In[342]:


while True:
    s = input('Enter something: ').strip   # no parentheses!
    
    if not s:
        break
        
    print(s)


# In[343]:


s


# In[344]:


bool(s)


# In[345]:


d = {'a':1, 'b':2, 'c':3}

for key, value in d.items():
    print(f'{key}: {value}')


# In[346]:


d = {'a':1, 'b':2, 'c':3}

for key, value in d.items:
    print(f'{key}: {value}')


# In[347]:


def hello():
    return 'Hello!'


# In[348]:


def hello(name):
    return f'Hello, {name}!'


# In[349]:


hello('world')


# In[350]:


hello()


# In[351]:


x = 5


# In[352]:


x = 7


# In[353]:


x*3


# # Two types of Python arguments
# 
# - Positional -- are assigned to parameters based on their positions.
# 
# ```python
# myfunc(10, 20, 30)  
# ```
# 
# In our call to `myfunc`, we're passing 10, 20, and 30 as positional arguments.
# 
# 
# - Keyword -- always come after positional arguments, and have the style of `name=value`.  No `=`?  Not a keyword argument.
# 
# 
# ```python
# myfunc(a=10, b=20, c=30)  
# ```
# 
# In this call to `myfunc`, we're passing three keyword arguments.
# 
# 
# ```python
# myfunc(10, 20, c=30)  
# ```
# In the above call to `myfunc`, the first two arguments are positional, and the third is keyword.

# In[354]:


hello('world')  # passing 'world' as a positional argument


# In[355]:


hello(name='world')  # passing 'world' as a keyword argument


# In[356]:


hello.__code__  # this is the actual brains of the function


# In[357]:


hello.__code__.co_argcount


# In[358]:


hello()


# In[359]:


hello.__code__.co_varnames


# In[360]:


def hello(name):
    output = f'Hello, {name}!'
    return output


# In[361]:


hello.__code__.co_argcount


# In[362]:


hello.__code__.co_varnames


# In[363]:


def add(a, b):
    return a + b


# In[364]:


add(10, 20)


# In[365]:


add(100, 200)


# In[366]:


add(5)


# In[367]:


add(a=5, b=6)


# In[368]:


add(5, b=6)


# In[369]:


# try to pass keyword before positional?  BAD NEWS
add(a=5, 6)


# In[370]:


def add(a, b=1):   # b has a default value!
    return a + b


# In[371]:


add(10, 5)


# In[372]:


add(10)


# In[373]:


add.__code__.co_argcount


# In[374]:


add.__defaults__


# In[375]:


def add(a, b, c, d=3, e=4, f=5):
    return a + b + c + d + e + f


# In[376]:


add(10, 20, 30)


# In[377]:


add.__code__.co_argcount


# In[378]:


add.__defaults__


# In[379]:


add(10, 20, 30, 40, 50)


# In[380]:


# are arguments in Python passed by value or by reference?
# answer: yes!
# or... no!


# In[381]:


x = 100

def myfunc(y):
    y = 200
    
myfunc(x)    
print(x)


# In[382]:


x = [10, 20, 30]

def myfunc(y):
    y.append(1)
    
myfunc(x)
print(x)


# In[383]:


def add_one(x=[]):
    x.append(1)
    return x

mylist = [10, 20, 30]
add_one(mylist)


# In[384]:


mylist


# In[385]:


add_one(mylist)
mylist


# In[386]:


add_one()


# In[387]:


add_one()


# In[388]:


add_one()


# In[389]:


def add_one(x=[]):   # MUTABLE DEFAULTS ARE BAD!!!
    x.append(1)
    return x


# In[390]:


add_one.__defaults__


# In[391]:


add_one() 


# In[392]:


add_one.__defaults__


# In[393]:


def add_one(x=None):
    if x is None:
        x = []    
    
    x.append(1)
    return x


# In[394]:


add_one()


# In[395]:


add_one()


# In[396]:


def hello(name):
    return f'Hello, {name}!'


# In[397]:


hello('world')


# In[398]:


hello(5)


# In[399]:


hello([10, 20, 30])


# In[400]:


hello(hello)


# In[405]:


def hello(name):
    if type(name) == str:
        return f'Hello, {name}!'
    else:
        raise ValueError('I wanted a string!')


# In[404]:


hello('world')


# In[406]:


hello(5)


# In[407]:


def hello(name):
    if isinstance(name, str):
        return f'Hello, {name}!'
    else:
        raise ValueError('I wanted a string!')


# In[408]:


bytes.__bases__


# In[409]:


def hello(name):
    """This is a very friendly function.
    
    Expects: A value, preferably a string
    Modifies: Nothing
    Returns: A new string, with a friendly greeting
    """
    return f'Hello, {name}!'


# In[410]:


hello('world')


# In[411]:


help(hello)


# In[412]:


hello.__doc__


# In[413]:


def hello(name:str) -> str:   # type hint or type annotation
    return f'Hello, {name}!'


# In[414]:


hello('world')


# In[415]:


hello(5)


# In[416]:


hello([10, 20, 30])


# In[417]:


hello(hello)


# In[418]:


hello.__annotations__


# In[419]:


from typing import Sequence


# # Exercise: firstlast
# 
# Write a function, `firstlast`, that takes any string, list, or tuple.  It returns a two-element value of the same type that it got in its input.  The returned value will contain the first and the last values from the input.
# 
# ```python
# firstlast('abcde')            # 'ae'
# firstlast([10, 20, 30, 40])   # [10, 40]
# firstlast((100, 200, 300))    # (100, 300)
# ```

# In[424]:


def firstlast(data):
    return data[:1] + data[-1:]

print(firstlast('abcde'))
print(firstlast([10, 20, 30, 40, 50]))
print(firstlast((100, 200, 300)))


# In[421]:


print(firstlast([10, 20, 30, 40, 50]))


# In[422]:


print(firstlast((100, 200, 300)))


# # Variable scoping roles
# 
# - Meaning: What variable exists when in Python?  
# - When do I have access to which variable?
# - When I assign to a variable, what am I assigning to?

# In[425]:


x = 100

print(f'{x=}')  # is x global? YES.  We get the value


# # Python has four variable scopes
# 
# - `L` Local (starts here if we're in a function body)
# - `E` Enclosing
# - `G` Global (starts here if we're *not* in a function body)
# - `B` Builtin

# In[426]:


'x' in globals()


# In[427]:


x = 100

def myfunc():
    print(f'In myfunc, {x=}') # is x local? NO... is x global? YES

print(f'Before, {x=}')  # is x global? YES
myfunc()
print(f'After, {x=}')  # is x global? YES


# In[428]:


myfunc.__code__.co_varnames


# In[429]:


x = 100

def myfunc():
    x = 200
    print(f'In myfunc, {x=}')  # is x local? YES

print(f'Before, {x=}')  # is x global? YES
myfunc()
print(f'After, {x=}')  # is x global? YES


# In[430]:


'x' in myfunc.__code__.co_varnames


# In[431]:


x = 100

def myfunc():
    print(f'In myfunc, {x=}')  # is x local? 
    x = 200

print(f'Before, {x=}')   # is x global? YES
myfunc()
print(f'After, {x=}')  


# In[432]:


'x' in myfunc.__code__.co_varnames


# In[433]:


x = 100

def myfunc():
    x += 1    # x = x + 1   # "hoisting problem"
    print(f'In myfunc, {x=}')  # is x local? 

print(f'Before, {x=}')   # is x global? YES
myfunc()
print(f'After, {x=}')  


# In[434]:


x = 100

def hello(name):
    return f'Hello, {name}!'

def myfunc():
    print(hello('world'))
    print(f'In myfunc, {x=}')  # is x local? 

print(f'Before, {x=}')   # is x global? YES
myfunc()
print(f'After, {x=}')  


# In[ ]:


x = 100
mylist = [10, 20, 30]

def myfunc():
    mylist[0] = '!!!'     # mylist.__setitem__(0, '!!!')
    print(f'In myfunc, {x=}')  # is x local? 

print(f'Before, {x=}')   # is x global? YES
myfunc()
print(f'After, {x=}')  


# In[438]:


x = 100

def myfunc():
    global x   # declaration: don't record x as local!
    x = 200    
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}')   # is x global? YES
myfunc()
print(f'After, {x=}')  


# In[436]:


'x' in myfunc.__code__.co_varnames


# In[439]:


import __main__   # this reflects global variables

x = 100

def myfunc():
    __main__.x = 200    
    print(f'In myfunc, {x=}')  

print(f'Before, {x=}')   # is x global? YES
myfunc()
print(f'After, {x=}')  


# In[440]:


for i in range(10):
    print(i, end= ' ')


# In[441]:


i


# In[442]:


sum = 0

for i in range(5):
    sum += i
    
sum


# In[443]:


sum([10, 20, 30])


# In[444]:


del(sum)


# In[445]:


sum([10, 20, 30])


# # Tomorrow
# 
# 1. `*args` 
# 2. `**kwargs`
# 3. Keyword-only and positional-only arguments
# 4. Nested functions and closures
# 5. Functions as nouns
# 6. Comprehensions (list, set, dict, nested)
# 7. `lambda` and sorting and key functions

# In[ ]:




