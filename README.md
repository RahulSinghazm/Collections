# Collections

* Collection types represented closes objects are stored in group of objects(elements).
* Collection types represented closes objects are iterable objects.
* Every collection type represented class provides, methods to perform operations on elements of those objects.

#### Python supports following collection types......
<pre>
1.List
2.Tuple
3.Set
4.Dict
</pre>

## List:-

* List objects can be created by using [ ] square brackets or by calling list functions.
* List objects are mutable objects.
* List can be muatable or immutable
* Insertion order is reserved list.
* Duplicate elements are allow in list.
* Hetrogenious elements are allow in list.
* List supports both + and - indexing.
* List is a iterables type.

### Example:
<pre>
a=[]
print(a)
print(type(a))
print(id(a))
print(len(a))

b=list()
print(b)
print(type(b))
print(id(b))
print(len(b))

c=[10,20,30,40,50]
print(c)
print(type(c))
print(id(c))
print(len(c))

d=[10,123.123,3+4j,True,'Rahul Singh']
print(d)
print(type(d))
print(id(d))
print(len(d))

e=[1,2,3,1,2,1]
print(e)
print(type(e))
print(id(e))
print(len(e))

f=list('Rahul Singh')
print(f)
print(type(f))
print(id(f))
print(len(f))

</pre>

### Output:
<pre>
[]
class 'list'
1867365174728
0
[]
class 'list'
1867367625288
0
[10, 20, 30, 40, 50]
class 'list'
1867365174088
5
[10, 123.123, (3+4j), True, 'Rahul Singh']
class 'list'
1867365173000
5
[1, 2, 3, 1, 2, 1]
class 'list'
1867365173512
6
['R', 'a', 'h', 'u', 'l', ' ', 'S', 'i', 'n', 'g', 'h']
class 'list'
1867367625352
11
</pre>

### Example:2-
<pre>
a=[10,20,30,40,50,60]
print(a)
print(a[2])
print(a[-2])
print(a[1:4])
print(a[4:1])
print(a[-4:-1])

a[2]=123
print(a)
</pre>

### Output:
<pre>
[10, 20, 30, 40, 50, 60]
30
50
[20, 30, 40]
[]
[30, 40, 50]
[10, 20, 123, 40, 50, 60]
</pre>

### Example:3-
<pre>
a=[10,20,30,40,50,60]
print(a)
s=0
for p in a:
    s=s+p
    print(s)
    i=0
    s2=0
    while i<len(a):
        s2=s2+a[i]
        i=i+1
print(s2)
</pre>
</pre>
### Output:
<pre>
[10, 20, 30, 40, 50, 60]
10
30
60
100
150
210
210
</pre>

## Nested List:-
a list can even have another list as an item. This is called nested list

### Example:
<pre>
a=[[10,20,30],[40,50,60],[70,80,90]]
print(a)
for p in a:
    print(type(p))
    for q in p:
        print(q)
</pre>   
 
### Output:
<pre>
 [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
class 'list'
10
20
30
class 'list'
40
50
60
class 'list'
70
80
90
</pre>

### Example:2-
<pre>
a=[[10,20,30],[40,50,60],[70,80,90]]
print(a)
for q in a:
    print(q, end="")
    print()
</pre>
</pre>

### Output:
<pre>
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
</pre>
</pre>

### Example:3-
<pre>
a=[[10,20,30],[40,50,60],[70,80,90]]
print(a)
for p,q,r in a:
    print(p,q,r)
</pre>
</pre>

### Output:
<pre>
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
10 20 30
40 50 60
70 80 90
</pre>
</pre>

### Example:4-
<pre>
a=[[1001,'Rahul',8000.00],[3003,'Rohit',6000.00],[2002,'Alok',4000.00]]
print('Befor Sorting')
for p in a:
    print(p)
a.sort()
print('After Sorting')
for q in a:
    print(q)
</pre>

### Output:

<pre>
Befor Sorting
[1001, 'Rahul', 8000.0]
[3003, 'Rohit', 6000.0]
[2002, 'Alok', 4000.0]
After Sorting
[1001, 'Rahul', 8000.0]
[2002, 'Alok', 4000.0]
[3003, 'Rohit', 6000.0]
</pre>

</pre>

## Tuple:
* Tuple object can be created by using parenthesis () or by calling tuple 
function or by assigning  multiple values to a single variable.
* Tuple objects are immutable objects
* Insertion order is preserved
* Duplicate elements are allowed
* Hetrogenious elements are allowed
* Tuple supports both positive and negative indexing
* The elements of the tuple can be mutable or immutable

### Example:-
<pre>
a=()
print(a)
print(type(a))
print(id(a))
print(len(a))
b=tuple()
print(b)
print(type(b))
print(id(b))
print(len(b))
c=10,20
print(c)
print(type(c))
print(id(c))
print(len(c))
d=(10,20,30,40,50,10,20,10)
print(d)
print(type(d))
print(id(d))
print(len(d))
e=(100,123.123,True,123+7j,"Rahul Singh")
print(e)
print(type(e))
print(id(e))
print(len(e))

</pre>
### Output:
<pre>
()
class 'tuple'
2097271734344
0
()
class 'tuple'
2097271734344
0
(10, 20)
class 'tuple'
2097312005576
2
(10, 20, 30, 40, 50, 10, 20, 10)
class 'tuple'
2097311922776
8
(100, 123.123, True, (123+7j), 'Rahul Singh')
class 'tuple'
2097311835680
5
</pre>

### Example:-
<pre>
a=((10,20,30),[40,50,60],(70,80,90))
print(a)
for p in a:
    print(p,type(p))
    a[1][1]=100
    print(a)

</pre>

### Output:
<pre>
((10, 20, 30), [40, 50, 60], (70, 80, 90))
(10, 20, 30) class 'tuple'
((10, 20, 30), [40, 100, 60], (70, 80, 90))
[40, 100, 60] class 'list'
((10, 20, 30), [40, 100, 60], (70, 80, 90))
(70, 80, 90) class 'tuple'
((10, 20, 30), [40, 100, 60], (70, 80, 90))
</pre>

### Example:-
<pre>
a=((10,20,30),(40,50,60),(70,80,90))
print(a)
for p in a:
    print(p)
    for q in p:
        print(q)

</pre>

### Output:
<pre>
((10, 20, 30), (40, 50, 60), (70, 80, 90))
(10, 20, 30)
10
20
30
(40, 50, 60)
40
50
60
(70, 80, 90)
70
80
90
</pre>


## Different between List and Tuple:
<pre>List                                                          Tuple</pre>
<pre>
1.List object are mutable object                   Tuple object are immutable object.

2.Applying iterable on list object                 Applying iterable on tuple object  
  takes more time                                  takes less time.                                                      
                                           
3.If the frequent operation is                      If the frequent operation is retriveal
  insertion or deletion of the                      of the elements then it is recommended 
  elements then it is recommended                    to use tuple.
  to use list
 
4.List cannot be use as a 'Key'                     Tuple can be use as a 'Key' for the 
  for the Dictionar                                 Dictionary if the tuple is storing only 
                                                    immutable elements.
 
5.List object cannot use as                         Tuple object can use as elements of the
  elements of Set                                   set.
  </pre>
  
  
  
  ## Set:
  * Set object can be created by using only braces or curlly or {} or by calling set function or set().
  * Insertion order is nor preserve in set.
  * Duplicates elements is not allowed.
  * Hetrogenious elements are allowed in set.
  * Set is not support indexing.
  * Set object are mutable object.
  * Elements of the set must be immutable.
  * We can perform the mathmeticals set operations like Union,InterSection, and difference and Symmetric differnt on set objects.
  
  
  ### Example:
  <pre>
  a={10}
print(a)
print(type(a))
print(len(a))
print(id(a))

b=set()
print(b)
print(type(b))
print(len(b))
print(id(b))

c={10,20,30,40,50}
print(c)

d={10,20,10,20,10,30}
print(d)

e={100,123.123,True,3+5j,"Rahul Singh"}
print(e)

p,q,r,s,t=e
print(e)
print(type(p))
print(type(q))
print(type(r))
print(type(s))
print(type(t))

  </pre>
  
### Output:
<pre>
{10}
class 'set'
1
2212222840616
set()
class 'set'
0
2212222839944
{40, 10, 50, 20, 30}
{10, 20, 30}
{True, 'Rahul Singh', 100, (3+5j), 123.123}
{True, 'Rahul Singh', 100, (3+5j), 123.123}
class 'bool'
class 'str'
class 'int'
class 'complex'
class 'float'
</pre>

* Tuple can be stored in set , as it is immutable object.
* Set in set also not possible in set, because set in set is immutable.

### Example:
<pre>
a={10,20,30,40,50}
print(a)
print(30 in a)
print(25 in a)
for p in a:
    print(p)
b={(10,20,30),(40,50,60),(70,80,90)}
print(a)
for q in b:
    print(q,type(q))
</pre>

### Output:
<pre>
 ======
{40, 10, 50, 20, 30}
True
False
40
10
50
20
30
{40, 10, 50, 20, 30}
(10, 20, 30) <class 'tuple'>
(40, 50, 60) <class 'tuple'>
(70, 80, 90) <class 'tuple'>

</pre>

* If tuple contains immutable elements then only we can use the tuple in the set.

### Example:
<pre>
a={(10,20,30),(40,50,60,[1,2,3]),(70,80,90)}
print(a)

</pre>

### Output:
<pre>
Traceback (most recent call last):
  File "C:\Users\Rahul SIngh\AppData\Local\Programs\Python\Python37\Test1.py", line 1, in <module>
    a={(10,20,30),(40,50,60,[1,2,3]),(70,80,90)}
TypeError: unhashable type: 'list
</pre>

* Discard method will not display any error if given no. is not 'Set'.
* Remove method will display 'Key Error' if given no. is not in 'Set'.

### Example:
<pre>
a={10,20,30,40,50}
print(a)
a.add(60)
print(a)
y=a.copy()
print(y)
a.remove(20)
print(a)
a.pop()
print(a)
a.discard(30)
print(a)
a.clear()
print(a)
b=[10,20,30,20,10,30]
print(b)
c=set(b)
print(c)
print(b)

</pre>

### Output:
<pre>
{40, 10, 50, 20, 30}
{40, 10, 50, 20, 60, 30}
{50, 20, 40, 10, 60, 30}
{40, 10, 50, 60, 30}
{10, 50, 60, 30}
{10, 50, 60}
set()
[10, 20, 30, 20, 10, 30]
{10, 20, 30}
[10, 20, 30, 20, 10, 30]
</pre>

### * We can perform the mathmeticals set operations like Union,InterSection, and difference and Symmetric differnt on set objects.


### Example:
<pre>
a={1,2,3,4,5}
print(a)
b={4,5,6,7,8}
print(b)
print(a|b)
print(b|a)
print(a.union(b))
print(b.union(a))
print(a&b)
print(b&a)
print(a.intersection(b))
print(b.intersection(a))
print(a-b)
print(b-a)
print(a.difference(b))
print(b.difference(a))
print(a^b)
print(b^a)
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

</pre>

### Output:
<pre>
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
{1, 2, 3, 4, 5, 6, 7, 8}
{4, 5}
{4, 5}
{4, 5}
{4, 5}
{1, 2, 3}
{8, 6, 7}
{1, 2, 3}
{8, 6, 7}
{1, 2, 3, 6, 7, 8}
{1, 2, 3, 6, 7, 8}
{1, 2, 3, 6, 7, 8}
{1, 2, 3, 6, 7, 8}
</pre>


### Example:
<pre>
a=[10,20,10,30,10,20]
print(a)
b=set(a)
print(b)
c='Rahul Rohit'
print(c)
d=set(c)
print(d)

</pre>

### Output:
<pre>
[10, 20, 10, 30, 10, 20]
{10, 20, 30}
Rahul Rohit
{'a', 'i', 'u', 'o', 't', 'R', 'l', 'h', ' '}
</pre>

## Set Comprehension:
* The concept of generating the elements into the set objects by writing some logic in the set is know as 'Set Comprehension'.

### Example:
<pre>
a={p for p in range(10)}
print(a)
b={q*q for q in range(10,20) if q%2==0}
print(b)
c={r for r in range(20,30) if r%2!=0}
print(c)
</pre>

### Output:
<pre>
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
{256, 196, 100, 324, 144}
{21, 23, 25, 27, 29}
</pre>
