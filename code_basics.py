```python
s='sathish'
print(5*'sathish')
```

    sathishsathishsathishsathishsathish
    

if its the   + operators both should be string type only

# write a program to read string from the keyboard and print its characters in both forward and backward direction?


```python
s=input('enter any string:')
print('character in forward direction')
i=0
while i<len(s):
    print(s[i])
    i=i+1
    
```

    enter any string:sathish full stock developer
    character in forward direction
    s
    a
    t
    h
    i
    s
    h
     
    f
    u
    l
    l
     
    s
    t
    o
    c
    k
     
    d
    e
    v
    e
    l
    o
    p
    e
    r
    


```python

print('character in forward direction')
i=0
while i<len(s):
    print(s[i])
    i=i+1
s=input('enter any string:')
print('character in backward direction')
i=-1
while i>=-len(s):
    print(s[i])
    i=i-1
```

    character in forward direction
    s
    a
    t
    h
    i
    s
    h
    enter any string:sathish
    character in backward direction
    h
    s
    i
    h
    t
    a
    s
    


```python
s=input('enter any string:')
s='sathish'
for x in s:
    print(x)
```

    enter any string:sathish
    s
    a
    t
    h
    i
    s
    h
    


```python
s=input('enter any string:')
for x in s[::-1]:
    print(x)
    

```

    enter any string:sathish
    h
    s
    i
    h
    t
    a
    s
    


```python
s1= 'babitha'
print('b' in s)
```

    False
    


```python
s1= 'babitha'
print('a' in s1)
```

    True
    


```python
s2= 'darshanala'
print('h' in s2)
```

    True
    


```python
print('o' in s2)
```

    False
    


```python
s= 'abcdefghijklmnopqrstuvwxyz'
s[1:0]
```




    ''




```python
s=input('enter any string:')
print('characters in forward direction')
for x in s:
    print(x)
    
```

    enter any string:sathish
    characters in forward direction
    s
    a
    t
    h
    i
    s
    h
    


```python
s=input('enter any string:')
print('the character in forward direction')
i=0
while i<len(s):
    print(s[i])
    i=i+1
    
```

    enter any string:darshanala
    the character in forward direction
    d
    a
    r
    s
    h
    a
    n
    a
    l
    a
    


```python
s='abcdefghij'# a b c d e f g h i j
                0 1 2 3 4 5 6 7 8 9
s[1:6:2]

```




    'bdf'




```python
s[::1]
```




    'abcdefghij'




```python
s[::-1]
```




    'jihgfedcba'




```python
s[3:7:-1]
```




    ''




```python
s[7:4:-1]
```




    'hgf'




```python
s=(input('enter any string:'))
print('the character in forward index')
i=0
while i<len(s):
    print(s[i])
    i=i+1
```

    enter any string:sathish
    the character in forward index
    s
    a
    t
    h
    i
    s
    h
    


```python
s=(input('enter any string:'))
for x in s[::-1]:
    print(x)
```

    enter any string:darshanala
    a
    l
    a
    n
    a
    h
    s
    r
    a
    d
    


```python
                
s1='abcdefghij'#
s1[-4:1-2]
```




    'ghi'




```python
[0:-10:-1]
```


```python
s[1:7:3]
```




    'be'




```python
s=(input('enter any value:'))
print('the character in forward direction')
i=0
while i<len(s):
    print(s[i])
    i=i+1
```

    enter any value:sathish
    the character in forward direction
    s
    a
    t
    h
    i
    s
    h
    


```python
s=(input('enter any value:'))
for x in s:
    print(x)
```

    enter any value:sathish
    s
    a
    t
    h
    i
    s
    h
    


```python
s=input('enter any value:')
i=-1
while i>=0 -len(s):
    print(s[i])
    i=i-1
```

    enter any value:susmitha sen
    n
    e
    s
     
    a
    h
    t
    i
    m
    s
    u
    s
    


```python

```


```python

```
