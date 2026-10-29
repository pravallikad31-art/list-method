Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a = [6,7.8,"python",8+9j,True,False]
a
[6, 7.8, 'python', (8+9j), True, False]
type(a)
<class 'list'>
b=2.3
type(b)
<class 'float'>
b = [2.3]
type(b)
<class 'list'>

#list methods
#append()
a = ["python","java","c","c++"]
a.append("c#")
a
['python', 'java', 'c', 'c++', 'c#']
a.append("go","R")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("go","R")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["go","R"])
a
['python', 'java', 'c', 'c++', 'c#', ['go', 'R']]

#extend()
a.extend("go","R")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.extend("go","R")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["go","R"])
a
['python', 'java', 'c', 'c++', 'c#', ['go', 'R'], 'go', 'R']

b = ["python","R programming","c"]
b.extend(["ml","dl"])
b
['python', 'R programming', 'c', 'ml', 'dl']

#insert(position,data)
c=["ml","dl","c","c++"]
c.insert(3,"go")
c
['ml', 'dl', 'c', 'go', 'c++']

a =["green","white"]
a.insert(1,"red")
a
['green', 'red', 'white']

#index
a=["apple","mango","kiwi"]
a.index("mango")
1
a.index("apple")
0

#copy()
a
['apple', 'mango', 'kiwi']
a.copy()
['apple', 'mango', 'kiwi']
b=a.copy()
b
['apple', 'mango', 'kiwi']

#pop()
a=["vja","vzg","hyd"]
a.pop()
'hyd'
a
['vja', 'vzg']
a.pop("vja")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.pop("vja")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(0)
'vja'
a
['vzg']
a.pop(1)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.pop(1)
IndexError: pop index out of range
a.pop(0)
'vzg'
a
[]

#remove
a = ["hi","hello","how"]
a
['hi', 'hello', 'how']
a.remove("hello")
a
['hi', 'how']
a.remove(1)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    a.remove(1)
ValueError: list.remove(x): x not in list

#clear()
a = ["rose","lily"]
a.clear()
a
[]
a.append("bhoomi")
a
['bhoomi']
a.expend("sai","venkat")
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.expend("sai","venkat")
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
a.expend(["sai","venkat"])
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a.expend(["sai","venkat"])
AttributeError: 'list' object has no attribute 'expend'. Did you mean: 'extend'?
a.extend(["sai","venkat"])
a
['bhoomi', 'sai', 'venkat']

#sort()
a=["banana","apple","kiwi","grapes"]
a.sort()
a
['apple', 'banana', 'grapes', 'kiwi']
b = [0,9,8,4,5]
b.sort()
b
[0, 4, 5, 8, 9]
c=[8+9j,2+5j] #not combine the str and int
c.sort()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    c.sort()
TypeError: '<' not supported between instances of 'complex' and 'complex'
d=[2,3.4,"hi","hello",True,False]
d.sort()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
g = [8.3,4.5,6.7,1.2]
g.sort()
g
[1.2, 4.5, 6.7, 8.3]
b = [True,False,False,True]
>>> b.sort()
>>> b
[False, False, True, True]
>>> 
>>> #reverse()
>>> a = [9,7,6,4,9,3]
>>> a.reverse()
>>> a
[3, 9, 4, 6, 7, 9]
>>> b = ["yellow","grey","blue"]
>>> b.reverse()
>>> b
['blue', 'grey', 'yellow']
>>> 
>>> #len()
>>> a=["java","dl","ai"]
>>> len(a)
3
>>> b="java"
>>> len(b)
4
>>> b=["java"]
>>> len(b)
1
>>> 
>>> #count
>>> a.copy()
['java', 'dl', 'ai']
>>> a.count("dl")
1
>>> a.count("a")
0
>>> b = ["java","python","c","ai"]
>>> b.count("python")
1
