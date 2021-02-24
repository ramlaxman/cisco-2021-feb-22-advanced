#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. `*args` 
# 2. `**kwargs`
# 3. Keyword-only and positional-only arguments
# 4. Nested functions and closures
# 5. Functions as nouns
# 6. Comprehensions (list, set, dict, nested)
# 7. `lambda` and sorting and key functions

# In[1]:


sum([10, 20, 30])


# In[2]:


def mysum(numbers):
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[3]:


mysum([10, 20, 30])


# In[4]:


mysum(10, 20, 30)


# In[5]:


def mysum(a=0, b=0, c=0, d=0, e=0):
    return a + b + c + d + e


# In[6]:


mysum(10, 20, 30)


# In[7]:


mysum(10, 20, 30, 40, 50)


# In[8]:


mysum(10, 20, 30, 40, 50, 60)


# In[10]:


# When I use *args:
# - args (or whatever variable name we use) is a tuple
# - the contents of args will be all of the positional arguments that no other parameter took

def mysum(*numbers):   # "splat args"  == "*args"
    print(f'{numbers=}')
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[11]:


mysum(10, 20, 30)


# In[12]:


def myfunc(a, b, *args):
    return f'{a=}, {b=}, {args=}'


# In[13]:


myfunc()


# In[14]:


myfunc(10, 20)


# In[15]:


myfunc(10, 20, 30)


# In[16]:


myfunc(10, 20, 30, 40)


# In[18]:


#             b takes positional arguments *but* has a default value, 5
def myfunc(a, b=5, *args):
    return f'{a=}, {b=}, {args=}'


# In[19]:


myfunc(10, 20, 30, 40, 50)


# In[20]:


# how can I give a value to a, values to args, and skip over b?
# answer: you can't.


# In[21]:


myfunc(10)


# In[22]:


myfunc(10, args=(10, 20, 30))


# # Order of parameters
# 
# - Mandatory positional (no defaults)
# - Optional positional (with defaults)
# - `*args` (a tuple, containing all positional arguments that nothing else grabbed)

# In[26]:


def mysum(numbers):
    print(f'{numbers=}')
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[27]:


mysum.__code__.co_argcount


# In[28]:


mysum.__code__.co_varnames


# In[29]:


def mysum(*numbers):
    print(f'{numbers=}')
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[30]:


mysum.__code__.co_argcount


# In[31]:


mysum.__code__.co_varnames


# In[32]:


mysum.__code__.co_flags


# In[33]:


bin(mysum.__code__.co_flags)


# In[34]:


import dis
dis.show_code(mysum)


# In[35]:


def mysum(numbers):
    print(f'{numbers=}')
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[36]:


dis.show_code(mysum)


# In[37]:


bin(mysum.__code__.co_flags)


# In[38]:


def mysum(*numbers):
    print(f'{numbers=}')
    total = 0
    
    for one_number in numbers:
        total += one_number
        
    return total


# In[39]:


mysum(10, 20, 30)


# In[40]:


nums = [10, 20, 30, 40, 50]

mysum(nums)


# In[41]:


nums = [10, 20, 30, 40, 50]

mysum(*nums)   # in the function call, putting a * before an iterable "unrolls" it


# In[42]:


def add(a, b):
    return a + b


# In[43]:


t = (10, 5)


# In[44]:


add(t)


# In[45]:


add(*t)


# # Exercise: all_lines
# 
# 1. Define a function, `all_lines`, that takes one mandatory positional argument, `outfilename`.  This will be the name of a file into which you will write the output.
# 2. The function can then take any number of additional arguments, each of which will be the name of an input file. 
# 3. Write all of the lines from the input files into the output file -- first all of the lines from the 1st argument, then from the 2nd argument, etc., until all file contents have been written into `outfilename`.

# In[47]:


for i in range(5):
    with open(f'file{i}.txt', 'w') as outfile:
        for index, one_word in enumerate('abc def ghi jkl mno'.split()):
            outfile.write(f'{i} {index} {one_word}\n')


# In[48]:


get_ipython().system('ls *.txt')


# In[49]:


get_ipython().system('cat file0.txt')


# In[50]:


get_ipython().system('cat file1.txt')


# In[52]:


def all_lines(outfilename, *args):
    with open(outfilename, 'w') as outfile:
        for one_filename in args:
            print(f'Now reading from {one_filename}')
            for one_line in open(one_filename):
                outfile.write(one_line)


# In[53]:


all_lines('myoutput.txt', 'file0.txt', 'file1.txt', 'file2.txt', 'file3.txt', 'file4.txt')


# In[54]:


get_ipython().system('cat myoutput.txt')


# In[55]:


import os
os.listdir('.')


# In[56]:


import glob
glob.glob('file*.txt')


# In[59]:


all_lines('myoutput.txt', *glob.glob('file*.txt'))


# In[ ]:


def all_lines(outfilename, *args):
    with open(outfilename, 'w') as outfile:  
        # outfile.__enter__()   -- for files, this does nothing
        for one_filename in args:
            print(f'Now reading from {one_filename}')
            for one_line in open(one_filename):  # the file is closed automatically, soon after the for loop exits
                outfile.write(one_line)
        # outfile.__exit__()  -- for files, this flushes + closes the file


# In[ ]:





# # Order of parameters
# 
# - Mandatory positional (no defaults)
# - Optional positional (with defaults)
# - `*args` (a tuple, containing all positional arguments that nothing else grabbed)

# In[60]:


def add(a, b):
    return a + b

add(a=10, b=5)


# In[61]:


add(a=10, b=5, c=12345)


# In[62]:


# **kwargs is a dict, containing all of the keyword arguments
# that no other parameter got


# In[63]:


def myfunc(a, b, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[65]:


myfunc(10, 20)


# In[66]:


myfunc(10, 20, 30)


# In[67]:


myfunc(10, 20, x=100, y=200, z=300)


# In[68]:


def myfunc(a, b=2, **kwargs):
    return f'{a=}, {b=}, {kwargs=}'


# In[69]:


myfunc(3, x=100, y=200)


# In[70]:


myfunc(a=3, b=4, x=100, y=200)


# In[72]:


dis.show_code(myfunc)


# In[73]:


def myfunc(a, *args, **kwargs):
    return f'{a=}, {args=}, {kwargs=}'


# In[74]:


myfunc(10, 20, 30, 40, 50)


# In[75]:


myfunc(10, 20, 30, 40, 50, x=100, y=200, z=300)


# # Why do we need `**kwargs`?
# 
# 1. We have a function that can take lots of different parameters. Rather than define the function with many parameters (and defaults), we can just use `kwargs` and search through the keys and values in the dict for what we want.
# 2. We have a function that knows what it wants to do with keys and values, but doesn't know what keys or what values it'll get. It'll accept lots of keys and values, whatever comes it way, and then formats/prints/uses them in the standard way.

# In[76]:


def myfunc():
    f = open('/etc/passwd')
    
myfunc()    


# In[77]:


mylist = [10, 20, 30]
mylist.append(mylist)


# In[78]:


mylist


# In[79]:


len(mylist)


# In[80]:


mylist[-1]


# In[81]:


mylist is mylist[-1]


# # Exercise: write_config
# 
# 1. Write a function that takes one mandatory argument, `outfilename`, and any number of keyword arguments.
# 2. The keyword arguments should be written to the file, one pair per line, in the format of `key=value`.

# In[82]:


def write_config(outfilename, **kwargs):
    with open(outfilename, 'w') as outfile:
        for key, value in kwargs.items():
            outfile.write(f'{key}={value}\n')


# In[83]:


write_config('myconfig.txt', a=1, b=2, c=3, d=[10, 20, 30])


# In[84]:


get_ipython().system('cat myconfig.txt')


# In[85]:


d = {'a':1, 'b':2, 'c':3, 'd':[100, 200, 300]}


# In[87]:


write_config('myconfig2.txt', **d)


# In[88]:


get_ipython().system('cat myconfig2.txt')


# In[89]:


def myfunc(a, b=5, *args):
    return f'{a=}, {b=}, {args=}'

myfunc(10, 20, 30, 40, 50)


# In[90]:


myfunc(10)


# In[91]:


# now b is a keyword-only argument
def myfunc(a, *args, b=5):
    return f'{a=}, {b=}, {args=}'

myfunc(10, 20, 30, 40, 50)


# In[92]:


myfunc(10, 20, 30, 40, 50, b=999)


# In[93]:


# b is still a keyword-only argument, and it's now mandatory!
def myfunc(a, *args, b):
    return f'{a=}, {b=}, {args=}'

myfunc(10, 20, 30, 40, 50)


# In[95]:


# b is keyword only, even though we don't have *args in this function

def myfunc(a, *, b):
    return f'{a=}, {b=}'

myfunc(10)


# In[96]:


myfunc(10, b=30)


# In[97]:


myfunc(10, 20, 30, b=40)


# In[98]:


myfunc(a=2, b=4)


# In[ ]:





# # Order of parameters
# 
# - Positional-only arguments (before the `/`)
# - Mandatory (no defaults, positional or keyword)
# - Optional positional (with defaults)
# - `*args` (a tuple, containing all positional arguments that nothing else grabbed)
# - `*` by itself, if there isn't a `*args` parameter, separates positional from keyword-only
# - Mandatory keyword-only arguments
# - Optional keyword-only arguments (with defaults)
# - `**kwargs` (gets all unclaimed keyword arguments)

# In[99]:


len('abcd')


# In[100]:


help(len)


# In[101]:


len(obj='abcd')


# In[102]:


def hello():
    return 'Hello!'


# In[103]:


hello.__code__.co_code


# In[104]:


dis.dis(hello)


# In[105]:


hello.__code__.co_consts


# In[106]:


def hello(name):
    return name


# In[107]:


dis.dis(hello)


# In[108]:


x = 100

def hello():
    return x


# In[109]:


dis.dis(hello)


# In[110]:


def hello():
    global name
    name = 'hello'
    return name


# In[111]:


dis.dis(hello)


# In[112]:


def myfunc():
    print('Hello')


# In[113]:


dis.dis(myfunc)


# In[114]:


def myfunc():
    print('hello')
    print('hello')
    print('hello')


# In[115]:


dis.dis(myfunc)


# In[116]:


myfunc.__code__.co_consts


# In[117]:


myfunc.__code__.co_code


# In[118]:


len(myfunc.__code__.co_code)


# In[119]:


def hello(name):
    return f'Hello, {name}!'


# In[120]:


dis.dis(hello)


# In[122]:


len(hello.__code__.co_code)


# In[123]:


hello.__code__.co_code


# # Remember:
# 
# 1. When we use `def`, we're creating a function object and assigning it to a variable.
# 2. When we assign to a variable inside of a function, the variable is local.
# 3. We can return any Python data structure from a function.

# In[124]:


def outer():
    def inner():
        return f'I am from inner!'
    return inner


# In[125]:


f = outer()


# In[126]:


type(f)


# In[127]:


f()


# In[128]:


f2 = outer()


# In[129]:


f2()


# In[138]:


# closure -- a function that retains access to its enclosing function's local variables

def outer(x):
    def inner(y):
        return f'Here, {x=} and {y=}'
    return inner


# In[135]:


func1 = outer(10)
func2 = outer(20)


# In[136]:


func1(5)


# In[137]:


func2(6)


# In[140]:


func1.__code__.co_freevars  # what variables come from the enclosing function?


# In[142]:


outer.__code__.co_cellvars  # what variables will be used by my inner functions?


# In[143]:


def outer(x):
    counter = 0  # local to outer, but available to inner
    
    def inner(y):
        return f'[{counter=}] Here, {x=} and {y=}'
    return inner


# In[144]:


func1 = outer(10)


# In[145]:


func1(5)


# In[146]:


func1(6)


# In[147]:


def outer(x):
    counter = 0  # local to outer, but available to inner
    
    def inner(y):
        counter += 1   # this is a local variable
        return f'[{counter=}] Here, {x=} and {y=}'
    return inner


# In[148]:


func1 = outer(10)


# In[149]:


func1(5)


# In[150]:


def outer(x):
    counter = 0  # local to outer, but available to inner
    
    def inner(y):
        nonlocal counter  # any assignment to counter goes to the outer scope
        counter += 1   
        return f'[{counter=}] Here, {x=} and {y=}'
    return inner


# In[151]:


func1 = outer(10)


# In[152]:


func1(5)


# In[153]:


func1(6)


# In[154]:


func1(7)


# # Exercise: password generator generator
# 
# 1. Write a function, `make_password_generator`, which takes one argument, a string.
# 2. It should return a function (`make_password`) that takes an integer as an argument.
# 3. When the inner function is called, it should return a string of the stated length, with each character taken from the outer function's argument.
# 
# It'll help to know that `random.choice(data)` returns one random element from the sequence `data`.

# In[156]:


import random

def make_password_generator(s):
    def make_password(n):
        output = ''
        for i in range(n):
            output += random.choice(s)
        return output
    return make_password

make_alpha_password = make_password_generator('abcde')
pw1 = make_alpha_password(5)
pw2 = make_alpha_password(10)


# In[157]:


pw1


# In[158]:


pw2


# In[159]:


make_symbol_password = make_password_generator('!@#$%^&*()_+')
pw3 = make_symbol_password(5)
pw4 = make_symbol_password(10)


# In[160]:


pw3


# In[161]:


pw4


# In[ ]:


import random

def make_password_generator(s):
    def make_password(n):
        return ''.join([random.choice(s)
                        for i in range(n)])
    return make_password

make_alpha_password = make_password_generator('abcde')
pw1 = make_alpha_password(5)
pw2 = make_alpha_password(10)


# In[163]:


def a():
    return "I'm in A!"

def b():
    return "I'm in B!"

while s := input('Enter a choice: ').strip():
    if s == 'a':
        print(a())
    elif s == 'b':
        print(b())
    else:
        print(f'{s} is not a valid option')


# In[164]:


def a():
    return "I'm in A!"

def b():
    return "I'm in B!"

# dispatch table
ops = {'a':a,
       'b':b}

while s := input('Enter a choice: ').strip():
    if s in ops:
        print(ops[s]())
    else:
        print(f'{s} is not a valid option')


# In[165]:


def hello(name):
    return f'Hello, {name}!'


# In[167]:


globals()['hello']


# In[169]:


x = 10

'yes' if x == 10 else 'no'


# # Exercise: Calculator
# 
# 1. Ask the user repeatedly to enter a math expression in prefix notation, meaning `+ 2 3`.
# 2. You should expect only two numbers, and the operators can be `+`, `-`, `/`, and `*`.
# 3. If the user enters one one of the expected operators, then invoke the appropriate function and print the result.  
# 4. If the user enters an unexpected operator, print an error message. (And let them try again.)
# 5. If the user enters an empty string, then stop asking.
# 6. Use a dispatch table (i.e., a dict with functions) to implement your calculator's functionality.

# In[171]:


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

ops = {'+':add,
      '-':sub,
      '/':div,
      '*':mul}

while s := input('Enter math expression: ').strip():
    op, *numbers = s.split()
    
    int_numbers = []
    for one_number in numbers:
        int_numbers.append(int(one_number))
    
    if op in ops:
        print(ops[op](*int_numbers))
    else:
        print(f'No such operator {op}')


# In[173]:


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mul(a, b):
    return a * b

ops = {'+':add,
      '-':sub,
      '/':div,
      '*':mul}

while s := input('Enter math expression: ').strip():
    op, *numbers = s.split()
    
    if op in ops:
        print(ops[op](*[int(one_number)
                        for one_number in numbers]))
    else:
        print(f'No such operator {op}')


# In[174]:


import operator

ops = {'+':operator.add,
      '-':operator.sub,
      '/':operator.truediv,
      '*':operator.mul}

while s := input('Enter math expression: ').strip():
    op, *numbers = s.split()
    
    if op in ops:
        print(ops[op](*[int(one_number)
                        for one_number in numbers]))
    else:
        print(f'No such operator {op}')


# # Functional programming
# 
# 1. Treat all data as immutable.
# 2. Avoid assignment as much as possible.
# 3. Treat functions as nouns, not just verbs.

# # Topics in functional programming
# 
# 1. Comprehensions
#    - List comprehensions
#    - Dict comprehensions
#    - Set comprehensions
#    - Nested comprehensions
# 2. Sorting and key functions
# 3. `lambda`
# 4. `map`, `filter`, and `reduce`

# In[175]:


numbers = list(range(10))
numbers


# In[176]:


# I want a list of these numbers, squared

# traditionally, I would write:

output = []

for one_number in numbers:
    output.append(one_number ** 2)


# In[177]:


output


# In[178]:


# the better way is: list comprehensions

[one_number ** 2            # ANY VALID expression -- SELECT
 for one_number in numbers] # ANY VALID iteration  -- FROM


# In[179]:


[print(one_number ** 2)            # ANY VALID expression -- SELECT
 for one_number in numbers] # ANY VALID iteration  -- FROM


# In[182]:


s = '10 20 30 40 50'

# I want to sum these numbers
sum([int(one_number)
     for one_number in s.split()])


# In[183]:


[int(one_number)
     for one_number in s.split()]


# # Exercises: Comprehensions
# 
# 1. Ask the user to enter a string. Using a comprehension, find out how many non-whitespace characters the string contains.
# 2. Ask the user to enter a sentence. Use a comprehension to return the sentence, but with each word capitalized. The result should be the same as running `str.title` on the string. But don't use `str.title`! You may use `str.capitalize`, if you want.

# In[184]:


s = input('Enter a sentence: ').strip()


# In[185]:


len(s)


# In[187]:


len(s.replace(' ', ''))


# In[190]:


sum([len(one_word)
 for one_word in s.split()])


# In[191]:


s


# In[192]:


s.title()


# In[193]:


s.capitalize()


# In[196]:


' '.join([one_word.capitalize()
          for one_word in s.split()])


# In[199]:


mylist = 'abcd efgh ij'.split()
mylist


# In[200]:


'*'.join(mylist)    # GLUE.join(ITERABLE)


# In[201]:


s.split()


# In[203]:


'***'.join(s.split())


# In[204]:


'*'.join([one_word
          for one_word in s.split()])


# In[205]:


'*'.join([one_word.upper()
          for one_word in s.split()])


# In[206]:


'*'.join([one_word[0]
          for one_word in s.split()])


# In[207]:


'*'.join([one_word.capitalize()
          for one_word in s.split()])


# In[208]:


' '.join([one_word.capitalize()
          for one_word in s.split()])


# In[210]:


[one_line.split(':')
 for one_line in open('/etc/passwd')]


# In[211]:


# get all usernames in /etc/passwd
[one_line.split(':')[0]
 for one_line in open('/etc/passwd')]


# In[212]:


# get all usernames in /etc/passwd
[one_line.split(':')[0]                # expression
 for one_line in open('/etc/passwd')   # iteration
 if not one_line.startswith('#')]      # condition


# In[213]:


numbers = [10, 20, 25, 35, 40, 100, 150, 155, 175]

[one_number ** 2
 for one_number in numbers]


# In[215]:


# I only want (a) odd numbers (b) bigger than 100

[one_number ** 2
 for one_number in numbers
 if one_number % 2 and one_number > 100]


# In[216]:


# I only want (a) odd numbers (b) bigger than 100

[one_number ** 2
 for one_number in numbers
 if one_number % 2 
 if one_number > 100]


# In[217]:


get_ipython().system('cat nums.txt')


# #  Exercise: Sum the numbers
# 
# Use a list comprehension to read through `nums.txt` and add the integers together. (The answer is 83.)

# In[219]:


[int(one_line)
for one_line in open('nums.txt')]


# In[220]:


int('5')


# In[221]:


int('    5       ')


# In[222]:


int('')


# In[223]:


int()


# In[224]:


[int(one_line)
for one_line in open('nums.txt')
if one_line.strip()]


# In[225]:


[int(one_line)
for one_line in open('nums.txt')
if one_line.strip().isdigit()]


# In[226]:


sum([int(one_line)
for one_line in open('nums.txt')
if one_line.strip()])


# In[227]:


get_ipython().system('head shoe-data.txt')


# # Exercise: Shoe data
# 
# 1. Use a list comprehension to create a list of dicts from `shoe-data.txt`.
# 2. Each of the lines has three columns, separated by tabs (`'\t'`).
# 3. Each dict (and there will be 100 of them in the end) will have three key-value pairs, with the keys being `brand`, `color`, `size`.
# 
# Suggestion: Use a function in your expression, rather than trying to do it all inline.

# In[230]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

[line_to_dict(one_line)
for one_line in open('shoe-data.txt')]


# In[ ]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

[line_to_dict(one_line)
for one_line in open('shoe-data.txt')]


# In[231]:


z = zip('abcd', [10, 20, 30, 40])


# In[232]:


list(z)


# In[251]:


z = zip('abcd', [10, 20, 30, 40])


# In[252]:


list(z)


# In[254]:


dict(list(z))


# In[ ]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

[line_to_dict(one_line)
for one_line in open('shoe-data.txt')]


# In[255]:


dict


# In[257]:


dict(a=1, b=2)


# In[258]:


dict([('a', 1), ('b', 2)])


# In[259]:


dict(zip('abc', [10, 20, 30]))


# In[260]:


def line_to_dict(one_line):
    return dict(zip(['brand', 'color', 'size'],
                   one_line.strip().split('\t')))

[line_to_dict(one_line)
for one_line in open('shoe-data.txt')]


# # Next up:
# 
# 1. Dict comprehensions
# 2. Set comprehensions
# 3. Nested comprehensions
# 4. Sorting and key functions
# 5. `lambda`

# In[262]:


# (1) username and (2) user ID -- index 0 and index 2

[ [  one_line.split(':')[0], one_line.split(':')[2]   ]
 for one_line in open('/etc/passwd')
if not one_line.startswith('#')]


# In[264]:


# (1) username and (2) user ID -- index 0 and index 2

dict([ one_line.split(':')[:3:2]   # [start:end+1:step]
 for one_line in open('/etc/passwd')
if not one_line.startswith('#')])


# In[265]:


# dict comprehension -- this creates *ONE* dictionary

{ one_line.split(':')[0]  : one_line.split(':')[2]
 for one_line in open('/etc/passwd')
if not one_line.startswith('#') }


# In[266]:


{ fields[0]  : fields[2]
 for one_line in open('/etc/passwd')
if not one_line.startswith('#') and (fields := one_line.split(':'))}


# In[267]:


{ one_line.split(':')[0]  : one_line.split(':')[1:]
 for one_line in open('/etc/passwd')
if not one_line.startswith('#') }


# In[268]:


get_ipython().system('ls *.txt')


# In[269]:


get_ipython().system('cat myconfig.txt')


# # Exercise: dict comprehension
# 
# Use a dict comprehension to read from a config file, and turn it into name-value pairs in a dict. Note that whatever values you read will be strings, regardless of what they look like or originally were.

# In[272]:


{one_line.strip().split('=')[0]  : one_line.strip().split('=')[1]
 for one_line in open('myconfig.txt')}


# In[273]:


# this is dangerous!

{one_line.strip().split('=')[0]  : eval(one_line.strip().split('=')[1])
 for one_line in open('myconfig.txt')}


# In[274]:


# eval overlaps 75% with evil!


# # Set comprehension
# 
# - Returns a new set
# - Just like a list comprehension, but uses `{}`
# - Don't put `:` between things, or it becomes a dict comprehension

# In[275]:


s = '10 20 30 40 50 10 20 30 40 50'

# list comprehension
sum([int(one_number)
     for one_number in s.split()])


# In[276]:


s = '10 20 30 40 50 10 20 30 40 50'

# set comprehension
sum({int(one_number)
     for one_number in s.split()})


# In[278]:


get_ipython().system('head -20 /etc/passwd')


# In[283]:


# What are the different shells in /etc/passwd?

{one_line.strip().split(':')[-1]
 for one_line in open('/etc/passwd')
 if not one_line.startswith('#')}


# # Exercises with comprehensions
# 
# 1. Create a set of the different IP addresses in `mini-access-log.txt`.
# 2. Find the 3 most common IP addresses in `mini-access-log.txt`.
# 

# In[284]:


get_ipython().system('head mini-access-log.txt')


# In[287]:


{one_line.split()[0]
for one_line in open('mini-access-log.txt')}


# In[289]:


from collections import Counter

c = Counter([one_line.split()[0]
         for one_line in open('mini-access-log.txt')])
c


# In[291]:


for key, value in c.items():
    print(f'{key:20}: {value}')


# In[294]:


for key, value in c.items():
    print(f'{key:20}: {"x" * (value // 2)}')


# In[296]:


c.most_common(3)


# In[297]:


mylist = [[10, 20, 30], [40, 45, 50, 55, 60, 65], 
          [70, 75, 80, 85, 90], [100, 110, 115, 120]]

mylist


# In[298]:


[one_number
 for one_number in mylist]


# In[299]:


[one_number
 for one_sublist in mylist
 for one_number in one_sublist]


# In[300]:


# I find this to be unreadable!
[one_number for one_sublist in mylist for one_number in one_sublist]


# In[301]:


[(x,y)
 for x in range(10)
 for y in range(10)]


# In[303]:


[one_number
 for one_sublist in mylist
 if len(one_sublist) > 3
 for one_number in one_sublist]


# In[304]:


# produces a list with the odd elements of mylist's longer sublists
[one_number
 for one_sublist in mylist
 if len(one_sublist) > 3
 for one_number in one_sublist
 if one_number % 2]


# In[305]:


get_ipython().system('head movies.dat')


# In[306]:


get_ipython().system('wc movies.dat')


# # Exercise: Movie categories
# 
# Use a list comprehension (and associated tools) to find the 5 most common movie categories in `movies.dat`.  Note that most movies have more than one category -- just count them multiple times.

# In[311]:


from collections import Counter

c = Counter([one_category
 for one_line in open('movies.dat', encoding='latin-1')
 for one_category in one_line.strip().split('::')[2].split('|')])
c


# In[312]:


c.most_common(5)


# In[313]:


Counter([one_category
for one_line in open('movies.dat', encoding='latin-1')
for one_category in one_line.strip().split('::')[2].split('|')]).most_common(5)


# In[315]:


c = Counter([one_category
for one_line in open('movies.dat', encoding='latin-1')
for one_category in one_line.strip().split('::')[2].split('|')])

for key, value in c.most_common(5):
    print(f'{key:10}{(value // 20) * "x"}')


# In[316]:


Counter([one_category
  for one_line in open('movies.dat', encoding='latin-1')
  for field_index, one_field in enumerate(one_line.strip().split('::'))
  for one_category in one_field.split('|')
  if field_index == 2])


# In[317]:


import random

numbers = [random.randint(0, 100)
           for i in range(10)]


# In[318]:


numbers


# In[319]:


# "sorted" is functional -- it doesn't change the source data, but returns a new list
sorted(numbers)


# In[320]:


words = 'This is a bunch of words for my Python class at Cisco'.split()


# In[321]:


sorted(words)


# In[322]:


'a' < 'b'  # meaning: does 'a' come before 'b'?


# In[323]:


'Z' < 'a'


# In[324]:


# If I want to sort these words case insensitively, how can I do that?

# (1) make all words lowercase , and sort them
# don't do this!


# In[325]:


# (1) ask the sorting system to compare them without regard to case, 
# but not change the data

# don't compare A and B
# rather, compare f(A) and f(B)


# In[326]:


sorted(words, key=str.lower)


# In[327]:


sorted(words, key=len)


# In[328]:


sorted(words, key=len, reverse=True)


# In[329]:


# sort words by their last letter, then 2nd to last, then 3rd to last, etc.

def by_backwards_word(one_word):
    return one_word[::-1]  # return the word, reversed

sorted(words, key=by_backwards_word)


# # Exercise: sort by vowel count
# 
# 1. Ask the user to enter a sentence.
# 2. Sort the words in the sentence according to how many vowels (a, e, i, o, and u) the sentence contains.
# 

# In[330]:


def by_vowel_count(one_word):
    total = 0
    
    for one_letter in one_word.lower():
        if one_letter in 'aeiou':
            total += 1
            
    return total

by_vowel_count('encyclopedia')


# In[331]:


s = input('Enter some words: ').strip()

sorted(s.split(), key=by_vowel_count)


# In[332]:


def by_vowel_count2(one_word):
    return sum([1
                for one_letter in one_word.lower()
                if one_letter in 'aeiou'])


# In[336]:


d = dict(zip('bdeca', 
             [random.randint(0, 100) for i in range(5)]))
d


# In[337]:


d


# In[338]:


for key, value in d.items():
    print(f'{key}: {value}')


# In[339]:


# how can we sort our dict by key?
sorted(d.items())


# In[340]:


for key, value in sorted(d.items()):
    print(f'{key}: {value}')


# In[341]:


# how can we sort our dict by value?

def by_value(t):
    return t[1]

for key, value in sorted(d.items(), key=by_value):
    print(f'{key}: {value}')


# In[342]:


# lambda -- creates and returns an anonymous function object


# In[343]:


3 + 5


# In[344]:


'abcd'.capitalize()


# In[345]:


def square(x):
    return x ** 2

square(5)


# In[346]:


# create an anonymous function that does the same thing
lambda x: x ** 2


# In[347]:


(lambda x: x ** 2)(5)


# In[348]:


s2 = lambda x: x ** 2  # basically the same as def

s2(5)


# In[349]:


# how can we sort our dict by value?

for key, value in sorted(d.items(), key=lambda t: t[1]):
    print(f'{key}: {value}')


# In[350]:


import operator


# In[351]:


# operator.itemgetter -- takes an argument, and returns a function
# that applies [argument]

s1 = 'abcde'
s2 = 'fghijk'

s1[3]


# In[352]:


s2[3]


# In[353]:


# operator.itemgetter is a function that returns a function!
# the returned function applies [] to its argument
get_3 = operator.itemgetter(3)


# In[354]:


get_3(s1)


# In[355]:


get_3(s2)


# In[356]:


# this is the winner -- no lambda, no one-time function
for key, value in sorted(d.items(), key=operator.itemgetter(1)):
    print(f'{key}: {value}')


# In[357]:


d.items()


# In[358]:


for t in d.items():
    print(t[0], t[1])


# # Exercise: Sorting shoes
# 
# 1. Sort the list of shoe dicts by size.
# 2. Sort the list of shoe dicts first by brand, and then by size.

# In[360]:


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand':brand,
           'color':color,
           'size':size}

shoes = [line_to_dict(one_line)
         for one_line in open('shoe-data.txt')]


# In[362]:


def by_size(shoe_dict):
    return shoe_dict['size']

sorted(shoes, key=by_size)


# In[363]:


sorted(shoes, key=lambda shoe_dict: shoe_dict['size'])


# In[364]:


sorted(shoes, key=operator.itemgetter('size'))


# In[365]:


def by_brand(shoe_dict):
    return shoe_dict['brand']

sorted(shoes, key=by_brand)


# In[366]:


def by_field(field_name):
    def get_field(shoe_dict):
        return shoe_dict[field_name]
    return get_field
    
sorted(shoes, key=by_field('size'))    


# In[369]:


def by_fields(*field_names):
    def get_fields(shoe_dict):
        return [shoe_dict[one_field]
                for one_field in field_names]
    return get_fields
    
sorted(shoes, key=by_fields('brand', 'size'))    


# In[370]:


sorted(shoes, key=operator.itemgetter('brand', 'size'))    


# In[371]:


fields = input('Enter sort fields: ')

print(sorted(shoes, key=operator.itemgetter(*fields.split())))


# In[373]:


[operator.itemgetter('brand', 'size')(one_shoe)
 for one_shoe in shoes]


# In[ ]:




