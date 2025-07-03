
'''
1. Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''
def f1(a,b):
	print('Sum: ',end='')
	yield a+b
	print('Difference: ',end='')
	yield a-b
	print('Product: ',end='')
	yield a*b
	print('Division: ',end='')
	yield a/b
a=int(input("enter a number: "))
b=int(input("enter a number: "))
try:
	for x in f1(a,b):
		print(x)
except ZeroDivisionError:
	print('Divsion by 0 not permitted') 

'''
2*. Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f2(a,b):
	while a<=b:
		yield a
		a+=1
	
a=int(input("enter start number: "))
b=int(input("enter end number: "))
for x in f2(a,b):
	print(x) 
'''
3.Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  ---> 9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  ---> 0  and  1

4) Use  generator  function  and  for  loop
'''
def fib(i):
	a,b=0,1
	while a<=i:
		yield  a
		a,b=b,a+b
i=int(input("Fibonnaci series until some number: "))
for x in fib(i):
	print(x) 
'''
4. Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
''' 
def words(x):
	a=x.split()
	for x in a:
		yield x
x=input("Enter a String: ")
for x in words(x):
	print(x) 
# 5.  Find  outputs
def   f1():
        yield   [10 , 20]
        yield  {30 , 40 , 50}
        yield  60  , 70 , 80 , 90
        yield  100
# End  of  generator
g = f1()
for   x   in   g:
	print(x) 
	print(type(x))
'''
[10 , 20]
class list
{30 , 40 , 50}
class set
(60  , 70 , 80 , 90)
class tuple 
100
int '''
# 6. Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1() # Creating an empty generator object 
print('Begin') # Begin
print(*g) # memory error bcz it takes lot os space to have this numbers in generator and unpack it 
print('End')

# 7. Find  outputs
g = (x * x  for  x  in  range(500000000000000000))
print(*g) # slow output .. console may crash 

# 8.  Find    outputs (Home  work)
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1()
for   m   in   g:
	print(m)
x ,  y ,  z  =  f1()
print(x)
print(y)
print(z)
'''
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3
''' 
# 9. Identify  error (Home  work)
def  f1():
        yield  10
        yield  20
        yield  30
        yield  40
#a , b , c = f1() #  too many values to unpack (expected 3)
#p , q , r , s , m = f1()  # not enough values to unpack (expected 5, got 4)

# 10. Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()
#print(len(g)) # error object of type 'generator' has no len()
# print(g * 3) # error unsupported operand type(s) for *: 'generator' and 'int'
#print(g[0]) # error 'generator' object is not subscriptable
#print(g[1 : 3]) #  error 'generator' object is not subscriptable
print(*g) # 1 2 3 


''' 1. Input : 123456789
Output  :  Twelve  crores  thirty  lakhs  fifty  six  thousand  seven  hundred  eighty  nine '''

from num2words import num2words

def number_to_indian_words(num):
    return num2words(num, lang='en_IN').replace(",", "").capitalize()

# Example usage
num = 123456789
print(number_to_indian_words(num)) 

