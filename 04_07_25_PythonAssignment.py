
#1)
# Public  and  Private  members  demo  program
class  Test:
	def  __init__(self):
		self.x=10
		self.__y=20
	def  m1(self):
		print('m1  method')
		print(t.x)
		print(t._Test__y)
		t._Test__m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(t.x)
		print(t._Test__y)
# End  of  the  class
t = Test()
print('Outside')
print(t.x)
print(t._Test__y)
#print(t .__y)
print(t . __dict__)
t.m1()
t._Test__m2()
#t . __m2()
print('End')

'''
Outside
10
20
{'x': 10, '_Test__y': 20}
m1  method
10
20
__m2  method
10
20
Back to m1 method
__m2  method
10
20
End
'''
#________________________________________________

#2)
#  Find  outputs
class  c1:
	def __init__(self):
		self.x=10 #How  to  initialize  public  variable  'x'  with  10
		self.__x=20 #How  to  initialize  private  variable  'x'  with  20
		self.__x__=30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  __m1__(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a.__x__) #How  to  print  public  dunder  variable  'x'
print(a._c1__x) #How  to  print   private  variable  'x'
#print(a . __x)
a.m1() #How  to  call  public  method  m1()
a.__m1__() #How  to  call  public  dunder  method  m1()
a._c1__m1() #How  to  call  private  method  m1()
#a .__m1()

