#!/usr/bin/env python
# coding: utf-8

# # Agenda
# 
# 1. What is an object?
# 2. Classes and instances
# 3. Attributes
# 4. `__init__` -- what it is (and isn't)
# 5. Other methods
# 6. Class attributes and the ICPO rule (instance, class, parent, object)
# 7. Inheritance
# 8. Magic methods
#     - `__str__` and `__repr__`
#     - `__len__`
#     - `__add__` and its friends
#     - `__eq__` and its friends
#     - `__format__`
#     - `__enter__` and `__exit__`
# 9. Data classes    
# 10. Properties and descriptors

# # What is an object?
# 
# 1. Every object has an `id`
# 2. Every object has a class (keyword to create new types( / type (function that identifies)
# 3. Every object has attributes (i.e., the things after dots)

# In[1]:


# this is a method call, but that's because b is an attribute of a that's callable
# a.b()


# In[2]:


# a.c   # no parentheses -- we're just retrieving data


# In[3]:


s = 'abcd'
type(s)


# In[4]:


x = 1234
type(x)


# In[5]:


d = {'a':1, 'b':2, 'c':3}
type(d)


# In[6]:


id(str)


# In[7]:


id(int)


# In[8]:


id(dict)


# In[9]:


type(str)


# In[10]:


type(int)


# In[11]:


type(dict)


# In[12]:


type(type)


# In[13]:


import random
random.randint(0, 100)   # random is a variable, and randint is an attribute of random


# In[14]:


import os
os.pathsep


# In[15]:


os.sep


# In[16]:


# we can see the attributes available on an object with "dir"
dir(s)


# In[17]:


x


# In[18]:


dir(x)


# In[20]:


x


# In[22]:


x.real


# In[24]:


class Company:
    pass


# In[25]:


type(Company)


# In[27]:


c1 = Company()   
c2 = Company()


# In[28]:


dir(c1)


# In[29]:


c1.name = 'My Company'
c1.country = 'Israel'

dir(c1)


# In[30]:


dir(c2)


# In[31]:


c2.industry = 'Computers'
c2.employee_count = 1000


# In[32]:


# the "vars" function returns a dict of all attributes set on an object
vars(c1)


# In[33]:


vars(c2)


# In[34]:


# we're going to tell our "Company" class what attributes to 
# set automatically each time we create a new instance

# we're going to do that with the __init__ method


# In[35]:


class Company:
    def __init__(self):
        self.name = 'My Company'
        self.industry = 'Computers'


# In[36]:


Company.__init__


# In[37]:


c1 = Company()
c2 = Company()


# In[38]:


vars(c1)


# In[39]:


vars(c2)


# When I call `Company()`:
# - Python invokes the constructor method, known as `__new__`
#     - (You probably never want to write this method)
#     - It allocates memory for the new object
#     - It assigns the new object to a local variable, which I call `o`
# - `__new__` calls calls `o.__init__(*args, **kwargs)`  
#     - The local variable `o` (in `__new__`) is the same as the local variable `self` in `__init__`
#     - The job of `__init__` is to add attributes to the new object
#     - It returns the new object to the caller

# In[40]:


import os


# In[41]:


os.company = 'Cisco'


# In[43]:


class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry


# In[44]:


c1 = Company()


# In[45]:


s = 'abcde'
s.upper()  # calling the "upper" method on s


# In[46]:


# that call to s.upper() was actually rewritten!
str.upper(s)  # the instance (s) was replaced by its class, and then shifted to the 1st arg


# In[47]:


c1 = Company('a', 'b')
c2 = Company('c', 'd')


# In[48]:


vars(c1)


# In[49]:


vars(c2)


# In[50]:


print(c1.name)


# In[51]:


c1.name = 'NewName!'
c1.name


# In[52]:


class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        
    def letterhead(self):
        return f'FROM {self.name} CORPORATION'


# In[54]:


c1 = Company('Cisco', 'networking')
c1.letterhead()   # Company.letterhead(c1)


# In[55]:


class Company:
    def __init__(self, name, industry):
        self.name = name
        self.industry = industry
        
    def letterhead(self, fancy_char='*'):
        return f'{fancy_char} FROM {self.name} CORPORATION {fancy_char}'


# In[56]:


c1 = Company('Cisco', 'networking')
c1.letterhead()   # Company.letterhead(c1)


# In[57]:


c1.letterhead('****')   # Company.letterhead(c1, '****')


# In[58]:


Company.letterhead(c1, '****')


# # Exercise: Book
# 
# 1. Create a `Book` class. Each instance of `Book` will have three attributes:
#     - `author`
#     - `title`
#     - `price`
# 2. Define three `Book` instances. Put them in a list, and iterate over them.  Print the title and price of each one.

# In[59]:


class Book:
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price
        
b1 = Book('author1', 'title1', 100)        
b2 = Book('author2', 'title2', 50)        
b3 = Book('author2', 'title3', 75)        

all_books = [b1, b2, b3]

for one_book in all_books:
    print(f'{one_book.title}: {one_book.price}')


# # Exercise: Shelf
# 
# 1. Create a `Shelf` class.  Each instance will contain zero or more instances of `Book`.
# 2. Define an `add_books` method on `Shelf` that takes any number of books to add.
# 3. Define a `titles` method that returns a list of strings, the titles of books on the shelf.
# 
# ```python
# s = Shelf()
# s.add_books(b1, b2)
# s.add_books(b3)
# s.titles()   # should return ['title1', 'title2', 'title3']
# ```

# In[60]:


class Shelf:
    def __init__(self):  
        self.books = []

    def add_books(self, *args):
        for one_book in args:
            self.books.append(one_book)
            
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
s = Shelf()
s.add_books(b1, b2)
s.add_books(b3)
s.titles()     


# In[64]:


class Person:
    def __init__(self, name):
        self.name = name
        Person.population += 1
        
    def greet(self):
        return f'Hello, {self.name}!'
    
Person.population = 0

print(f'Before, population = {Person.population}')
p1 = Person('name1')
p2 = Person('name2')
print(f'After, population = {Person.population}')

print(p1.greet())
print(p2.greet())


# In[65]:


print('A')
class Person:
    print('B')
    def __init__(self, name):   # defines Person.__init__
        print('C')
        self.name = name
    print('D')
print('E')
        
p1 = Person('name1')
p2 = Person('name2')


# In[66]:


def myfunc():
    asdfsaffafsafafafsadf


# In[67]:


def myfunc():
    asdfsaffafsafafafsadf
    asdfasfafasfasfasf


# In[68]:


def myfunc():
    asdfsaffafsafafafsadf
     asdfasfafasfasfasf


# In[70]:


class Person:
    population = 0  # this is a CLASS ATTRIBUTE (Person.population), not a variable!

    def __init__(self, name):
        self.name = name
        Person.population += 1
        
    def greet(self):
        return f'Hello, {self.name}!'
    
print(f'Before, population = {Person.population}')
p1 = Person('name1')
p2 = Person('name2')
print(f'After, population = {Person.population}')
print(f'After, p1.population = {p1.population}')
print(f'After, p2.population = {p2.population}')

print(p1.greet())
print(p2.greet())


# # attribute lookup
# 
# - `I` instance
# - `C` instance's class
# - `P` for the parent(s) of the class
# - `O` the `object` class, at the top of our hierarchy

# In[71]:


class Person:
    population = 0  # this is a CLASS ATTRIBUTE (Person.population), not a variable!

    def __init__(self, name):
        self.name = name
        self.population += 1   # self.population = self.population + 1
        
    def greet(self):
        return f'Hello, {self.name}!'
    
print(f'Before, population = {Person.population}')
p1 = Person('name1')
p2 = Person('name2')
print(f'After, population = {Person.population}')
print(f'After, p1.population = {p1.population}')
print(f'After, p2.population = {p2.population}')

print(p1.greet())
print(p2.greet())


# # Using class attributes
#  
# - If you're retrieving a class attribute, you can use either the class name or `self`.  `self` is a bit more flexible
# - If you're assigning to a class attribute, *ONLY USE THE CLASS NAME*.  Never use `self`, or you'll get into trouble.

# In[72]:


class Shelf:
    def __init__(self):  
        self.books = []

    def add_books(self, *args):
        for one_book in args:
            self.books.append(one_book)
            
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
s = Shelf()
s.add_books(b1, b2)
s.add_books(b3)
s.titles()     


