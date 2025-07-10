#  Find  outputs (Home  work)
from threading import *
import time
def f1():
    for i in range(10):
        print('child  thread') # child  thread (printed multiple times depending on time.sleep)
        time.sleep(2)
main = main_thread()
print(main.daemon) # False
# main.daemon = True # AttributeError will occur here if uncommented
t = Thread(target = f1)
print(t.daemon) # False
t.daemon = True
print(t.daemon) # True
t.start()
t.daemon = True # No effect (must be before start)
time.sleep(5)
print('End  of  main  thread') # End  of  main  thread

'''(Home  work)
Find  outputs

Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop  for  each  thread
'''
from  threading  import  *
def    f1():
	name = current_thread() . name
	for  i  in  range(1 , 11):
			print(name , ' : ' , i)
	print(name , 'is  dead')
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t3 . daemon = True
t1 . start()
t2 . start()
t3 . start()
print('main  thread  is  dead')
'''output:  main  thread  is  dead
			One  :  1
			Two  :  1
			Three  :  1
			One  :  2
			Two  :  2
			Three  :  2
			One  :  3
			Two  :  3
			Three  :  3
			One  :  4
			Two  :  4
			Three  :  4
			One  :  5
			Two  :  5
			Three  :  5
			One  :  6
			Two  :  6
			One  :  7
			Two  :  7
			One  :  8
			Two  :  8
			One  :  9
			Two  :  9
			One  : 10
			Two  : 10
			One is  dead
			Two is  dead
'''
'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  rational  class  objects

1) First  rational  number  --->  2 / 3
   Second  rational  number ---> 5 / 9
   What  is  the  sum  ?  --->   2 / 3 + 5 / 9 =  (18 + 15) / 27 =  33 / 27 =  11 / 9
   What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 =  (18 - 15) / 27 =  3 / 27 =  1 / 9
   What  is  the  product  ?  --->  2 / 3 * 5 / 9 =  10 / 27 =  10 / 27
   What  is   the  division  ?  --->   2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 = 18 / 15 = 6 / 5

2) First  rational  number  --->  2 / 3
   Second  rational  number ---> 0 / 9
   What  is  the  sum  ?  --->  2 / 3 + 0 / 9 =  (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  --->  2 / 3 - 0 / 9 = (18 - 0) / 27 = 18 / 27 = 2 / 3…
'''
from math import gcd

class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        self.simplify()

    def simplify(self):
        g = gcd(self.num, self.den)
        self.num //= g
        self.den //= g

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Rational(n, d)

    def __sub__(self, other):
        n = self.num * other.den - other.num * self.den
        d = self.den * other.den
        return Rational(n, d)

    def __mul__(self, other):
        return Rational(self.num * other.num, self.den * other.den)

    def __truediv__(self, other):
        return Rational(self.num * other.den, self.den * other.num)

# Test Case 1
r1 = Rational(2, 3)
r2 = Rational(5, 9)
print("Sum:", r1 + r2)         # 11/9
print("Difference:", r1 - r2)  # 1/9
print("Product:", r1 * r2)     # 10/27
print("Division:", r1 / r2)    # 6/5

# Test Case 2
r3 = Rational(2, 3)
r4 = Rational(0, 9)
print("Sum:", r3 + r4)         # 2/3
print("Difference:", r3 - r4)  # 2/3
print("Product:", r3 * r4)     # 0/1
print("Division:", r3 / Rational(1, 1)) # safe division
'''
Write  a  program  to  overload  + ,   -  ,  *   and   /   operators  on  complex  class  objects  without
using  pre-defined  complex  object

First  complex  number  --->  3 + 4i
Second  complex  number ---> 5 + 6i
What  is  the  sum  ?  --->   8 + 10i
What  is  the  difference  ?  --->  -2 - 2i
What  is  the  product  ?  ---> (3 + 4i) * (5 + 6i) =   15 + 18i + 20i - 24 =   -9 + 38i
What  is   the  division  ?  --->  (3 + 4i) / (5 + 6i) =   (3 + 4i) * (5 - 6i) / (5 + 6i) * (5 - 6i) =
 											     =  (15 - 18i + 20i + 24) / (25 + 36) =  39 / 61 + 2i / 61
'''
class Complex:
    def __init__(self, real=0, imag=0):
        self.r = real
        self.i = imag

    def get(self):
        self.r = int(input("Enter real part: "))
        self.i = int(input("Enter imaginary part: "))

    def __str__(self):
        if self.i >= 0:
            return f"{self.r} + {self.i}i"
        else:
            return f"{self.r} - {abs(self.i)}i"

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.r ** 2 + other.i ** 2
        real = (self.r * other.r + self.i * other.i) / denom
        imag = (self.i * other.r - self.r * other.i) / denom
        return Complex(round(real, 2), round(imag, 2))

# Test
c1 = Complex(3, 4)
c2 = Complex(5, 6)

print("First Complex Number:", c1)       # 3 + 4i
print("Second Complex Number:", c2)      # 5 + 6i
print("Sum:", c1 + c2)                   # 8 + 10i
print("Difference:", c1 - c2)            # -2 - 2i
print("Product:", c1 * c2)               # -9 + 38i
print("Division:", c1 / c2)              # 0.64 + 0.03i

'''
Overload   > ,  < ,  == ,  >=  , <=  , !=  on   Rational   class  objects

1) Let  object  'a'   contain   2 / 3  and   object  'b'  contain  5 / 9
    What  is  the  result  of  a > b ?  --->  True  due  to 18 > 15
    What  is  the  result  of  a < b ?  --->  False  due  to  18  is  not  <  15
    What  is  the  result  of  a == b ?  --->  False  due  to  18  is  not  =  15
    What  is  the  result  of  a >= b ?  ---> True  due  to 18 >= 15
    What  is  the  result  of  a <= b ?  --->  False  due  to  18  is  not  <=  15
    What  is  the  result  of  a != b ?  --->  True  due  to 18 != 15

2) Imp  point  is  cross  product

3) What  is  the  method  call  to  _gt_()  method ?  --->  a > b
     What  is  the  method  call  to  _lt_()  method ?  ---> …'''
class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return f"{self.num} / {self.den}"

    def __gt__(self, other):  # a > b
        return self.num * other.den > other.num * self.den

    def __lt__(self, other):  # a < b
        return self.num * other.den < other.num * self.den

    def __eq__(self, other):  # a == b
        return self.num * other.den == other.num * self.den

    def __ge__(self, other):  # a >= b
        return self.num * other.den >= other.num * self.den

    def __le__(self, other):  # a <= b
        return self.num * other.den <= other.num * self.den

    def __ne__(self, other):  # a != b
        return self.num * other.den != other.num * self.den
a = Rational(2, 3)   # 2/3
b = Rational(5, 9)   # 5/9

print("a:", a)                       # 2 / 3
print("b:", b)                       # 5 / 9
print("a > b :", a > b)              # True  (2*9 > 5*3) => 18 > 15
print("a < b :", a < b)              # False
print("a == b :", a == b)            # False
print("a >= b :", a >= b)            # True
print("a <= b :", a <= b)            # False
print("a != b :", a != b)            # True

# Find  outputs  (Home work)
class c1:
    def __init__(self, y):               
        self.x = y

    def __ge__(m, n):                     
        print('_ge_ method :', m.x, n.x)
        return m.x > n.x                  # Not >=, only >

# End of the class
a = c1(10)
b = c1(20)

print(a >= b)  # _ge_ method : 10 20 → False
print(a <= b)  # TypeError: '<=' not supported between instances of 'c1' and 'c1'

# Find  outputs  (Home  work)
class c1:
    def __init__(self, y):                    
        self.x = y

    def __eq__(m, n):                          
        print('__eq__ method :', m.x, n.x)
        return m.x == n.x                      # Returns True if values equal

# end of the class
a = c1(10)
b = c1(20)

print(a == b)     # __eq__ method : 10 20 → False
print(a != b)     # __eq__ method : 10 20 → True

# Find  outputs  (Home  work)
class c1:
    def __init__(self, y):                    
        self.x = y

    def __eq__(m, n):                        
        print('__eq__ method  :', m.x, n.x)   # No return → defaults to None

# End of the class

a = c1(25)
b = c1(25)

print(a == b)       # __eq__ method  : 25 25 → None (no return = Falsey)
print(a != b)       # __eq__ method  : 25 25 → True (since None → not equal)
print(a.x != b.x)   # False (25 == 25)

# Find  outputs  (Home  work)
class c1:
    def __init__(self, y):                   
        self.x = y

    def __ne__(m, n):                          
        print('__ne__ method :', m.x, n.x)
        return m.x != n.x                      # Returns True if values not equal

# end of the class

a = c1(25)
b = c1(25)

print(a != b)      # __ne__ method : 25 25 → False
print(a == b)      # → Uses default object __eq__ → different objects → False
print(a is b)      # → False (different memory addresses)

# Find  outputs  (Home  work)
class c1:
    def __init__(self, y):                    
        self.x = y

    def __ne__(m, n):                         
        print('__ne__ method  :', m.x, n.x)
        return m.x != n.x

# end of the class

a = c1(10)
b = a

print(a != b)      # __ne__ method  : 10 10 → False
print(a == b)      # → True (same object, default __eq__ uses identity)

# Find  outputs  (Home  work)
class c1:
    def __init__(self, y):                            
        self.x = y
    def __gt__(p, q):                                 # Corrected __gt__ for >
        print('c1 class __gt__ method:', p.x, q.x)
        return p.x > q.x

class c2:
    def __init__(self, y):                           
        self.x = y
    def __gt__(p, q):                                 # Corrected __gt__ for >
        print('c2 class __gt__ method:', p.x, q.x)
        return p.x > q.x

# End of class definitions
a = c1(10)
b = c1(20)
a > b        # c1 class __gt__ method: 10 20 → returns False
a < b        # No __lt__ defined → TypeError

m = c2(30)
n = c2(40)
a < m        # No __lt__ defined in c1 or c2 → TypeError
n < b        # No __lt__ defined in c2 or c1 → TypeError

# Overload  *  operator  to  multiply  2  different  class  objects
class c1:
    def __init__(self):
        self.empno = 25
        self.hr = 25                         # hourly rate

    def __mul__(self, other):               # overload * for c1 * c2
        print('__mul__ method of class c1')
        return self.hr * other.noh          # 25 * 8 = 200

class c2:
    def __init__(self):
        self.empno = 25
        self.noh = 8                        # number of hours

    def __mul__(self, other):              # overload * for c2 * c1
        print('__mul__ method of class c2')
        return self.noh * other.hr         # 8 * 25 = 200

# End of the classes

a = c1()
b = c2()

print(a * b)     # __mul__ method of class c1 → 200
print(b * a)     # __mul__ method of class c2 → 200

# Find  outputs  (Home  work)
class c1:
    def __add__(x, y):                    
        return '__add__ method of class c1'

class c2:
    pass

a = c1()
b = c1()
print('a + b : ', a + b)                 # a + b :  __add__ method of class c1
print('a + 7 : ', a + 7)                 # a + 7 :  __add__ method of class c1
print(7 + a)                             # TypeError: unsupported operand type(s) for +: 'int' and 'c1'
print('7 + 8 : ', 7 + 8)                 # 7 + 8 :  15
m = c2()
n = c2()
print(m + n)                             # TypeError: unsupported operand type(s) for +: 'c2' and 'c2'
print('a + m : ', a + m)                 # a + m :  __add__ method of class c1
print(m + a)                             # TypeError: unsupported operand type(s) for +: 'c2' and 'c1'

# Overload  +  operator  such  that  numbers  are  added  and  strings  are  joined
class c1:
    def __init__(self, y):                       # Constructor
        self.x = y

    def __add__(self, other):                    # Overloading + operator
        return self.x + other.x                  # Works for both int and str

# end of the class

a = c1(10)
b = c1(20)
m = c1('10')
n = c1('20')

print('Sum :', a + b)                            # Sum : 30
print('Join :', m + n)                           # Join : 1020

'''
Producer  Consumer  problem  with  Queue  class  (Home  work)

Assume  that  random  numbers  are  58 , 75 , 29 , 64 , 13 , ....
'''
from threading import Thread
from queue import Queue
import time
import random

# Create a shared queue with max size
q = Queue(maxsize=5)

# Producer function
def producer():
    while True:
        if not q.full():
            num = random.choice([58, 75, 29, 64, 13])  # Random from predefined list
            print(f'Producer produced: {num}')
            q.put(num)
            time.sleep(1)
        else:
            time.sleep(0.5)

# Consumer function
def consumer():
    while True:
        if not q.empty():
            num = q.get()
            print(f'Consumer consumed: {num}')
            time.sleep(2)
        else:
            time.sleep(0.5)

# Create and start threads
t1 = Thread(target=producer)
t2 = Thread(target=consumer)

t1.daemon = True
t2.daemon = True

t1.start()
t2.start()

# Let the main thread wait to observe output
time.sleep(15)
print('Main thread ends')
'''output:  Producer produced: 58
			Consumer consumed: 58
			Producer produced: 29
			Producer produced: 75
			Consumer consumed: 29
			Producer produced: 13
			Consumer consumed: 75
			Producer produced: 64
			...
'''
# Find  outputs  (Home  work)
class outer:
    def __init__(self):  # Corrected from _init_ to __init__
        print('Outer class object is created')  # Output

    def m1(self):
        print('Outer class method')  # Output

    class inner:
        def __init__(self):  # Corrected from _init_ to __init__
            print('Inner class object is created')  # Output

        def m1(self):
            print('Inner class method')  # Output


# How to call m1() method of outer class
o = outer()         # Outer class object is created
o.m1()              # Outer class method

# How to call m1() method of inner class
i = outer.inner()   # Inner class object is created
i.m1()              # Inner class method

# How to call m1() method of inner class in another way
x = o.inner()       # Inner class object is created
x.m1()              # Inner class method

# How to call m1() method of inner class in one more way
y = outer().inner() # Outer class object is created, Inner class object is created
y.m1()              # Inner class method

# i = inner()  ← This will cause NameError because 'inner' is not global
# Correct way: i = outer.inner()

# Find  outputs  (Home  work)
class emp:
    def __init__(self):  # Corrected _init_ to __init__
        self.empno = 25  # Initialize empno to 25
        self.ename = 'Rama Rao'  # Initialize ename
        self.sal = 10000.0  # Initialize salary
        self.d = self.date()  # Create date class object

    def disp(self):
        print(self.empno, self.ename, self.sal)  # 25 Rama Rao 10000.0
        self.d.disp()  # Call date's disp()

    class date:
        def __init__(self):  # Corrected _init_ to __init__
            self.dd = 15  # Initialize dd
            self.mm = 8   # Initialize mm
            self.yy = 1947  # Initialize yy

        def disp(self):
            print(self.dd, self.mm, self.yy)  # 15 8 1947

# How to call disp() method of emp class
e = emp()  # Creates emp and inner date object
e.disp()  # 25 Rama Rao 10000.0 15 8 1947

# Find outputs (Home  work)
class outer:
	def __init__(self):  # corrected _init_ to __init__
		self.x = 25  # initialize variable 'x' of object self to 25
		self.i1 = outer.inner1()  # create inner1 class object
		self.i2 = outer.inner2()  # create inner2 class object

	def disp(self):
		print(self.x)  # 25

	class inner1:
		def disp(self):
			print('1st inner class method')  # 1st inner class method

	class inner2:
		def disp(self):
			print('2nd inner class method')  # 2nd inner class method


# How to call disp() method of outer class
o = outer()  # creates outer object, initializes x = 25, and inner objects
o.disp()  # 25

# How to call disp() method of inner1 class
o.i1.disp()  # 1st inner class method

# How to call disp() method of inner2 class
o.i2.disp()  # 2nd inner class method

# Find  outputs  (Home  work)
class c1:
	def __init__(self):  
		print('outer class c1 constructor')  # outer class c1 constructor

	class c2:
		def __init__(self):  
			print('inner class c2 constructor')  # inner class c2 constructor

# end of the class

class c2:
	def __init__(self):  
		print('outer class c2 constructor')  # outer class c2 constructor

# end of the class

# How to create c1 class object
a = c1()  # outer class c1 constructor

# How to create inner c2 class object
b = c1.c2()  # inner class c2 constructor

# How to create outer c2 class object
c = c2()  # outer class c2 constructor

# Find  outputs  (Home  work)
class c2:
	def __init__(self):  
		print('outer class constructor')  # outer class constructor

	class c2:
		def __init__(self):  
			print('inner class constructor')  # inner class constructor

# end of the class

# How to create outer c2 class object
a = c2()  # outer class constructor

# How to create inner c2 class object
b = c2.c2()  # inner class constructor

# How to create inner c2 class object in another way
c = a.c2()  # inner class constructor

'''s

Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import mysql.connector

# Step 1: Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

# Step 2: Create cursor
cur = con.cursor()

# Step 3: Execute the query
cur.execute("SELECT * FROM emp")

# Step 4: Print table header
print('Emp Number\tEmp Name\tSalary')

