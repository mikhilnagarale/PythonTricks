
#is operator compares the object from their actual references.
#== operator compares the objects onlyby it's contents

#Ref - https://www.youtube.com/watch?v=CZ8bZPqtwU0

#Eg-

>>> a=[1,2,3]
>>> b=a
>>> a is b
True
>>> a == b
True
>>> a[0]='hello'
>>> a
['hello', 2, 3]
>>> b
['hello', 2, 3]
>>> a is b
True
>>> a == b
True
>>> c = list(a)
>>> a
['hello', 2, 3]
>>> b
['hello', 2, 3]
>>> c
['hello', 2, 3]
>>> a is c
False
>>> a == c
True
>>> b is c
False
>>> b == c
True
>>> a
['hello', 2, 3]
>>> b
['hello', 2, 3]
>>> c
['hello', 2, 3]
>>> a[0] = 1
>>> a
[1, 2, 3]
>>> b
[1, 2, 3]
>>> c
['hello', 2, 3]
>>>