'''2. with dict '''
def words(n):
	a={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
	c=''
	for x in n:
		c+= a[int(x)] +' '
	return c
n=input("Enter a number: ")
print(words(n))

'''3. Repeat roman numbers with dict'''
def roman(n):
	a= {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,'L': 50, 'XL': 40,'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
	c=''
	for sym,val in a.items():
		count=n//val
		c+=sym * count
		n-=val*count
	print(c)
n= int(input("Enter a number: "))
roman(n)
''' 
# 4.  (Home  work)
print('Begin')
print(How  to  print  variable  'x'  of  cal   module
print(y)
print(cal . x)
print
print(sub(10 , 7))
print(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7)
print(div(10 , 7))
'''
'''
#cal.py
if  __name__=='__main__':
	
	def sub(a,b):
		return a-b
	def div(a,b):
		return a/b
x=100
y=200
def add(a,b):
	return a+b
def mul(a,b):
	return a*b

class c1:
	def m1(self):
		print('m1 Method')'''
import cal #How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ? 
print('Begin')
from cal import x,add,mul,c1 #How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle  with  from  statement
print(cal.x)
#print(y) # error call with mosule name 
print(add(10,7))
#(How  to  call  add()  function  of  cal  module  by  passing  10  and  7)
#print(sub(10,7)) # error not executed  writing sub and div under if condition 
#print(div(10 , 7)) # error  not executed 
print(mul(10,7))
a=c1()
a.m1() #How to print m1() method of class c1 

# 5. Module  alias
print('Begin')
# How  to  import  cal  module  with   another  name  using  import  statement
import cal as c
print(c.x) #(How  to  print  variable  'x'  of  cal   module
print(c.y) #(How  to  print  variable  'y'  of  cal   module
print(c.add(10,7)) #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(c.sub(10,7)) #(How  to  call  sub()  function  of  cal  module  by  passing  10  and  7
print(c.mul(10,7)) #How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
print (c.div(10,7)) #(How  to  call  div()  function  of  cal  module  by  passing  10  and  7
#How  to  call  m1()  method  of  c1  class  in  cal  module
cl=c.c1()
cl.m1()
#print(cal . x) # error it has alias 
#from  math  as   m  import  * #  error module name cant have alias 

# 6. Member  alias
from cal import x as a,add as ad,mul as m,c1 as c # How  to  import  members   x , add , mul  and  class  c1  of  cal  moudle   with  another  name   using   from  statement
print(a)#(How  to  print  variable  'x'  of  cal   module
#print(x) # error no x in this program
print(ad(10,7))  #(How  to  call  add()  function  of  cal  module  by  passing  10  and  7
print(m(10,7)) #(How  to  call  mul()  function  of  cal  module  by  passing  10  and  7
m2=c()
m2.m1()#How  to  call  m1()  method  of  class  c1  in  cal  module
#print(add(10 , 7)) # error it has an alias 
#b = c1() # error class as an alias 

# 7. Find  outputs  (Home  work)
x = 30
def   disp(): 
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *
from  mod1  import   *
print(x) # 10
disp() # disp  function  of mod 1
a = c1() 
a . m1() # m1  method of  class  c1  in mod 1

# 8. Find outputs  (Home  work)
from  mod1  import  *
from  mod2  import  *
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) # 30
disp()  # disp  function  of  same  module
a = c1()
a . m1()  #m1  method of  class  c1  in  same  module

#9. How  to  use  members  of  all  the  3  modules(mod1 , mod2  and  current  module)  with  import  statement ?
#How  to  import  mod1  and  mod2
import mod1,mod2
x = 30
def   disp():
		print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(mod1.x) #(How  to  print  variable  'x'  of  mod1
print(mod1.disp()) #How  to  call  disp()  function  of  mod1
c=mod1.c1()
c.m1() #How  to  call  method  m1()  of  class   c1  in  mod1
print()
print(mod2.x)  #(How  to  print  variable  'x'  of  mod2
print(mod2.disp()) #How  to  call  disp()  function  of  mod2
cm=mod2.c1()
cm.m1()#How  to  call  method  m1()  of  class   c1  in  mod2
print()
print(x)#(How  to  print  variable  'x'  of  current  module)
print(disp()) #How  to  call  disp()  function  of current  module
cc=c1()
cc.m1()#How  to  call  method  m1()  of  class   c1  in  current  module 

# 10.How  to  use  members  of  all  the  three  modules  with  from  statement ?
from mod1 import * #How  to  import  members  of  mod1
from mod2 import * #How  to  import  members  of  mod2
x = 30
def   disp():
        print('disp  function  of  same  module')
class  c1:
	def   m1(self):
		print('m1   method  of  class  c1  in  same  module')
''' #(How  to  print  variable  'x'  of  mod1)
How  to  call  disp()  function  of  mod1
How  to  call  method  m1()  of  class   c1  in  mod1 # members of mod 1 and mod 2 cant be used in this program bcz they are not replaced with current module values 
print()
print()
print(How  to  print  variable  'x'  of  mod2)
How  to  call  disp()  function  of  mod2
How  to  call  method  m1()  of  class   c1  in  mod2 '''
print()
print()
print(x)#(How  to  print  variable  'x'  of  current  module)
disp()#How  to  call  disp()  function  of current  module
c=c1()
c.m1()#How  to  call  method  m1()  of  class   c1  in  current  module 

'''
#cal . py
x = 100
y = 200
def add(a , b):
	return a + b
def sub(a,b):
    return a - b
def mul(a , b): 
    return a * b
def div(a , b):
    return a / b
class c1:
	 def m1 (self) :
		 print ('m1 method')
'''

# 1. Find  outputs
import  cal
print(cal . x) #100
print(cal . y) #200
print(cal . add(10 , 7)) #17
print(cal . sub(10 , 7)) #3
print(cal . mul(10 , 7)) #70
print(cal . div(10 , 7)) #1.4285714285714286
a = cal . c1()
a . m1()		#m1 method

'''
2. Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '_name' . startswith('_')  ?  --->  True

2) What  is  the  result  of  '_spec' . endswith('_')  ?  --->  True

3) What  is  the  result  of  'spec_' . startswith('_')  ?  --->  False

4) Hint:  Use  startswith()  and  endswith()  methods  of  str  class

5) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables

OUTPUT: ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
 '''
import cal
a=[]
b=dir(cal)
for mem in b:
	if mem.startswith('__') or mem.endswith('__'):
		pass
	else:
		a.append(mem)
print(a)


#3.  Find  outputs
print(dir()) # [Environment variable]
print()
from  cal  import  *
print()
print(dir()) # ['add','sub','mul','div',c1,Environment variable]
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
'''

# 4. Find  outputs
print(dir())
print()
from  cal  import  add , mul , x
print()
print(dir())
'''
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']


['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'mul', 'x']
'''
'''
PROGRAM_1:
'''
# Identify  error  (Home work)
'''
class c1:
	def m1(self):
		pass
class c2:
	pass
class c3:
'''
# Find  outputs  (Home  work)
class   c1:
	pass
a = c1()
print(id(a))
print(type(a))
print(a.__dict__) 
print(a)
del a
#print(a) -->after object deletion,these is no name defined as a
'''
OUTPUT:
2568541336112
<class '__main__.c1'>
{}
<__main__.c1 object at 0x0000025608FE7230>
'''
#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):
		print('1st  method')
	def   m1(self):
		print('2nd  method')
	#def   m1(self): method should contain program for operation
a=c1()
a.m1()
m1()
'''
OUTPUT:
2nd method
Function
'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x , y):
		print('Two  argument  method : ' , x , y)
a = c1()
a . m1(10 , 20)
#a.m1(30) --> c1.m1() missing 1 required positional argument: 'y'
#a.m1() -->c1.m1() missing 2 required positional arguments: 'x' and 'y'
'''
OUTPUT:
Two  argument  method :  10  20
'''
#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('No  argument  method')
	def   m1(self , x):
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):
		print('Two  argument  method : ' , x , y)
a = c1()
a.m1(10 , 20)
a.m1(30)
a.m1()
'''
OUTPUT:
Two  argument  method :  10 20
Two  argument  method :  30 2
Two  argument  method :  1 2
'''
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  third  c1  class')
a=c1()
a.m1()
'''
OUTPUT:
Method  of  third  c1  class
'''
# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:
	pass
a=c1()
#a.m1() -->c1 object has no method named m1
'''
OUTPUT:
c1 object has no method named m1
'''
#  Find  outputs (Home  work)
class  c1:
        pass
a = c1()
print(a . __dict__)
a . x = 10
print(a . __dict__)
a . y = 20
print(a . __dict__)
a . x = 30
print(a . __dict__)
a . y = 40
print(a . __dict__)
del  a . x
print(a . __dict__)
del  a . y
print(a . __dict__)
del   a
#print(a.__dict__)-->object a is deleted.therefore no dictionary typecasting is possible
'''
OUTPUT:
{}
{'x':10}
{'x':10,y:20}
{'x':30,y:20}
{'x':30,y:40}
{'y':40}
{}
'''
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):
		self.a=int(input("Enter side a : "))
		self.b=int(input("Enter side b : "))
		self.c=int(input("Enter side c : "))
	def  test(self):
		if  self.a+self.b>self.c or self.b+self.c>self.a or self.c+self.a>self.b:
			pass
		else:
				print('Not  a  triangle')
				exit()
	def  area(self):
		s=(self.a+self.b+self.c)/2
		return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
	def  peri(self):
			return self.a+self.b+self.c