# # Exercise: Limit shelf space
# 
# 1. We'll say that every shelf has a maximum number of 3 books on it.
# 2. Add this limitation as a class attribute on your `Shelf` class, and modify `add_books` such that it takes this into account.
# 3. If you try to add more than 3 books to a shelf, raise an exception.

# In[74]:


class TooManyBooksOnShelfError(Exception):
    pass

class Shelf:
    max_books = 3

    def __init__(self):  
        self.books = []

    def add_books(self, *args):
        for one_book in args:
            if len(self.books) >= self.max_books:
                raise TooManyBooksOnShelfError('Too many books!')
            self.books.append(one_book)
            
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
s = Shelf()
s.add_books(b1, b2)
s.add_books(b3, b3)
s.titles()     


# - Inheritance
# - Magic methods
# - Special methods (class and static methods)
# 

# In[75]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


# In[76]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        
    def greet(self):
        return f'Hello, {self.name}!'
    
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())
print(e2.greet())


# # Class relationships
# 
# - `is-a`: inheritance. A is-a B? If so, then A inherits from B.  Employee is-a Person. Car is-a Vehicle. Book is-a Publication.
# - `has-a`: composition. Book has-a title. Car has-a Engine. 

# In[79]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee(Person):
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        
e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print(e1.greet())  # does e1's class's parent have a "greet" attribute? YES
print(e2.greet())


# # Three paradigms for method inheritance
# 
# 1. Do nothing; the child class doesn't implement the method, and we thus rely on the parent class to implement it.
# 2. (overriding) The child class implements a method, and thus we never invoke the parent class's method.
# 3. (mixture) Invoke the parent class's method, and then add to its functionality or result.

# In[85]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


class Employee(Person):
    def __init__(self, name, id_number):
        # Person.__init__(self, name)
        super().__init__(name)
        self.id_number = id_number
        
    def greet(self):
        return f'{super().greet()}!!!!!!'
        
e1 = Employee('emp1', 1)  
e2 = Employee('emp2', 2)

print(e1.greet())  
print(e2.greet())


# In[86]:


class TooManyBooksOnShelfError(Exception):
    pass

class Shelf:
    max_books = 3

    def __init__(self):  
        self.books = []

    def add_books(self, *args):
        for one_book in args:
            if len(self.books) >= self.max_books:
                raise TooManyBooksOnShelfError('Too many books!')
            self.books.append(one_book)
            
    def titles(self):
        return [one_book.title
               for one_book in self.books]
    
s = Shelf()
s.add_books(b1, b2)
s.add_books(b3, b3)
s.titles()     


# # Exercise: BigShelf
# 
# Add a new class, `BigShelf`, that is the same as `Shelf`, but can have up to 5 books (rather than 3).  Modify `Shelf` as little as possible (if at all) for this to work, and keep `BigShelf` as short as possible, taking advantage of `Shelf` where you can .

# In[92]:


class TooManyBooksOnShelfError(Exception):
    pass

class Shelf:
    max_books = 3

    def __init__(self):  
        self.books = []

    def add_books(self, *args):
        for one_book in args:
            if len(self.books) >= self.max_books:  # does s's class have max_books? YES -- 5
                raise TooManyBooksOnShelfError('Too many books!')
            self.books.append(one_book)
            
    def titles(self):
        return [one_book.title
               for one_book in self.books]

class BigShelf(Shelf):
    max_books = 5     
    
s = BigShelf()
#  in __new__, Python says o.__init__() -- does o's class's parent have an __init__ ? NO
s.add_books(b1, b2)  # does s's class's parent have an attribute add_books? Yes
#   Shelf.add_books(s, b1, b2)
s.add_books(b3, b3, b2)
s.titles()     


# In[93]:


class MyClass:
    pass


# In[94]:


m = MyClass()


# In[96]:


object.__init__(m)


# In[97]:


type(Shelf)


# In[98]:


Shelf.__bases__


# In[99]:


type(object)


# In[100]:


object.__bases__


# In[101]:


type.__bases__


# In[102]:


type(type)


# In[103]:


# ICPO -- instance, class, parent(s), object


# In[104]:


# Python resolves this with the "MRO" -- method resolution order
BigShelf.__mro__


# In[105]:


Shelf.__mro__


# In[106]:


object.__mro__


# In[107]:


Shelf.__mro__ = (object,)


# In[130]:


# multiple inheritance

class A:
    def __init__(self, x):
        self.x = x
        
    def x2(self):
        return self.x * 2
    
    def hello(self):
        return f'Hello from A!'
    
class B:
    def __init__(self, y):
        self.y = y
        
    def y3(self):
        return self.y * 3
    
    def hello(self):
        return f'Hello from B!'

class C(A, B):
    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)
        
        


# In[116]:


C.__bases__


# In[117]:


C.__mro__


# In[124]:


c = C(10, 20)


# In[125]:


vars(c)


# In[126]:


c.y3() 


# In[127]:


c.x2()


# In[128]:


c.hello()


# In[131]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


# In[132]:


print(p1)


# In[133]:


print(p2)


# In[134]:


# str(SOMETHING) -> SOMETHING.__str__()


# In[135]:


object.__str__(p1)


# In[136]:


p1


# In[137]:


str(p1)  # this is the string version of our object, via __str__  : meant for users


# In[139]:


p1  # this is the "representation" of our object, via __repr__ : meant for developers


# In[140]:


# if you just define __repr__, then it is used whenever __str__ is required
# (but the opposite is not true -- if you just define __str__, it isn't used for
# __repr__)

# advice: always implement __repr__, and add __str__ if and when you need to


# In[146]:


class Person:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        return f'Hello, {self.name}!'
    
    def __repr__(self):
        return f'I am a Person, name is {self.name}!'
    
p1 = Person('name1')
p2 = Person('name2')

print(p1.greet())
print(p2.greet())


# In[147]:


print(p1)


# In[148]:


print(p2)


# In[149]:


p1


# In[150]:


p2


# In[151]:


# Use an IDE to do this exercise

# use a module (animals.py) for all of the class definitions
# use a separate program that loads the module and uses the classes there


# In[ ]:


wolf = Wolf('black')            # species, color, # legs
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('black')

print(wolf)                      # black wolf, 4 legs
print(sheep1)                    # white sheep, 4 legs
print(sheep2)                    # white sheep, 4 legs
print(snake)                     # brown snake, 0 legs
print(parrot)                    # black parrot, 2 legs


c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)
print(c1)                        # cage number + animal printouts


c2 = Cage(2)                    # an ID number, not that important
c2.add_animals(snake, parrot)
print(c2)                        # cage number + animal printouts

z = Zoo()
z.add_cages(c1, c2)
print(z)                           # show all cages, all animals

print(z.animals_by_color('black'))
print(z.number_of_legs())


# In[152]:


Shelf.__name__  # just like a module, a class object has __name__, a string with its name


# 1. Magic methods
#     - `__len__`
#     - `__add__` and its friends
#     - `__eq__` and its friends
#     - `__format__`
#     - `__enter__` and `__exit__`
# 2. Class and static methods
# 3. Data classes    
# 4. Properties and descriptors

# In[169]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __repr__(self):
        return f'MyClass instance, x = {x}'
    
class ChildClass(MyClass):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y
        
    def __repr__(self):
        # return f'ChildClass instance, x = {self.x}, y = {self.y}'
        s = super().__repr__()
        return f'ChildClass with {self.y=}, and ... {s}'
    
m = MyClass(10)
print(m)


# In[170]:


c = ChildClass(10, 20)
vars(c)


# In[171]:


print(c)


# In[172]:


len('abcd')


# In[173]:


len([10, 20, 30])


# In[174]:


len({'a':1, 'b':2})


# In[175]:


len(5)


# In[180]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __repr__(self):
        return f'MyClass instance, x = {self.x}'
    
    # len() looks for the method __len__
    def __len__(self):
        return self.x    
  
m = MyClass(10)
print(m)


# In[181]:


len(m)


# In[182]:


x = 1
y = 2

x + y


# In[183]:


x = '1'
y = 2

x + y


# In[184]:


y + x


# In[185]:


str.__add__(x, y)   # translated into x.__add__(y) ... str.__add__(x, y)


# In[186]:


int.__add__(y, x)


# In[190]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __repr__(self):
        return f'MyClass instance, x = {self.x}'
    
    def __add__(self, other):
        return MyClass(self.x + other.x)

m1 = MyClass(10)
m2 = MyClass(20)