#_________________________________
#3)
'''
Find  outputs
Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End    of    the    class
a = c1()
a = None
b = c1()
del    b
c = c1()
c = c1()
d = c1()
e = c1()

"""
Object  is  created  at  address  :   4378602400
Object  at  address  4378602400  is  lost
Object  is  created  at  address  :   4379872144
Object  at  address  4379872144  is  lost
Object  is  created  at  address  :   4379872144
Object  is  created  at  address  :   4379059488
Object  at  address  4379872144  is  lost
Object  is  created  at  address  :   4379059792
Object  is  created  at  address  :   4378800304
Object  at  address  4379059488  is  lost
Object  at  address  4379059792  is  lost
Object  at  address  4378800304  is  lost
"""
#___________________________________________________________
#4)
# Identify  Error (Home  work)
class   c1:
	def  __del__(self,x):
		print('destructor')
a = c1()
a . __del__(25)#c1.__del__() missing 1 required positional argument: 'x'

#___________________________________________________________

#5)
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
			print('destructor')
			b = c1()
a = c1() #infinite
#____________________________________________________________

#6)
# Find  outputs (Home  work)
class   c1:
	def  __init__(self):
		print('constructor')
		del  self
	def  __del__(self):
		print('destructor')
		b = c1()
a = c1()#infinate loop

#______________________________________________________________

#7)
#  Find  outputs( Home  work)
class   c1:
	def  __del__(self):
		print('1st  destructor')
	def  __del__(self):
		print('2nd  destructor')
	def  __del__(self):
		print('3rd  destructor')
# End  of  the  class
a = c1()


"""
3rd  destructor
"""

#______________________________________________________________

#8
#Find  outputs (Home  work)
class   c1:
	def   __init__(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   __del__(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
print()
del   a
print('Hello')
del   b
print('Hi')
del   c
print('Bye')
d = c1()
print('End')



"""
Object  is  created  at  address  :   4366444800

Hello
Hi
Object  at  address  4366444800  is  lost  
Bye
Object  is  created  at  address  :   4368075344
End
Object  at  address  4368075344  is  lost 
"""
#______________________________________________________________

#9)
# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list

"""
Object  is  created  at  address  :   4333742336
Object  is  created  at  address  :   4335716944
Object  is  created  at  address  :   4335717264
Object  at  address  4335717264  is  lost 
Object  at  address  4335716944  is  lost 
Object  at  address  4333742336  is  lost 
"""

#______________________________________________________________

#10)
# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()
#print(a . _del_())
print('Hello')
del   a

"""
Hello
destructor
"""
#1)
# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()
print(sys . getrefcount(b))#5
print(sys . getrefcount(c1()))#1
print(sys . getrefcount(25))#734697
print(sys . getrefcount([10 , 20 , 15 , 18]))#1
print(sys . getrefcount(10.8))#3
print(sys . getrefcount({10 , 20 , 15 , 18}))#1
print(sys . getrefcount('Hyd'))#3
print(sys . getrefcount({10 : 20 , 30 : 40}))#1
print(sys . getrefcount((10 , 20 , 30 , 40)))#3

#2)
# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test()
print(t . __init__())
print(sys . getrefcount(t))
print(t . __del__())
print(sys . getrefcount(t))
print('Bye')



"""
Constructor  :   4303644928
Constructor  :   4303644928
None
2
Destructor  :   4303644928
25
2
Bye
Destructor  :   4303644928
"""

#3)
#  Gift
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()
	print(a)
	print('Function  end')
	return   a
print('Program  Begin')
b = f1()
print(b)
print('Program  End')



"""
Program  Begin
Function  Begin
<__main__.c1 object at 0x1025de900>
Function  end
<__main__.c1 object at 0x1025de900>
Program  End
"""
#4)
#  Gift
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
        return   a
print('Program  Begin')
f1()
print('Program  End')


"""
Program  Begin
Function  begin
Object  is    created
Function  end
Object  is  lost
Program  End
"""
#5)
# Find  outputs (Home  work)
class  c1:
	def  _init_(self):
		print('Object  is    created')
	def  _del_(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()
        print('Function  end')
print('Program  Begin')
b = f1()
print(b)
print('Program  End')

"""
Program  Begin
Function  begin
Function  end
None
Program  End
"""
#6)
# Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):#
		print('c1  class  object  is  created')
		self . b = k
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):
		print('c2  class  object  is  created')
		self . a = c1(self)#x.a=c1()
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()
print('program end')

"""
Program  begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
program end
c2  class  object  is  lost
c1  class  object  is  lost
"""

#7)
# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('Destructor')
		global  b
		b = self
a = c1()
del  a
print('Hello')

"""
Destructor
hello
"""

#8)
#(Home  work)
#  Can  string  be  enumerated ?
import   time
a = input('Enter  any  string  :  ')   #  Assume  that  input  is   HYD
e = enumerate(a)
while   True:
	try:
		print(next(e))
		time . sleep(1)
	except  StopIteration:
		break

"""
(0, 'h')
(1, 'y')
(2, 'd')
"""

#9)
# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
b = enumerate(a . keys())
disp(b)
c = enumerate(a . values())
disp(c)
d = enumerate(a . items())
disp(d)
f = enumerate(a , start = 5)
disp(f)
"""
(0, 'Empno')
(1, 'Emp Name')
(2, 'Sal')

(0, 25)
(1, 'Rama Rao')
(2, 10000.0)

(0, ('Empno', 25))
(1, ('Emp Name', 'Rama Rao'))
(2, ('Sal', 10000.0))

(5, 'Empno')
(6, 'Emp Name')
(7, 'Sal')
"""

#10)
# Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore' , 'Chennai' , 'Mumbai']
c = enumerate(a)
for  i , element  in  c:
	print(F'{element:15}  ... {b[i]}')
	time . sleep(1)

"""
Telangana        ... Hyderabad
Andhra  Pradesh  ... Amaravathi
Karnataka        ... Bangalore
TamilNadu        ... Chennai
Maharastra       ... Mumbai
"""
"""
#  Find  outputs  (Home  work)
import   time
a = [ 'Empno' , 'Emp Name' , 'Salary']
b = [ 25 , 'Rama  Rao' , 10000.0 , 'Male' , True]
c = zip(a , b)
while   True:
	try:
		print(next(c))
		time . sleep(1)
	except:
		break
 #  Find  outputs  (Home  work)
import   time
a = ['Telangana' , 'Andhra  Pradesh' , 'Karnataka' , 'TamilNadu' , 'Maharastra']
b = ['Hyderabad' , 'Amaravathi' , 'Banglore' , 'Chennai' , 'Mumbai']
c = [50000000 , 40000000 , 70000000 , 60000000 , 30000000]
for   x   in   zip(a , b , c):
	print(x)
	time . sleep(1)

#output
('Empno', 25)
('Emp Name', 'Rama  Rao')
('Salary', 10000.0)
('Telangana', 'Hyderabad', 50000000)
('Andhra  Pradesh', 'Amaravathi', 40000000)
('Karnataka', 'Banglore', 70000000)
('TamilNadu', 'Chennai', 60000000)
('Maharastra', 'Mumbai', 30000000)

# Find  outputs   (Home  work)
import   time
a = [1 , 2 , 3]
b = [4 , 5 , 6 , 7 , 8]
for  x , y  in   zip(a , b):
	print(x + y)
	time . sleep(1)


# Find outputs  (Home  work)
import   time
def   disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
	print()
a = [10 , 20 ,  30]
b = {1 : 2 , 3 : 4 , 5 : 6}
c = zip(a , b . keys())
disp(c)
d = zip(a , b . values())
disp(d)
e = zip(a , b . items())
disp(e)
f = zip(a , b)
disp(f)
g = zip(a)
disp(g)
h = zip(b)
disp(h)
i = zip()
disp(i)
#output
(10, 1)
(20, 3)
(30, 5)

(10, 2)
(20, 4)
(30, 6)

(10, (1, 2))
(20, (3, 4))
(30, (5, 6))

(10, 1)
(20, 3)
(30, 5)

(10,)
(20,)
(30,)

(1,)
(3,)
(5,)


# Find  outputs  (Home  work)
z = zip(range(5) , range(20 , 25))
a = [ [x , y]  for  x , y   in   z]
print(a)#[[0, 20], [1, 21], [2, 22], [3, 23], [4, 24]]

# Find  outputs (Home  work)
a = 'RAMA'
b = reversed(a)
print(type(b))#<class 'reversed'>
print(b)#<reversed object at 0x0000012F648FD6A0>
print(id(b))#address
print(*b)#A M A R
#print(b[0])
#print(b[1 : 3])
#print(b * 2)
#print(len(b))

# Can  tuple  be  reversed ?   (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)
print(type(b))
for  x  in   b:
	print(x)
	time . sleep(1)
# Can  dictionary  be  reversed  ? (Home  work)
import   time
def   disp(r):
	while  True:
		try:
			print(next(r))
			time . sleep(1)
		except:
			break
	print()
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Kiran' , 18 : 'Amar'}
#b = reversed(a . keys())
disp(b)
#c = reversed(a . values())
#disp(c)
#d = reversed(a . items())
#disp(d)
#e = reversed(a)
#disp(e)

#output
<class 'reversed'>
True
Hyd
10.8
25


# Find  outputs
a = 25
print(a)
'''
for  x   in   a:
	print(x)
print(iter(a))
print(next(a))
'''
"""
#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)
print(type(z))
print(z)
print('Iterate  zip  object  with   next()   function')
print(next(z))#How  to   iterate  zip  object  with  next  function
print('Iterate  zip  object  with  next  method')
print(z.__next__())#How  to   iterate  zip  object  with  next  method
print('Iterate  zip  object  with   for  loop')
for x,y in z:
	print(next(z)) #How  to   iterate  zip  object  with  for  loop
print('Iterate  elements  of  each  tuple  in  zip  object')
#How  to   iterate  elements  of  each  tuple  of  zip  object  with  for  loop
print('Unpacks  zip  object  with   *  operator  :  ' )
z = zip(a , b) 
print(*z)#How  to   unpack  zip  object   with  *  operator)
print()
z = zip(a , b) 
print('zip   object  in  the  form  of   list  :  ' ,list(z)) #How  to  convert  zip  object  to  list)
print()
z = zip(a , b) 
print('zip   object  in  the  form  of   dictionary :  ',dict(z) )  #How  to  convert  zip  object  to  dictionary)



#1. Find  outputs (Home  work)

'''
import  time
a = [25 , 10.8 , 3 + 4j , 'Hyd' , False]
f = filter(lambda   x :   True ,   a)
while  True:
	try:
		print(next(f)) #25   10.8   (3 + 4j)  Hyd False
		time . sleep(1)
	except:
		break
		
'''


#2. Find  outputs (Home  work)
'''
import  time
a = [25 , 10.8 , 3 + 4j ,  'Hyd' , True]
f = filter(lambda  x  :  False ,  a)
while  True:
	try:
		print(next(f)) #SIE 
		time . sleep(1)
	except:
		break
		
'''


#3.Find  outputs (Home  work)
'''
import  time
a = [25 , 10.8 , False ,  3 + 4j , 0 , 'Hyd' , '' , (25,)  ,  () ]
f = filter(lambda   x   :   x   ,   a)
while  True:
	try:
		print(next(f)) #25  10.8  (3 + 4j)  Hyd  (25,) 
		time . sleep(1)
	except:
		break
'''


#4. Find outputs

'''
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
list = [10 , 0 ,  -25 , () , (25,) , 'Hyd', '' , [] , 10.8 , 0.0 , [10 , 20] , True , False]
f1 = filter(lambda  x : None  , list)
print('Filter  f1') #Filter f1 
disp(f1) # No output 
f2 = filter(None , list)
print('Filter  f2') #Filter f2 
disp(f2) #10 -25 (25,) Hyd 10.8 [10,20] True 
'''



#5. Find outputs  (Home  work)

'''
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a)
while   True:
	try:
		print(next(f)) #Rama Rao Rajesh Kiran Manohar Vamsi
		time . sleep(1)
	except:
		break
'''

#6.Find  outputs (Home  work)

'''
import   time
list=[('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18)]
f = filter(lambda   x  :   x[1]  >=  12 , list)
while   True:
	try:
		print(next(f)) #('B',20) ('C' , 15) ('E' , 18)
		time . sleep(1)
	except:
		break
		
'''


#7. Find  outputs (Home  work)
"""
import   time
list = [
             {
                'Roll Num' :  10 ,
                'Stud Name' : 'Rama Rao' ,
                'Marks' : 75
              } ,
              {
                'Roll Num' :  20 ,
                'Stud Name' : 'Sita' ,
                'Marks' : 52
              } ,
             {
               'Roll Num'  :  15 ,
               'Stud Name' : 'Kiran' ,
               'Marks' : 65
             } ,
             {
               'Roll Num'  :  18 ,
               'Stud Name' : 'Amar' ,
               'Marks' : 48
             } ,
             {
               'Roll Num' :  5 ,
               'Stud Name' : 'Rajesh' ,
               'Marks' : 82
             }
        ]  #  List  of  dictionaries
f = filter(lambda  x :  x['Marks'] >= 60 , list)
while   True:
	try:
		print(next(f)) 
		'''
		 {'Roll Num' :  10 ,'Stud Name' : 'Rama Rao' ,'Marks' : 75}
		 {'Roll Num'  :  15 ,'Stud Name' : 'Kiran' ,'Marks' : 65}
		 {'Roll Num' :  5 , 'Stud Name' : 'Rajesh' ,'Marks' : 82}
		'''
		time . sleep(1)
	except:
		break
		
"""

#8.Find  outputs (Home  work)

"""
import  time
def  disp(f):
	while  True:
		try:
			print(next(f))
			time . sleep(1)
		except:
			break
a = [   { 'country' : 'India' , 'sale' : 150.5} ,
          { 'country' : 'china' , 'sale' : 200.2} ,
          { 'country' : 'USA' , 'sale' : 300.3} ,
          { 'country' : 'UK' , 'sale' : 210.4} ]
f1 = filter (lambda  x  :   x['country'] . startswith('U') , a)
print('Filter  f1') #Filter  f1
disp(f1)
'''
{ 'country' : 'USA' , 'sale' : 300.3} 
{ 'country' : 'UK' , 'sale' : 210.4}

'''
f2 = filter(lambda  x  :  x['sale']  >=  200  , a)
print('Filter  f2') #Filter  f2
disp(f2)
'''
 { 'country' : 'china' , 'sale' : 200.2} 
 { 'country' : 'USA' , 'sale' : 300.3} 
 { 'country' : 'UK' , 'sale' : 210.4}
'''

"""


#9. How  to  print  fliter  object  in  different  ways ?
'''
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while(True):
    try:
        print(next(f)) #How  to iterate  filter  object  with  next()  function
        time.sleep(1)
        
    except:
        break 
    
print('Iterate  filter  object  with   for  loop')
for i in filter(lambda  x  :  x  %  2  ==  0 , a):
    print(i) #How  to iterate  filter  object  with  for  loop
    time.sleep(1)
    
print('Unpacking  filter  object :  ' , *filter(lambda  x  :  x  %  2  ==  0 , a)) # How  to  unpack  filter  object
print()

print('filter  object  in  the  form  of  list  :  ' ,list(filter(lambda  x  :  x  %  2  ==  0 , a)))
# How  to  convert  filter  object  to  list

'''

'''
# 10.Write  a  program  to  print  odd  numbers  between  1  and  20  with  filter  iterator
Odd  numbers  between  1  and  20
1
3
5
7
9
11
13
15
17
19
'''

'''
from time import sleep
f= filter(lambda x:x%2==1,range(1,21))

print("Odd  numbers  between  1  and  20")
for i in f:
    print(i)
    sleep(1)
'''


'''
#11. Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set

Enter  mixed  case   string  :  RamA raO
{'O', 'A'}
'''

'''
s=input("Enter  mixed  case   string  : ").upper()
f=filter(lambda x: x in "AEIOU" ,s)
S=set()

for i in f:
    S.add(i)
    
print(S)
'''


#12. Nested  filter  i.e.  filter  on  filter
'''
import   time
list =  [ (10 , 'Rama' , 10000.0) ,
            (20, 'Sita' , 7000.0) ,
            (15 , 'Rajesh' , 15000.0) ,
            (5 , 'Amar' ,  12000.0) ,
            (18 , 'Ramesh' , 8000.0) ]
f = filter(lambda  x :  x[1] . startswith('R')  , filter(lambda  x :  x[2] >= 10000 , list))
while   True:
	try:
		print(next(f)) # (10 , 'Rama' , 10000.0) (15 , 'Rajesh' , 15000.0)
		time .  sleep(1)
	except:
		break
		
'''

#13. Modify  following  program  with  regular  function  and  for  loop
'''
import  time

def square(x):
    return x*x 
    
a = [10 , 20 , 15 , 18 , 5]
m = map(square ,  a)
print(type(m)) #<class 'map'>
print(m) #<map object at 0xaddress>

for i in m:
    print(i)
    time.sleep(1)
    
'''

#14. Find  outputs (Home  work)
'''
import  time
a = [ ('A' , 10) , ('B' , 20) , ('C' , 15) , ('D' , 5) , ('E' , 18) ]
m = map(lambda   x  :  x[1]  ,  a)
while   True:
	try:
		print(next(m)) # 10 20 15 5 18 
		time . sleep(1)
	except  StopIteration:
		break
    
'''


#15. Find  outputs (Home  work)

import   time
def  disp(m):
	while   True:
		try:
			print(next(m))
			time . sleep(1)
		except:
			break
list = [    { 'country' : 'India' , 'sale' : 150.5} ,
              { 'country' : 'China' , 'sale' : 200.2} ,
              { 'country' : 'USA' , 'sale' : 300.3} ,
              { 'country' : 'UK' , 'sale' : 210.4} ]
m1 = map(lambda  x  :  x['country'] , list)
print('Map   m1') #Map m1 
disp(m1) # India China USA UK 
m2 = map(lambda  x  :  x['sale']  , list)
print('Map   m2') #Map m2 
disp(m2) # 150.5 200.2 300.3 210.4 



'''
#16. Write  a  program  to  convert  each  celsius  temperature  of  the  list  to  farenheit  temperature

1) What  is  the  formula  to  convert  celsius  temperature  to  farenheit ?  --->   1.8 * celsius  temp + 32

2) Let  input  be   list  of  celsius  temperatures  such  as  [30 , 40 , 50 , 25]
    What  is  the  output ?  --->   1.8 * 30 + 32
							                      1.8 * 40 +32
								                  1.8 * 50 + 32
								                  1.8 * 25 + 32
								                  
Enter  list  of  celsius  temperatures :  [10,20,15,18]
Farenheit   temperatures
50.0
68.0
59.0
64.4
'''

c=eval(input("Enter  list  of  celsius  temperatures : "))
m=map(lambda x:9*x/5 + 32 , c)
print("Farenheit   temperatures")
for i in m:
    print(i)
    



'''
#17.Write  a  program  to  print  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ....... 2 ^ 9  using  map   object (Home  work)

Powers  of   2
1
2
4
8
16
32
64
128
256
512

'''

from time import sleep
m=map(lambda x:2**x ,range(10))
print("Powers  of   2")

for i in m:
    print(i)
    sleep(1)
    


'''
#18. Write  a  program  to  determine  area  of  circle  for  each  radius  in  the  list

1) What  is  area  of  circle ?  --->  pi * r * r

2) Let  input  be  [3.5 , 2.8 , 4.2  , 1.9]
    What  are  the  outputs ?  --->  Area  of  radius  3.5
						                              Area  of  radius  2.8
						                              Area  of  radius  4.2
						                              Area  of  radius  1.9
						                              
Enter  list  of  radii  :   [1,2,3,4]
Area  of  each  radius  in  the  list
3.14
12.57
28.27
50.27
'''


from math import * 
from time import sleep 

r=eval(input("Enter  list  of  radii  : "))
m=map(lambda x:pi*x*x  , r)
print("Area  of  each  radius  in  the  list")
for i in m:
    print(round(i,2))
    sleep(1)


'''
#19.Write  a  program  to  add  two  tuples  of  difierent  sizes  and  store  the  results  in  3rd  tuple

Let  1st  tuple  be  (10 , 20 , 30 , 40)  and  2nd  tuple  be  (1 , 2 , 3 , 4 ,  5  ,  6)
What  is  the  3rd  tuple ?  --->  (10 + 1 , 20 + 2 , 30 + 3 , 40 + 4)   and  5  and 6  are  ignored


Enter  first  tuple :  (10,20,15,18)
Enter  second  tuple :  (30,40,35,12,100,200)
Addition  tuple  :   (40, 60, 50, 30)
'''


t1=eval(input("Enter  first  tuple : "))
t2=eval(input("Enter  second  tuple : "))
l=[]

m=map(lambda x,y:x+y,t1,t2)

for i in m:
    l.append(i)

print("Addition  tuple  :",tuple(l))



'''
#20. Write  a  program  to  multiply  two  lists  and  store  results  in  3rd  list

Let  1st  list  be  [10 , 20 , 15 , 18 , 19 , 17]  and  2nd  list  be  [1 , 5 , 3 , 2]
What  is  the  3rd  list ?  ---> [10 * 1 , 20 * 5 , 15 * 3 , 18 * 2]  and  ignores  19  and  17

Hint:  Use  map

Enter  first  list :  [10,20,15,18]
Enter  second  list :  [1,2,3,4]
Multiplication  list :   [10, 40, 45, 72]
'''


l1=eval(input("Enter  first  list : "))
l2=eval(input("Enter  second  list : "))
l=[]

m=map(lambda x,y:x*y,l1,l2)

for i in m:
    l.append(i)

print("Multiplication  list :",l)

'''

#21. filter  inside  map

'''
import  time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
m = map(lambda  y  :   y + y ,  filter(lambda  x  :  x >= 15 , a))
while   True:
	try:
		print(next(m)) # 40 30 36 50 34 
		time . sleep(1)
	except:
		break
'''

#22. map  inside  filter (Home  work)
'''
import   time
a = [10 , 20 , 15 , 12 , 18 , 5 , 14 , 25 , 17]
f = filter(lambda  y  :   y  % 2 == 0 , map (lambda  x : x ** 2 , a))
while   True:
	try:
		print(next(f)) #100 400 144 324 196 
		time . sleep(1)
	except:
		break
		


'''
#23. Write  a  program  to  determine  largest  element  of  the  list  with  reduce()  function

Let  list   be  [10 , 20 , 15 , 30 , 25 , 40 , 35]
What  is   the  largest  element  of  list ?  ---> 40

Hint:  Use  reduce()  function


Enter list of numbers (or) strings:[10 , 20 , 15 , 30 , 25 , 40 , 35]
Largest  element  :    40
'''

from functools import reduce 

l=eval(input("Enter list of numbers (or) strings: "))
r=reduce(lambda x,y:max(x,y),l)
print("Largest  element  :",r)

'''


#24. Find  outputs  (Home  work)

'''
from  functools  import  reduce
a = [ 10 , 20 , 15 , 5 , 12 , 18 , 25 , 14]
ans = reduce( lambda  x , y  : x + y , map(lambda  y :  y ** 2 , filter(lambda  x  :  x  >= 15 , a)))
#[400+225+324+625] =(1574)
print(ans)


# Find   outputs (Home  work)
from  itertools  import  count
c = count()
print('While  loop')
while   True:
        x = next(c)
        if   x > 9:
                break
        print(x)
print('For  loop')
for  x  in  count():
	if  x  >  20:
		break
	print(x)
#end  of  for  loop
print('Element :  ' , end = '\t')
print(next(count()))
c = count()
print(*c)
#  Find  outputs (Home  work)
from  itertools  import  count
def  disp(cnt):
        for  i  in   range(4):
                print(next(cnt) , end = '\t')
        print()
#end  of  the  function
a = count(start = 10)
disp(a)
b = count(start = 10 , step = 5)
disp(b)
c = count(start = 10 , step = -2.5)
disp(c)
d = count()
disp(d)
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(list , cnt)
print('While  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(list , cnt)
print('Next  element :  ' , next(z3))
print('*z3 :  ' ,  *z3)
z4 = zip(list , cnt)
print('Next  element  : ' ,  next(z4))
#  Find  outputs (Home  work)
from   itertools    import    count
cnt = count()
list = [10 , 20 , 15 , 18]
z1 = zip(cnt , list)
print('while  loop')
while   True:
        try:
                print(next(z1))
        except:
                break
z2 = zip(list , cnt)
print('for  loop')
for  x   in    z2:
        print(x)
z3 = zip(cnt , list)
print(next(z3))
print(*z3)
z4 = zip(list , cnt)
print(next(z4))
#  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)
print(type(z1))
disp(z1)
z2 = zip_longest(range(7) , list)
print(type(z2))
disp(z2)
#  Find  outputs  (Home  work)
import   time
from    itertools    import  cycle
list = [10 , 20 , 30 , 40]
c = cycle(list)
print(type(c))
while   True:
	print(next(c))
	time . sleep(1)
#  Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
r = repeat(25 , times = 3)
print('1st  repeat  object')
while   True:
	try:
		print(next(r))
		time . sleep(1)
	except:
		break
print('2nd  repeat  object')
r  =  repeat('Hyd')
while   True:
	print(next(r))
	time . sleep(1)
# Find  outputs  (Home  work)
import  time
from  itertools  import  repeat
m = map(pow , range(10) ,  repeat(2))
while   True:
	try:
		print(next(m))
		time . sleep(1)
	except:
		break
#  Find  outputs (Home  work)
import  time
def  disp(itr):
	while  True:
		try:
			print(next(itr))
			time . sleep(1)
		except:
			break
from  itertools  import  combinations,permutations
list = ['A' , 'B' , 'C' , 'D']
c = combinations(list , 3)
print('Different  Combinations')
disp(c)
print('Different   Permutations')
p = permutations(list , 3)
disp(p)

# Find  outputs
import  time
class   c3:
	def  __iter__(self):
		print('_iter_  method ')
		return  reversed([10 , 20 , 15 , 18])
# End  of  the  class
itr = c3()
for  x  in   itr:
	print(x)
	time . sleep(1)
#print(next(itr))
'''
Output:
_iter_ method
18
15
20
10
'''
# Identify  Error  (Home  work)
class   c4:
	def  __iter__(self):
		print('_iter_  method ')
		return   self
# End  of  the  class
itr = c4()
for  x  in itr:
	print(x)
'''
Output:
_iter_  method
iterator has to be returned but no iterator
'''
# Identify  Error
class   c5:
	def  __iter__(self):
		print('_iter_  method ')
# End  of  the  class
itr = c5()
for x in itr:
	print(x)
'''
Output:
_iter_  method 
itr returning none but object for for loop has to be iterator
'''
# Identify  Error
class   c6:
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a=c6()
print(dir(c6))
for  x  in  a:
        print(x)
while  True:
	print(next(a))
a.next()
'''
Output:
c6 is not iterable
and is not iterator
'''
# Find  outputs(Home  work)
class   c1:
	def   __init__(self):
		self . x =  1
	def   __iter__(self):
		print('_iter_    method')
		return  self
	def  __next__(self):
		value =  self . x
		self . x  +=  1
		return  value
a = c1()
print('Elements  of  iterator  with  for  loop')
for   element   in   a:
	print(element)
	if  element==5:
               break
print('Elements  of  iterator  with  next()  function')
while    True:
	element = next(a)
	print(element)
	if  element==10:
		break
print('Elements  of  iterator  with  for  loop')
for   element   in    a:
	print(element)
	if  element==15:
		break
'''
Output:
Elements  of  iterator  with  for  loop
_iter_    method
1
2
3
4
5
Elements  of  iterator  with  next()  function
6
7
8
9
10
Elements  of  iterator  with  for  loop
11
12
13
14
15
'''
# Find  outputs (Home  work)
import   time
class  Remote:
	def    __init__(self):
		self . list = ['Tv 9' , 'Espn' , 'Zee Tv' , 'ETV']
		self . index = -1
	def   __iter__(self):
		return  self
	def   __next__(self):
		self . index += 1
		if   self.index==len(self . list):
			raise  StopIteration
		return    self.list[self . index]
# End  of  the  class
r = Remote()
for   x    in    r:
	print(x)
	time.sleep(1)
'''
Output:
Tv 9
Espn
Zee Tv
ETV
'''
'''
PROGRAM:

Write  an  iterator  which  yields  10 , 11 , 12 , 13 , ...... 20

Hint: Use  for  loop
'''
class sol:
	def __iter__(self):
		self.first=int(input("enter starting number :"))
		self.last=int(input("enter starting number :"))
		print(self.first)
		return self
	def __next__(self):
		if self.first<self.last:
			self.first+=1
			return self.first
		else:
			raise StopIteration
a=sol()
for i in a:
	print(i)
'''
Output:
enter starting number :10
enter starting number :20
10
11
12
13
14
15
16
17
18
19
20
'''
'''
PROGRAM :
Design  an  iterator  which  yields  powers  of  two   i.e.  2 ^ 0 , 2 ^ 1 , 2 ^ 2 , ........ 2 ^ 7

Use  for  loop
'''
class c1:
	def __iter__(self):
		self.x=-1
		return self
	def __next__(self):
		if self.x<=7:
			self.x+=1
			return 2**self.x
		else:
			raise StopIteration
if __name__=="__main__":
	a=c1()
	for i in a:
		print(i)
'''
Output:
1
2
4
8
16
32
64
128
256
'''
# Find  outputs (Home  work)
class c1:
    x = 10 #static variable due to inside the class
    def __init__(self):
	    self . y = 20 #instance variable due to self 
a = c1() #object a is created and constructor will execute
b = c1() #object b is created and constructor will execute
a . x += 1 #static varible is modified to 11
b . y += 1 #static varible is modified to 11
print(a . x)#11
print(a . y) #20
print(b . x) # 10
print(b . y) #21
print(c1 . x) #10
print(a . __dict__) #{y:20,x:11}
print(b . __dict__) #{y:21}
print(c1 . __dict__) #{x:10}

object a--> y=20,

object b-->y=20

# Find  outputs (Home  work)
class  c1:
	x = 10 #ststic variable
	def  m1(self):
		self . x = 20 #instance variable
a = c1() #object is created
a . m1() 
print(c1 . x) #10
print(a . x) #20

#object a--> x=20

# Find  outputs  (Home  work)
class   c1:
	x = 10
	def  __init__(self):
		self . y = 20
	@classmethod
	def   m1(cls):
		cls . x = 30
		cls . y = 40
# End  of  the  class
a = c1() #constructor is executed 
b = c1()
c1 . m1()
print(a . x) #30
print(a . y) #20
print(b . x)#30
print(b . y)#20
print(c1 . x , c1 . y)#(30,40)
#print(cls . x , cls . y)#error only inside classmethod it is used
#print(self . x , self . y)#self is not defined


object a-->y=20

object b-->y=20

static method-->x=30,y=40

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1(35) #35

#  Find  outputs
class   c1:
	
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #25
a = c1()
a . m1()#type and adress
a . m1(35)#error

#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print('static  method')
		print(self)
	def   m1(self):
		print('instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) #'static  method'  <next line> 25
a = c1()
a . m1() #'instance  method' <next line> type and adress

# How  to  access  static  variable  in  different  ways  ?
class   c1:
	x = 25
	def   __init__(self):
		print(self.x) #How  to  print  static  variable  'x'
		print(c1.x)#How  to  print  static  variable  'x'  in  another  way
		#print(x)
	def   m1(self):
		#print(x)#How  to  print  static  variable  'x'
		print(self.x)#How  to  print  static  variable  'x'  in  another  way
		print(c1 . x)
	@classmethod
	def   m2(cls):
		#print(x)#How  to  print  static  variable  'x'
		print(cls.x)#How  to  print  static  variable  'x'  in  another  way
		#print(self . x)
	@staticmethod
	def   m3():
		pass
		#print(x)#How  to  print  static  variable  'x'
		#print(cls . x)
		#print(self . x)
# End  of  the  class
print(c1.x)#How  to  print  static  variable  'x'
print(x)#How  to  print  static  variable  'x'  in  another  way
print(x)
print(self . x)
print(cls . x)
a=c1()
a.m1()#How  to  call  method  m1()
c1.m2()#How  to  call  method  m2()
c1.m3()#How  to  call  method  m3()

# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a=10 #How  to  add  static  variable  'a'  with  value  10
	def    __init__(self):
		c1.b=20 #How  to  add  static  variable  'b'  with  value  20
		self.c=30 #How  to  add  instance  variable  'c'  with  value  30
		#cls . k = 25
	def   m1(self):
		c1.d=40 #How  to  add  static  variable  'd'  with  value  40
		self.e=50 #How  to  add  instance  variable  'e'  with  value  50
	@classmethod
	def   m2(cls):
		cls.f=60 #How  to  add  static  variable  'f'  with  value  60
		c1.g=70 #How  to  add  static  variable  'g'  with  value  70  in  another  way
		#self . k = 25
	@staticmethod
	def   m3():
		c1.h=80 #How  to  add  static  variable  'h'  with  value  80
		#self . k = 25
		#cls . k = 35
#End  of  the  class
print('Begin')
print(c1 . __dict__)
print()
print()
x = c1()
print('Constructor')
print(c1 . __dict__)
print()
print()
x.m1()#How  to  call  m1()  method
print('Instance  method  m1')
print(c1 .__dict__)
print()
print()
c1.m2()#How  to  call  m2()  method
print('class  method   m2')
print(c1 . __dict__)
print()
print()
c1.m3()#How  to  call  m3()  method
print('static   method   m3')
print(c1 . __dict__)
print()
print()
c1.i=90 #How  to  add  static  variable  'i'  with  value  90
x.j=100 #How  to  add  instance  variable  'j'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)
print()
print()
print("Object  'x' ")
print(x . __dict__)

outputs---
Begin
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None}


Constructor
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20}


Instance  method  m1
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50}


class  method   m2
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50, 'f': 60, 'g': 70}


static   method   m3
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50, 'f': 60, 'g': 70, 'h': 80}


Outside  the  class
{'__module__': '__main__', 'a': 10, '__init__': <function c1.__init__ at 0x000001C40D9B2DD0>, 'm1': <function c1.m1 at 0x000001C40D9B2E60>, 'm2': <classmethod(<function c1.m2 at 0x000001C40D9B2EF0>)>, 'm3': <staticmethod(<function c1.m3 at 0x000001C40D9B2F80>)>, '__dict__': <attribute '__dict__' of 'c1' objects>, '__weakref__': <attribute '__weakref__' of 'c1' objects>, '__doc__': None, 'b': 20, 'd': 40, 'e': 50, 'f': 60, 'g': 70, 'h': 80, 'i': 90}


Object  'x'
{'c': 30, 'j': 100}


# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4)
# End  of  the  class
print(c1.a) #How  to  print  variable  'a'
print(c1.b) #How  to  print  variable  'b'
print(c1.c) #How  to  print  variable  'c'

outputs--
1
2
3

# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70 (Home  work)
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  ')) #10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  ')) #a.y=20,b.y=40,c.y=60
		self . z = int(input('Enter  any  number  :  ')) #a.z=30,b.z=50,c.z=70
	def   compute(self):
		Test . x += 1 #11
		self . y  += 1 #41
		self . z  += 1 #51
		self . x  += 1 #13
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()
a = Test()
b = Test()
c = Test()
a . get2()
b . get2()
c . get2()
a . compute()
b . compute()
c . compute()
a . disp()
b . disp()
c . disp()

outputs--
1st--13 21 31 12
2nd--13 41 51 13
3rd--13 61 71 14


Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  --->  x . a[i]
    How  to  access  elements  of  2nd  list ?  --->  y . a[i]

4) How  to  access  static  variable  'n' ?  --->  vector . n

class  vector:
	@staticmethod
	def get1():
		vector.n=int(input('enter no of elements:')) #How  to  read  number  of  elements  into  variable  'n'
	def get2(self):
		self.d=eval(input('enter list elements:'))#How  to  read  the  list  into  the  object
	def add(self , x , y):
		self.d=[]
		for i in range(vector.n):
				self.d.append(a.d[i]+b.d[i]) #How  add  the  lists  held  by  objects  'x'  and  'y'  and  store  the  results  in  list  held  by  owner  object
a=vector()
vector.get1() #How  to  call  get1()  method
a.get2() #How  to  read  the  list  into  1st  object
b=vector()
b.get2() #How  to  read  the  list  into  2nd  object  'b'
c=vector()
c.add(a,b)#How  to  add  the  lists  held  by  objects  'a'  and  'b'  and  store  the  results  in  list  of  3rd  object  'c'
print(c.d) #How  to  print  the  list  of  3rd   object

outputs--
enter no of elements:4
enter list elements:[1,2,3,5]
enter list elements:[4,5,6,7]
[5, 7, 9, 12]


Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods

class  c1:
	x = 1
	y = 2
	z = 3
a={}
b=(c1.__dict__)
for key in b:
	if not key.startswith('__') and not key.endswith('__'):
				 a[key]=b[key]
print('static varibles:',a)	
outputs--
static varibles: {'x': 1, 'y': 2, 'z': 3}
#  End  of  the  class'''
