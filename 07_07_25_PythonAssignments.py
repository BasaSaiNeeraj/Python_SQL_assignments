# Find outputs
class Person:
    def __init__(self):
        self.name = ''                # Setter Method

    @property
    def name(self):
        print('getter method')       # Called whenever p.name is accessed
        return self.__name

    @name.setter
    def name(self, value):
        print('Setter Method')       # Called during assignment to p.name
        self.__name = value

    @name.deleter
    def name(self):
        print('Deleter method')      # Called during del p.name
        del self.__name

# end of class

p = Person()                         # Setter Method
print(p.name)                        # getter method
                                     # <prints empty string: ''>

p.name = 'Vamsi'                     # Setter Method
print(p.name)                        # getter method
                                     # Vamsi

del p.name                           # Deleter method
print(p.name)                        # getter method
                                     # AttributeError: 'Person' object has no attribute '_Person__name'

del p                                # No output

'''
1) Write  a  program  to  validate  emp  number , emp  name  and  salary  and  also  print  them

2) Emp  number  and  salary  can  not  be  -ve

3) Emp  name  can  not  be  empty  string

4) class  name   is  Emp

5) 3  getter  and  3  setter  methods

6) Constructor  initializes  empno , ename  and  sal

7) Outside  the  class
    ----------------------
    a) Create  Emp  class  object
    b) Print  empno , ename  and  sal
'''
class Emp:
    def __init__(self, empno, ename, sal):
        self.empno = empno  # Calls setter
        self.ename = ename  # Calls setter
        self.sal = sal      # Calls setter

    # Getter for empno
    @property
    def empno(self):
        return self.__empno

    # Setter for empno
    @empno.setter
    def empno(self, value):
        if value < 0:
            raise ValueError("Empno cannot be negative")
        self.__empno = value

    # Getter for ename
    @property
    def ename(self):
        return self.__ename

    # Setter for ename
    @ename.setter
    def ename(self, value):
        if value.strip() == '':
            raise ValueError("Emp name cannot be empty string")
        self.__ename = value

    # Getter for salary
    @property
    def sal(self):
        return self.__sal

    # Setter for salary
    @sal.setter
    def sal(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__sal = float(value)

# --------------------
# Outside the class
# --------------------

while True:
    try:
        empno = int(input("Enter employee number: "))
        ename = input("Enter employee name: ")
        sal = float(input("Enter salary: "))
        e = Emp(empno, ename, sal)
        break
    except ValueError as ve:
        print(ve)
        print()

# Print employee details
print("\nEmployee number  :", e.empno)
print("Employee name    :", e.ename)
print("Employee salary  :", e.sal)
'''output:  Enter employee number: -10
			Empno cannot be negative

			Enter employee number: 10
			Enter employee name: 
			Emp name cannot be empty string

			Enter employee number: 10
			Enter employee name: Rama Rao
			Enter salary: -10
			Salary cannot be negative

			Enter employee number: 10
			Enter employee name: Rama Rao
			Enter salary: 100000

			Employee number  : 10
			Employee name    : Rama Rao
			Employee salary  : 100000.0
'''
# parent  and  child  classes  have  different  Instance  methods
class parent:
    def m1(self):
        print('parent method')

class child(parent):
    def m2(self):
        # How to call m1() method of parent class
        super().m1()   #  Best way to call parent method from child 

        # Another way without creating another object
        parent.m1(self)   #  Alternative way using class name

        print('child method')

# Outside function with same name
def m1():
    print('Function')

# Create object of child class
c = child()

# How to call m1() method of parent class:
c.m1()   # calls parent.m1() because child does not override m1

# How to call m2() method of child class:
c.m2()   # calls child.m2(), which also calls parent.m1()

# How to call global function m1():
m1()     # calls the function outside the class

#  parent  and  child  classes  have  same  Instance  method
class parent:
    def m1(self):
        print('Parent Method')                # Output: when parent.m1() is called

class child(parent):
    def m1(self):
        # How to call m1() method of parent class
        super().m1()                          # Output: Parent Method

        # How to call function m1()
        m1()                                  # Output: m1 function

        # self.m1() would call child.m1 again and cause recursion
        # self.m1()                          # Don’t do this — causes infinite recursion

        print('Child Method')                 # Output: Child Method

# End of class

# Function with same name outside class
def m1():
    print('m1 function')                      # Output: m1 function

# How to call m1() method of child class
c = child()
c.m1()                                       # Output:
                                            # Parent Method
                                            # m1 function
                                            # Child Method
# How to call m1() method of parent class directly
p = parent()
p.m1()                                       # Output: Parent Method
# parent  and  child  classes  have  different  class  methods
class parent:
    @classmethod
    def m1(cls):
        print('parent Method')              # Output when parent.m1() is called
class child(parent):
    @classmethod
    def m2(cls):
        # How to call m1() method of parent class
        parent.m1()                         # Way 1: using parent class name
        super().m1()                        #  Way 2: using super() in classmethod
        cls.m1()                            #  Way 3: using cls inside classmethod
        child.m1()                          #  Way 4: using child class name
        print('child Method')              # Output: child Method

# parent  and  Child  classes  have  same  class   method
class parent:
    @classmethod
    def m1(cls):
        print('parent Method')  # Output when parent.m1() is called

class child(parent):
    @classmethod
    def m1(cls):
        # How to call m1() method of parent class (inside overridden m1)
        parent.m1()            # Way 1: Call directly using parent class name
        super().m1()           # Way 2: Call using super() from classmethod

        #  cls.m1() would call child.m1 again (infinite recursion)
        #  self.m1() → 'self' not defined in @classmethod
        #  m1() → Not defined in current scope (no global function)

        print('child Method')  # After parent method calls

# Parent  and  Child  classes  have  different  static  methods
class parent:
    @staticmethod
    def m1():
        print('parent method')   # Output when parent.m1() is called

class child(parent):
    @staticmethod
    def m2():
        # How to call m1() method of parent class

        parent.m1()       # using parent class name
        child.m1()        # inherited method via child class
        # super().m1()    # INVALID in staticmethod: No self or cls
        # self.m1()       # INVALID: 'self' not available in staticmethod
        # cls.m1()        # INVALID: 'cls' not available in staticmethod

        print('child method')    # Output: child method
# How to call m1() method of parent class
parent.m1()    # Output: parent method

# How to call m1() method of parent class through child
child.m1()     # Output: parent method (inherited)

# How to call m2() method of child class
child.m2()
# Output:
# parent method
# parent method
# child method

# Parent  and  Child  classes  have  same  static  method
class parent:
    @staticmethod
    def m1():
        print('parent method')

class child(parent):
    @staticmethod
    def m1():
        # Using class name directly
        parent.m1()

        # Using __bases__[0]
        child.__bases__[0].m1()

        print('child method')
# How to call m1() method of parent class
parent.m1()     # Output: parent method

# How to call m1() method of child class
child.m1()      # Output:
                # parent method
                # parent method
                # child method

# Parent  and  child  classes  have   static  variables  with  different  names
class parent:
    x = 10  # Class variable of parent

    def m1(self):
        # How to print variable 'x'
        print(self.x)             # Way 1: Access through instance

        # How to print variable 'x' in another way
        print(parent.x)           # Way 2: Access through class name

        # print(x)  # Invalid: 'x' is not defined in local/global scope


class child(parent):
    y = 20  # Class variable of child

    def m2(self):
        # How to print variable 'x' (inherited from parent)
        print(self.x)             # Access through instance

        # How to print variable 'x' in another way
        print(parent.x)           # Using parent class name

        # How to print variable 'x' in one more way
        print(child.x)            # Access from child class (inherited)

        # How to print variable 'x' in last way
        print(super().x)          # Access using super()

        # How to print variable 'y'
        print(self.y)             # Through instance

        # How to print variable 'y' in another way
        print(child.y)            # Using child class name

        # print(super().y)  # Error: 'super' refers to parent; 'y' is in child
        # print(y)  # Error: undefined in local scope
# How to call m1() method of parent class
p = parent()
p.m1()            # Output:
                  # 10
                  # 10

# How to call m2() method of child class
c = child()
c.m2()            # Output:
                  # 10
                  # 10
                  # 10
                  # 10
                  # 20
                  # 20

# Parent  and  Child  classes  have  static  variables  with  same  name
class parent:
    x = 10  # Class variable in parent

    def m1(self):
        # How to print variable 'x' of parent class
        print(self.x)           # Way 1: via instance

        # How to print variable 'x' of parent class in another way
        print(parent.x)         # Way 2: directly using class name


class child(parent):
    x = 20  # Class variable in child (shadows parent's x)

    def m1(self):
        # How to print variable 'x' of parent class
        print(parent.x)         # Way 1: directly using parent class

        # How to print variable 'x' of parent class in another way
        print(super().x)        # Way 2: using super()

        # How to print variable 'x' of child class
        print(self.x)           # Way 1: through instance

        # How to print variable 'x' of child class in another way
        print(child.x)          # Way 2: directly using child class name
# How to call m1() method of parent class
p = parent()
p.m1()
# Output:
# 10
# 10

# How to call m1() method of child class
c = child()
c.m1()
# Output:
# 10   (parent.x)
# 10   (super().x)
# 20   (self.x)
# 20   (child.x)

#  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
class parent:
    def get(self):
        # Read inputs into variables a and b of object self
        self.a = int(input("Enter a: "))
        self.b = int(input("Enter b: "))

    def disp(self):
        # Print variables a and b of object self in same line separated by tab
        print(self.a, self.b, sep='\t')

# End of Parent class

class child(parent):
    def get(self):
        # Read inputs into variables a and b of object self
        super().get()

        # Read inputs into variables c and d of object self
        self.c = int(input("Enter c: "))
        self.d = int(input("Enter d: "))

    def disp(self):
        # Print variables a and b of object self in same line separated by tab
        super().disp()

        # Print variables c and d of object self in same line separated by tab
        print(self.c, self.d, sep='\t')

    def total(self):
        # Return sum of values in object
        return self.a + self.b + self.c + self.d

# Outside the class
c = child()
c.get()
c.disp()
print("Total:", c.total())


'''
Write  a  program  to  determine  area  and  circumference  of  circle.
Also  find  area  and  volume  of  cylinder

1) What  is  the  area  of  circle ?  --->  3.14159 * r ^ 2

2) What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

3) What  is  the  area  of  cylinder ?  --->  2 * 3.14159  r ^ 2 + 2 * 3.14159 * r * h

4) What  is  the  volume  of  cylinder ?  --->  3.14159 * r ^ 2 *  h

5) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
'''
import math

class circle:
    def get(self):
        # Read radius into object self
        self.r = float(input("Enter radius of the circle/cylinder: "))

    def area(self):
        # Return area of circle
        return 3.14159 * self.r ** 2

    def cir(self):
        # Return circumference of circle
        return 2 * 3.14159 * self.r

# End of circle class

class cylinder(circle):
    def get(self):
        # Read radius using parent class method
        super().get()
        # Read height into object self
        self.h = float(input("Enter height of the cylinder: "))

    def area(self):
        # Area of cylinder = 2 * pi * r^2 + 2 * pi * r * h
        return 2 * 3.14159 * self.r ** 2 + 2 * 3.14159 * self.r * self.h

    def volume(self):
        # Volume of cylinder = pi * r^2 * h
        return 3.14159 * self.r ** 2 * self.h

# Outside the class
c = cylinder()
c.get()

print("Area of circle:", super(cylinder, c).area())  # using parent class method
print("Circumference of circle:", super(cylinder, c).cir())  # using parent class method
print("Area of cylinder:", c.area())  # child class method
print("Volume of cylinder:", c.volume())  # child class method

'''
Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
Also  find  surface  area  and  volume  of  cube

1) What  is  the  area  of  square ?  --->  a ^ 2
    What  is  the  perimeter  of  square ?  --->  4 *  a

2) What  is  the  area  of  rectangle ?  --->  a * b
    What  is  the  perimeter  of  rectangle ?  --->  2 * (a + b)

3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
     What  is  the  volume  of  cube  ?  ---> a ^ 3

4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
'''
class Square:
    def get(self):
        # Read side of square
        self.a = float(input("Enter side of the square/cube: "))

    def area(self):
        # Area of square = a^2
        return self.a ** 2

    def peri(self):
        # Perimeter of square = 4 * a
        return 4 * self.a

class Rectangle(Square):
    def get(self):
        # Read length and breadth
        self.a = float(input("Enter length of rectangle: "))
        self.b = float(input("Enter breadth of rectangle: "))

    def area(self):
        # Area of rectangle = a * b
        return self.a * self.b

    def peri(self):
        # Perimeter of rectangle = 2 * (a + b)
        return 2 * (self.a + self.b)

class Cube(Square):
    def surface_area(self):
        # Surface area of cube = 6 * a^2
        return 6 * self.a ** 2

    def volume(self):
        # Volume of cube = a^3
        return self.a ** 3

# --- Test the classes ---

# Square
print("\n--- Square ---")
s = Square()
s.get()
print("Area of Square:", s.area())
print("Perimeter of Square:", s.peri())

# Rectangle
print("\n--- Rectangle ---")
r = Rectangle()
r.get()
print("Area of Rectangle:", r.area())
print("Perimeter of Rectangle:", r.peri())

# Cube
print("\n--- Cube ---")
c = Cube()
c.get()
print("Surface Area of Cube:", c.surface_area())
print("Volume of Cube:", c.volume())
# Find  outputs
class c1:
    def m1(self):
        print('m1 method of class c1')

class c2:
    def m1(self):
        print('m1 method of class c2')

class c3:
    @classmethod
    def m1(cls):
        print('m1 method of class c3')

class c4:
    @staticmethod
    def m1():
        print('m1 method of class c4')

class c5(c1):
    def m1(self):
        print('m1 method of class c5')

    def m2(self):
        # Call m1() method of class c3
        c3.m1()

        # Call m1() method of class c4
        c4.m1()

        # Call m1() method of class c2
        c2().m1()

        # Call m1() method of class c1
        c1().m1()

        # Call m1() method of class c5
        self.m1()

        # Call m1() function
        m1()

# End of class c5

def m1():
    print('m1 function')

# End of the function

# How to call m2() method of class c5
obj = c5()
obj.m2()

# find outputs
class c1:
    pass

class c2(c1):
    pass

# End of the class

print(issubclass(c2, c1))        # True - c2 inherits from c1
print(issubclass(int, float))    # False - int is not a subclass of float
print(issubclass(str, object))   # True - all classes in Python inherit from object
print(issubclass(c1, object))    # True - user-defined classes inherit from object
print(issubclass(c2, object))    # True - because c2 -> c1 -> object

a = c1()
b = c2()

print(issubclass(b, a))          # Error - TypeError: issubclass() arg 1 must be a class
print(issubclass(c2, a))         # Error - TypeError: issubclass() arg 2 must be a class
# find outputs
class c1:
    pass

class c2(c1):
    pass

class c3(c2):
    pass

class c4(c3):
    pass

print(issubclass(c4, c3))                                # True  - c4 directly inherits from c3
print(issubclass(c4, c2))                                # True  - c4 -> c3 -> c2
print(issubclass(c4, c1))                                # True  - c4 -> c3 -> c2 -> c1
print(issubclass(c4, object))                            # True  - all classes inherit from object
print(issubclass(c4, (int, float, str, bool)))           # False - c4 is not a subclass of any of these
print(issubclass(c4, (int, float, c1, str, bool)))       # True  - c4 is a subclass of c1
print(issubclass(c4, [int, float, c1, str, bool]))       # TypeError - 2nd argument must be a class or tuple of classes
# find outputs
class c1:
    pass

class c2(c1):
    pass

class c3(c2):
    pass

class c4:
    pass

# End of the class

print(isinstance(25, int))             # True - 25 is an integer
print(isinstance(10.8, float))         # True - 10.8 is a float
print(isinstance('Hyd', str))          # True - 'Hyd' is a string
print(isinstance(3 + 4j, complex))     # True - complex number
print(isinstance(True, bool))          # True - True is a boolean
print(isinstance(True, int))           # True - bool is subclass of int in Python
print(isinstance('True', str))         # True - 'True' (string) is of type str
print(isinstance(True, str))           # False - True is bool, not str

print()  # blank line

a = c3()

print(isinstance(a, c3))               # True - object is of class c3
print(isinstance(a, c2))               # True - c3 is subclass of c2
print(isinstance(a, c1))               # True - c3 -> c2 -> c1
print(isinstance(a, object))           # True - all classes inherit from object
print(isinstance(a, c4))               # False - c3 and c4 are unrelated

print(isinstance(a, (int, float, str, bool)))            # False - object of c3 is not any of those types
print(isinstance(a, (int, float, c3, str, bool)))         # True - a is instance of c3
print(isinstance(a, (int, float, c1, str, bool)))         # True - a is instance of subclass of c1
print(isinstance(a, [int, float, c3, str, bool]))         # TypeError - 2nd argument must be a class or **tuple** of classes


# Multilevel inheritance demo program
class A:
    def m1(self):
        print('class A method')

class B(A):
    def m1(self):
        print('class B method')

class C(B):
    def m1(self):
        print('class C method')

class D(C):
    def m1(self):
        print('class D method')

        # Call method m1() of class C (immediate parent)
        super().m1()

        # Another way to call class C's m1()
        C.m1(self)

        # One more way (but same as above, explicit call)
        super(D, self).m1()

        # Call method m1() of class B
        B.m1(self)

        # Another way to call B's method (via super chain)
        super(C, self).m1()   # jumps to B in MRO

        # Call method m1() of class A
        A.m1(self)

        # Another way to call A's method (via super chain)
        super(B, self).m1()   # jumps to A in MRO

        # Invalid: super(A, self).m1() – would skip to object, not valid
        # Invalid: super(C).m1() – must be used in classmethods, not in instance context

# End of the class

# How to call method m1() of class D
obj = D()
obj.m1()

# Find  outputs  (Home  work)
class father:
    def height(self):
        print('Father Height')

class mother:
    def color(self):
        print('Mother Color')

class child(mother, father):
    def qualification(self):
        print('Child Qualification')

# End of the class

c = child()
c.qualification()    # Output: Child Qualification
c.color()            # Output: Mother Color (from mother class)
c.height()           # Output: Father Height (from father class)
c.m1()               # Error: AttributeError - 'child' object has no attribute 'm1'

#  Find  outputs
class uncle:
    def m1(self):
        print('Uncle Method')

class mother:
    def m1(self):
        print('Mother Method')

class father:
    def m1(self):
        print('Father Method')

class child(father, mother, uncle):  # Multiple inheritance
    def m1(self):
        print('Child Method')

# End of the class

c = child()
c.m1()     # Output: Child Method

# Find  outputs
class uncle:
    def m1(self):
        print('Uncle Method')

class mother:
    def m1(self):
        print('Mother Method')

class father:
    def m1(self):
        print('Father Method')

class child(father, mother, uncle):
    pass  # child does not override m1()

# end of the class

c = child()
c.m1()  # ?

# Find  outputs
class uncle:
    def m1(self):
        print('Uncle Method')

class mother:
    def m1(self):
        print('Mother Method')

class father:
    pass

class child(father, mother, uncle):
    pass

# end of the class

c = child()
c.m1()

# Find  outputs
class uncle:
    def m1(self):
        print('Uncle Method')

class mother:
    pass

class father:
    pass

class child(father, mother, uncle):
    pass

c = child()
c.m1()

# Find  outputs
class uncle:
    pass

class mother:
    pass

class father:
    pass

class child(father, mother, uncle):
    pass

c = child()
c.m1()

# Parent  and  child  class  constructors (Home  work)
class parent:
    def __init__(self):  # correct: double underscores
        print('parent constructor')
    
    def __del__(self):   # correct: double underscores
        print('parent destructor')

class child(parent):
    def __init__(self):  # correct constructor
        super().__init__()                   # Call parent constructor
        print('child constructor')
    
    def __del__(self):
        super().__del__()                    # Call parent destructor
        print('child destructor')

# End of the class

c = child()
print('Bye')

# Find  outputs  (Home  work)
class parent:
    def __init__(self):                     # corrected from _init_ to __init__
        print('parent constructor')         # will be printed if called

    def __del__(self):                      # corrected from _del_ to __del__
        print('parent destructor')          # will be printed on object deletion

class child(parent):
    def __init__(self):                     # corrected from _init_ to __init__
        print('child constructor')          # printed when child object is created

    def __del__(self):                      # corrected from _del_ to __del__
        print('child destructor')           # printed when child object is deleted

# End of the class

c = child()       # Output: child constructor  ← only child’s constructor is called
print('Bye')      # Output: Bye

# Object `c` is destroyed when program ends, so:
# Output: child destructor
#         (parent destructor is NOT printed because parent's __init__ was never called)

# Find  outputs  (Home  work)
class parent:
    def _init_(self):                  # Error should be __init__
        print('parent constructor')
    def _del_(self):                   # Error should be __del__
        print('parent destructor')

class child(parent):
    pass

# End of the class

c = child()
print('Bye')

# Parent  and  Child  constructor  demo  program  (Home  work)
class parent:
    def __init__(self, a1, b1):  # corrected from _init_ to __init__
        self.a = a1
        self.b = b1

    def disp(self):
        print(self.a, self.b, sep='\t', end='\t')

class child(parent):
    def __init__(self, a2=0, b2=0, c2=0, d2=0):  # corrected
        super().__init__(a2, b2)  # call parent constructor with a2, b2
        self.c = c2
        self.d = d2

    def disp(self):
        super().disp()  # call parent disp()
        print(self.c, self.d, sep='\t')

# end of the class

x = child(10, 20, 30, 40)  # sets: a=10, b=20, c=30, d=40
y = child()                # sets: a=0, b=0, c=0, d=0

print('Object x')
x.disp()   # Output: 10    20    30    40

print('Object y')
y.disp()   # Output: 0     0     0     0

# Find outputs  (Home  work)
class parent:
    x = 100  # class/static variable

    def __init__(self):          
        self.x = 10              # instance variable

class child(parent):
    def __init__(self):          
        super().__init__()       # correct call to parent's constructor
        self.y = 20              # instance variable

    def disp(self):
        print(parent.x)      # static/class variable from parent
        print(self.x)        # instance variable from object c (set by parent)
        print(self.y)        # instance variable from object c

# end of the class

c = child()
c.disp()

# Find  outputs
class parent:
    x = 10
    def __init__(self):
        self.x = 20

class child(parent):
    def __init__(self):
        self.x = 30
        print(self.x)         # prints 30
        super().__init__()    # sets self.x = 20

    def disp(self):
        print(self.x)         # prints 20 (overwritten by parent constructor)
        print(super().x)      # prints 10 (class variable from parent)

# End of the class
c = child()
c.disp()

# Find outputs
class parent:
    a = 10  # static variable added to class

    def __init__(self):
        print('Parent constructor')  # Output: Parent constructor
        self.x = 30  # instance variable

    def m1(self):
        print('Parent class instance method :', self.x)  # Output: 30

    @classmethod
    def m2(cls):
        print('Parent class "class" method :', cls.a)             # Output: 10
        print('Parent class "class" method :', parent.a)          # Output: 10
        # print(self.a)        Error becoz this is invalid in a classmethod — `self` is not defined

    @staticmethod
    def m3():
        print('Parent class static method :', parent.a)           # Output: 10

    def __del__(self):
        print('parent destructor :', self.x)  # Output: 30 (when object is deleted)

# -----------------------
# Testing the class:

p = parent()
p.m1()       # Output: Parent class instance method : 30
p.m2()       # Output:
             # Parent class "class" method : 10
             # Parent class "class" method : 10
p.m3()       # Output: Parent class static method : 10
del p        # Output: parent destructor : 30


# Find  outputs
class father:
    def m1(self):
        print('m1 method of Father class')

class mother:
    def m1(self):
        print('m1 method of Mother class')

class uncle:
    def m1(self):
        print('m1 method of Uncle class')

class child(father, mother, uncle):
    def m1(self):
        print('m1 method of child class')                      # Output
        father.m1(self)                                        # Call m1 of Father class
        super().m1()                                           # Another way to call Father m1 (based on MRO)
        mother.m1(self)                                        # Call m1 of Mother class
        uncle.m1(self)                                         # Call m1 of Uncle class
        super(uncle, self).m1()                                # Skips uncle in MRO and goes to next class

# End of class

# Print Method Resolution Order (MRO)
print(child.__mro__)  
# Output: (<class '__main__.child'>, <class '__main__.father'>, <class '__main__.mother'>, <class '__main__.uncle'>, <class 'object'>)

# Call m1 method of child class
c = child()
c.m1()
# Output:
# m1 method of child class
# m1 method of Father class
# m1 method of Father class
# m1 method of Mother class
# m1 method of Uncle class
# m1 method of Father class

print('Bye')  # Output: Bye

# Find outputs  (Home  work)
class A:
    def m1(self):
        super().m1()
        print('class A method')

class B:
    def m1(self):
        super().m1()
        print('class B method')

class C:
    def m1(self):
        super().m1()
        print('class C method')

class D:
    def m1(self):
        print('class D method')

class X(A, B):
    def m1(self):
        super().m1()
        print('class X method')

class Y(B, C, D):
    def m1(self):
        super().m1()
        print('class Y method')

class P(X, Y, C):
    def m1(self):
        super().m1()
        print('class P method')

# Check MRO (Method Resolution Order)
print(P.mro())
# Output:
# [<class '__main__.P'>,
#  <class '__main__.X'>,
#  <class '__main__.A'>,
#  <class '__main__.Y'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.D'>,
#  <class 'object'>]

obj = P()
obj.m1()

# Output:
# class D method
# class C method
# class B method
# class Y method
# class A method
# class X method
# class P method
print('Bye')  # Output: Bye

# Find  outputs  (Home  work)
class D:
    def __init__(self):
        super().__init__()
        print('class D constructor')  # class D constructor

class E:
    def __init__(self):
        super().__init__()
        print('class E constructor')  # class E constructor

class F:
    def __init__(self):
        super().__init__()
        print('class F constructor')  # class F constructor

class B(D, E):
    def __init__(self):
        super().__init__()
        print('class B constructor')  # class B constructor

class C(D, E, F):
    def __init__(self):
        super().__init__()
        print('class C constructor')  # class C constructor

class A(B, C):
    def __init__(self):
        super().__init__()
        print('class A constructor')  # class A constructor

#end of the class

print(A.mro())  
# [<class '__main__.A'>, 
#  <class '__main__.B'>, 
#  <class '__main__.C'>, 
#  <class '__main__.D'>, 
#  <class '__main__.E'>, 
#  <class '__main__.F'>, 
#  <class 'object'>]

obj = A()  
# class D constructor
# class E constructor
# class F constructor
# class C constructor
# class B constructor
# class A constructor
print('Bye')

# Identify  Error
class  c1(c1): # Error: name 'c1' is not defined
	pass
# Find  outputs
class c1:
    def m1(self):
        print('Parent  Method')  # Output: Parent  Method

class c1(c1):  # This redefines c1, inheriting from the original c1
    def m1(self):
        super().m1()             # Calls the parent class method
        print('Child  Method')   # Output: Child  Method

a = c1()         # Creates an object of the redefined c1 (child class)
a.m1()           # Output:
                 # Parent  Method
                 # Child  Method

# Identify  Error
class   c1(c2):
	pass
class  c2(c1): #Error: name 'c2' is not defined
	pass
# Find  outputs
class c2:               # Defines class c2
    pass

class c1(c2):           # c1 inherits from c2 (valid here)
    pass

class c2(c1):           # ERROR: Redefines class c2 to now inherit from c1, which causes circular inheritance
    pass

#  Find  outputs  (Home  work)
class parent:
	def m1(self):
		print('Overridden  Method')     # This is the method in the parent class

class child(parent):
	def m1(self):
		print('Overriding  Method')     # This method overrides the one in parent

# end of the class

x = parent()
x.m1()         # Output: Overridden  Method

x = child()
x.m1()         # Output: Overriding  Method

# Find  outputs   (Home  work)
class parent:
	def m1(self):
		print('m1  method  of  parent  class')     # method m1 in parent

	def m2(self):
		print('m2  method  of  parent class')      # method m2 in parent

class child(parent):
	def m1(self):
		print('m1  method  of  child  class')      # overridden method m1 in child

	def m3(self):
		print('m3  method  of  child  class')      # method m3 in child

# end of the class

x = parent()
x.m1()     # Output: m1  method  of  parent  class
x.m2()     # Output: m2  method  of  parent class
x.m3()     # Error: parent class has no method m3()

x = child()
x.m1()     # Output: m1  method  of  child  class
x.m2()     # Output: m2  method  of  parent class (inherited)
x.m3()     # Output: m3  method  of  child  class

# Find  outputs  (Home  work)
class parent:
    def marriage(self):
        print('Arranged Marriage')

    def property(self):
        print('One  Crore')

    def study(self):
        print('Studies only', end = '\t')

class child(parent):
    def marriage(self):
        print('Love Marriage')                       # Overridden method will be called

    def study(self):
        super().study()                              # Calls parent's study()
        print(' + Entertainment')                    # Adds additional behavior

# end of the class
c = child()
c.marriage()      # Love Marriage
c.property()      # One  Crore
c.study()         # Studies only	 + Entertainment

# Find  outputs  (Home  work)
#find outputs
class parent:
    def add(self, x, y):
        return x + y

class child(parent):
    def add(self, x, y, z):
        return x + y + z

# End of the class
c = child()
print(c.add(10, 20, 30))   # 60
print(c.add(10, 20))       # Error: missing 1 required positional argument 'z'

# Find  outputs  (Home  work)
class parent:
    def add(self, x, y):
        print('parent  method')
        return x + y

class child(parent):
    def add(self, x, y, z=3):    # Overrides parent method with default z=3
        print('child  method')
        return x + y + z

# End of the class
c = child()
print(c.add(10, 20, 30))   # child  method\n60
print(c.add(10, 20))       # child  method\n33 (z defaults to 3)

#Find  outputs  (Home  work)
class parent:
    def m1(self, a, b, /): 
        print(f'parent  method   a  :  {a}  \t  b  :  {b}')

class child(parent):
    def m1(self, x, y):  # Overrides parent method
        print(f'child  method   x  :  {x}  \t  y  :  {y}')

# End of the class
c = child()
c.m1(x = 10, y = 20)     # child method   x  :  10    y  :  20
c.m1(30, 40)             # child method   x  :  30    y  :  40

# Find  outputs (Home  work)
from abc import *
class c1(ABC):
    @abstractmethod
    def m1(self):
        pass
    def __init__(self):                      # Corrected constructor name
        print('c1 class constructor')

class c2(ABC):
    def m1(self):                            # Not abstract — regular method
        pass
    def __init__(self):
        print('c2 class constructor')

class c3:                                    # Not inheriting from ABC, but has abstractmethod =>  Error
    @abstractmethod
    def m1(self):
        pass
    def __init__(self):
        print('c3 class constructor')

class c4(c1):
    def m1(self):                            # Implements abstract method => OK
        pass
    def __init__(self):
        print('c4 class constructor')

class c5(c1):
    def __init__(self):
        print('c1 class constructor')        # Does NOT implement abstract method => Error
# End of the class
c1()     # Error: Can't instantiate abstract class c1 with abstract method m1
c2()     # Output: c2 class constructor
c3()     # Error: Can't instantiate abstract class c3 with abstract method m1
c4()     # Output: c4 class constructor
c5()     # Error: Can't instantiate abstract class c5 with abstract method m1


'''
Write  a  program  to  determine  area  and  perimeter  of  triangle , circle , rectangle  and  square

1) What  is  the  parent  class ?  ---> shape
    What  are  child  classes ?  ---> triangle , circle , rectangle , square

2) What  is  the  area  of  triangle  ?  --->  sqrt(s * (s - a) *  (s - b) * (s - c))
    What  is  the  value  of  's' ?  ---> (a + b + c) / 2
    What  is  the  perimeter  of  triangle ?  ---> a + b + c

3) What  is  the  area  of  circle ?  --->  3.14159 * a ^ 2  where  'a'  is  radius  of  circle
    What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * a

4) What  is  the  area  of  rectangle  ?  --->  a * b  where  'a'  is  length and  'b'  is  breadth
    What  is  the  perimter  of  rectangle ?  ---> 2 * (a + b)
'''

# Find  outputs (Home  work)
from abc import *

class parent(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    @abstractmethod
    def m3(self):
        pass

class child(parent):
    def m1(self):
        print('m1 method of child class')   # Only m1() is implemented, m2() and m3() are still abstract

class gc(child):
    def m2(self):
        print('m2 method of gc class')       # Now m1 and m2 are implemented, m3 is still abstract

class ggc(gc):
    def m3(self):
        print('m3 method of ggc class')      # All abstract methods m1, m2, m3 are now implemented

# End of the class

a = ggc()            # No error: ggc() implements all abstract methods
a.m1()               # Output: m1 method of child class
a.m2()               # Output: m2 method of gc class
a.m3()               # Output: m3 method of ggc class

parent()             # Error: Can't instantiate abstract class parent with abstract methods m1, m2, m3
child()              # Error: Can't instantiate abstract class child with abstract methods m2, m3
gc()                 # Error: Can't instantiate abstract class gc with abstract method m3

 
#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from abc import *

class person(ABC):
    def get(self):
        self.number = int(input("Enter number: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.gender = input("Enter gender: ")

    def disp(self):
        print(self.number, self.name, self.age, self.gender, sep='\t', end='\t')

    @abstractmethod
    def compute(self):
        pass

class student(person):
    def get(self):
        super().get()
        self.marks = []
        for i in range(1, 4):
            mark = float(input(f"Enter marks of subject {i}: "))
            self.marks.append(mark)

    def compute(self):
        self.total = sum(self.marks)
        self.average = self.total / 3

    def disp(self):
        super().disp()
        print(f"{self.total}\t{self.average:.2f}")

class teacher(person):
    def get(self):
        super().get()
        self.basic = float(input("Enter basic salary: "))
        self.da = float(input("Enter DA: "))
        self.hra = float(input("Enter HRA: "))
        self.pf = float(input("Enter PF: "))
        self.it = float(input("Enter IT: "))

    def compute(self):
        self.gross = self.basic + self.da + self.hra
        self.net = self.gross - (self.pf + self.it)

    def disp(self):
        super().disp()
        print(f"{self.gross}\t{self.net}")

# --- Example Usage ---
print("\nStudent Information:")
s = student()
s.get()
s.compute()
s.disp()

print("\nTeacher Information:")
t = teacher()
t.get()
t.compute()
t.disp()
#output : 
'''Student Information:
Enter number: 101
Enter name: Ravi
Enter age: 20
Enter gender: Male
Enter marks of subject 1: 78
Enter marks of subject 2: 88
Enter marks of subject 3: 92
101	Ravi	20	Male	258.0	86.00

Teacher Information:
Enter number: 201
Enter name: Lakshmi
Enter age: 35
Enter gender: Female
Enter basic salary: 25000
Enter DA: 8000
Enter HRA: 5000
Enter PF: 2000
Enter IT: 1000
201	Lakshmi	35	Female	38000.0	35000.0
'''

#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from abc import ABC, abstractmethod

class datatype(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def add(self, m, n):
        pass

    @abstractmethod
    def display(self):
        pass

class number(datatype):
    def get(self):
        self.x = int(input("Enter any number: "))

    def add(self, m, n):
        self.x = m.x + n.x

    def display(self):
        print("Sum  :  ", self.x)

class string(datatype):
    def get(self):
        self.x = input("Enter any string: ")

    def add(self, m, n):
        self.x = m.x + n.x

    def display(self):
        print("Join  :  ", self.x)

# -------- Menu Driven Program --------
while True:
    print("\n1. Add numbers")
    print("2. Join Strings")
    print("3. Exit")
    ch = int(input("Enter choice : "))
    
    if ch == 1:
        a = number()
        b = number()
        c = number()
        a.get()
        b.get()
        c.add(a, b)
        c.display()
        
    elif ch == 2:
        a = string()
        b = string()
        c = string()
        a.get()
        b.get()
        c.add(a, b)
        c.display()

    elif ch == 3:
        break
    else:
        print("Invalid choice!")
# output :
'''1. Add numbers
2. Join Strings
3. Exit
Enter choice : 2
Enter any string: 10
Enter any string: 20
Join  :   1020

1. Add numbers
2. Join Strings
3. Exit
Enter choice : 1
Enter any number: 10
Enter any number: 20
Sum  :   30

1. Add numbers
2. Join Strings
3. Exit
Enter choice : 2
Enter any string: Hyder
Enter any string: abad
Join  :   Hyderabad

1. Add numbers
2. Join Strings
3. Exit
Enter choice : 3
'''
# Identify  Error  (Home  work)
try: # Error becoz there is no except or finally for try block
	print('Hyd')
	print('Sec')
	print('Cyb')
    
# Find  outputs  (Home  work)
#print(7 / 0)  # ZeroDivisionError: division by zero (Program terminates here, nothing else is executed)

try:
	print(7 / 0)  # ZeroDivisionError is raised here
except ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')  # Division  by  zero  is  not  permitted

print(7 / 0)  # ZeroDivisionError: division by zero (Program terminates here)
print('Bye')  # Not executed


# Identify  error  (Home  work)
except: # Error becoz there is no try block
        print('Hyd')
        print('Sec')
        print('Cyb')
# Find  outputs (Home  work)
try:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
#print('Four') # Error becoz should not write any code indented with try and except
except:
		print('Five') # Five
		print('Six') # Six
		print('Seven') # Seven
print('Eight') # Eight
# Identify  error  (Home  work)
try:
	print('try suite')         # Output: try suite
except:                        # SyntaxError: default 'except:' must be last
	print('default  except')  
except NameError:              # This block is unreachable and causes SyntaxError
	print('Name  Error')

# Identify  error  (Home  work)
try:
	print('try suite')                 # Output: try suite
except:
	print('1st  default  except')      # SyntaxError: multiple default excepts not allowed
except:
	print('2nd  default  except')      # SyntaxError: only one default except is allowed