# In[191]:


m1 + m2


# In[192]:


m1 + 50


# In[193]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __repr__(self):
        return f'MyClass instance, x = {self.x}'
    
    def __add__(self, other):
        if hasattr(other, 'x'):
            return MyClass(self.x + other.x)
        else:
            return MyClass(self.x + int(other))

m1 = MyClass(10)
m2 = MyClass(20)


# In[194]:


m1 + m2


# In[195]:


m2 + m1


# In[196]:


m1 + 100


# In[197]:


m1 + '100'


# In[198]:


m1 + 'abcd'


# In[199]:


100 + m1


# In[200]:


int.__add__(100, m1)


# In[201]:


type(NotImplemented)


# In[202]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __repr__(self):
        return f'MyClass instance, x = {self.x}'
    
    def __add__(self, other):
        if hasattr(other, 'x'):
            return MyClass(self.x + other.x)
        else:
            return MyClass(self.x + int(other))
        
    def __radd__(self, other):
        return self + other

m1 = MyClass(10)
m2 = MyClass(20)


# In[203]:


m1 + 100


# In[204]:


100 + m1


# In[233]:


from functools import total_ordering

@total_ordering
class MyClass:
    def __init__(self, x):
        self.x = x
        
    def __repr__(self):
        return f'MyClass instance, x = {self.x}'
    
    def __eq__(self, other):
        if hasattr(other, 'x'):
            return self.x == other.x
        return False
    
    def __lt__(self, other):
        return self.x < other.x
    
m1 = MyClass(10)
m2 = MyClass(20)


# In[234]:


m1 == m2


# In[235]:


m1 < m2


# In[236]:


m2 < m1


# In[237]:


m1 <= m2


# In[238]:


m2 >= m1


# In[ ]:





# In[239]:


MyClass.__gt__


# In[240]:


MyClass.__ge__


# 1. Magic methods
#     - `__len__`
#     - `__add__` and its friends
#     - `__eq__` and its friends
#     - `__format__`
#     - `__enter__` and `__exit__`
# 2. Class and static methods
# 3. Data classes    
# 4. Properties and descriptors

# In[242]:


s1 = 'abcd'
s2 = 'efghijk'

print(f'{s1:15}: {s2:12}')


# In[243]:


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __repr__(self):
        return f'{self.first} {self.last}'
    
p = Person('Reuven', 'Lerner')
print(p)


# In[246]:


class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def __repr__(self):
        return f'[repr] {self.first} {self.last}'
    
    def __format__(self, format_code):
        if format_code == 'china':
            return f'[__format__] {self.last} {self.first}'
        
        return f'[__format__] {self.first} {self.last}'
    
p = Person('Reuven', 'Lerner')
print(p)


# In[247]:


print(f'{p}')


# In[248]:


print(f'{p:china}')


# In[249]:


# context manager == an object that knows how to behave inside of a "with" block

with open('myfile.txt', 'w') as f:
    f.write('stuff\n')


# In[ ]:


with OBJECT as ALIAS:
    ALIAS.__enter__()
    CODE
    ALIAS.__exit__()


# In[250]:


with 5:
    pass


# In[253]:


class LoudCM:
    def __init__(self, x):
        print(f'Now in LoudCM.__init__, x = {x}')
        self.x = x
        
    def __enter__(self):
        print(f'Now in LoudCM.__enter__')
        return self
    
    def __exit__(self, ex_type, ex_obj, ex_backtrace):
        print(f'Now in LoudCM.__exit__')
        
with LoudCM(10) as c:
    print('Hello')


# # Exercise: Context managers
# 
# 1. Write a new class, TempOutput, which is a context manager.
# 2. TempOutput will take one argument, the name of a file to which all standard output should be written within the `with` block.
# 3. Meaning: If someone uses `print` within the block, the output should not be written to the screen, but rather to the named file.
# 4. (The file can be reset to zero each time we use the context manager.)
# 5. Upon exit from the context manager, the earlier output (probably stdout) is restored.

# In[254]:


import sys
sys.stdout


# In[ ]:


import sys

