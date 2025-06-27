# Write  a  program  to  remove  all  15's  from  the  list
a = [10 , 20 , 15 , 18 , 12 , 15 , 19 , 25 , 15 , 14 , 12]
while  15 in a: # Repeat  until  there  is  no  15  in  the  list
	a.remove(15) # How  to  remove  each  15  from  the  list
print(a)


'''
while  cond:
		statements
statements
'''
#  Find  outputs  (Home  work)
a = (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(a) # (25 , 10.8 , 'Hyd' , True , 3+4j , None , 'Hyd' , 25)
print(*a) # 25 10.8 'Hyd' True 3+4j None 'Hyd' 25
print(type(a)) # <class'tuple'>
print(len(a)) # 8
print(a[2 : 5]) # ('Hyd' , True , 3+4j)
print(*a[2 : 5]) # 'Hyd' True 3+4j
a[2] = 'Sec'
a . append('Sec') # Error becoz no append method in tuple
a . remove('Hyd') # Error becoz no remove method in tuple
b =  10 , 20 , 30
print(b) # (10 , 20 , 30)
print(b * 2) # (10 , 20 , 30 , 10 , 20 , 30)
c = 40 , 50 , 60,
print(c) # (40 , 50 , 60)
print(type(c)) # <class'tuple'>
# Find  outputs  (Home  work)
a = (25)
b = 25,
c = 25
d = (25,)
print(type(a)) # <class 'int'>
print(type(b)) # <class 'tuple'>
print(type(c)) # <class 'int'>
print(type(d)) # <class 'tuple'>
print(a * 4) # 100
print(b * 4) # (25,25,25,25)
print(c * 4) # 100
print(d * 4) # (25,25,25,25)
# tuple()  function  demo  program  (Home  work)
a = tuple('Hyd')
print(a) # ('H','y','d')
print(type(a)) # <class'tuple'>
print(len(a)) # 3
b = [10 , 20 , 15 , 18]
print(tuple(b)) # (10 , 20 , 15 , 18)
print(tuple(range(5))) # (0,1,2,3,4)
print(tuple(25)) # Error becoz it is an int datatype



'''
tuple()  function
-------------------
1) What  does  tuple(sequence)  do ?  --->  Converts  sequence  to  tuple

2) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  tuple(No  args)  do ?  --->  Returns  an  empty  tuple
'''
# Find  outputs (Home  work)
a = ()
print(type(a))
print(a)
print(len(a))
b = tuple()
print(b)
print(len(b))
#  Gift
# Find  outputs (Home  work)
a = (10 , 20 , 30)
print(a)
print(id(a))
a = a * 2
print(a)
print(id(a))
#  set  object  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True , 3+4j , None , 25 , 'Hyd'}
print(a)
print(type(a))
print(len(a))
print(a[2])
print(a[1 : 4])
a[2] = 'Sec'
print(a * 2)
print(a * a)
# Gift 
# Find  outputs (Home  work)
a = {1 , 'Hyd' , False , True , 0.0 , '' , 1.0 ,  0}
print(a)
print(len(a))
print(type(a))
#  set()  function demo  program
a = set('Rama rAo')
print(a)
print(len(a))
print(set([10 , 20 , 15 , 20]))
print(set((25 , 10.8 , 'Hyd' , 10.8)))
print(set(range(10 , 20 , 3)))
print(set(25))



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
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(a)
print(b)
print(c)
print(d)
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
print(a)
a . remove(25)
print(a)
a . append(100)
a . add(set())
# How  to  print  set  in  two  differnet ways  (Home  work)
a = {25 , True , 'Hyd' , 10.8}
print('set  with  print  function')
print(How  to  print  set)
print('Iterate  elements  of  set  with  for  loop')
How  to  iterate  set  with  for  loop
------------------------------
18th February 25
# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a)
print(type(a))
print(a[10])
print(a[20])
print(a[15])
print(a[18])
print(a[19])
print(a[0])
print(a['Amar'])
a[15] = 'Krishna'
del   a[20]
a[25] = 'Vamsi'
print(a)
print(len(a))
print(a * 2)
# Find  outputs  (Home  work)
a = {10 : 'Hyd' , 10 : 'Sec'}
print(a)
print(len(a))
b = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue' , 'Y' : 'Yellow' , 'G' : 'Gray' , 'B' : 'Black'}
print(b)
print(len(b))
#  Gift 
# Find output  (Home  work)
a = {True : 'Yes' , 1 : 'No' , 1.0 : 'May  be'}
print(a)
print(len(a))
# Find  outputs
a = { [ ] : 25}
b = { ( ) : 25}
print(b)
c = { { } : 25}
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]}
print(d)
print(len(d))
e = {set() : 10.8}
# Find  outputs
a = {}
print(type(a))
print(len(a))
print(a)
b = dict()
print(type(b))
print(len(b))
print(b)
----------------------------------------
19th February 25
# Gift
# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(How  to  print  dictionary)
print('Keys  of  dictionary')
How  to  print  each  key of  dictionary  with  for  loop
print('Values  of  dictionary')
How  to  print  each  value  of  dictionary  with  for  loop
print('All  the  tuples  of  dict_items   object')
How  to  print  each  tuple  of  dictionary  with  for  loop
print('Elements  of  each   tuple')
How  to  print  elements  of  tuple   in  dictionary  with  for  loop
print('Keys  and  values  of  dictionary')
How  to  print  each  key of  dictionary  with  for  loop  along   with  corresponding  value
# Gift
#  Find  outputs (Home  work)
a = {
		print('Hyd') ,
		print('Sec') ,
		print('Cyb')
     }
print(type(a))
print(a)
print(len(a))
#  Anonymous  object  demo  program
_ = 25
print(_)
print(type(_))
a , _ , c = 10 , 20 , 30
print(a)
print(_)
print(c)
for  _  in  range(5):
	print(_ , 'Hello')
#  Find  outputs
a = 25
print(id(a))
a = 35
print(id(a))
# Find  outputs (Home  work)
a = 25.7
print(id(a))
print(a)
a = 35.6
print(id(a))
print(a)
b = True
print(id(b))
b = False
print(id(b))
c = None
print(id(c))
c = None
print(id(c))
#  Find  outputs (Home  work)
a = 'Hyd'
print(id(a))
a[1] = 'e'
a = 'Sec'
print(id(a))
b = (10 , 20 , 15 , 18)
print(id(b))
b[2] = 19
b = (30 , 40 , 35 , 32)
print(id(b))
c = range(5)
print(id(c))
c[3] = 10
c = range(5)
print(id(c))
# Find  outputs  (Home  work)
a = 25
b = 25
print(a  is  b)
c = 'Hyd'
d = 'Hyd'
print(c  is  d)
e = False
f = False
print(e  is  f)
g = range(10)
h = range(10)
print(g  is  h)
#Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a  is  b)
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c  is  d)
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e  is  f)
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g  is  h)
# Find outputs (Home work)
print(10 + 20)
print(10.8 + 20.6) 
print(3 + 4j + 5 + 6j) 
print(True + False) 
print('Hyder' + 'abad') 
print('Sankar' + 'Dayal' + 'Sarma') 
print('10' + '20') 
print([10 , 20 , 30] + [1 , 2 , 3]) 
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) 
print({10 , 20} + {30 , 40})
print({10 : 'Hyd'} + {20 : 'Sec'}) 
print(range(4) + range(5)) 
print(10 + '20')
print([10 , 20 , 30] + 5) 
print([10 , 20 , 30] + (40 , 50 , 60))
# Find outputs (Home work)
print(25 * 3)
print(10.8 * 25.6) 
print(True * False) 
print((3 + 4j) * (5 + 6j)) 
print(3 + 4j * 5 + 6j) 
print('25' * 3) 
print(3 * '25') 
print('Hyd' * 4)
print([10 , 20 , 15] * 2) 
print((25, 10.8, 'Hyd', True) * 3) 
print([10 , 20 , 15] * 3.0) 
print({10 , 20 , 15} * 2) 
print({10 : 20 , 30 : 40} * 2) 
print([10] * [20])
# Find outputs
print(7 / 0) 
print(7 // 0) 
print(7 % 0)
# ** operator demo program
print(3 ** 4)   #  3 ^ 4 = 81
print(10 ** -2)
print(4 * 3 * 2)
print(3 + 4 * 5 - 32 / 2 ** 3)
#  Relational  operators  demo  program (Home  work)
print(9 >= 5)  #  True  becoz  >  is  satisfied
print(9 >= 9)   #  True  becoz  =  is  satisfied
print(9 >= 12)   #  False  becoz    both  are  not  satisfied
print(6 <= 8)
print(6 <= 6)
print(6 <= 4)
print(9 != 7)
print(6 == 8)
print(True  >  False)
print(3 + 4j == 3 + 4j)
print(3 + 4j == 5 + 6j)
print(3 + 4j != 5 + 6j)
print(10 == 10.0)
print(3 + 4j >  3 + 4j)
#  Find  outputs  (Home  work)
print('Rama'   >  'Rajesh')   #   True  becoz  'm' > 'j'
print('Rama'  <  'Sita')
print('Hyd'  ==  'Hyd')
print('Rama'  <=   'Ramana')
print('Rama  Rao'  >=  'Rama')
print('Hyd'  != 'Sec')
print('HYD'  <   'hyd')



'''
1) Can  strings  be  compared  with  > ,  < , == ,  >= , <=  and  != ?  --->  Yes  only  in  python  but  not  in  other  languages

2) What  are  compared  internally  when  strings  are  compared ? ---> 1st  non-matching  characters

3) Are  characters  compared  (or)  their  unicode  values ?  --->  Unicode  values

4) How  many  unicode  values  exist ?  --->  512

5) What  is  the  range  of  unicode  values ?  --->  0  to  511

6) What  are  the  unicode  values  of  'A'  to  'Z'  ?  --->  65  to  90
    W…
# Chaining  relational  opeartors  (Home work)
print(10 < 20 < 30)    #   True  becoz  both  are  satisfied
print(10 >= 20 < 30)   #  False  becoz  1st  cond  is  not  satisfied
print(10 < 20 > 30)   
print(1 < 2 < 3 < 4)  
print(1 < 2 > 3 > 1)  
print(4 > 3 >= 3 > 2)
20th February 25
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




'''
and  operator
----------------
1) When  is  the  result  of  and  operator  False ?  --->  When  at  least  one  operand  is  False
    When  is  the  result  of  and  operator  True ?  --->When  both  the  operands  are  True

2) What  is  the  result  of  op1  and  op2  when  op1  is  True ?  --->  op2
    What  is  the  result  of  op1  and  op2  when  op1  is  False ?  --->	op1

3) Is  0  True…
#  or  operator  demo program
print(True  or  False)   #   True
print(False  or  True)   #  True
print(True  or  True) #  True
print(False  or   False)    # False
print(10  or  20)   #  10
print(0   or  20)  #   20
print(-25  or  0)
print(''  or  35)
print(6j  or  'Hyd')
print(0.0  or  3 + 4j)
print('Hyd'   or   10.8)



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
print(not  25)
print(not  0)
print(not  'Hyd')
print(not  '')
print(not  -10)
print(not  not  'Hyd')



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
print(i)
print(not(6 < 4  or  9 >= 5  and  6 != 6))
21st February 25
#  Assignment  operators  demo  program  (Home  work)
a = 25 
print(a)  
b =  a  
print(b)  
print(a  is  b)  
x = 4
y = 5
z = x + y * 6  
print(z)  
25 = a  
a + b = x + y
# Find outputs (Home work)
a = b = c = 25  
print(id(a)) 
print(id(b)) 
print(id(c)) 
print(a , b , c)
# Multiple  Assignment (Home work)
x , y , z = 25 , 10.8 , 'Hyd'  
print(x)
print(y)
print(z)
# Find outputs (Home work)
a , b , c = 3 , 4 , 5
a *= b + c
print(a)
# Find outputs (Home work)
a = 20
a %= 3 + 2 * 4 
print(a)
# Find outputs (Home work)
a = 3
a **= 4 
print(a)
# Identity operators demo program
a = 25
b = 25
print(a is b)
print(a is not b)
print(a == b)



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
print(a is b) 
print(a is not b) 
print(a == b)
# Find outputs (Home work)
a = 'Hyd' 
b = 'Hyd' 
print(a  is  b) 
print(a  is  not  b) 
print(a == b) 
print()
x = [1 , 2 , 3 , 4]  
y = [1 , 2 , 3 , 4]  
print(x is y)
print(x  is  not  y) 
print(x == y) 
print()
m = (1 , 2 , 3 , 4) 
n = (1 , 2 , 3 , 4)  
print(m  is  n) 
print(m  is  not  n) 
print(m == n)
# Membership operators demo program (Home work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)
print(19 in list)
print(14 not in list)
print(15 not in list)
s = 'Hyd is green city'
print( 'is' in s)
print('was' in s)
print('g' in s)
print('z' in s)
print(' ' in s)
print('gre' in s)
print('yd i' in s)
print('' in s)
print('' not in s)



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
print(--a)
print(a--)
print(a--1)
print(-a)
print(+-a)
print(-+a)
#  Semicolon  demo  program
print('One'); 
print('Two'); 
print('Three'); 
print('Hyd')  ; print('Sec')  ;  print('Cyb');
#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8))  #  Previous  integer  of  10.8  i.e.  10
print(math . ceil(10.8))  #  Next  integer  of  10.8  i.e.  11
print(math . floor(25.0))
print(math . ceil(25.0))
print(math . floor(-3.5))
print(math . ceil(-3.5))
print(math . floor(-9.0))
print(math . ceil(-9.0))
print(math . floor(25.1))
print(math . ceil(25.1))
print(floor(3.5))
print(ceil(3.5))



'''
1) What  does  floor(x)  do ?  --->  Returns  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  next  integer  of  'x'
'''
#  abs()  function  demo  program
from  builtins  import  abs
print(abs(-35.8))
print(abs(-27))
print(abs(29.5))
print(abs(32))
import  builtins
print(builtins . abs(-25))
#  max()  and  min()   functions  demo  program
from  builtins  import   max , min
print(max(10.8 , 20.6))
print(min(10.8 , 20.6 , 5.9 , 12.3))
print(max(25 , 10.8))
import  builtins
print(builtins . max(10 , 20 , 30))
print(builtins . min(10 , 20 , 15 , 5 , 12))
# pow()  function  demo  program
from  builtins  import  pow
print(pow(10 , -2))
print(pow(4 , pow(3 , 2)))
import  builtins
print(builtins . pow(2 , 3))
print(builtins . pow(-2 , -3))
# Find  outputs
How  to  import   kw  list
print(How  to  print  kwlist)
print(How  to  print  number  of  keywords)
print(How  to  print  type  of kwlist)
print(keyword . kwlist)
#  Find  outputs  (Home  work)
How  to  import   keyword  module
print(How  to  print  kwlist)
print(How  to  print  number  of  keywords)
print(How  to  print  type  of kwlist)
print(kwlist)

# eval()  function  demo  program
print(eval('25'))  #  Converts  '25'  to  25
print(eval('10.8'))  #  Converts  '10.8'  to   10.8
print(eval('False'))
print(eval('3+4j'))
print(eval("    'Hyd'   "))
print(eval('3 + 4 * 5'))
print(eval('[10 , 20 , 15 , 18]'))
print(eval('{10,20,15,18,20,12,18}'))
print(eval('(10 , 20 , 30)'))
print(eval("{10 : 'Hyd' , 10 : 'Sec'}"))
print(eval(4 + 5))




'''
eval()  function
------------------
1) What  does  eval()  function  do ?  --->  Converts  string  to  appropriate  object

2) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer
    What  does  float(x)  do  ?  ---> Converts   object  'x'   to  float
    What  does  complex(x)  do  ?  ---> Converts   object  'x'  to  complex  number
    What  does  bool…
# Gift
# Find  outputs  (Home  work)
print(eval("    'hyd'   "))
hyd = 'Sec'
print(eval('hyd'))
sec = '25'
print(eval('sec'))
print(eval(sec))
cyb = 10.8
print(eval('cyb'))
print(eval(cyb))
#  Gift
#  Find  output  (Home  work)
print(eval('print("Hyd")'))
#  Find  outputs  (Home  work)
print(bool('False'))
print(eval('False'))
print(bool(''))
print(eval('  ""  '))
print(eval(''))
print(eval('  " "   '))
print(eval(' '))
# What  is  the  advantage  of  eval(input()) ?
x = eval(input('Enter  any  input  :  '))
print(type(x))
print(x)
# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')
print(len(a))
print(a)
b = eval(input('Enter   any  string  : '))
print(len(b))
print(b)
# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t')
print(a , b , c , sep = '---')
print(a , b , c , sep = '\n')
print(a , b , c)
print(a , b , c , separator = ':')




'''
1) What  is  the  default  separator  for  print()  function ?  --->  Space

2) Can  separator  be  modified  ? --->  With  sep  argument  of print()  function

3) What  does  sep = 'delimeter'  do ?  --->  Modifies  the  separator  to  the  specified  delimeter

4) print(object , sep = ' , ')
    Is  sep  argument  required  in  the  above  print()  function ?  ---> No  becoz  single  object  is  being  printed

5) When  is  sep  argument  required  in  print()  function  ?  --->  When…
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , end = '---')
print(a , b , c , sep = ',,,')
print(a , b , c , sep = ':::' , end = '\t\t\t')
print(a , b , c)
# Find outputs  (Home  work)
print('Hyd')
print()
print('Sec')
print()
print('Cyb')
# Find  outputs  (Home  work)
l = [10 , 20 , 30 , 40]
t = (10 , 20 , 30 , 40)
s = {10 , 20 , 30 , 40}
print(l , t , s)
#  Find  outputs (Home  work)
a = 25
b = '%f'  %a
print(b)
print(type(b))
x = 10.8
y = '%d'  %x
print(y)
print(type(y))
m = [10 , 20 , 15 , 18]
n = '%s'  %m
print(n)
print(type(n))
# Find  Outputs  (Home  work)
a = 10.9274
print('%8.2f'  %a)  #  <3  spaces>10.93
print('%9.1f'  %a)
print('%10.3f'  %a)
print('%.2f'  %a)
print('%.6f'  %a)
print('%f'  %a)
# Find  outputs (Home  work)
a = 'Hyd'
print('%7s'  %a)  #   <4  spaces>Hyd
print('%-7s'  %a)  #  Hyd<4  spaces>
print('%2s'  %a)
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print(a)
# Find  outputs  (Home  work)
a = [10 , 20 , 30 , 40]
print('%s'  %a)
print('%s' , a)
print('%s'  a)
print('%s' , %a)
print('%l'  %a)
print(a)
#Find outputs  (Home  work)
a = 25
b = 10.9274
c = 'Hyd'
print('%d    %f    %s'  %(a , b , c))
print('%i    %g    %s'    %(a , b , c))
print('%s    %s    %s'  %(a , b , c))
print('%d    %g    %s'  , a , b , c)
print('%d    %g      %s'   a , b , c)
print('%d    %g    %s'  ,  %(a , b , c))
print('%d    %g    %s'    %a%b%c)
print('%d'    %a  ,  '%f'     %b  ,  '%s'   %c)
#  Find  outputs  (Home  work)
x = 25
y = F'{x}'
print(y)
print(type(y))
x = 10.8
y = F'{x}'
print(y)
print(type(y))
x = [10,20,30,40]
y = F'{x}'
print(y)
print(type(y))
#Find  outputs  (Home  work)
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')
print(F'{a=}  \t   {b=}   \t  {c=}')
print(F'{a:}  \t   {b:}   \t  {c:}')
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')
print(F'a  =  a  \t  b  =  b  \t  c  =  c')
print(F'{x =}  \t   {y =}   \t  {z =}')
#  Find  outputs  (Home  work)
x = 25
print(F'{x}')  #  25
print(F'{{x}}')   #  {x}
print(F'{{{x}}}')  #   {25}
print(F'{{{{x}}}}')
print(F'{{{{{x}}}}}')
print(F'{{{{{{x}}}}}}')
print(F'{{{{{{{x}}}}}}}')
print(F'{{{{{{{{x}}}}}}}}')



'''
1) What  is  printed  when  'x'  is  in  even  number  of  braces ?  --->  'x'  itself

2) What  is  printed  when  'x'  is  in  odd  number  of  braces ?  --->  Value   of  'x'  in  the  form  of  string

3) How  many  braces  are  printed  in  the  output ?  --->  Number  of  braces  //  2
'''
---------------------------