# Step 5: Fetch and print each row using fetchone()
count = 0
while True:
    row = cur.fetchone()
    if row is None:
        break
    print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}')
    count += 1

# Step 6: Print number of tuples
print('Number of tuples :', count)

# Step 7: Close connection
con.close()
'''output:  Emp Number	Emp Name	Salary
			111		Rama Rao	10000.0
			222		Sita		20000.0
			333		Rajesh		15000.0
			Number of tuples : 3
'''
'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import mysql.connector

# Step 1: Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with actual password
    database="your_database"   # Replace with your DB name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Get condition from user
cond = input("Enter any condition : ")

# Step 4: Execute the query with user condition
cur.execute(F"SELECT * FROM emp WHERE {cond}")

# Step 5: Print header
print("Emp Number\tEmp Name\tSalary")

# Step 6: Fetch and display records
count = 0
while True:
    row = cur.fetchone()
    if row is None:
        break
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
    count += 1

# Step 7: Display count of tuples
print("Number of tuples :", count)

# Step 8: Close connection
con.close()
'''output:  Enter any condition : sal > 10000
			Emp Number	Emp Name	Salary
			222		Sita		20000.0
			333		Rajesh		15000.0
			Number of tuples : 2
                     
            Enter any condition : ename like 'S%'
			Emp Number	Emp Name	Salary
			222		Sita		20000.0
			Number of tuples : 1
                     
            Enter any condition : sal between 100000 and 200000
			Emp Number	Emp Name	Salary
			Number of tuples : 0        
         
'''
'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import mysql.connector

# Step 1: Connect to database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # Replace with your actual password
    database="your_database"   # Replace with your database name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Read the column name (with optional order) from user
colname = input("Enter column name: ")  # Example: sal desc or ename

# Step 4: Execute SQL query with ORDER BY clause
cur.execute(F"SELECT * FROM emp ORDER BY {colname}")

# Step 5: Print table header
print("Emp Number\tEmp Name\tSalary")

# Step 6: Fetch and display rows using fetchone()
count = 0
while True:
    row = cur.fetchone()
    if row is None:
        break
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
    count += 1

# Step 7: Display number of rows
print("Num of rows :", count)

# Step 8: Close the connection
con.close()
'''output:  Enter column name: sal desc
			Emp Number	Emp Name	Salary
			222		Sita		20000.0
			333		Rajesh		15000.0
			111		Rama Rao	10000.0
			Num of rows : 3
                     
            Enter column name: ename
			Emp Number	Emp Name	Salary
			333		Rajesh		15000.0
			111		Rama Rao	10000.0
			222		Sita		20000.0
			Num of rows : 3
         
'''
'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  --->  Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
import mysql.connector

# Step 1: Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",      # Replace with your password
    database="your_database_name"  # Replace with your DB name
)

# Step 2: Create cursor
cur = con.cursor()

# Step 3: Read table name from user
table = input("Enter table name: ")  # Example: emp

# Step 4: Execute query
cur.execute(F"SELECT * FROM {table}")

# Step 5: Print table header
print("Emp Number\tEmp Name\tSalary")

# Step 6: Use next() function to fetch rows one by one
count = 0
try:
    while True:
        row = next(cur)  # gets next row
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
        count += 1
except StopIteration:
    pass

# Step 7: Print total count
print("Number of tuples :", count)

# Step 8: Close the connection
con.close()
'''output:  Enter table name: emp
			Emp Number	Emp Name	Salary
			111		Rama Rao	10000.0
			222		Sita		20000.0
			333		Rajesh		15000.0
			Number of tuples : 3
'''
'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import mysql.connector

# Step 1: Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",       # Replace with your MySQL password
    database="your_database_name"   # Replace with your database name (e.g., demo)
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Execute query to get all data from emp table
cur.execute("SELECT * FROM emp")

# Step 4: Fetch all rows into a list of tuples
rows = cur.fetchall()

# Step 5: Print header
print("Emp Number\tEmp Name\tSalary")

# Step 6: Use for loop to display each row
for row in rows:
    print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")

# Step 7: Print number of tuples
print("Number of tuples :", len(rows))

# Step 8: Close connection
con.close()
'''output:  Emp Number	Emp Name	Salary
			111		Rama Rao	10000.0
			222		Sita		20000.0
			333		Rajesh		15000.0
			Number of tuples : 3
'''
'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import mysql.connector

# Step 1: Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",         #  Replace with your MySQL password
    database="your_database_name"     #  Replace with your database name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Execute query to get data from emp table
cur.execute("SELECT * FROM emp")

# Step 4: Read how many rows user wants
n = int(input("How many rows? : "))

# Step 5: Fetch 'n' rows
rows = cur.fetchmany(n)

# Step 6: Process based on input
if n > 0 and rows:
    print("Emp Number\tEmp Name\tSalary")
    for row in rows:
        print(f"{row[0]}\t\t{row[1]}\t\t{row[2]}")
    print("Number of tuples fetched :", len(rows))
elif n == 0:
    print("Number of tuples : 0")
elif n < 0:
    print("Emp Number\tEmp Name\tSalary")
    print("Number of tuples fetched : 0")

# Step 7: Close connection
con.close()
'''output:  How many rows? : 2
			Emp Number     Emp Name        Salary
			111            Rama Rao        10000.0
			222            Sita            20000.0
			Number of tuples fetched : 2

			How many rows? : 0
			Number of tuples : 0

			How many rows? : -1
			Emp Number     Emp Name        Salary
			Number of tuples fetched : 0
'''
'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->  cur . execute(F'insert  into  emp  values  ({empno} ,  '{ename}' , {sal})')

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3)  What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  inputs  for  empno , ename  and  sal

4) What  action  to  be  made  after  insert ?  --->  Call  commit()  method

5) What  does  commit()  method  do ?  --->  Makes  insertion  becomes  permanent

6) What  happens  when  commit()  is  not  called ?  --->  Insertion  is  only  temporary

7) In  other  words,  insertion  does  not  happen

8) Where  is  commit()  method  defined ?  --->  In  MySqlConnection  c…'''
import mysql.connector

# Step 1: Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",          # Replace with your MySQL password
    database="your_database_name"      # Replace with your database name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Loop to insert rows one by one
while True:
    try:
        # Step 3a: Read input from user
        empno = int(input("Enter Emp Number : "))
        ename = input("Enter Emp Name : ")
        sal = float(input("Enter Salary : "))

        # Step 3b: Execute insert query
        cur.execute(F"INSERT INTO emp VALUES ({empno}, '{ename}', {sal})")
        con.commit()  # Make the insertion permanent
        print("1 Row is inserted")

    except mysql.connector.IntegrityError as err:
        print(f"Row can not be inserted as empno is duplicate : {err}")
    
    # Step 3c: Ask user to continue or not
    ch = input("Do you wish to insert another row ? (Y / N) : ").lower()
    if ch != 'y':
        break

# Step 4: Close the connection
con.close()
'''output:  Enter Emp Number : 444
			Enter Emp Name : Sai
			Enter Salary : 25000
			1 Row is inserted
			Do you wish to insert another row ? (Y / N) : y

			Enter Emp Number : 555
			Enter Emp Name : Kiran
			Enter Salary : 32000
			1 Row is inserted
			Do you wish to insert another row ? (Y / N) : y

			Enter Emp Number : 222
			Enter Emp Name : AAA
			Enter Salary : 20000
			Row can not be inserted as empno is duplicate : 1062 (23000): Duplicate entry '222' for key 'PRIMARY'
			Do you wish to insert another row ? (Y / N) : n
'''

'''
Write  a  program  to  insert  multiple  rows  into  emp  table

1) How  to  insert  multiple  rows  into  the  table ?  --->  With  executemany()  method

2) Where  is  executemany()  method  defined ?  --->  In  MySqlCursor  class

3) cur . executemany('insert   into  emp  values (%s,%s,%s)' ,  list)
    What  does  the  method  do ?  ---> Inserts  all  the  tuples  present  in  the  list  into  emp  table

4) What  does  first  %s  represent ?  --->  First  element  of  each  tuple  in  the  list
    What  does  2nd  %s  represent ?  --->  2nd  element  of  each  tuple  in  the  list
    What  does  3rd  %s  represent ?  --->  3rd  element  of  each  tuple  in  the  list