class TempOutput:
    def __init__(self, outfilename):
        print(f'Now in TempOutput.__init__, outfilename = {outfilename}')
        self.outfile = open(outfilename, 'w')
        self.old_stdout = None
        
    def __enter__(self):
        print(f'Now in TempOutput.__enter__')
        self.old_stdout = sys.stdout
        sys.stdout = self.outfile
        return self
    
    def __exit__(self, ex_type, ex_obj, ex_backtrace):
        print(f'Now in TempOutput.__exit__')
        self.old_stdout = None
        sys.stdout = self.old_stdout
        self.outfile.close()
        
with TempOutput('tempout.txt'):
    print('Hello')    


# In[1]:


5


# In[1]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def hello(self):
        return 'Hello!'
    
m = MyClass(10)    
m.hello()


# In[2]:


MyClass.hello()


# In[3]:


MyClass.hello(m)


# In[4]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    def hello():
        return 'Hello!'
    
m = MyClass(10)    
m.hello()


# In[5]:


MyClass.hello()


# # Static method
# 
# A method, defined on a class, that can be invoked from an instance or from the class (without any instances as arguments).  It can take other arguments!

# In[9]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    @staticmethod
    def hello(name):
        return f'Hello, {name}!'
    
m = MyClass(10)    
m.hello('world')


# In[10]:


MyClass.hello('world again')


# In[11]:


dict()


# In[12]:


dict.fromkeys('abc')


# In[13]:


help(dict.fromkeys)


# In[14]:


class MyClass:
    def __init__(self, x):
        self.x = x
        
    @classmethod
    def hello(cls, name):
        return f'Hello, {name}, from {cls}!'
    
m = MyClass(10)    
m.hello('world')


# In[15]:


MyClass.hello('out there')


# In[16]:


class Thermostat:
    def __init__(self, temp=20):
        self.temp = temp
        
t = Thermostat()
print(t.temp)
t.temp = 22
print(t.temp)


# In[17]:


t.temp = -10


# In[18]:


t.temp = 100


# In[19]:


class Thermostat:
    def __init__(self, temp=20):
        self.temp = temp
        
t = Thermostat()
print(t.temp)
t.temp = 22
print(t.temp)


# In[26]:


class Thermostat:
    def __init__(self, temp=20):
        self._temp = temp
        
    @property
    def temp(self):
        print(f'Yes, Thermostat.temp is running!')
        return self._temp
    
    @temp.setter
    def temp(self, new_temp):
        print(f'Yes, Thermostat temp *setter* is running')
        self._temp = new_temp    
        
t = Thermostat()
print(t.temp)


# In[27]:


t.temp = 22


# In[28]:


t.temp


# In[29]:


class TempTooLowException(Exception):
    pass

class TempTooHighException(Exception):
    pass

class Thermostat:
    def __init__(self, temp=20):
        self._temp = temp
        
    @property
    def temp(self):
        print(f'Yes, Thermostat.temp is running!')
        return self._temp
    
    @temp.setter
    def temp(self, new_temp):
        print(f'Yes, Thermostat temp *setter* is running')
        
        if new_temp > 30:
            raise TempTooHighException('Too hot!')
            
        if new_temp < 10:
            raise TempTooLowException('Too cold!')
        
        self._temp = new_temp    
        
t = Thermostat()
print(t.temp)


# In[30]:


t.temp = 22


# In[31]:


t.temp = 0


# In[32]:


t.temp


# In[33]:


t.temp = 100


# In[34]:


t.temp


# In[35]:


Thermostat.temp


# # Exercise: Random History 
# 
# 1. Define a class, `RandHist`, that takes two integers (low and high limits) when you create the new instance.
# 2. When you retrieve from the instance's `number` attribute, you get a random integer between those limits. (A new random number each time!)
# 3. You can also ask for the `history` attribute, which is a list containing all previously retrieved random numbers.
# 4. Assigning to the `number` attribute zeroes out the historical list.
# 
# ```python
# rh = RandHist(0, 100)
# rh.number   # 5
# rh.number   # 36
# rh.number   # 12
# rh.history  # [5, 36, 12]
# 
# rh.number = 10
# rh.number   # 45
# rh.history  # [45]
# 
# random.randint(0, 100)  # get a random int from 0-100
# ```

# In[40]:


import random

class RandHist:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num
        self.history = []
        
    @property
    def number(self):
        n = random.randint(self.min_num, self.max_num)
        self.history.append(n)
        return n
    
    @number.setter
    def number(self, new_number):
        self.history = []
    
