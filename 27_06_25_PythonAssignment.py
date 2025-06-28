# Find  outputs (Home  work)
a = ()
print(type(a)) # <class 'tuple'>
print(a) # ()
print(len(a)) # 0
b = tuple() 
print(b) # ()
print(len(b)) # 0
#  Gift
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a) # (10 , 20 , 30)
print(id(a)) # Address of a
a = a * 2 # (10 , 20 , 30 , 10 , 20 , 30)
print(a) # (10 , 20 , 30 , 10 , 20 , 30)
print(id(a)) # Address of a
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a) # {25 , 10.8 , 'Hyd' , True , 3+4j , None}
print(type(a)) # <class 'set'>
print(len(a)) # 6
print(a[2]) # Error : No indexing in set
print(a[1 : 4]) # Error : No slicing beccoz of no index
a[2] = 'Sec' # Error : No substituting
print(a * 2) # Error : No repeating in set becoz of duplicate elements will occur
print(a * a) # Error : unsupported operand type(s) for *: 'set' and 'set'
# Gift 
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a) # {1 , 'Hyd' , False , ''}
print(len(a)) # 4
print(type(a)) # <class 'set'>
#  set()  function demo  program
a = set('Rama rAo')
print(a) # {'R','a','m',' ','r','A','o'}
print(len(a)) # 7
print(set([10 , 20 , 15 , 20])) # {10, 20, 15}
print(set((25 , 10.8 , 'Hyd' , 10.8))) # {'Hyd', 25, 10.8}
print(set(range(10 , 20 , 3))) # {16, 10, 19, 13}
print(set(25)) # Error becoz int objct not iterable



'''
set()  function 
-----------------
1) What  does  set(sequence)  do ?  --->  Converts  sequence  to  set

2) Is  set(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  set(No  args)  do ?  ---> Returns  an  empty  set
'''
#  Gift
# Find  outputs  (Home  work)
a =   [ ]
b =   ( )
c =   { }
d =   set()
print(type(a)) # <class 'list'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'dict'>
print(type(d)) # <class 'set'>
print(a) # []
print(b) # ()
print(c) # {}
print(d) # set()
#  Gift
# add()  and  remove()  methods  (Home  work)
a = set()
a . add(25) 
a . add(10.8)
a . add('Hyd')
a . add(True)
a . add(None)
a . add('Hyd')
a . add(1)
print(a) # {25,10.8,'Hyd',True,None}
a . remove(25)
print(a) # {10.8,'Hyd',True,None}
a . append(100) # Error no append method in set
a . add(set()) # Error becoz set is mutable not support in set
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8} 
print('set with print function')#'set  with  print  function'
print(a) # How  to  print  set
print('Iterate  elements  of  set  with  for  loop') # 'Iterate  elements  of  set  with  for  loop'
for x in a:# How  to  iterate  set  with  for  loop
    print(x)


# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) # {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(a[10]) # Ramesh
print(a[20]) # Kiran
print(a[15]) # Amar
print(a[18]) # Sita
print(a[19]) # Error becoz there is no key 19
print(a[0]) # Error becoz there is no key 0
print(a['Amar']) # Error becoz only key to call value
a[15] = 'Krishna' # replace 'Amar' with 'Krishna'
del   a[20] # Deletes the key value pair 20 : 'Kiran'
a[25] = 'Vamsi' # Appends the new key value pair
print(a) # {10: 'Ramesh', 15: 'Krishna', 18: 'Sita', 25: 'Vamsi'}
print(len(a)) # 4
print(a * 2) # Error: unsupported operand type(s) for *: 'dict' and 'int'
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a) # {10 : 'Sec'}
print(len(a)) # 1
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b) # {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Black' , 'Y' : 'Yellow'}
print(len(b)) # 4
#  Gift 
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a) # {True : 'May  be'}
print(len(a)) # 1
# Find  outputs
a = { [ ] : 25} # Error becoz the key is mutable
b = { ( ) : 25} 
print(b) # {(): 25}
c = { { } : 25} # Error { } is mutable key
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d) # {'Ramesh': [9948250500, 9848565090, 9440250404]}
print(len(d)) # 1
e = {set() : 10.8} # Error becoz the set() is mutable
# Find  outputs
a = {}
print(type(a)) # <class 'dict'>
print(len(a)) # 0
print(a) # {}
b = dict()
print(type(b)) # <class 'dict'>
print(len(b)) # 0
print(b) # {}


# Gift
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function') # Dictionary  with  print  function
print(a) #How  to  print  dictionary
print(*a) # Keys  of  dictionary
for i in a:
     print(i) #How  to  print  each  key of  dictionary  with  for  loop
print('Values  of  dictionary')
for x in a:
     print(a[x]) #How  to  print  each  value  of  dictionary  with  for  loop
print('All  the  tuples  of  dict_items   object')
#How  to  print  each  tuple  of  dictionary  with  for  loop
print('Elements  of  each   tuple')
#How  to  print  elements  of  tuple   in  dictionary  with  for  loop
print('Keys  and  values  of  dictionary')
#How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value
# Gift
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
     }
print(type(a)) # Hyd <nxt line> Sec <nxt line> Cyb
print(a) # {None}
print(len(a)) # 1
#  Anonymous  object  demo  program
_ = 25
print(_) # 25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a) # 10
print(_) # 20
print(c) # 30
for  _  in  range(5):
	print(_ , 'Hello') # 0 Hello <nxt line> 1 Hello <nxt line> 2 Hello <nxt line> 3 Hello <nxt line> 4 Hello
#  Find  outputs
a = 25
print(id(a)) # Address of a
a = 35
print(id(a)) # diff Address of a
# Find  outputs (Home  work)
a = 25.7
print(id(a)) # Address of a
print(a) # 25.7
a = 35.6
print(id(a)) # diff Address of a 
print(a) # 35.6
b = True
print(id(b)) # Address of b
b = False
print(id(b)) # diff Address of b
c = None
print(id(c)) # Address of c
c = None
print(id(c)) # Same address of c
#  Find  outputs (Home  work)
a = 'Hyd'
print(id(a)) # Address of a
a[1] = 'e' # Error str doesn't support item assignment becoz it is immutable
a = 'Sec'
print(id(a)) # diff address of a
b = (10 , 20 , 15 , 18)
print(id(b)) # address of b
b[2] = 19 # Error becoz tuple is immutable
b = (30 , 40 , 35 , 32) 
print(id(b)) # diff address of b
c = range(5) 
print(id(c)) # address of c
c[3] = 10
c = range(5)
print(id(c)) # diff address of c
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b) # True
c = 'Hyd'
d = 'Hyd'
print(c  is  d) # True
e = False
f = False
print(e  is  f) # True
g = range(10)
h = range(10)
print(g  is  h) # False becoz range is immutable but not reusable
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b) # False becoz list is mutable not reusable
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d) # False becoz dict is mutable not reusable
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f) # True becoz tuple is immutable and resuable
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h) # False becoz set is mutable not resuable
# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) # 31.4
print(3 + 4j + 5 + 6j)  # 8+10j
print(True + False) # 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') # SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10 , 20 , 30 , 1 , 2 , 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25 , 10.8 , 'Hyd' , 3 + 4j , True , None)
print({10 , 20} + {30 , 40}) # Error: unsupported operand type(s) for +: 'set' and 'set'
print({10 : 'Hyd'} + {20 : 'Sec'})  # Error: unsupported operand type(s) for +: 'set' and 'set'
print(range(4) + range(5)) # Error: unsupported operand type(s) for +: 'range' and 'range'
print(10 + '20') # Error: unsupported operand type(s) for +: 'int' and 'str'
print([10 , 20 , 30] + 5) # Error: can only concatenate list (not "int") to list
print([10 , 20 , 30] + (40 , 50 , 60)) # Error: can only concatenate list (not "tuple") to list
# Find outputs (Home work)
print(25 * 3) # 75
print(10.8 * 25.6) # 276.48
print(True * False) # 0
print((3 + 4j) * (5 + 6j)) # 15 + 18j + 20j + 24(-1) = -9+38j
print(3 + 4j * 5 + 6j)  # 3 + 26j
print('25' * 3) # 252525
print(3 * '25') # 252525
print('Hyd' * 4) # HydHydHydHyd
print([10 , 20 , 15] * 2) # [10 , 20 , 15 , 10 , 20 , 15]
print((25, 10.8, 'Hyd', True) * 3) # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
#print([10 , 20 , 15] * 3.0) # Error: can't multiply sequence by non-int of type 'float'
#print({10 , 20 , 15} * 2) # Error becoz set can't have repeatation
#print({10 : 20 , 30 : 40} * 2)  # Error becoz dict can't have repeatation
#print([10] * [20]) # Error: can't multiply sequence by non-int of type 'list'
# Find outputs
print(7 / 0) # ZeroDivision Error
print(7 // 0) # ZeroDivision Error
print(7 % 0) # ZeroDivision Error
# ** operator demo program
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2) # 10 ^ -2 = 0.01
print(4 * 3 * 2) # 24
print(3 + 4 * 5 - 32 / 2 ** 3) # 3 + 20 - 32/8 ==> 23 - 4 = 19.0
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #  True  becoz  >  is  satisfied
print(9 >= 9)   #  True  becoz  =  is  satisfied
print(9 >= 12)   #  False  becoz    both  are  not  satisfied
print(6 <= 8) # True becoz < is satisfied
print(6 <= 6) # True becoz = is satisfied
print(6 <= 4) # False becoz    both  are  not  satisfied
print(9 != 7) # True
print(6 == 8) # False
print(True  >  False) # True
print(3 + 4j == 3 + 4j) # True
print(3 + 4j == 5 + 6j) # False
print(3 + 4j != 5 + 6j) # True
print(10 == 10.0) # True
print(3 + 4j >  3 + 4j) # Error: '>' not supported between instances of 'complex' and 'complex'
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita') # True becoz 'R' < 'S'
print('Hyd'  ==  'Hyd') # True
print('Rama'  <=   'Ramana') # True
print('Rama  Rao'  >=  'Rama') # True
print('Hyd'  != 'Sec') # True
print('HYD'  <   'hyd') # True



'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->  Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? ---> 1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  --->  512

5) What  is  the  range  of  unicode  values ?  --->  0  to  511

6) What  are  the  unicode  values  of  'A'  to  'Z'  ?  --->  65  to  90
    W…
'''# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)   # False becoz 2nd cond is not satisfied
print(1 < 2 < 3 < 4)  # True all are satisfied
print(1 < 2 > 3 > 1)  # False
print(4 > 3 >= 3 > 2) # True all are satisfied

#  Find  outputs
print({10 , 20}  |  {30 , 20})
print({10 : 'Hyd' , 20 : 'Sec'} |  {30 : 'Cyb' , 20 : 'Vja'})
print(range(4) | range(5))
#  and  operator  demo  program
print(True  and  False)    #  False
print(False  and  True)  #  False
print(False  and   False)  #   False
print(True  and  True)  # True
print(10  and  20)  #  20
print(0  and  20) #  0
print(-25  and  0)  #  0
print(''  and  25)
print(6j  and  'Hyd')
print(0j  and  'Sec')
print('Hyd'   and  10.8)
print(10  and  20  and  30)


''''
and  operator
----------------
1) When  is  the  result  of  and  operator  False ?  --->  When  at  least  one  operand  is  False
    When  is  the  result  of  and  operator  True ?  --->When  both  the  operands  are  True

2) What  is  the  result  of  op1  and  op2  when  op1  is  True ?  --->  op2
    What  is  the  result  of  op1  and  op2  when  op1  is  False ?  --->	op1

3) Is  0  True…  '''
#  or  operator  demo program
print(True  or  False)   #   True
print(False  or  True)   #  True
print(True  or  True) #  True
print(False  or   False)    # False
print(10  or  20)   #  10
print(0   or  20)  #   20
print(-25  or  0) #  -25
print(''  or  35) # 35
print(6j  or  'Hyd') # 6j
print(0.0  or  3 + 4j) # 3+4j
print('Hyd'   or   10.8) # Hyd



'''
or  operator
--------------
1) When  is  the  result  of  or  operator  True ?  --->  When  at  least  one  operand  is  True
    When  is  the  result  of  or  operator  False ?  ---> When  both  the  operands  are  False

2) What  is  the  result  of  op1  or  op2  when  op1  is  False ?  ---> op2
    What  is  the  result  of  op1  or  op2  when  op1  is  True ?  ---> op1

3) and ,  or  operators  are  quite  opposite
'''
# not  operator  demo  program
print(not  True)  #  False
print(not  False)  #  True
print(not  25) # False
print(not  0) # True
print(not  'Hyd') # False
print(not  '') # True
print(not  -10) # False
print(not  not  'Hyd') # True



'''
not  operator
----------------
1) What  does  not  operator  do ?  --->  Complement  operation

2) Is  not  a  unary  operator  ?  --->  Yes  due  to  single  operand
    What  about  and ,  or ? --->  Binary  operators  due  to  two  operands

3) What  is  the  associativity  of  unary  operators ?  --->  Right  to  Left
    What  is  the  associativity  of  binary  operators ?  --->  Left  to  Right  except  for  **
'''
#  Find   outputs (Home work)
i = 10
i = not  i > 14
print(i) # True
print(not(6 < 4  or  9 >= 5  and  6 != 6)) # True

#  Assignment  operators  demo  program  (Home  work)
a = 25 
print(a)  # 25
b =  a  
print(b)  # 25
print(a  is  b)  # True
x = 4
y = 5
z = x + y * 6  
print(z)  # 4 + 5 * 6 = 34
25 = a  # Error: cannot assign to literal
a + b = x + y 
# Find outputs (Home work)
a = b = c = 25  
print(id(a)) # address of a
print(id(b)) # same address of a 
print(id(c)) # same address of a
print(a , b , c) # 25 25 25
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'  
print(x) # 25
print(y) # 10.8
print(z) # Hyd
# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c # a * (b+c) = a * b + a * c = 3 * 4 + 3 * 5
print(a) # 27
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4  # a = a % (3+2*4) = 20 % 11
print(a) # 9
# Find outputs (Home work)
a = 3
a **= 4 # a ** 4
print(a) # 81
# Identity operators demo program
a = 25
b = 25
print(a is b) # True
print(a is not b) # False
print(a == b) # True



'''
Identity    operators
-------------------------
1) What  are  the  two  identity  operators ? --->  is  and  is  not

2) What  does  ref1  is  ref2  do ?  --->  Compares  references
     What  does   ref1 == ref2  do ?  ---> Compares  objects  pointed  by  ref1  and  ref2

3) What  is  the  result  of  ref1  is  ref2 ?  --->
														True  when  both  the  references  point  to  same  object  and  False  otherwise
    What  is  the  result  of  ref1  ==  ref2 ?  --->
	                                                             True  when  both  the  objects  have  same  value  and  False  otherwise

4) is  and  is  not  are  quite  opposite  operators
'''
# Find outputs (Home work)
a = 25 
b = 25.0  
print(a is b) # False
print(a is not b) # True
print(a == b) # True
# Find outputs (Home work)
a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) # True
print(a  is  not  b)  # False
print(a == b) # True
print()
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y) # False because it mutable 
print(x  is  not  y) # True
print(x == y) # True
print()
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)  
print(m  is  n) # True becoz immutable
print(m  is  not  n) # False
print(m == n) # True
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list) # True
print(19 in list) # False
print(14 not in list) # True
print(15 not in list) # False
s = 'Hyd is green city'
print( 'is' in s) # True
print('was' in s) # False
print('g' in s) # True
print('z' in s) # False
print(' ' in s) # True
print('gre' in s) # True
print('yd i' in s) # True
print('' in s) # True
print('' not in s) # False



'''
Membership    operators
------------------------------
1) What  are  the  two  membership  operators ?  --->  in  and  not  in

2) What  is  the  syntax  of  'in'  operator ?  --->  element  in  sequence

3) What  does  in  operator  do ? --->  Returns  True  when  element  is  in  the  sequence  and  False  otherwise

4) What  does  not  in  operator  do ? --->  Quite  opposite  to  in  operator
'''
#  ++  and  --  operators  demo  program
a = 25
print(++a)  #  +(+a) = +a = 25
print(a++) #  (a+)+  = a+ = 25+  throws  error
print(a++1)  # a + (+1)  =  25 + 1 = 26
print(--a) # -(-a) = +25
print(a--) # (a-)- = 25+ throws error
print(a--1) # (a-)-1 = 25+1 = 26
print(-a) # -25
print(+-a) # -25
print(-+a) # -25
#  Semicolon  demo  program
print('One'); # One
print('Two'); # Two
print('Three'); # Three
print('Hyd')  ; print('Sec')  ;  print('Cyb'); # Hyd <nxt line> Sec <next line> Cyb
#  floor()  and  ceil()  functions  demo  program
import math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0)) # Previous  integer of 25
print(math . ceil(25.0)) # Next  integer  of 25
print(math . floor(-3.5)) # Previous  integer of -4
print(math . ceil(-3.5)) # Next  integer  of -3
print(math . floor(-9.0)) # Previous  integer of -9
print(math . ceil(-9.0)) # Next  integer  of -9
print(math . floor(25.1)) # Previous  integer of 25
print(math . ceil(25.1)) # Next  integer  of 26
print(floor(3.5)) # Error becoz no math module
print(ceil(3.5)) # Error becoz no math module 



'''
1) What  does  floor(x)  do ?  --->  Returns  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  next  integer  of  'x'
'''
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8)) # 35.8
print(abs(-27)) # 27
print(abs(29.5)) # 29.5
print(abs(32)) # 32
import  builtins
print(builtins . abs(-25)) # 25
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 10.8
import  builtins
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2)) # 0.01
print(pow(4 , pow(3 , 2))) # 262144
import  builtins
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) # -0.125
#Find outputs
import keyword #How  to  import   kw  list
print(keyword.kwlist)#How  to  print  kwlist
print(len(keyword.kwlist))#How  to  print  number  of  keywords
print(type(keyword.kwlist))#How  to  print  type  of kwlist
print(keyword . kwlist)
#  Find  outputs  (Home  work)
import keyword#How  to  import   keyword  module
print(keyword.kwlist) # How  to  print  kwlist
print(len(keyword.kwlist)) # How  to  print  number  of  keywords
print(type(keyword.kwlist)) # How  to  print  type  of kwlist
print(keyword.kwlist)

# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False')) # Converts 'False' to False
print(eval('3+4j')) # Converts '3+4j' to (3+4j)
print(eval("    'Hyd'   ")) #    'Hyd'  to   Hyd
print(eval('3 + 4 * 5')) # '3+4*5' to 23
print(eval('[10 , 20 , 15 , 18]')) # [10,20,15,18]
print(eval('{10,20,15,18,20,12,18}')) # 10,20,15,12,18}
print(eval('(10 , 20 , 30)')) # (10,20,30)
print(eval("{10 : 'Hyd' , 10 : 'Sec'}")) # {10 : 'Sec'}
#print(eval(4 + 5)) # Error becoz of no codes inside eval



# Gift
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec')) # 25
print(eval(sec)) # 25
cyb = 10.8 
print(eval('cyb')) # 10.8
#print(eval(cyb)) # Error: eval() arg 1 must be a string, bytes or code object
#  Gift
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd <nl> None
#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False
print(eval('  ""  ')) # empty
#print(eval('')) # Error: invalid syntax
print(eval('  " "   ')) # empty
#print(eval(' ')) # Error: invalid syntax
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x)) # <class 'int'>
print(x) # 25
# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ') # Hyderabad
print(len(a)) # 9
print(a) # Hyderabad
b = eval(input('Enter   any  string  : ')) # 'SaiRam'
print(len(b)) # 6
print(b) # SaiRam
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t') # 25  10.8    Hyd
print(a , b , c , sep = '---') # 25---10.8---Hyd
print(a , b , c , sep = '\n') # 25 <next line> 10.8 <next line> Hyd
print(a , b , c) # 25 <next line> 10.8 <next line> Hyd
#print(a , b , c , separator = ':') # Error becoz of separator can use sep


# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---') # 25 10.8 Hyd---
print(a , b , c , sep = ',,,') # 25 , 10.8 , Hyd
print(a , b , c , sep = ':::' , end = '\t\t\t') # 25:::10.8:::Hyd <tab> <tab> <tab>
print(a , b , c) # 25 10.8 Hyd
# Find outputs  (Home  work)
print('Hyd') # Hyd
print()
print('Sec') # Sec
print()
print('Cyb') # Cyb'''
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]  
t = (10 , 20 , 30 , 40)  
s = {10 , 20 , 30 , 40} 
print(l , t , s) # [10 , 20 , 30 , 40] (10 , 20 , 30 , 40) {10 , 20 , 30 , 40}