obj=triangle()
obj.get()
obj.test()
print('Area : ',obj.area())
print('Perimeter : ',obj.peri())
'''
OUTPUT:
Enter 1st side of the triangle : 3
Enter 2nd side of the triangle : 4
Enter 3rd side of the triangle : 5
Area :  6.0
Perimeter :  12
'''
#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x)
		print(self . x)
		x += 5
		self.x += 7
	def   m2(self):
		#print(x) -->name x is not defined
		print(self.x)
		self . x += 6
a = c1()
a . m1()
a . m2()
print(a.x)
#print(self.x) -->no self is defined
#print(x) -->no global variable x defined 
'''
OUTPUT:
10
20
27
33
'''
#  Find  outputs (Home  work)
class  Date:
	pass
a=Date()
a.dd=15
a.mm=8
a.yy=1947
print(a)
'''
OUTPUT:
<__main__.Date object at 0x000001867B857230>
'''
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self.x=int(input("Enter x value : "))
		 self.y=int(input("Enter y value : "))
		 self.z=int(input("Enter z value : "))
	def   add(self,m,n):
		self.x=m.x+n.x
		self.y=m.y+n.y
		self.z=m.z+n.z
	def  disp(self):
		 print('x: ',self.x)
		 print('y: ',self.y)
		 print('z: ',self.z)
a=Test()
b=Test()
c=Test()
print('First  Object')
a.get()
print('Second  Object')
b.get()
c.add(a,b)
print('Addition  results')
c.disp()
'''
OUTPUT:
First  Object
Enter x value : 10
Enter y value : 20
Enter z value : 30
Second  Object
Enter x value : 40
Enter y value : 50
Enter z value : 60
Addition  results
x:  50
y:  70
z:  90
'''
#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)
#print(b)
#print(c) -->__str__ returned non-string (type NoneType)
#print(d) -->c4.__str__() missing 1 required positional argument: 'x'
print(b.__str__())
print(c.__str__())
print(d.__str__(50))
'''
OUTPUT:
<__main__.Date object at 0x0000025C18D37230>
25
35
Hyd
None
50
'''

#  Repeat  previous  program  such  that  OTP  can  be  between  000000  and   999999  (may  be   000156)
import random

print("Generated OTPs:")
for _ in range(10):
    otp = random.randint(0, 999999)
    formatted_otp = f"{otp:06d}"
    print(formatted_otp)

#reuse
# Save  in  any  file  of  cwd
from  p1   import  mod1
print(mod1.x)#How  to  print  variable  'x'  of  mod1  in  package  p1
mod1.f1() #How  to  call  function  f1()  of  mod1  in  package  p1
a=mod1.c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # error p1 not imported
#print(p1 . _init_ . x) # error 
#print(_init_ . x) # error 

# Save  in  any  file  of  cwd
from  p1 . mod1   import  *
print(x)#How  to  print  variable  'x'  of  mod1  in  package  p1
f1()#How  to  call  function  f1()  of  mod1  in  package  p1
a=c1()
a.m1()#How  to  call  method  m1()  of  class  c1  in  mod1  of  package  p1
#print(p1 . x) # error 
#print(p1 . _init_ . x) # error 
#print(_init_ . x) # error 
#  p1  import  mod1 . * # error 

# Save  in  any  file  of  cwd
import p1.__init__ #How  to  import  _init_  module  of  package  p1  with  import  statement
print(p1.x) #How  to  print  variable  'x'  of   _init_  module   in   package  p1
p1.f1() #How  to  call  function  f1()  of   init  module  in  package  p1
a=p1.c1()
a.m1()
#How  to  call method  m1()  of  class  c1  in   init  module  of  package  p1
from p1 import *
print(x) #How  to  print  variable  'x'  of   _init_  module   in   package  p1  in  another  way
f1()#How  to  call  function  f1()  of   _init_  module  in  package  p1  in  another  way
a=c1()
a.m1() #How  to  call  method  m1()  of  class  c1  in   _init_  module  of  package  p1  in  another  way
#print(p1 . mod1 . x)
#from p1 import __init__  # Will give an ImportError

# Save  in  any  file  of  cwd
import   p1  # executes __init __
import  p1 . mod1 # 
from   p1   import  mod1
from   p1 . mod1  import   *
import  p1 . _init_

# Identify  error  (Home work)
class c1:
    def m1(self):
        pass


class c2:
    pass


class c3:  # Indensation error


# ============================================
#  Find  outputs  (Home  work)
class c1:
    def m1(self):
        x = 10
        self.x = 20
        print(x)
        print(self.x)
        x += 5
        self.x += 7

    def m2(self):
        # print(x)
        print(self.x)
        self.x += 6


# End  of  the  class
a = c1()
a.m1()
a.m2()
print(a.x)


# print(self . x)
# print(x)

# =================================================
# Find  outputs  (Home  work)
class c1:
    pass


# End  of  the  class
a = c1()
print(id(a))  # address of an object
print(type(a))  # class type class '__main__'.c1
print(a.__dict__)  # {}
print(a)  # type and address
del a


# print(a)
# =====================================================

#  Find  outputs  (Home  work)
def m1():
    print('Function')  # Function 2nd


class c1:
    def m1(self):
        print('1st  method')

    def m1(self):
        print('2nd  method')

    def m1(self):
        print('3rd  method')  # 3rd method 1st


# End  of  class  c1
a = c1()
a.m1()
m1()


# ============================================================

#  Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('No  argument  method')

    def m1(self, x):
        print('Single  argument  method : ', x)

    def m1(self, x, y):
        print('Two  argument  method : ', x, y)  # Two  argument  method : 10 20


# End  of  class  c1
a = c1()
a.m1(10, 20)


# a .m1(30)
# a.m1()

# ===================================================================================================
#  Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('No  argument  method')

    def m1(self, x):
        print('Single  argument  method : ', x)

    def m1(self, x=1, y=2):
        print('Two  argument  method : ', x, y)


# End  of  class  c1
a = c1()
a.m1(10, 20)  # Two  argument  method : 10 20
a.m1(30)  # Two  argument  method : 30 2
a.m1()  # Two  argument  method : 1 2


# ==================================================================

# Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('Method  of  first  c1  class')


class c1:
    def m1(self):
        print('Method  of  second  c1  class')


class c1:
    def m1(self):
        print('Method  of  third  c1  class')  # Method  of  third  c1  class


a = c1()
a.m1()


# ==================================================================================

# Find  outputs  (Home  work)
class c1:
    def m1(self):
        print('Method  of  first  c1  class')


class c1:
    def m1(self):
        print('Method  of  second  c1  class')


class c1:
    pass


a = c1()


# a.m1()#error
# ========================================================================
#  Find  outputs (Home  work)
class c1:
    pass


# End  of  class
a = c1()
print(a.__dict__)  # {}
a.x = 10
print(a.__dict__)  # {'x':10}
a.y = 20
print(a.__dict__)  # {'x':10,'y':20}
a.x = 30
print(a.__dict__)  # {'x':10,'y':20,'x':30}
a.y = 40
print(a.__dict__)  # {'x':10,'y':20,'x':30,'y':40}
del a.x
print(a.__dict__)  # {'y':40}
del a.x
del a.y
print(a.__dict__)  # {}
del a
# print(a.__dict__)
# ===================================================================

import math


class triangle:
    def get(self):
        self.a = float(input("Enter side a: "))
        self.b = float(input("Enter side b: "))
        self.c = float(input("Enter side c: "))

    def test(self):
        # Triangle inequality test
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            pass  # valid triangle
        else:
            print("Not a triangle")
            exit()  # stop execution

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def peri(self):
        return self.a + self.b + self.c


# --- Usage ---
t = triangle()  # create triangle object
t.get()  # read inputs
t.test()  # check if it's a valid triangle

print('Area :', t.area())
print('Perimeter :', t.peri())


# ==================================================================================

class Test:
    def get(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))
        self.z = int(input("Enter z: "))

    def add(self, m, n):
        self.x = m.x + n.x
        self.y = m.y + n.y
        self.z = m.z + n.z

    def disp(self):
        print(f"x = {self.x}, y = {self.y}, z = {self.z}")


# End of the class

# Creating three objects
a = Test()
b = Test()
c = Test()

print("First Object:")
a.get()

print("Second Object:")
b.get()

# Adding a and b, store result in c
c.add(a, b)

print("Addition Results:")
c.disp()


# =============================================================================
#  Find  outputs (Home  work)
class Date:
    pass


# End of the class
a = Date()
a.dd = 15
a.mm = 8
a.yy = 1947
print(a)  # type and address


# ==================================================

#  Find  outputs (Home  work)
class c1:
    def __str__(self):
        return '25'


class c2:
    def __str__(self):
        return 35


class c3:
    def __str__(self):
        print('Hyd')


class c4:
    def __str__(self, x):
        return F'{x}'


# end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)
# print(b)#error due to non string
# print(c)#error
# print(d)
print(b.__str__())
print(c.__str__())
print(d.__str__(50))
# =======================================================
'''
PROGRAM_1:
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  and   use  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
'''
from progtriangle import triangle 
obj1=triangle()
obj1.get()
obj1.test()
print('Area : ',triangle.area(obj1))
print('Perimeter: ',triangle.peri(obj1))
'''
'''
OUTPUT:
Enter side a : 3
Enter side b : 4
Enter side c : 5
Area :  6.0
Perimeter:  12
'''
'''
PROGRAM_2:

Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		self.rollnum=int(input("Enter Roll Number    : "))
		self.stu_name=input("Enter student name   : ")
		self.gender=input("Enter gender name    : ")
		self.marks=[]
		for i in range(3):
			self.marks.append(eval(input("Enter list of marks  : ")))
	def   compute(self):
		self.total=sum(self.marks)
		self.average=self.total/len(self.marks)
		if  min(self.marks)<40:
			     self.grade="Fail"
		elif  self.average>=70:
				 self.grade='Distinction'
		elif  self.average>= 60:
				 self.grade='First  class'
		elif  self.average>= 50:
				 self.grade='Second  class'
		else:
			     self.grade='Third  class'
	def  disp(self):
		print('Roll  Number   :  ' ,self.rollnum)
		print('Student  Name  :  ' ,self.stu_name)
		print('Gender         :  ' ,self.gender)
		print('Total  Marks   :  ' ,self.total)
		print('Average        :  ' ,self.average)
		print('Grade          :  ' ,self.grade)
	def   __str__(self):
		return  f'Roll Number: {self.rollnum},Student Name: {self.stu_name},Gender : {self.gender},Total Marks: {self.total},TotalMarks: {self.total},Average: {self.average},Grade: {self.grade}'
if __name__=="__main__":
		obj=Student()
		obj.get()
		obj.compute()
		obj.disp()
		print(obj)
'''
OUTPUT:
Enter Roll Number    : 79
Enter student name   : Pavan
Enter gender name    : m
Enter list of marks  : 47
Enter list of marks  : 56
Enter list of marks  : 77
Roll  Number   :   79
Student  Name  :   Pavan
Gender         :   m
Total  Marks   :   180
Average        :   60.0
Grade          :   First  class
Roll  Number : 79,Student  Name  : Pavan,Gender : m,Total  Marks : 180,Total  Marks : 180,Average : 60.0,Grade : First  class
'''
#  Find  outputs  (Home  work)
class      Rat:
	def    m1():
		pass
if __name__=="__main__":
		a = Rat()
		a . nr = 22
		print(hasattr(a , 'nr'))
		print(hasattr(a , 'dr'))
		print(hasattr(a , 'm1'))
		print(hasattr(a , 'm2'))
		print(hasattr(Rat,'m1'))
		print(hasattr(Rat,'m2'))
		print(hasattr(Rat,'nr'))
'''
OUTPUT:
True
False
True
False
True
False
False
'''
# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
if __name__=="__main__":
	a=[Cat(),Dog(),Goat()]
	for  x  in   a:
		if   hasattr(x,'talk'):
			x.talk()
		else:
		    x.bark()
'''
OUTPUT:
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ....
'''
#  Find  outputs  (Home  work)
class    c1:
        pass
a = c1()
a . x = 10
if __name__=="__main__":
	varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
	value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
	setattr(a , varname , value)
	print(a . __dict__)
	print(a . x)
	while  True:
		try:
			varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')
										#  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
			print(getattr(a , varname))
		except:
			print(F'Invalid  variable   name   :  {varname}')
			break
'''
OUTPUT:
Enter  variable  name  to  be  added  to  object  :  y
Enter  value  of  the  variable  :  20
{'x': 10, 'y': 20}
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  x
10
Enter  variable  name  whose  value  is  to  be  retrieved  :  y
20
Enter  variable  name  whose  value  is  to  be  retrieved  :  z
Invalid  variable   name   :  z
'''
'''
PROGRAM_3:
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e=Emp()
if __name__=="__main__":
	for i,j in dict.items():
		setattr(e,i,j)
	for i in dict.keys():
		print(getattr(e,i))
'''
OUTPUT:
25
Rama  Rao
10000.0
'''
'''
PROGRAM_3:

Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  --->  2 / 3 + 5 / 9 = (18 + 15) / 27 =  33 / 27 =  11 / 9
    What  is  the  difference  ?  --->  2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 =  1 / 9
    What  is  the  product  ?  --->	2 / 3 * 5 / 9 =  10 / 27  =  10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 =  2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 =  (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->  2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted

3) When  is  simplification  required ?  --->  When  numerator  is  non-zero
'''
import  math
class  Rat:
	def  get(self):
		self.nr=eval(input("Enter numerator : "))
		self.dr=eval(input("Enter denominator : "))
		self.test()
	def  test(self):
		while True:
			if self.dr==0:
				print("Re-enter the denominator value : ")
				self.dr=eval(input("Enter denominator : "))
			else:
				break
	def  __str__(self):
			 return f'{self.nr} / {self.dr}'
	def   add(self , a , b):
		self.nr=a.nr*b.dr+b.nr*a.dr
		self.dr=a.dr*b.dr
		self.simplify(self.nr,self.dr)
	def   sub(self , a , b):
		self.nr=a.nr*b.dr-b.nr*a.dr
		self.dr=a.dr*b.dr
		self.simplify(self.nr,self.dr)
	def   mul(self , a , b):
		self.nr=a.nr*b.nr
		self.dr=a.dr*b.dr
		self.simplify(self.nr,self.dr)
	def    div(self , a , b):
		self.nr=a.nr*b.dr
		self.dr=a.dr*b.nr
		self.simplify(self.nr,self.dr)
	def   simplify(self,nr,dr):
			self.nr=nr//math.gcd(nr,dr)
			self.dr=dr//math.gcd(nr,dr)
a=Rat()
b=Rat()
c=Rat()
d=Rat()
e=Rat()
f=Rat()
a.get()
b.get()
c.add(a,b)
d.sub(a,b)
e.mul(a,b)
f.div(a,b)
print("Addition  : ",c)
print("Substraction : ",d)
print("Multiplication : ",e)
if a.dr!=0 and b.nr!=0:
	print('Division : ',f)
else:
	print('Division  is  not  permitted')
'''
OUTPUT:
Enter numerator : 2
Enter denominator : 3
Enter numerator : 5
Enter denominator : 9
Addition  :  11 / 9
Substraction :  1 / 9
Multiplication :  10 / 27
Division :  6 / 5
'''
'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import  and  use  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again

from Apr08Opps import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
b.get()
c.add(a,b)
print('Sum:',c)
c.sub(a,b)
print('sub:',c)
c.mul(a,b)
print('mul:',c)
c.div(a,b)
if b.numerator!=0:
		
		print('div:',c)
else:
	print('Division not possoble:')


Repeat  prog10a  with  list  of  6  objects

Hint:  import  and  use  rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from  Apr08Opps import Rat
a=[]
for i in range(6):
		a.append(Rat())
a[0].get()
a[1].get()

a[2].add(a[0],a[1])
print('sum:',a[2])
a[3].sub(a[0],a[1])
print('sub:',a[3])
a[4].mul(a[0],a[1])
print('mul:',a[4])
a[5].div(a[0],a[1])
print('div:',a[5])



# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9) #object is intialized with nr=9, dr=7
c = Rat(5,  8)#object is intialized with nr=5, dr=8
d = Rat(dr1 = 9)#object is intialized with nr=22, dr=9
e = Rat(dr1 = 3 , nr1 = 2)#object is intialized with nr=2, dr=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y)#object is intialized with nr=11, dr=15
print('a  :  ' , a)#22/7
print('b  :  ' , b)#9/7
print('c  :  ' , c)#5/8
print('d  :  ' , d)#22/9
print('e  :  ' , e)#2/3
print('f  :  ' , f)#11/15
c . __init__()
print('c  :  ' , c)#22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a)#3.8/4.6
#g = Rat(nr1 = 9 , 5)#error positional argument follows keyword argument
h = Rat(nr1 = 9 , dr1 = 5) 

outputs--
Enter numerator  :  11
Enter Denominator  :  15
a  :   22  /  7
b  :   9  /  7
c  :   5  /  8
d  :   22  /  9
e  :   2  /  3
f  :   11  /  15
c  :   22  /  7
a  :   3.8  /  4.6

# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)#{15:8:1947}
print('b  :  ' , b . __dict__)#{ dd1 : 26, mm1 : 1,yy1 : 1950 , }
print('c  :  ' , c . __dict__)#{ dd1 : 19 ,mm1 : 7 , yy1 : 1985}
d = Date()#error 
#e = Date(dd = 30 , mm = 4 , yy = 2022)
#f = Date(dd1 = 26 , mm1 = 8 , 2023)#error

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		#return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
a = c1()#'c1  class  constructor'
b = c2()#'c2  class  constructor'
print(b)#'c2  class  constructor' <next line> None
print(b . __init__())#'c2  class  constructor' <next line> None
c = c3()#'c3  class  constructor'
print(c . __init__())#'c3  class  constructor' <next line> None

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		#b = c1() #recursion
# End  of  class
a = c1()#'Constructor'

#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()#'Constructor'
print(a . __dict__)#{x:10,y:20}
b = c2()#'Method'
print(b . __dict__)
b . init()#error
print(b . __dict__)#{x:30,y:40}

# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1()#
print(x . __dict__)#{a:10}
x . m1()
print(x . __dict__)#{a:10,b:20}
f1()
print(x . __dict__)#{a:10,b:20,c:30}
x . d = 40
print(x . __dict__)#{a:10,b:20,c:30,d:40}
y = c2()
y . m3()
print(x . __dict__)#{a:10,b:20,c:30,d:40,e:50}
z = c1()
print(z . __dict__)#{a:10}


# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)#{x:10,y:20,z:30}
print(b . __dict__)#{x:10,y:20,z:30}
del  a . x
del  b . y
print(a . __dict__)#{y:20,z:30}
print(b . __dict__)#{x:10,z:30}
#print(a . x)#error
#print(b . y)#error

#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1()#'3rd  constructor'

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#'Two  argument  constructor : ' , 10,20
#b = c1(30)#error
#c = c1()#error

#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)#'Two  argument  constructor : ' , 10,20
b = c1(30)#'Two  argument  constructor : ' , 30 , 200
c = c1()#'Two  argument  constructor : ' , 100,200

# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1()#'Constructor'
print(a)#type and adress

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1()#
print(a)#'Function' <Next line> None

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25)
print(b)#'Function : ' , 25 <next line>None

#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9b')
a = c1()

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
 #How  to  import  class  c1  from  prog9a   with  from  statement
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1() #How  to  create  c1  class  object  of  current  module
from prog9a import c1
b=c1() #How  to  create  c1  class  object  of  prog9a


#How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement


class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1() #How  to  create  c1  class  object  of  current  module
from   prog9a import c1
b=c1() #How  to  create  c1  class  object  of  prog9a'''


#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  Student_class  import  Student
s = Student()
print(s . __dict__) #{}
s . get()
print(s . __dict__) 
s . compute()
print(s . __dict__) 

'''
{}
Enter roll no of student: 1
Enter name of the student: sita
Enter gender of the student: female
Enter marks of 3 subjects in the form of list:  [30,40,50]
{'rno': 1, 'sname': 'sita', 'gender': 'female', 'm': [30, 40, 50]}
{'rno': 1, 'sname': 'sita', 'gender': 'female', 'm': [30, 40, 50], 'tot': 120, 'avg': 40.0, 'grade': 'Fail'} '''

'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import  and  use  Rat  class  defined  in  prog10a  but  do  not  define  Rat  class   again
'''
from Rat import Rat
a=Rat()
b=Rat()
c=Rat()
a.get()
b.get()
c.add(a,b)
print(c)
c.sub(a,b)
print(c)
c.mul(a,b)
print(c)
if b.nr==0:
	print("Division is not permitted")
else:
	c.div(a,b)
	print(c) 
from Rat import Rat
a=[Rat(),Rat(),Rat(),Rat(),Rat(),Rat()]
a[0].get()
a[1].get()
a[2].add(a[0],a[1])
a[3].sub(a[0],a[1])
a[4].mul(a[0],a[1])
print(a[2])
print(a[3])
print(a[4])
if a[1].nr==0:
	print("Division is not permitted")
else:
	a[5].div(a[0],a[1])
	print(a[5])


# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):
		self . nr = nr1
		self . dr = dr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat() #   Object  is  initialized  with  nr =  22 , dr = 7  by  constructor
b = Rat(9) #nr1 =9 and dr1 =7
c = Rat(5,  8) # nr1=5 dr1=8
d = Rat(dr1 = 9) # nr1=22 dr 1=9
e = Rat(dr1 = 3 , nr1 = 2) # nr1=2 dr1=3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) # nr1=11 dr1=15
print('a  :  ' , a) # 22/7
print('b  :  ' , b) #9/7
print('c  :  ' , c) #5/8
print('d  :  ' , d) #22/9
print('e  :  ' , e) #2/3
print('f  :  ' , f) #11/15
c . __init__()
print('c  :  ' , c) #22/7
a . __init__(3.8  , 4.6) #  Modifies  object  'a'   to  nr = 3.8 , dr = 4.6   replacing  22  and   7
print('a  :  ' , a) #3.8/4.6
#g = Rat(nr1 = 9 , 5) # error ka cant be before pa
#h = Rat(nr = 9 , dr = 5) # error no nr and dr 

# Find  outputs (Home  work)
class  Date:
        def   __init__(self , dd1 , mm1  , yy1):
                self . dd = dd1
                self . mm = mm1
                self . yy = yy1
# End  of  the  class
a = Date(15 , 8 , 1947)
b = Date(yy1 = 1950 , mm1 = 1 , dd1 = 26)
c = Date(mm1 = 7 , dd1 = 19 , yy1 = 1985)
print('a  :  ' , a . __dict__)
print('b  :  ' , b . __dict__)
print('c  :  ' , c . __dict__)
#d = Date() # Date.__init__() missing 3 required positional arguments: 'dd1', 'mm1', and 'yy1'
#e = Date(dd = 30 , mm = 4 , yy = 2022)
#f = Date(dd1 = 26 , mm1 = 8 , 2023) # positional argument follows keyword argument
'''
a  :   {'dd': 15, 'mm': 8, 'yy': 1947}
b  :   {'dd': 26, 'mm': 1, 'yy': 1950}
c  :   {'dd': 19, 'mm': 7, 'yy': 1985} ''' 
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
#a = c1() __init__() should return None, not 'int'
b = c2() #c2 class constructor 
print(b) # type n address
print(b . __init__()) #  c2 class constructor none 
c = c3() # c3 class constructor 
print(c . __init__()) # c3 class constructor none 

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1() #RecursionError: maximum recursion depth exceeded Dont create an object inside constructor 
# End  of  class
a = c1() 

#  Difference  between  init()    and  _init_()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1() # constructor 
print(a . __dict__) #{x:10,y:20}
b = c2() # 
print(b . __dict__) #{}
b . init() #Method
print(b . __dict__) #{x:30,y:40}



# Find  outputs (Home  work)
class   c1:
        def   __init__(self):
                self . a = 10
        def   m1(self):
                self . b = 20
#End  of  class  c1
class   c2:
        def  m3(self):
                x . e = 50
# End  of  class  c2
def   f1():
        x . c = 30
#  End  of  function  f1
x = c1() 
print(x . __dict__) #{a:10}
x . m1() 
print(x . __dict__) #{a:10,b:20}
f1()
print(x . __dict__) #{a:10,b:20,c:30}
x . d = 40
print(x . __dict__) #{a:10,b:20,c:30,d:40}
y = c2()
y . m3()
print(x . __dict__) #{a:10,b:20,c:30,d:40,e:50}
z = c1()
print(z . __dict__) #{a:10} 

# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1()
b = c1()
print(a . __dict__)
print(b . __dict__)
del  a . x
del  b . y
print(a . __dict__)
print(b . __dict__)
#print(a . x)
#print(b . y)
'''
{'x': 10, 'y': 20, 'z': 30}
{'x': 10, 'y': 20, 'z': 30}
{'y': 20, 'z': 30}
{'x': 10, 'z': 30}'''
#  Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('1st  constructor')
	def  __init__(self):
		print('2nd  constructor')
	def  __init__(self):
		print('3rd  constructor')
# End  of  the  class
a = c1() #3rd Constructor 

#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
#b = c1(30) # error need 2 arguments 
#c = c1() # error 
#  Find  outputs
class   c1:
	def  __init__(self):
		print('No  argument  constructor')
	def  __init__(self , x):
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) # Two  argument  constructor : 10 20
b = c1(30) # Two  argument  constructor : 30 200
c = c1() # Two  argument  constructor : 100 200 
# What  happens  when  function  and  class  have  same  name ?
def   f1():
	print('Function')
	return  25
class   f1:
	def  __init__(self):
		print('Constructor')
#end of the  class
a = f1() # f1 refers to class object 
print(a) #Constructor
#<__main__.f1 object at 0x000002583ED16A50>

# Find  outputs (Home  work)
class    c1:
	def   __init__(self):
		print('Constructor')
def  c1(): #recognised
	print('Function')
#end of the  class
a = c1() # function 
print(a) # none   

# Find outputs  (Home  work)
class    c1:
        def  __init__(self):
                print('Constructor')
def    c1(x):
        print('Function : ' , x)
# End  of  class  c1
#a = c1()
b = c1(25) # fucntion : 25
print(b) # none 
'''
#  Save  the  program  in  prog9a.py  file
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9a') '''


#  Find  outputs (Home  work)
from  prog9a  import  c1
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() # c1 class  of prog9b

#  Find  outputs (Home  work)
class   c1:
	def  _init_(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1
a = c1() # c1  class  of  prog9a

#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  from  statement
#How  to  import  class  c1  from  prog9a   with  from  statement
from prog9a import c1 as c2
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a=c1()
#print(a)
b=c2()
#print(b)
#How  to  create  c1  class  object  of  current  module
#How  to  create  c1  class  object  of  prog9a 
'''
How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
'''
#How  to  import  prog9a
import prog9a
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a=c1()
b=prog9a.c1()
#How  to  create  c1  class  object  of  current  module
#How  to  create  c1  class  object  of  prog9a