rh = RandHist(0, 100)    
rh.number


# In[41]:


rh.number


# In[42]:


rh.number


# In[43]:


rh.history


# In[ ]:





# In[44]:


rh.number = 1


# In[45]:


rh.history


# # Descriptors (and the descriptor protocol)
# 
# 1. If `a` is a class attribute
# 2. We access `a` via an instance (i.e., not the class)
# 3. If `a`'s class defines the method `__get__`, then that method is run and returned when we retrieve `a` (via the instance)
# 4. If `a`'s class defines the method `__set__`, then that method is run when we assign to `a` (via the instance)

# In[49]:


# our "PersonName" class is a string that cannot be empty and contains <= 10 characters
# (sorry, people with long names! )

class PersonName:
    def __init__(self, name=''):
        print('Now in PersonName.__init__')
        self._name = name
        
    def __get__(self, instance, container_class):
        print(f'{instance=}, {container_class=}')
        print(f'Now in PersonName.__get__')
        return self._name
        
class Person:
    person_name = PersonName()  # class attribute ('name')
    
p = Person()
p.person_name  # accessing the class attribute person_name via the instance


# In[50]:


Person.person_name


# In[53]:


# our "PersonName" class is a string that cannot be empty and contains <= 10 characters
# (sorry, people with long names! )

class PersonName:
    def __init__(self, name=''):
        print('Now in PersonName.__init__')
        self._name = name
        
    def __get__(self, instance, container_class):
        print(f'{instance=}, {container_class=}')
        print(f'Now in PersonName.__get__')
        return self._name
    
    def __set__(self, instance, new_value):
        print(f'{instance=}, {new_value=}')
        print(f'Now in PersonName.__set__')
        self._name = new_value
        
class Person:
    person_name = PersonName()  # class attribute ('name')
    
p = Person()
p.person_name  # accessing the class attribute person_name via the instance
p.person_name = 'hello'


# In[54]:


p.person_name


# In[56]:


# our "PersonName" class is a string that cannot be empty and contains <= 10 characters
# (sorry, people with long names! )

class PersonName:
    def __init__(self):
        print('Now in PersonName.__init__')
        self._name = {}
        
    def __get__(self, instance, container_class):
        print(f'{instance=}, {container_class=}')
        print(f'Now in PersonName.__get__')
        return self._name[instance]
    
    def __set__(self, instance, new_value):
        print(f'{instance=}, {new_value=}')
        print(f'Now in PersonName.__set__')
        self._name[instance] = new_value
        
class Person:
    person_name = PersonName()  # class attribute ('name')
    
p1 = Person()
p1.person_name = 'hello'

p2 = Person()
p2.person_name = 'goodbye'

p1.person_name


# In[58]:


p1.person_name


# In[59]:


p2.person_name


# In[64]:


# our "PersonName" class is a string that cannot be empty and contains <= 10 characters
# (sorry, people with long names! )

from weakref import WeakKeyDictionary

class PersonName:
    def __init__(self):
        print('Now in PersonName.__init__')
        self._name = WeakKeyDictionary()
        
#        PersonName    Person()    Person class
    def __get__(self, instance, container_class):
        print(f'{instance=}, {container_class=}')
        print(len(self._name))
        print(f'Now in PersonName.__get__')
        return self._name[instance]
    
    def __set__(self, instance, new_value):
        print(f'{instance=}, {new_value=}')
        print(len(self._name))
        print(f'Now in PersonName.__set__')
        self._name[instance] = new_value
        
class Person:
    person_name = PersonName()  # class attribute ('name')
    
p1 = Person()
p1.person_name = 'hello'

p2 = Person()
p2.person_name = 'goodbye'

p1.person_name


# In[65]:


p3 = Person()
p3.person_name = 'third'


# In[66]:


p3.person_name


# In[67]:


del(p1)


# In[68]:


del(p2)


# In[69]:


p3.person_name


# In[ ]:


a.b   # ICPO rule ... 


# # Tomorrow
# 
# 1. The iterator protocol
#     - Adding iteration to your classes
#     - Different techniques for that
# 2. Generator functions
# 3. Generator comprehensions
# 4. Decorators
# 5. Threading and multiprocessing 

# In[ ]:




