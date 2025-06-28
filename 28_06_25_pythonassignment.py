'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  --->  length * breadth

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
'''
l = float(input('Enter length of rectangle :'))#Enter  length  of  rectangle  : 4
b = float(input('Enter breadth of rectangle :')) # Enter  breadth  of  rectangle :  5
Area  = l*b
Perimeter = 2*(l+b)
print(F'Area of rectangle: {Area:.2f}') # Area of rectangle: 20.00
print(F'Perimeter of rectangle: {Perimeter:.2f}') # Perimeter of rectangle: 18.00
'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
'''
import math
r = float(input('Enter a no:')) #Enter  radius  :  3.5
v = 4/3 * math.pi * r ** 3
print(F'Volume of the sphere : {v:.2f}') # Volume of the sphere : 179.59
'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  ---> ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
p = float(input('Enter a principle amount:')) #Enter  principle  :  10000
t = float(input('Enter time:')) #Enter  time  : 3
r = eval(input('Enter rate:')) #Enter  rate  of  interest :  7.5
SI = (p*t*r)/100              #Simple  Interest : 2250.00
CI = p*(1+r/100)**t-p        #Compound  Interest : 2422.97
print(F'Simple Interest : {SI : .2f}')
print(F'Compount Interest : {CI : .2f}')
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10
'''
x = int(input('Enter 1st input:'))                 #Enter  1st  input  : 10
y = int(input('Enter 2nd input:')) #Enter  2nd  input  : 25
temp = x
x = y
y = temp
print(F'After swap: x = {x} y = {y}')
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = -200
y =  100
'''
x = int(input('Enter a no:')) #Enter  1st  input  : 100
y = int(input('Enter a no:')) #Enter  2nd  input  : -200
x = x+y #Before  swap :  x=100.0           y=-200.0
y = x-y#After  swap :  x=-200.0           y=100.0
x = x-y
print(F'After swap : x = {x}  y = {y}') # After swap x = 100  y = -200
'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using 3rd  object

Hint: One  multiplication  and  two  divisions

x =  25
y =  10
'''
x = int(input('Enter a no:')) #Enter  1st  input  : 25
y = int(input('Enter a no:')) #Enter  2nd  input  : 10
x = x*y
y = x/y
x = x/y
print(F'After swap : x = {x}  y = {y}') # After swap x = 10  y = 25
'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

Let  first  input   be  3 + 4j  and  second  input  be   5 + 6j
What  is  the  sum ? --->  (3 + 4j) + (5 + 6j) =  8 + 10j
What  is  the  difference ?  --->  (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  --->  (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 = -9 + 38j
What  is  the  division ?  --->  (3 + 4j) / (5 + 6j)  =  (3 + 4j) * (5 - 6j) / (5 + 6j)  * (5 - 6j)
												=  (15 - 18j + 20j + 24) / (25 + 36)
												=   39 / 61  + 2j / 61
'''
x = complex(input('Enter a complex no:'))#Enter first complex number : 3+4j
y = complex(input('Enter a complex no:'))#Enter second complex number: 5+6j
print(F'Sum : x + y = {x+y} ') #Sum :  (8+10j)
print(F'Difference : x - y = {x-y} ')#Difference :  (-2-2j)
print(F'Product : x * y = {x*y} ') #Product:  (-9+38j)
print(F'DIvision : x / y = {x/y} ') #Division :  (0.6393442622950819+0.03278688524590165j)
'''
Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.
Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input

Hint:  Use  F  string  to  print  results
'''
x = eval(input('Enter a  no:')) # Enter 1st  integer  number :  10
y = eval(input('Enter a  no:'))#Enter 2nd  integer  number :  7
print(f'{x+y}')#10 + 7 = 17
print(f'{x-y}') #10 - 7 = 3
print(f'{x*y}')#10 * 7 = 70
print(f'{x/y}') #10 / 7 = 1.4285714285714286
print(f'{x%y}')#10 % 7 = 3
print(f'{max(x,y)}')#max(10 , 7) = 10
print(f'{min(x,y)}') #min(10 , 7) = 7
print(f'{x**y}') #10 ^ 7 = 10000000
print(f'{math.sqrt(x)}')#sqrt(10) = 3.1622776601683795
print(f'{math.gcd(x,y)}')#gcd(10 , 7) = 1
print(f'{math.factorial(x)}') #fact(10) = 3628800
'''
Gift
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = eval(input('Enter a no:')) #Enter  1st  input  : 25
y = eval(input('Enter a no:')) #Enter  2nd  input  : Hyd
x , y = y , x
print(F'After swap : x = {x}  y = {y}')
'''
Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10  and  20 ?   ---> 20

2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8

3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'

4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15

5) Use   ternary  operator
'''
'''Enter 1st input : 'Rama'
Enter 2nd input : 'Rajesh'
Largest  Input  :   Rama'''
'''
Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function

1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20

2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8

3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'

4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]

5) Use  nested  ternary  operator
'''
x = eval(input('Enter list:'))#Enter 1st input : [10,20,15,18]
y = eval(input('Enter list:'))#Enter 2nd input : [10,20,32,19]
z = eval(input('Enter list:'))#Enter 3rd input : [10,20,25,17]
print(max(x,y,z))#Largest  Input  :  [10, 20, 32, 19]
'''
Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,
                                               '<'  if  1st  input  <  2nd  input  and
                                               '='  if  inputs  are  same

1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <

2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >

3) What  is  the  result  if  inputs  are  25  and  25 ?  --->  =

4) Inputs  can  be  integers , floats , strings  and  so  on

5) Use  ternary  operator
'''
x = eval(input('Enter 1st input :')) # 10
y = eval(input('Enter 2nd input :')) # 20
if x>y:
    print('Result : >')
elif x<y:
    print('Result : <')
else:
    print('Result : =')    

#Result :   <
'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1

2) What  is  the  result  if  input  is  75 ?  --->  1

3) What  is  the  result  if  input  is  0 ?  ---> 0

4) Use  nested  ternary  operator
'''
x = int(input('Enter any number :' ))
res = 1 if x>0 else(-1 if x<0 else 0)
print(res)
'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2

3) Use  ternary  operator
'''
x = int(input('Enter any number except 0:' ))
res = 'Even' if x%2==0 else 'Odd'
print(res)

# Identify  error
'''else: # Error becoz no if condition to else
		print('else  suite')
print('Outside') '''
# Identify  error
#if  9 > 5 # Error becoz of no : after the if condition
	#print('Hello')
#print('Bye')
# Identify  error
if  9 > 12:
	print('Hyd')
#else # Error becoz of no : after else conditon
	print('Sec')
# Identify  error
if  (10,20,15):
#print('Hyd') # Indentation Error becoz after if condition no space or tab 
#else:
#print('Sec') ## Indentation Error becoz after if condition no space or tab 
# Identify  error
#if  ():
			print('Hyd')
	#else:  # if and else condition should be indented and same for print stmnts inside condition
					#print('Sec')
print('Bye')
# Identify  error
'''if  { }: # Error becoz of print stmnt are in suite
{
	print('One')
	print('Two')
	print('Three')
}
else:  # Error becoz of print stmnt are in suite
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')'''
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []: # Error becoz of if condition should be after inside else Indentation Error
	print('Four')
	print('Five')
	print('Six')
#else:  # Error becoz of if condition should be after inside else Indentation Error
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd') # Hyd
	print('Sec') # Sec
	print('Cyb') # Cyb
print('Bye') #Bye
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n = int(input('Enter a Integer No:'))
if n%2==0:
		print('Even',n)
else:
		print('Odd',n)	
# Find outputs  (Home  work)
if():
        print('Hyd') 
        print('Sec')
        print('Cyb')
else:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
print('Bye') # Bye
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') # Hyd
        print('Sec') # Sec
        print('Cyb') # Cyb
print('Bye') # Bye
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
	n = int(input('Enter month number (1 - 12)')) # 7
	if n==1:
		print('January')
	elif n==2:
		print('February')
	elif n==3:
		print('March')
	elif n==4:
		print('april')
	elif n==5:
		print('May')
	elif n==6:
		print('June')
	elif n==7:
		print('July')
	elif n==8:
		print('August')
	elif n==9:
		print('September')
	elif n==10:
		print('October')
	elif n==11:
		print('November')
	elif n==12:
		print('December')											
	else:
		print('Input Should be b/w 1 and 12')
except:
	print('Input should be Integer:')

#Enter month number (1 - 12): 13
#Input  should  be  between  1  and   12
#Enter month number (1 - 12): 10.8
#Input  should  be  an  integer

'''Write  a  program  to  test  year  is  leap  year  or  not

1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400

2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs

3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years

4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years

5) Hint:  3  conditions'''

x = int(input('Enter  4-digit  year :')) #  2024
if(x%4==0 & x%100!=0):
	print('Leap Year:',x)
elif(x%400==0):
	print('Leap Year:',x)	
else:
	print('Not Leap Year:',x)	


#Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else

#Hint:  Write  multiple  conditions

x=int(input('Enter 1st input : ')) #10
y=int(input('Enter 2nd input : ')) #20
z=int(input('Enter 3rd input : ')) #15
if x>y and x>z:
    print('x is greater: ',x)
if y>x and y>z:
    print('y is greater: ',y)
else:
    print('z is greater: ',z)	

'''Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa

1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32

2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8'''

x=int(input('Enter  1  to  convert  celsius  to  farenheit  and  2  to  convert  fahrenheit  to  celsius : '))
if x==1:
    temp = float(input('Enter the temperature in Celsius: '))
    f = 1.8 * temp + 32
    print(F'Fahrenheit : {f : .2f}')
elif x==2:
    temp = float(input('Enter the temperature in Fahrenheit: '))    
    c = (temp-32) / 1.8
    print(F'Celsius : {c : .2f}')
else:
    print('Enter 1 or 2 only: ') 

'''Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  ---> Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  …
'''
x=int(input("Enter  value  of  x  co-ordinate : "))
y=int(input("Enter  value  of  y  co-ordinate : "))
if x>0 and y>0:
	print("1st  quadrant ")
elif x<0 and y>0:
    print("2dn  quadrant ")
elif x<0 and y<0:
    print("3rd  quadrant ")
elif x>0 and y<0:
    print("4th  quadrant ")
elif (x<0 or x>0) and y==0:
    print("x - axis ")
elif x==0 and (y<0 or y>0):
    print("y - axis ")
else :
    print("origin")
'''
Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers

a = 10
b = 20
c = 7
max = 20
min =  7
mid =  (10 + 20 + 7) - (20 + 7) = 37 - 27 = 10

1) What  is  the  initial  value  of  max  ?  --->  a

2) Whichever  input >  max,  copy  that  input  to  max

3) What  is  the  initial  value  of  min  ?  --->  'a'

4) Whichever  input  <  min,  copy  that  input  to  min

5) How  to  obtain  middle  number ?  --->   Eliminate  max  and  min  from  a , b , c
'''
a=int(input("Enter 1st input:"))
b=int(input("Enter 2nd input:"))
c=int(input("Enter 3rd input:"))
if a>b>c:
    max=a
    print("max=",a)
elif b>a>c:
    max=b
    print('max=',b)
else:
    max=c
    print('max=',c)
if a<b<c:
    min=a
    print('min=',a)
elif b<a<c:
    min = b
    print("min=",b)
else:
    min = c
    print("main=",c)

print(f'mid ={(a+b+c)-(min+max)}')
'''
Write  a  program  to  determine  three  sides  form  a  triangle  or  not

1) Find  area  if  it  is  an  equilateral  triangle
    What  is  an  equilateral  triangle ?  ---> All  the  three  sides  should  be  same
    What  is  the  area  of  equilateral  triangle ?  --->  sqrt(3) / 4 * a ^ 2

2) Find  perimeter  if  it  is  an  isosceles  triangle
    What  is  an  isoscles  triangle ?  ---> Any  two  sides  are  same
    What   is  the  perimeter  of  isoscles  triangle ?  ---> a + b + c

3) Find  both  if  it  is  scalene  triangle
    What  is  a  scalene  triangle ?  ---> All  the  three  sides  are  different
    What  is  the  area  of  scalene  triangle ?  ---> sqrt(s * (s - a) * (s - b) * (s - c))
	What  is  the  value  of  's'  ?  --->  	(a…
Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 5
Scalene  triangle
Area : 6.00
Perimeter : 12.0
Enter  1st  side : 7
Enter  2nd  side : 8
Enter  3rd  side : 7
Isoscles  triangle
Perimeter : 22.0
Enter  1st  side : 7
Enter  2nd  side : 7
Enter  3rd  side : 7
Equilateral  triangle
Area : 21.22
Enter  1st  side : 3
Enter  2nd  side : 4
Enter  3rd  side : 8
Not  a  triangle
'''
try:
    import math

    a = int(input("Enter 1st side:"))
    b = int(input("Enter 2nd side:"))
    c = int(input("Enter 3rd side:"))
    if (a + b > c) and (b + c > a) and (a + c > b):
        if a == b == c:
            print("equilateral  triangle")
            print(f'area={math.sqrt(3 / 4) * a ** 2}')
            print(f'perimeter={a + b + c}')
        elif a == b or b == c or c == a:
            print("isoscles  triangle ")
            print(f'perimeter={a + b + c}')
        elif a != b or b != c or c != a:
            print("scalene  triangle")
            s = (a + b + c) / 2
            k = s * (s - a) * (s - b) * (s - c)
            y = math.sqrt(k)
            print(f'area={y:.2f}')
            print(f'perimeter={a + b + c}')
    else:
        print("not a triangle, sum of every two sides should be > 3rd side")
except:
    print("inputs should be an integer")
    
'''
Write  a  program  to  determine  roots  of  a  quadtratic  equation  a * x ^ 2 + b * x + c = 0  where  a  ! = 0

1) What  is  the  value  of  discriminant ?  --->  b ^ 2 - 4ac

2) What  are  the  roots  called  if  disc > 0 ?  --->  Real  and  distinct
     What  is  the  formula  for  root1  ?  ---> (-b + sqrt(disc)) / 2a
     What  is  the  formula  for  root2 ?  ---> (-b - sqrt(disc)) / 2a

3) What  are  the  roots  called  if  disc  is  0 ?  --->  Real  and  same
     What  is  the  formula  for  root  ?  --->  -b / 2a

4) What  are  the  roots  called  if  disc < 0 ?  --->  Complex  (or)  Imaginary  roots
     What  is  the  formula  for  real  part ?  --->  -b / 2a
	 What  is  the  formula  for  imag  part ?  --->  sqrt(-disc) / 2a
	 What  is  roo…
Enter  value  of  a : 5
Enter  value  of  b : 6
Enter  value  of  c : 5
Roots  are  imaginary  (or) complex
Root 1 : -0.6 +  0.8j
Root 2 : -0.6 -  0.8j
Enter  value  of  a : 3
Enter  value  of  b : 10
Enter  value  of  c : 3
Roots  are  real  and  distinct
Root 1 : -0.33
Root 2 : -3.00
Enter  value  of  a : 5
Enter  value  of  b : 10
Enter  value  of  c : 5
Roots are real and equal
Root 1 : -1.0
Root 2 : -1.0
Enter  value  of  a : 0
Value  of  a  can  not  be  0
'''

import math
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
disc=b**2-4*a*c
if a==0:
    print("Value  of  a  can  not  be  0")


else :
    if disc==0:
        print("Roots are real and equal")
        print(f'Root1 = {-b/(2*a)}')
        print(f'Root2 = {-b/(2*a)}')
    elif disc>0:
        print("Roots  are  real  and  distinct")
        k=(-b + math.sqrt(disc))/(2*a)
        g=(-b - math.sqrt(disc))/(2*a)
        print((f'Root1 = {k:.2f}'))
        print(f'Root2 = {g:.2f}')
    elif disc<0:
        print("Roots  are  imaginary  (or) complex")
        real=-b/(2*a)
        imag=math.sqrt(-disc)/(2*a)
        k=(f'{imag}j')
        print(f'Root1 = {real}+ {k}j')
        print(f'Root1 = {real}-{k}j')





'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units								Rs. 3.00 / unit

Next  100  units								Rs. 3.50 / unit

Next  200  units								Rs. 4.00 / unit

Next  300  units								Rs. 4.50 / unit

Above  700  units								Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else'''

units = int(input('Enter  units :   '))

match  int(units/100):
	case 0:
		cost =units*3
	case 1:
	    cost =100*3 + (units-100)*3.5
	case 2 | 3:
		cost =100*3 + 100*3.5 + (units-200)*4
	case  4 | 5 | 6:
		cost =100*3 + 100*3.5 + 200*4 + (units-400)*4.5
	case _:
		cost=100*3 + 100*3.5 + 200*4 + 300*4.5 + (units-700)*5
print('Bill  amount  :  ',cost)
'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  input  be   10
What  are  the  outputs  ?  ---> 0 , 1 , 1 , 2 , 3 , 5 , 8

1) What  is  10th  term ?  --->  9th  term + 8th  term
    What  is  3rd  term ?  --->  2nd  term + 1st  term
    What  is  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->  0  and  1

3) Hint:  Use  while  loop
'''

x = int(input("Enter a Number : "))
a = 0
b = 1
c = a + b
if x == a:
    print(a)
elif x == b:
    print("Fibonacci series :", a, b, sep="\n")
else:
    print("Fibonacci series :", a, b, sep="\n")
    while c < x:
        print(c)
        a = b
        b = c
        c = a + b

#  Find  outputs
while  True:
	print('Hello') # Hello
print('Bye') # Bye
#  Find  outputs
while  False: 
	print('Hello')
print('Bye') # Bye
