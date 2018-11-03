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
### Output:
<pre>
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]
</pre

### Example:3-
<pre>
a=[[10,20,30],[40,50,60],[70,80,90]]
print(a)
for p,q,r in a:
    print(p,q,r)
</pre>
### Output:
<pre>
[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
10 20 30
40 50 60
70 80 90
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
</pre