5) How  many  rows  are  inserted  if  there  are  four  tuples  in  the  list  …'''
import mysql.connector

# Step 1: Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",             # Replace with your password
    database="your_database_name"         # Replace with your DB name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Read how many rows to insert
n = int(input("How many rows would you like to insert : "))
data = []

# Step 4: Collect all tuples into a list
for i in range(n):
    print(f"Employee {i + 1}")
    empno = int(input("Enter employee number : "))
    ename = input("Enter employee name : ")
    sal = float(input("Enter salary : "))
    data.append((empno, ename, sal))

# Step 5: Insert all tuples into emp table using executemany
try:
    cur.executemany("INSERT INTO emp VALUES (%s, %s, %s)", data)
    con.commit()
    print(f"{n} Row{'s' if n > 1 else ''} are inserted")
except mysql.connector.IntegrityError as err:
    print("Error while inserting:", err)

# Step 6: Close the connection
con.close()
'''output:  How many rows would you like to insert : 3
			Employee 1
			Enter employee number : 666
			Enter employee name : PPP
			Enter salary : 60000
			Employee 2
			Enter employee number : 777
			Enter employee name : QQQ
			Enter salary : 70000
			Employee 3
			Enter employee number : 888
			Enter employee name : RRR
			Enter salary : 80000
			3 Rows are inserted
'''

'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
import mysql.connector

# Step 1: Connect to the database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",           # Replace with your MySQL password
    database="your_database_name"       # Replace with your database name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Read user condition
cond = input("Enter condition: ")

# Step 4: Execute delete query with given condition
query = F"DELETE FROM emp WHERE {cond}"
cur.execute(query)

# Step 5: Commit changes
con.commit()

# Step 6: Print number of deleted rows
print(cur.rowcount, "Rows Deleted")

# Step 7: Close the connection
con.close()
'''output:  Enter condition: sal > 50000
			3 Rows Deleted
'''
'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->   cur . execute(F'update  emp  set  {cname}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->Read  cname  and  cond
'''
import mysql.connector

# Step 1: Connect to MySQL database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",           # Replace with your MySQL password
    database="your_database_name"       # Replace with your database name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Get update details from the user
cond = input("Enter condition: ")                      # e.g., sal <= 20000
cname = input("Enter column name = value: ")           # e.g., sal = sal + 1000

# Step 4: Execute update query
query = F"UPDATE emp SET {cname} WHERE {cond}"
cur.execute(query)

# Step 5: Commit the update
con.commit()

# Step 6: Show how many rows were updated
print(cur.rowcount, "Rows Updated")

# Step 7: Close connection
con.close()
'''output:  Enter condition: sal <= 20000
			Enter column name = value: sal = sal + 1000
			3 Rows Updated
'''
'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
																			Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
import mysql.connector

# Step 1: Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",              # 🔁 Replace with your password
    database="your_database_name"          # 🔁 Replace with your DB name
)

# Step 2: Create cursor object
cur = con.cursor()

# Step 3: Read table name from user
tablename = input("Enter name of the table: ")

# Step 4: Try to create table
try:
    cur.execute(F"create table {tablename}(rollno int primary key, sname char(20), marks float)")
    print(f"{tablename} table created")
except:
    print(f"{tablename} table is deleted")
    cur.execute(F"drop table {tablename}")
    cur.execute(F"create table {tablename}(rollno int primary key, sname char(20), marks float)")
    print(f"{tablename} table created")

# Step 5: Close connection
con.close()
'''output:  Enter name of the table: stud
			stud table created

            Enter name of the table: stud
			stud table is deleted
			stud table created
                  
'''
'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import mysql.connector

# Step 1: Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",           # 🔁 Replace with your password
    database="your_database_name"       # 🔁 Replace with your DB name
)

# Step 2: Create cursor
cur = con.cursor()

# Step 3: Execute query to get all rows
cur.execute("select * from emp")

# Step 4: Fetch all rows to count them
all_rows = cur.fetchall()
total = len(all_rows)

# Step 5: Ask user how many rows to fetch
n = int(input("How many rows? : "))

if n > total or n < 0:
    print("Invalid input")
elif n == 0:
    print("Number of tuples: 0")
else:
    # Re-execute since fetchall() consumed the cursor
    cur.execute("select * from emp")
    rows = cur.fetchmany(n)
    print("Emp Number       Emp Name        Salary")
    for row in rows:
        print(f"{row[0]:<17}{row[1]:<16}{row[2]:.2f}")
    print("Number of tuples fetched:", len(rows))

# Step 6: Close connection
con.close()
'''output:  How many rows? : 2
			Emp Number       Emp Name        Salary
			111              Rama Rao        10000.00
			222              Sita            20000.00
			Number of tuples fetched: 2
                     
            How many rows? : 7
            Invalid input         
'''
#  Modify  following  program  with  'with'  statement
def create(fname):
    try:
        with open(fname, 'w') as f:  # open file using 'with' statement
            print('Type text terminated by ctrl+z')
            while line := input():  # keep reading until EOFError (Ctrl+Z)
                f.write(line + '\n')
    except EOFError:
        print(f'File {fname} is created')

# end of function

fname = input('Enter filename: ')  # a.txt
create(fname)  # call function

'''
Repeat  prog5b(File-Create)  with  writelines()  method

1) Let  input  be
    Rama  Rao
    9247
    +-$
    Hyd is green city
    ctr+z

2) Keyboard   ------------->   str  object  ----------------->  list  ------------------->   File
                          input()                                 append()                      writelines()
'''
def create(f):
    print('Enter text terminated by ctrl + z')
    lines = []  # list to store lines
    try:
        while line := input():  # read until Ctrl+Z (EOFError)
            lines.append(line + '\n')  # append each line with newline
    except EOFError:
        f.writelines(lines)  # write list to file
        print(f'File {f.name} is created')  # print filename

# End of the function

fname = input('Enter filename: ')  # read filename
f = open(fname, 'w')  # open file for writing
create(f)  # call create() function
f.close()  # close the file
'''Input:   Rama Rao
			9247
			+-$
			Hyd is green city
			Ctrl+Z (to stop input)
                     
  output:   Enter filename: a.txt
			Enter text terminated by ctrl + z
			File a.txt is created
								
'''
'''
Write  a  program  to  print  contents  of  the  file

 File ------------>  str  obj    -------------> monitor
            read()                           print()
'''
def create(f):
    print('Enter text terminated by ctrl + z')
    lines = []  # list to store lines
    try:
        while line := input():  # read until Ctrl+Z (EOFError)
            lines.append(line + '\n')  # append each line with newline
    except EOFError:
        f.writelines(lines)  # write list to file
        print(f'File {f.name} is created')  # print filename

# End of the function

fname = input('Enter filename: ')  # read filename
f = open(fname, 'w')  # open file for writing
create(f)  # call create() function
f.close()  # close the file
'''Input:   Rama Rao
			9247
			+-$
			Hyd is green city
			Ctrl+Z (to stop input)
   output:  Enter filename: a.txt
			Enter text terminated by ctrl + z
			File a.txt is created
							
'''
'''
Repeat  prog8c(File-page-wise)   with  readline()  method

1) Let  file  contain
    Rama  Rao
    9247
    +-$
    Hyd is green city

2) File  a.txt   ----------> str  obj  ------------> monitor
                        readline()                    print()

3) Hint:  Use   while  loop  and  :=  walrus  operator
'''
import os

def disp(f):
    print(f'Contents of the file {f.name}')
    count = 0
    while (line := f.readline()):
        print(line, end='')  # avoid extra newline
        count += 1
        if count == 20:
            input('Press enter to continue...')
            count = 0

# End of the function

try:
    fname = input('Enter filename: ')  # How to read filename
    f = open(fname, 'r')  # How to open the file
    disp(f)  # How to call disp() function
    f.close()  # How to close the file
except:
    print(f'File {fname} does not exist')  # How to print filename here
'''output:  Rama Rao
			9247
			+-$
			Hyd is green city
'''
'''
Repeat  prog8c(File-page-wise)  with  for  loop

Let  file  contain
Rama  Rao
9247
+-$
Hyd is green city

File  ----------> str  obj  ------------> monitor
          for  loop                    print()
'''
import os

def disp(f):
    print(f'Contents of the file {f.name}')  # How to print filename here
    count = 0
    for line in f:  # How to print each line of the file
        print(line, end='')  # print to monitor
        count += 1
        if count == 20:
            input('Press enter to continue...')
            count = 0

# End of the function

try:
    fname = input('Enter filename: ')  # How to read filename
    f = open(fname, 'r')  # How to open the file
    disp(f)  # How to call disp() function
    f.close()  # How to close the file
except:
    print(f'File {fname} does not exist')  # How to print filename here

'''
Repeat  prog8c(File-page-wise)  with  readlines()  method


 File   ----------------->   list   --------------->    monitor
              readlines()                    for  loop

'''
import os

def disp(f):
    print(f'Contents of the file {f.name}')  # Print filename
    lines = f.readlines()  # Read all lines into a list
    count = 0
    for line in lines:
        print(line, end='')  # Print each line
        count += 1
        if count == 20:
            input('Press enter to continue...')
            count = 0

# End of the function

try:
    fname = input('Enter filename: ')  # Read filename
    f = open(fname, 'r')  # Open file in read mode
    disp(f)  # Call disp() function
    f.close()  # Close the file
except:
    print(f'File {fname} does not exist')  # Handle file-not-found error


'''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1) 1st    file   ---------->    str   object     -------->   2nd   file
                        read()                                write()

2) What  is  the  mode  in  which  is  1st  file  opened ?  --->  'r'  mode
    What  is  the  mode  in  which  is  2nd  file  opened ?  --->  'w'   mode

3) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

4) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

5) What  action  to  be  made  when  both  the  files  are  existing ? --->
								Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no

6) Hint:  Use  i…
'''
import os

# Step 1: Read filenames
src = input("Enter name of source file: ")    # e.g., a.txt
dst = input("Enter name of destination file: ")  # e.g., b.txt

# Step 2: Check if source file exists
if not os.path.exists(src):
    print(f"Source file '{src}' does not exist.")
else:
    # Step 3: If destination file exists, ask permission to overwrite
    if os.path.exists(dst):
        choice = input(f"Destination file '{dst}' already exists. Do you want to overwrite? (yes/no): ")
        if choice.lower() != 'yes':
            print("Copy operation aborted.")
        else:
            # Perform copy
            with open(src, 'r') as f1, open(dst, 'w') as f2:
                content = f1.read()
                f2.write(content)
            print(f"File '{src}' successfully copied to '{dst}'.")
    else:
        # Destination doesn't exist — copy without prompt
        with open(src, 'r') as f1, open(dst, 'w') as f2:
            content = f1.read()
            f2.write(content)
        print(f"File '{src}' successfully copied to '{dst}'.")
'''
Write  a  program  to  append  contents  of  a  file  to  another  file

1) What  is  the  mode  in  which  can  1st  file  be  opened ?  --->  'r'   mode
    What  is  the  mode  in  which  is  2nd  file  opened ?  ---> 	'a'  mode

2) Where  does  file  handle  points  to  when  file  is  opened  in  append  mode ?  --->  End  of  the  file
    Where  does  file  handle  points  to  when  file  is  opened  in  read  or  write  mode ? ---> Begining  of  the  file

3) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

4) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

5) What  action  to  be  made  when  both  the  files  are  existing ? --->  Append  1st  file  …
'''
import os

# Step 1: Read filenames
src = input("Enter name of source file: ")    # e.g., a.txt
dst = input("Enter name of destination file: ")  # e.g., b.txt

# Step 2: Check if source file exists
if not os.path.exists(src):
    print(f"Source file '{src}' does not exist.")
else:
    # Step 3: Open source in 'r' mode, destination in 'a' mode
    with open(src, 'r') as f1, open(dst, 'a') as f2:
        content = f1.read()
        f2.write(content)
    print(f"Contents of '{src}' appended to '{dst}'.")
'''Input:   Enter name of source file: a.txt
			Enter name of destination file: b.txt
			Output: Contents of 'a.txt' appended to 'b.txt'.
 '''
'''Write  a  function  to  return  average  of  numbers  in  the  file

Let  file  contain
10
20.8
True
15
18.4
eof

sum = 0 + 10 + 20.8 + True + 15 + 18.4
ctr = 0 + 1 + 1 + 1 + 1 + 1
'''
def avg(f):
    total = 0
    count = 0
    for line in f:
        value = line.strip()
        if value.lower() == 'eof':
            break
        try:
            if value == 'True':
                total += 1
            else:
                total += float(value)
            count += 1
        except ValueError:
            pass  # Ignore non-numeric and invalid entries
    if count == 0:
        return 0
    return total / count
# End of the function

try:
    fname = input('Enter filename: ')   # e.g., data.txt
    f = open(fname, 'r')
    result = avg(f)
    print('Average =', result)
    f.close()
except:
    print('File does not exist')

'''Input:   10
			20.8
			True
			15
			18.4
			eof
   Output: Enter filename: data.txt
           Average = 13.04        
'''




'''
Write  a  function  to  return  average  of  numbers  in  the  file

Let  file  contain
10
20.8
True
15
18.4
eof

sum = 0 + 10 + 20.8 + True + 15 + 18.4
ctr = 0 + 1 + 1 + 1 + 1 + 1
'''

def avg(f):
    total = 0
    count = 0
    for line in f:
        val = line.strip()
        if val.lower() == 'eof':
            break
        try:
            if val == 'True':
                total += 1
            else:
                total += float(val)
            count += 1
        except:
            pass  # skip non-numeric values
    if count == 0:
        return 0
    return total / count
# End of the function

try:
    fname = input('Enter filename: ')  # e.g., data.txt
    f = open(fname, 'r')
    print('Average =', avg(f))
    f.close()
except:
    print('File does not exist')
'''Input:   10
			20.8
			True
			15
			18.4
			eof
   Output:  Enter filename: data.txt
			Average = 13.04
         
'''

'''
Write  a  program  to  merge  two  files  to  form  a  new  file

1) Let  1st  file  contain  10  lines  and   2nd  file  contain  7  lines
    What  does  3rd  file  contain ?  ---> 10 + 7 = 17  lines

2) What  action  to  be  made  when  both  the  files  are  existing ?  --->  Merge  them  to  form  a  new  file

3) What  action  to  be  made  when  2nd  file  is  not  existing ?  --->  Copy  1st  file  to  3rd  file

4) What  action  to  be  made  when  1st  file  is  not  existing ?  --->  Copy  2nd  file  to  3rd  file

5) What  action  to  be  made  when  both  the  files  are  not  existing ?  --->  Print  a  message
'''
import os

def copy(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'a') as f2:
        for line in f1:
            f2.write(line)

# End of the function

f1name = input('Enter 1st filename: ')
f2name = input('Enter 2nd filename: ')
f3name = input('Enter 3rd filename (to be created): ')

f1_exists = os.path.exists(f1name)
f2_exists = os.path.exists(f2name)

if f1_exists and f2_exists:
    # Merge both files
    open(f3name, 'w').close()  # create/clear the file
    copy(f1name, f3name)
    copy(f2name, f3name)
    print(f'Files {f1name} and {f2name} are merged into {f3name}')
elif f1_exists:
    copy(f1name, f3name)
    print(f'File {f1name} is copied to {f3name}')
elif f2_exists:
    copy(f2name, f3name)
    print(f'File {f2name} is copied to {f3name}')
else:
    print('Both files do not exist. Cannot merge.')

'''
Write   a  program  to  count  number  of   lines , characters , words , vowels , consonants ,  spaces , tabs  and   sentences  in  a  file

Let  file  contain

Rama Rao
9247<tab>Sita
+-$ Hyd

str  object   --->  'Rama Rao\n9247<tab>Sita\n+-$ Hyd\n'

List 1  --->  ['Rama Rao' , '9247<tab>Sita' , '+-$ Hyd']   --->  Split  on  '\n'

List 2--->  ['Rama' ,  'Rao' , '9247' , 'Sita' , '+-$' ,  'Hyd']   ---->  Split  on  white  space

vowel = 0 + 1 + 1

consonant = 0 + 1 + 1 + 1

                           0		 1             2           3              4             5                  6             7
List  'a'  --->   [   3       ....            6           2              1             0                  ...              ...]
                      Lines    Chars …
'''
def count_file_stats(filename):
    try:
        with open(filename, 'r') as f:
            text = f.read()

            lines = text.split('\n')                    # List of lines
            words = text.split()                        # List of words
            chars = len(text)                           # All characters including \n, tabs, etc.
            spaces = text.count(' ')
            tabs = text.count('\t')
            sentences = text.count('.') + text.count('!') + text.count('?')

            vowels = consonants = 0

            for ch in text:
                if ch.isalpha():
                    if ch.lower() in 'aeiou':
                        vowels += 1
                    else:
                        consonants += 1

            print(f'Lines         : {len(lines)}')
            print(f'Characters    : {chars}')
            print(f'Words         : {len(words)}')
            print(f'Vowels        : {vowels}')
            print(f'Consonants    : {consonants}')
            print(f'Spaces        : {spaces}')
            print(f'Tabs          : {tabs}')
            print(f'Sentences     : {sentences}')

    except FileNotFoundError:
        print(f'File "{filename}" does not exist.')

# Main
filename = input("Enter filename: ")
count_file_stats(filename)
'''Input:   Rama Rao
			9247	Sita
			+-$ Hyd.
               
   Output:  Lines         : 3
			Characters    : 26
			Words         : 6
			Vowels        : 3
			Consonants    : 6
			Spaces        : 4
			Tabs          : 1
			Sentences     : 1
            
'''
'''
Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

Let  file  contain
Hyd  is  green  city.
Hyd  is  hitec  city.
Hyd  is  beautiful  city.

str  object  --->  Hyd  is  green  city.\nHyd  is  hitec  city.\nHyd  is  beautiful  city.]n

What  is  the  result  when  'Hyd'  is  searched  in  the  file ?  --->
'''
def search(f, s):
    text = f.read()
    words = text.split()
    return words.count(s)
# End of the function

try:
    fname = input('Enter the filename: ')     # Example: data.txt
    f = open(fname, 'r')                      # Open file in read mode
    word = input('Enter the word to search: ')  # Example: Hyd
    count = search(f, word)
    print(f"'{word}' is found {count} times in the file.")
    f.close()
except FileNotFoundError:
    print('File does not exist')
'''Input:   Hyd is green city.
			Hyd is hitec city.
			Hyd is beautiful city.
   output:  Enter the filename: data.txt
			Enter the word to search: Hyd
			'Hyd' is found 3 times in the file.
            
'''
'''
Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file

Hint:  Use  math . factorial()  function
'''
import math

def fact(f, n):
    for i in range(n + 1):
        f.write(f"{i}! = {math.factorial(i)}\n")
# End of the function

# Read the filename
fname = input('Enter the filename: ')  # e.g., factorials.txt

# Open the file in write mode
f = open(fname, 'w')

# Read value of 'n'
n = int(input('Enter the value of n: '))

# Call fact() function
fact(f, n)

# Close the file
f.close()

# Confirmation message
print(f"View {fname} for results")
'''Input:   Enter the filename: factorials.txt
			Enter the value of n: 5
               
   Output:  0! = 1
			1! = 1
			2! = 2
			3! = 6
			4! = 24
			5! = 120
            
'''
#  Find  outputs  (Home  work)
f = open('a.txt' , 'w+')                      # open file for read/write, create/overwrite
f.write('Hyd is green city.')                 # write 20 chars
f.seek(0)                                     # move cursor to beginning
f.write('Sec')                                # overwrite first 3 chars
f.seek(0)
print(f.read())                               # output 1
f.seek(7)
print(f.read(5))                              # output 2
f.seek(0 , 2)                                 # move to end
f.write('Hyd is Hitec city.')                 # append
f.seek(0)
print(f.read())                               # output 3
f.seek(7)
f.write('red')                                # overwrite 3 chars from position 7
f.seek(0)
print(f.read())                               # output 4

#  Find  outputs (Home  work)
f = open('a.txt', 'w+')        # Open for read/write, truncate if exists
print(f.tell())               # 1. Cursor position
f.write('Hyd is green city')  # 2. Write 18 characters
print(f.tell())               # 3. Cursor after writing
f.seek(7)                     # 4. Move cursor to 7th byte
print(f.read(5))              # 5. Read 5 characters from position 7
print(f.tell())               # 6. Final cursor position

'''
Write  a   program  to  remove  all  the   comments  in  a  python  file

1) Remove  all  single  line  comments  only  but  not   multi-line  comments

2) Do  not  remove  lines  which  starts  with  #
     #statement  --->  Do  not  delete

3) Input  is  filename
'''
def remove_single_line_comments(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            stripped = line.lstrip()
            if stripped.startswith('#'):
                # Keep lines that start with '#'
                new_lines.append(line)
            elif '#' in line:
                # Remove inline comment (not at the start)
                index = line.find('#')
                code = line[:index].rstrip()
                if code:
                    new_lines.append(code + '\n')
            else:
                new_lines.append(line)

        with open(filename, 'w') as f:
            f.writelines(new_lines)

        print(f"Single-line comments removed from {filename}")

    except FileNotFoundError:
        print(f"File '{filename}' does not exist.")


# --- Main Program ---
fname = input("Enter Python filename: ")  # e.g., test.py
remove_single_line_comments(fname)

'''
Write  a  program  to  print  each  file  of  zipfile

Let  zip  file  contain  1.py , 2.py , 3.txt , 4.txt

1) Print  each  file  name  and   file  contents

2) Also  execute  the  file  if  is  a  py  file

3) How  to  execute  python  file  from  python  program ?  --->   os . system('py   filename.py')
'''
from zipfile import ZipFile
import os

def display(zipfile, fname):
    with zipfile.open(fname) as f:
        print(f"\nContents of the file: {fname}")
        data = f.read().decode()
        print(data)
        
        # If file is a Python file, save and execute
        if fname.endswith('.py'):
            temp_file = '__temp__.py'
            with open(temp_file, 'w') as temp:
                temp.write(data)
            print(f"\n--- Executing {fname} ---")
            os.system(f'python {temp_file}')
            os.remove(temp_file)

def disp(zipname):
    if not os.path.exists(zipname):
        print(f"Zip file '{zipname}' not found.")
        return
    
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen
    with ZipFile(zipname, 'r') as zf:
        file_list = zf.namelist()
        for fname in file_list:
            display(zf, fname)

# --- Main Program ---
zipname = input("Enter zip file name: ")  # e.g., myfiles.zip
disp(zipname)

'''   (Home  work)
1) 1st  input  ---> 'Hyd is green city'
    2nd  input  --->  'Green'
	What  are  the  outputs  --->

2) 1st  input  --->  'Hyd is green city'
    2nd  input ---> 'red'
    What  are  the  outputs  --->
'''
import   re
string = input('Enter  any  string  :  ')
pattern = input('Enter  pattern  :   ')
m  =  re . search(pattern , string , re . IGNORECASE)
print(type(m))
if  m:
	print(F'{m . group()}  is found  between  indexes  {m . start()}   and   {m . end() - 1}')
else:
	print(pattern , ' is  not  found ')
'''output:  <class 're.Match'>
			green is found between indexes 7 and 11
            <class 'NoneType'>
            red is not found
   
'''     
#  Find  outputs  (Home  work)
import re

m = re.search('^learn', 'Learning Python is simple', re.IGNORECASE)
if m:
    print('String starts with', m.group())
else:
    print('String does not start with learn')

m = re.search('Simple$', 'Learning Python is simple', re.IGNORECASE)
if m:
    print('String ends with', m.group())
else:
    print('String does not end with Simple')
'''output:  String starts with Learn
			String ends with simple
'''
'''  (Home  work)
What  are  the  outputs
1st  input  --->  'Hyd is green city. Hyd IS hitec city. Hyd Is hiS city'
2nd  input  --->  'is'
What  are  the  outputs  --->
'''
import re
string  =  input('Enter  any  string  :  ')
pattern = input('Enter  pattern  to  be  searched : ')
itr = re . finditer(pattern , string , re . IGNORECASE)
ctr = 0
while  True:
	try:
		m = next(itr)
		print(F'{m . group()}  is found  between   indexes   {m . start()}  and {m . end() - 1}')
		ctr += 1
	except  StopIteration:
		break
print('Found ' , ctr ,' times')
#Input : Enter any string: Hyd is green city. Hyd IS hitec city. Hyd Is hiS city
         #Enter pattern to be searched: is
'''output:  is  is found  between   indexes   4  and 5
			IS  is found  between   indexes   23  and 24
			Is  is found  between   indexes   40  and 41
			iS  is found  between   indexes   47  and 48
			Found  4  times
'''
# Find  outputs (Home  work)
import  re
itr  =  re . finditer('[IEY]' , 'Hyd Is greEn citY', re . IGNORECASE)
while  True:
	try:
		m = next(itr)
		print(m . group() , 'is  at index : ' , m . start())
	except  StopIteration:
		break
'''Input: Index : 0123456789.......
		  String: H y d   I s   g r e E n   c i t Y
  Output:   y is  at index :  1
			I is  at index :  4
			e is  at index :  9
			E is  at index :  10
			Y is  at index :  16
'''     
# Find  outputs (Home  work)
import re

itr = re.finditer('[A-Za-z0-9]', 'm$9 K,d%5@E&')

while True:
	try:
		m = next(itr)
		print(m.group(), ' is  at  index :  ', m.start())
		# Output:
		# m  is  at  index :  0
		# 9  is  at  index :  2
		# K  is  at  index :  4
		# d  is  at  index :  6
		# 5  is  at  index :  9
		# E  is  at  index : 11
	except:
		break

#  Find  outputs (Home  work)
import re

string = 'z7.Q-$2 b[9.a%6$G&k.%'

print(re.findall('[a-z]', string))  
# Output: ['z', 'b', 'a', 'k']
# Explanation: All lowercase letters

print()

print(re.findall('[0-9]', string))  
# Output: ['7', '2', '9', '6']
# Explanation: All digits

print()

print(re.findall('[^A-Za-z0-9]', string))  
# Output: ['.', '-', '$', ' ', '[', '.', '%', '$', '&', '.', '%']
# Explanation: All characters **not** A-Z, a-z, or 0-9

print()

print(re.findall('.', string))  
# Output: ['z', '7', '.', 'Q', '-', '$', '2', ' ', 'b', '[', '9', '.', 'a', '%', '6', '$', 'G', '&', 'k', '.', '%']
# Explanation: `.` matches every character (including special chars)

print()

print(re.findall('[.]', string))  
# Output: ['.', '.', '.']
# Explanation: Matches only literal `.` (dot)

print()

print(re.findall('[$]', string))  
# Output: ['$', '$']
# Explanation: Matches only literal dollar symbol

print()

print(re.findall('[%]', string))  
# Output: ['%', '%']
# Explanation: Matches only literal percent symbol

print()

print(re.findall('[az-]', string))  
# Output: ['z', '-', 'a']
# Explanation: Character class includes `'a'`, `'z'`, and `'-'` (dash as a character)

''' (Home  work)
1) 1st  string --->  'Sankar  dayal  sarma'
    2nd  string ---> 'san'
    What  are  the  outputs ?  --->

2) 1st  string  ---> 'Hyderabad'
    2nd  string  --->  'Sec'
    What  are  the  outputs ?  --->
'''
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re.match(pattern , string , re.IGNORECASE)
if  m:
	print(string  ,  'starts  with ' , m.group())
else:
	print(string , 'does not start with' , pattern)
'''Output : Sankar dayal sarma starts with  san
            Hyderabad does not start with Sec
'''
#  Identify  Error  (Home  work)
import re
string  =  input('Enter  any  string : ')
pattern = input('Enter  any pattern : ')
m  =  re . match(^pattern , string , re . IGNORECASE)#Error ^pattern is invalid Python syntax — ^ is a regex symbol and cannot be used directly like this in code
if  m:
	print(string  ,  'starts  with ' , m . group())
else:
	print(string , 'does not start with' , pattern)
'''  (Home   work)
1) What  are  the  outputs  if  inputs  are  'HYD'  and  'hyd' ?  --->

2) What  are  the  outputs  if  inputs  are  'HYD'  and  'SEC' ?  --->
'''
import re
s1 = input('Enter first string  : ')       # First input string
s2 = input('Enter second string  : ')      # Second input string

# Check if s2 fully matches s1 (case insensitive)
m = re.fullmatch(s1, s2, re.IGNORECASE)

if m:
    print('Same strings after ignoring the case')
else:
    print('Different strings')
'''Output: Same strings after ignoring the case
           Different strings
'''
'''
Write  a  regular  expression  to  represent  a  10-digit  mobile  number

Rules:
1) It  should  be  a  10-digit  number

2) First  digit  can  be  6 , 7 , 8  or  9

3) Number  may  start  with  0  (or)  +91

4) Which  of  the  following  are  valid ?
     a) 5948250500  --->   Invalid  becoz  first  character  '6'  is  not  between  '7'  and  '9'
     b) 994825050 --->  Invalid  becoz  length  of  the  string  is  not  10
     c) 9948-250500  --->  Invalid  due  to  '-'
     d) 9948250500  ---> Valid
     e) 09948250500  ---> Valid  becoz  number  may  start  with  '0'
     f) +919948250500 ---> Valid  becoz  number  may  start  with  +91
     g) 919948250500  --->  Inavlid  becoz  length  of  the   string  is  not  10

5) What  is  the  regular  expres…
'''
import re

pattern = r'^(0|\+91)?[6-9]\d{9}$'

numbers = [
    '5948250500',     # Invalid (starts with 5)
    '994825050',      # Invalid (only 9 digits)
    '9948-250500',    # Invalid (contains hyphen)
    '9948250500',     # Valid
    '09948250500',    # Valid (starts with 0)
    '+919948250500',  # Valid (starts with +91)
    '919948250500'    # Invalid (11 digits, no +)
]

for num in numbers:
    if re.fullmatch(pattern, num):
        print(num, '=> Valid')
    else:
        print(num, '=> Invalid')
'''output:  5948250500 => Invalid
			994825050 => Invalid
			9948-250500 => Invalid
			9948250500 => Valid
			09948250500 => Valid
			+919948250500 => Valid
			919948250500 => Invalid
'''
'''Write  a  program  to  validate  date  i.e.  dd/mm/yyyy

1) What  is  the  valid  character  after  '0'  in  the  date ?  --->  1  to  9
    What  is  the  valid  character  after  '1'  in  the  date ?  ---> 0  to  9
    What  is  the  valid  character  after  '2'  in  the  date ?  --->  0  to  9
    What  is  the  valid  character  after  '3'  in  the  date ?  --->  0  (or)  1

2) Is  0  mandatory  for  single  digit  date ?  --->  No  and  it  is  optional

3) What  is  the  valid  character  after  '0'  in  the  month ?  --->  1  to  9
     What  is  the  valid  character  after  '1'  in  the  month ?  --->  0  to  2

4) Is  0  mandatory  for  single  digit  month ?  --->  No  and  it  is  optional

5) Which  of  the  following  are  valid ?
     a) 0…
'''
import re

def validate_date(date):
    pattern = r'^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/(\d{4})$'
    if re.fullmatch(pattern, date):
        return "Valid date"
    else:
        return "Invalid date"

# Test cases
dates = [
    '01/01/2024',  # Valid
    '1/1/2024',    # Valid
    '31/12/1999',  # Valid
    '00/01/2024',  # Invalid (00 is not valid day)
    '32/01/2024',  # Invalid (max day is 31)
    '15/13/2024',  # Invalid (month can't be 13)
    '29/2/2021',   # Valid by pattern, but invalid logically unless leap year (not handled here)
]

for d in dates:
    print(f'{d} => {validate_date(d)}')
'''
Write  a  program  to validate  address  :  streetname , city ,  State - PIN code

Eg:  Khairtabad , Hyderabad , Telangana - 500004

1) street name  should  have  alphabets  (or)  spaces
2) ,  is   mandatory  between  street  name  and  city
3) City  name  should  have  alphabets  (or)  spaces
4) ,  is   mandatory  between  city  and  state
5) State  name  should  have  alphabets  (or)  spaces
6) -  is  mandatory  between  state  and  pincode
7) Pincode should  be  a  six-digit  number
'''
import re

def validate_address(address):
    pattern = r'^[A-Za-z ]+ , [A-Za-z ]+ , [A-Za-z ]+ - \d{6}$'
    if re.fullmatch(pattern, address):
        return "Valid address"
    else:
        return "Invalid address"

# Test the function
address = input("Enter address (street , city , state - PIN): ")
print(validate_address(address))

'''
Write  a  program  to  validate  credit card  number
 1) It must start with 4, 5 or 6
 2) It must contain exactly 16 digits
 3) It must consist of digits from 0 to 9
 4) It may have digits in a group of 4 separated by one hyphen'-'
 5) It must not use any other separators like  _ ,  / , etc
'''
import re

def validate_credit_card(card):
    # Pattern 1: Plain 16 digits (no hyphens)
    pattern1 = r'^[4-6]\d{15}$'
    
    # Pattern 2: 4 groups of 4 digits separated by single hyphen
    pattern2 = r'^[4-6]\d{3}(-\d{4}){3}$'
    
    # Check if input matches either pattern
    if re.fullmatch(pattern1, card) or re.fullmatch(pattern2, card):
        return "Valid credit card number"
    else:
        return "Invalid credit card number"

# Read input from user
card = input("Enter credit card number: ")
print(validate_credit_card(card))

# sub()  function  demo  program (Home  work)
import re

print(re.sub('-', '/', '15 - Aug - 1947'))      
# Output: '15 / Aug / 1947'   → replaces all '-' with '/'

print(re.sub(' ', ':', '18 52 36'))            
# Output: '18:52:36'         → replaces all spaces with ':'

print(re.sub('[0-9]', '$', 'a7b8c6d5'))        
# Output: 'a$b$c$d$'         → replaces each digit with '$'

print(re.sub('[a-z]', '%', 'a7b8G6d5'))        
# Output: '%7%8G6%5'         → replaces each lowercase letter with '%'

print(re.sub('is', 'was', 'Hyd is his city'))  
# Output: 'Hyd was hwas city' → replaces all 'is' with 'was'

print(re.sub('a', 'b', 'Rama  Rao'))           
# Output: 'Rbmb  Rbo'        → replaces all lowercase 'a' with 'b'

#  subn()  finction  demo  program  (Home  work)
import re

print(re.subn('[a-z]', '#', 'a7G9c5D8e'))        
# Output: ('#7G9#5D8#', 3)
# → Replaces all lowercase letters with '#' (a, c, e) → total 3 replacements

print(re.subn(' ', ':', '18 52 46'))             
# Output: ('18:52:46', 2)
# → Replaces all spaces with ':' → total 2 replacements

print(re.subn('-', '/', '15-Aug-1947'))          
# Output: ('15/Aug/1947', 2)
# → Replaces all '-' with '/' → total 2 replacements

print(re.subn('is', 'was', 'Hyd is his city'))   
# Output: ('Hyd was hwas city', 2)
# → Replaces 'is' with 'was' in both 'is' and 'his' → total 2 replacements

print(re.subn('a', 'b', 'Rama rao'))             
# Output: ('Rbmb rbo', 3)
# → Replaces each 'a' with 'b' → total 3 replacements

#  split()  function  demo  program  (Home  work)
import re

print(re.split(',' , 'Hyd,Pune,Chennai,Delhi,Vijayawada'))       
# ['Hyd', 'Pune', 'Chennai', 'Delhi', 'Vijayawada']
# → Splits the string at every comma

print(re.split('-' , '15-Aug-1947'))                            
# ['15', 'Aug', '1947']
# → Splits the string at every hyphen '-'

print(re.split(':' , '18:52:46'))                               
# ['18', '52', '46']
# → Splits the string at every colon ':'

print(re.split(' ' , 'Hyd is green city'))                      
# ['Hyd', 'is', 'green', 'city']
# → Splits the string at every space

# ----------------------
# Special cases below:

print(re.split('[.]' , 'www.gmail.com'))                         
# ['www', 'gmail', 'com']
# → Splits at literal '.' characters (using a character set [.] to treat dot as normal character)

print(re.split('.' , 'www.gmail.com'))                           
# ['', '', '', '', '', '', '', '', '', '', '', '', '']
# → WRONG output due to `.` meaning “any character” in regex
# → It splits on every single character

# To fix this, escape the dot:
# print(re.split(r'\.', 'www.gmail.com')) → ['www', 'gmail', 'com']

'''
Write  a  program  to  extract  all  mobile  numbers  present  in  a  file  to  another  file
and  mobile  numbers  are  mixed  with  normal  text  in  the  file

1) Let  input.txt  file  contain
    hyd9948250500sec09848565090cyb
    ap +919440250404 tel
    kar 9848066695 tn
    04023304078
    xnmxcnmxvncx 989898989898
    nnvbnvn
    969696
    919948250500

2) What  does  output.txt  file  contain ?  --->  9948250500
																	      09848565090
																	     +919440250404
																	     9848066695
																	     9898989898
																	     9199482505
'''
import re

def extract_mobiles(src, tgt):
    try:
        with open(src, 'r') as fsrc, open(tgt, 'w') as ftgt:
            content = fsrc.read()

            # Extract possible mobile numbers with optional prefixes
            pattern = r'(?:\+91|91|0)?[6-9]\d{9}'
            matches = re.findall(pattern, content)

            for num in matches:
                # Extract only last 10 digits for consistency
                ftgt.write(num[-10:] + '\n')

        print(f'Mobile Numbers in {src} are redirected to {tgt} file')
    except FileNotFoundError:
        print(f'File {src} does not exist')

# Driver code
src_file = input('Enter source filename  : ')
tgt_file = input('Enter target filename : ')
extract_mobiles(src_file, tgt_file)
'''Input:   hyd9948250500sec09848565090cyb
			ap +919440250404 tel
			kar 9848066695 tn
			04023304078
			xnmxcnmxvncx 989898989898
			nnvbnvn
			969696
			919948250500
               
  Output:   9948250500
			09848565090
			9440250404
			9848066695
			9898989898
			9948250500
						
 '''
# Find  outputs
import  os
os . system('dir')
os . system('pause')
os . system('cls')
os . system('py  test.py')
'''output:  Volume in drive C is OS
			Volume Serial Number is XXXX-XXXX

			Directory of C:\Users\YourName

			07/08/2025  08:50 PM    <DIR>          .
			07/08/2025  08:50 PM    <DIR>          ..
			07/08/2025  08:30 PM               128 test.py
						1 File(s)            128 bytes
						2 Dir(s)  XXX,XXX,XXX bytes free
'''
'''
Write  a  program  to  create  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
import os

# Read directory name or path
dirname = input('Enter directory name (or) path : ')

# Check if parent directory exists for nested folders
parent = os.path.dirname(dirname)
if parent != '' and not os.path.exists(parent):
    print('Directory does not exist')
else:
    # Create directory if it doesn't exist
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print(f'Directory {dirname} created')
    else:
        print(f'Directory {dirname} already exists')
'''output:  Enter directory name (or) path : Telangana
			Directory Telangana created
            Enter directory name (or) path : Telangana
            Directory Telangana already exists
            Enter directory name (or) path : Telangana/Hyd
            Directory Telangana/Hyd created
            Enter directory name (or) path : a/b
            Directory does not exist

        
'''
'''
Write  a  program  to  create  a  group  of  directories.
Input :  a/b/c
'''
import os

# Read the nested directory path from the user
dirname = input('Enter group of directories (e.g., a/b/c): ')

# Check if the full directory path exists
if not os.path.exists(dirname):
    os.makedirs(dirname)  # Creates all intermediate folders
    print(f'Directories {dirname} created')
else:
    print(f'Directories {dirname} already exist')
#output : Directories a/b/c created
#Input: Enter group of directories (e.g., a/b/c): a/b/c
#output: Directories a/b/c already exist
'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
import os

# Read the directory name or path from user
dirname = input('Enter directory name (or) path to delete: ')

# Check if the path exists and is a directory
if os.path.exists(dirname):
    try:
        os.rmdir(dirname)  # Deletes only if the directory is empty
        print(f'Directory {dirname} deleted')
    except OSError:
        print(f'Directory {dirname} is not empty or cannot be deleted')
else:
    print(f'Directory {dirname} does not exist')
#Input: Enter directory name (or) path to delete: a/b/c
#Output: Directory a/b/c deleted
#output: Directory a/b/c is not empty or cannot be deleted

'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
import shutil
import os

# Read the directory path from user
dirpath = input('Enter directory path to delete: ')

# Check if the directory exists
if os.path.exists(dirpath):
    try:
        shutil.rmtree(dirpath)  # Deletes the directory and all its contents
        print(f'Directory {dirpath} and all its subdirectories deleted')
    except Exception as e:
        print(f'Error: {e}')
else:
    print(f'Directory {dirpath} does not exist')
#Input: Enter directory path to delete: a/b/c
#output: Directory a/b/c and all its subdirectories deleted

'''
Write  a  program  to  rename  a  file  (or)  directory

Input  is  filename  (or)  directory  name
'''
import os

# Read the current name
old_name = input('Enter 1st filename (or) directory name: ')

# Read the new name
new_name = input('Enter 2nd filename (or) directory name: ')

# Check if the file or directory exists
if os.path.exists(old_name):
    try:
        os.rename(old_name, new_name)
        print(f'File or directory {old_name} is renamed to {new_name}')
    except Exception as e:
        print(f'Error: {e}')
else:
    print(f'{old_name} does not exist')
'''Input: Enter 1st filename (or) directory name: test.py
          Enter 2nd filename (or) directory name: sample.py
   Output: File or directory test.py is renamed to sample.py
       
'''
'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
Input :  Directory  (or)  path
Output:  Print  Two  lists  where  1st  list  contains  all  the  files  and  2nd  list  contains  all  the  directories
'''
import os

# Read directory path from user
path = input('Enter directory name (or) path: ')

# Check if the path exists and is a directory
if os.path.exists(path) and os.path.isdir(path):
    files = []
    dirs = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            files.append(item)
        elif os.path.isdir(full_path):
            dirs.append(item)

    print('\nList of the files:', files)
    print('\nList of the directories:', dirs)
else:
    print('Invalid path or directory does not exist')
'''Input: Enter directory name (or) path: d:\sairam
  Output: List of the files: ['file1.txt', 'file2.txt', 'file3.txt']
          List of the directories: ['dir1', 'dir2']
  '''
