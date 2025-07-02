#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) 
print(lambda  x  :  print(x) (s))
print((lambda  x  :  print(x)) (s))
(lambda  x  :  print(x)) (s)
'''
OUTPUT:
<function <lambda> at 0x000002736E9A8360>
<function <lambda> at 0x000002736E9A8360>
Hyd
None
Hyd
'''


# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y
x = 10
adder2 = lambda  y , x = x : x + y
x = 20
print(adder1(100))   # 105
print(adder2(200))   # 210
print(adder1(300 , 400)) #700
'''
OUTPUT:
105
210
700
'''



#Find  outputs  (Home  work)
a = [lambda   x  :  x * 2 , lambda   x  :  x * 3 ,  lambda   x  :  x ** 4]
for   fun   in   a:
        print(fun(5)) #10 <nextline> 15 <nextline> 625
'''
OUTPUT:
10
15
625
'''



#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()
#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]
print(a)
a = [f1() , f2()]
print(a)
'''
OUTPUT:
Hyd
Sec
[<function f1 at 0x000001F579B08400>, <function f2 at 0x000001F579B087C0>]
Hyd
Sec
[None, None]
'''
# Find output  (Home  work)
a = {'power_2'  :  lambda   x  :  x ** 2 ,
       'power_3'  :  lambda   x  :  x ** 3 ,
  	   'power_4'  :  lambda   x  :  x ** 4}
key = 'power_3'
print(a[key])
print(a[key](5))
'''
OUTPUT:
<function <lambda> at 0x000002813E98F060>
125
'''





# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3)
print(type(f1))
print(type(lamb))
print(lamb(2)) #9
print(lamb(5)) #243
print(lamb)
#print(lamb())
'''
OUTPUT:
<class 'function'>
<class 'function'>
9
243
<function f1.<locals>.<lambda> at 0x0000021A3F10F060>
'''








# Find  outputs   (Home  work)
def   eval(a , b , c):
        return   lambda    x  :    a *   x **  2  +   b * x  +  c
lam  = eval(3 , 4 , 5)
print(lam(2)) #25
print(lam(2.5))
print(lam(4))
'''
OUTPUT:
25
33.75
69
'''


#Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y
a = add()
print(a(20)) #30
print(add(30)(40))#70
'''
OUTPUT:
30
70
'''



# Find  outputs
a= ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2000.0) , (15 ,'Rajesh' , 500.0) ,  (18 , 'Kiran' , 2800.0) , (5 , 'Amar' , 1300.0))   #  Nested  tuple
b = sorted(a)  # Sorts   tuple  'a'  based  on  1st  element  of  each  inner  tuple
print(b)  # [(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]
print()
c = sorted(a , reverse = True)  #  Sorts  tuple  'a'  in descendig  order  of   1st  element  of  inner  tuples
print(c)  #  [(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]
print()
d = sorted(a ,  key =  lambda   x  :  x[1])  # Sorts   tuple  'a'  based  on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(d)  # [(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]
print()
e = sorted(a , key =  lambda   x  :  x[2])  #Sorts   tuple  'a'  based  on   3rd  element  of  each  inner  tuple  due  to  x[2]
print(e)    #[(15, 'Rajesh', 500.0),(10, 'Rama', 1000.0),(5, 'Amar', 1300.0),(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]
print()
f = sorted(a , key = lambda   x  :  x[0])##Sorts   tuple  'a'  based  on   1st  element  of  each  inner  tuple  due  to  x[0]
print(f) #[(5, 'Amar', 1300.0),(10, 'Rama', 1000.0),(15, 'Rajesh', 500.0),(18, 'Kiran', 2800.0),(20, 'Sita', 2000.0)]
print()
g = sorted(a , key = lambda  x : x[1] , reverse = True) # # Sorts   tuple  'a' in descending order based  on   2nd  element  of  each  inner  tuple  due  to  x[1]
print(g) #[(20, 'Sita', 2000.0),(10, 'Rama', 1000.0),(15, 'Rajesh', 500.0),(18, 'Kiran', 2800.0),(5, 'Amar', 1300.0)]
#print(sorted(a , key = x[1]))
'''
OUTPUT:
[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0)]

[(5, 'Amar', 1300.0), (18, 'Kiran', 2800.0), (15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (20, 'Sita', 2000.0)]

[(15, 'Rajesh', 500.0), (10, 'Rama', 1000.0), (5, 'Amar', 1300.0), (20, 'Sita', 2000.0), (18, 'Kiran', 2800.0)]

[(5, 'Amar', 1300.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (20, 'Sita', 2000.0)]

[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
'''




# Find outputs  (Home  work)
a = [ {'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013} ,
        {'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999} ,
        {'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008} ]
b = sorted(a , key = lambda  x  :  x['Year']) # #  Sorts  list  'a'  in ascending order   of   year  element  of  inner  dictionary
print(b)   #[{'Make' : 'Tesla' , 'Model' : 'X' , 'Year' : 1999},{'Make' : 'Mercedes' , 'Model' : 'C350E' , 'Year' : 2008},{'Make' : 'Ford' , 'Model' : 'Focus' , 'Year' : 2013}]
#print(sorted(a))  #Error
'''
OUTPUT:
[(20, 'Sita', 2000.0), (10, 'Rama', 1000.0), (15, 'Rajesh', 500.0), (18, 'Kiran', 2800.0), (5, 'Amar', 1300.0)]
[{'Make': 'Tesla', 'Model': 'X', 'Year': 1999}, {'Make': 'Mercedes', 'Model': 'C350E', 'Year': 2008}, {'Make': 'Ford', 'Model': 'Focus', 'Year': 2013}]
'''



# Find outputs  (Home  work)
a = ((10 , 'Rama' , 1000.0) , (20 , 'Sita' , 2800.0) , (15 , 'Vamsi' , 2000.0) , (25 , 'Kiran' , 1500.0) ,  (5 , 'Amar' , 1300.0))
print(max(a , key = lambda  x  :  x[0] )) #(25, 'Kiran', 1500.0)
print(max(a , key = lambda  x  :  x[1] )) #(15, 'Vamsi', 2000.0)
print(max(a , key = lambda  x  :  x[2] )) #(20, 'Sita', 2800.0)
print(max(a))#(25, 'Kiran', 1500.0)
'''OUTPUT:
(25, 'Kiran', 1500.0)
(15, 'Vamsi', 2000.0)
(20, 'Sita', 2800.0)
(25, 'Kiran', 1500.0)
'''



# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) #False
add = lambda  x = 25 :   x == 35
print(add()) #False
#add = lambda  x  :   x = 25 #can't assign for lambda
#add = lambda  x  :   x := 25
'''
OUTPUT:
False
False
'''




#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()
f2()
print(f1  is  f2) #False
f2 = f1
#f2()
print(f1  is  f2)#True
f2 = f1()
print(f2) #f1 function
#f2()

f1    function
f2  function
False
True
f1    function
None




# Find  outputs (Home  work)
#How  to  assign  ref  'p'  to  print()  function
p=print
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hyderabad'
p('hyderabad')
p=print
print=None
p('Hello')
#How  to  call  print()  function  thru  ref  'p'  and   print  'Hello'

'''OUTPUT:
hyderabad
Hello'''





# Find   outputs (Home  work)
#How  to  assign  ref  'x'  to  id()  function
x=id
#How  to  call  id()  function  thru  ref  'x'  and   print  id  of  object 25
p=print
p=x
p(25)
print(p(25))#140721753491112
#How  to  assign  ref  'p'  to  len()  function
p=len
#How  to  call  len()  function  thru  ref  'p'  and   print  length  of  'Hyd
print(p('hyd')) #3'''




#  Find  outputs (Home  work)
def  outer():
	print('Outer  function')
	def  inner():
		print('Inner  function')
	# End  of  inner  function
	print('Hello')
	inner()
	print('Back  to  outer  function')
def  other():
	#inner()
	print('Other  function')
# End  of  the  function
print('Begin')
outer()
print('Hi')
#inner()
other()
print('Bye')
'''
OUTPUT:
Begin
Outer  function
Hello
Inner  function
Back  to  outer  function
Hi
Other  function
Bye
'''




# Find  output(Home  work)
def    f1(a):
	def   f2():
		return  10
	# End  of  f2  function
	return  f2() + 20 +  a #10+20+30
# End  of  f1  function
print(f1(30)) #60





# Find  outputs (Home  work)
def  outer():
	print('Outer  function') #Outer function
	def  inner1():
		print( '1st  inner  function')
	def  inner2():
		print('2nd  inner  function')
	print('Hi') #Hi
	inner2()    #2nd inner function
	print('Hello') #Hello
	inner1()    #1st inner function
	print('Back  to  outer  function') #Back to outer function
# End of the function
print('Begin') #Begin
outer()
print('Bye') #Bye
'''
OUTPUT:
Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye
'''




# Find  outputs  (Home  work)
x = 10
def  outer():
	x = 20
	def   inner():
		x = 30
		print(x)
		print(globals()['x'])
	inner()
outer()
print('Bye')
'''
OUTPUT:
30
10
Bye
'''





# Find  outputs  (Home   work)
x = 10
def  outer():
	x = 20
	def   inner():
		print(x)
		print(globals()['x'])
	inner()
outer()
'''
OUTPUT:
20
10
'''



# Find  outputs  (Home  work)
x = 10
def  outer():
	def   inner():
		print(x)
	inner()
outer()
'''
OUTPUT:
10
'''


# Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		x = 20
		print(x)
		x +=  7
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  the  function
outer()
print('Bye')
'''
OUTPUT:
10
20
15
Bye
'''



#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		nonlocal  x
		print(x)
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)
'''
OUTPUT:
15
20
25
10
'''
print()

#  Find  outputs  (Home  work)
def  outer():
	x = 10
	def  inner():
		#print(x)
		#nonlocal  x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
'''
OUTPUT:
10
20
15
'''




#  Find   outputs(Home  work)
def  outer():
	x = 10
	def  inner():
		global   x
		x = 20
		print(x)
		x += 5
	# End  of  inner  function
	print(x)
	x += 5
	inner()
	print(x)
# End  of  outer  function
outer()
print(x)
'''
OUTPUT:
10
20
15
25
'''
print()




# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x
		x = 20
		print(x)
	# End  of  inner  function
	inner()
	#print(x)
# End  of  the  function
outer()
#print(x)
'''
OUTPUT:
20
'''




# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x
		x = 20
		print(x)
		x = x + 5
	# End  of  inner  function
	inner()
	print(x)
# End  of  the  function
outer()
print(x)
'''
OUTPUT:
20
25
25
'''



#  Identify  Error
'''def   f1():
        #nonlocal   x
		pass'''





# Find  outputs (Home  work)
def  outer():
	a = 10
	b = 20
	def   inner():
		nonlocal   a
		a = 100
		b = 200
		print(a , b)
	# End  of  inner  function
	print(a , b)
	inner()
	print(a , b)
#end of outer function
outer()
'''
OUTPUT:
10 20
100 200
100 20
'''




# Find  outputs (Home  work)
def   f1():
	x = 'John'
	def  f2():
		nonlocal  x
		x =  'Hello'
	#end of inner function
	f2()
	return  x
#  End  of  f1()  function
print(f1())
'''
Hello
'''



# Find  output(Home  work)
def  fun():
	x = 10
	def    gun():
		#x =  x +  20
		print(x)
	#end of inner function
	gun()
#end of outer function
fun()
'''
OUTPUT:
10
'''

#  Identify  Error
x = 10
def   outer():
	x = 20
	def  inner():
		global   x
		#nonlocal x


#  Find  outputs  (Home   work)
def   f1():
	x = 10
	def  f2():
		nonlocal   x
		def  f3():
			nonlocal   x
			print(x)
		f3()
	f2()
f1()
'''
OUTPUT:
10
'''

#1  Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2(fun):
	print('f2  function')
	fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1)
print('End')

'''Output:
Begin
f2  function
f1  function
Back  to  f2  function
End'''

#2 Find  outputs  (Home  work)
def  f1():
	print('f1  function')
def   f2 (fun):
	print('f2  function')
	#fun()
	print('Back  to  f2  function')
# end of the function
print('Begin')
f2(f1())
print('End')

'''Output:
Begin
f1  function
f2  function
Back  to  f2  function
End'''

#3 Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner
# End  of  the  function
fun = outer()
print('Hello')
fun()
print('Bye')
#inner()

'''Output:
Outer  Function
Hello
Inner function
Bye'''

#4 Find  outputs (Home  work)
def  outer(x):
	print('Outer  Function')
	def  inner1():
		print('1st  inner  function')
	# End  of  inner1
	def  inner2():
		print("2nd  inner  function")
	# End  of  inner2
	if   x == 10:
		return  inner1
	else:
		return  inner2
#end of the function
f1 = outer(10)
f2 = outer(20)
f1()
f2()

'''Output:
Outer  Function
Outer  Function
1st  inner  function
2nd  inner  function'''

#5 Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner
# End  of  the  function
hi_fun = outer('Hi')
hello_fun = outer('Hello')
hi_fun()
hello_fun()

'''Output:
Hi
Hello'''

#6 Find  outputs  (Home  work)
def   decor(fun):
#	print(fun . _name_)
	def   inner():
		return   fun() +  2
	return  inner
@decor
def   f1():
	return  10
# End of the function
print('End')

#Output: End

#7  How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun):
	def   inner():
		x = fun()
		return   x + 2
	return  inner
def  f1():
        return  10
#end  of  the  function
f1 = decor(f1)
print(f1())

Output: 12

#8 Find  outputs(Home  work)
def   decor(fun):
	def  inner(x , y):
		try:
			return  fun(x , y)
		except:
			return   'Division   by  0  is  not  permitted'
	return  inner
@decor
def  div(a , b):
        return  a / b
# End  of  the  function
print(div(10 , 3))
print(div(10 , 0))
#print(inner(10 , 3))

Output: 3.3333333333333335
#Division   by  0  is  not  permitted

#9 Modify  following  div  function  such  that  div(9 , 2)   and   div(2 , 9)  should  return  4.5  only
def  decor(fun):
	def inner(a,b):
		if a<b:
			a,b=b,a
		return fun(a,b)
	return inner
@decor
def  div(a , b):
    return   a /b
print(div(9 , 2)) #  4.5
print(div(2 , 9)) #  4.5

'''Output:
4.5
4.5'''

#10 Find  outputs (Home  work)
def   decor(fun):
	def   inner():
#		print(F'Decorating  {fun . _name_}  function')
		fun()
		print('Decoration  is  finished')
	return  inner
@decor
def   f1():
	print('Hello')
# End  of  the  function
f1()
print('Bye')

'''Output:
Hello
Decoration  is  finished
Bye'''

#11 Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
#	print(fun . _name_)
	def   inner(*x):  #  x  is  var-arg  parameter
		print(x)
		fun(*x)  #  Unapcks  object   'x'  to  elements
		print('End  of  decoration')
	return  inner
@decor
def   f1(x):
	print('f1  function  :  ' , x)
@decor
def   f2(x , y):
	print('f2  function  :  ' , x , y )
@decor
def  f3(x , y , z):
	print('f3 function : ' , x , y , z)
@decor
def   f4():
	print('f4 function')
# end of function
f1(10)
f2(25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j)
f4()

'''Output:
(10,)
f1  function  :   10
End  of  decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration'''

#12 Find  outputs  (Home  work)
def  square(fun):
	def  inner1():
		x = fun()
		return  x * x
	return  inner1
def   double(fun):
	def  inner2():
		y = fun()
		return  2 * y
	return   inner2
@double
@square
def  num():
	return  10
#end of the function
print(num())

Output: 200

#13  Find  outputs  (Home  work)
def   bold(fun):
	def  inner1():
		return  '<b>'  +  fun()  +  '</b>'
	return  inner1
def   italic(fun):
	def   inner2():
		return  '<i>'  +  fun() +  '</i>'
	return  inner2
def   underline(fun):
	def   inner3():
		return  '<u>'  +  fun()  +  '</u>'
	return  inner3
@bold
@italic
@underline
def   f1():
       return  'Hello  World'
# End  of  the  function
print(f1())

#Output: <b><i><u>Hello  World</u></i></b>

#14  Write  a  recursive  function  to  determine  gcd (or) hcf  of  2 numbers
#1) gcd(12 , 15) =  gcd(15 , 12) = gcd(12 , 3) = gcd(3 , 0) = 3
#2) gcd(4 , 7) = gcd(7 , 4) = gcd(4 , 3) = gcd(3 , 1) = gcd(1 , 0) = 1
def  gcd(m , n):
	if  n==0:
		return  m
	else:
		return  gcd(n, m%n)
m = int(input('Enter  any  number  :  '))
n = int(input('Enter  any  number  :  '))
print('Gcd :  ' ,  gcd(m,n))

'''Output:
Enter  any  number  :  12
Enter  any  number  :  36
Gcd :   12'''

#15 Write  a  recursive  function  to  find  sum of  the  digits  of  a  number
sod(678) =  678 % 10 + sod(678 // 10)
               =  8 + sod(67)
               =  8 + 67 % 10 + sod(67 // 10)
               =  8 + 7 + sod(6)
               =  8 + 7 + 6 % 10 + sod(6 // 10)
               =  8 + 7 + 6 + sod(0)
               =  8 + 7 + 6 + 0
               =  21
1) How  many  function  calls  are  in  sod(678) ?  --->  4
2) How  many  function  calls  are  in  sod(n-digit  number) ?  --->  n + 1
def   sod(n):
	if  n==0:
		return  0
	else:
		return  n%10 + sod(n//10)
n = int(input('Enter  any  number :   '))
print('Sum of the digits :   ' ,  sod(n))

'''Output:
Enter  any  number :   9427
Sum of the digits :    22'''

#16 Write  a  recursive  function  for  fibonacci  term
'''Use  the  function  to  generate  fibonacci  series
1) What  is  the  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , ....
2) What  is  the  formula  for  10th  term ?  --->  9th  term +  8th  term
     What  is  the  formula  for  3rd  term ?  --->  2nd  term +  1st  term
     What  is  the  formula  for  ith  term ?  ---> (i - 1)th   term +  (i - 2)  term
3) What  are  the  first   two  terms ?  --->  0  and  1'''

def  fib(i):  #  'i'  is  term  number
	if  i==0:
		return   0
	if  i==1:
		return  1
	return  fib(i-1) + fib(i-2)
n = int(input('How many terms ? :  '))
print('Fibonacci  series')
for i in range(n):
    print(fib(i), end=" ") 

'''Output:
How many terms ? :  7
Fibonacci  series
0 1 1 2 3 5 8 '''

'''#17 Write  a  recursive  power  function
1) What  is  the  formula  for  4.5 ^ 3 ?  --->  4.5 * 4.5 ^ 2
2) What  is  the  formula  for  4.5 ^ -3 ?  --->  1/4.5 * 4.5 ^ -2
3) What  is  4.5 ^ 0 ?  --->  1'''

def pow(a, b):
    if b == 0:
        return 1
    if b > 0:
        return a * pow(a, b - 1) 
    else:
        return 1 / pow(a, -b) 
a = float(input('Enter  base :  '))
b = int(input('Enter  power :  '))
print(f"{a} ^ {b} = {pow(a, b)}")

'''Output:
Enter  base :  8
Enter  power :  6
8.0 ^ 6 = 262144.0'''

'''#18 Write  a   recursive  function  to  reverse  a  number
rev(678) =  678 % 10 * 10 ^ 2 + rev(678 // 10)
              =  800 + rev(67)
              =  800 + 67 % 10 * 10 ^ 1 + rev(67 // 10)
              =  800 + 70 + rev(6)
              =  800 + 70 + 6 % 10 * 10 ^ 0 + rev(6 // 10)
              =  800 + 70 + 6 + rev(0)
              =  800 + 70 + 6 + 0
			  = 876
1) How  many  function  calls  are  in  rev(678) ?  --->  4
2) How  many  function  calls  are  in  rev(n-digit number)  ? ---> n + 1
3) How  to  obtain  length  of a  number ?  --->  len(str(number))'''

from math import log10

def rev(n):
    if n == 0:
        return 0
    num_digits = int(log10(n)) 
    return (n % 10) * (10 ** num_digits) + rev(n // 10)  
n = int(input('Enter  any  number :  '))
print('Reverse   Number :  ' , rev(n))

'''Output:
Enter  any  number :  7581346
Reverse   Number :   643185'''

#  1.   Find  outputs
def  f1():
	a = 3
	if  a > 0:
		print(a) 
		a = a - 1
		#f1() #RecursionError: maximum recursion depth exceeded
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
f1() 
print('End')

'''
3
i think infinte recrussion error bcz 3 is reduced 2 and everytime condition is checked. '''

#* 2. Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40: 
		return
	x += y
	f1(x , y)
	print(x)
#End  of  the  function
x = 10 
f1(x , x := x + 1)
print(x)
'''
11>40
21>40 false
32>40
43>40 True 
print 43 

Output: 43
32
21
11 bcz stack saves after function call they executed last in last out 
''' 
# 3*.  Find  outputs   (Home  work)
def  f1(x):
	print(x)
	if   x:
		f1(x - 1)
	print(x)
# End  of  the  function
f1(3) 
'''

outputs :
	3
	2
	1
	0
	0
	1
	2
	3 ''' 
# 4.  Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1())) 
	'''
	empty generator is created 
	25
	25
	25  continously '''
# 5. How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
#  End  of  for  loop
print('End')
print(g)
#print(next(g)) # error 
g = f1()
print(next(g))

'''
one 
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
Type and address
One
25

'''

# *6.  Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))
for  x  in   g:
	print(x)
print()
for  x  in   f1():  # a new generator object  is created 
	print(x)
print()
gen = f1()
print(next(gen)) #25
for  x  in   f1():  # a new generator object is created 
	print(x)
print(next(gen))
'''
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8 '''

#7. Find  outputs (Home  work) 
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g: # for loop same generator which is exhusted 
	print(y)
'''
0
Hello
1
Hello 
4
Hello
9
Hello
16
Hello
 '''
 # 8. Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
'''
0
1
4
9
16
0
1
4
9
16 '''

# 9. Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)

'''
0
1
4
9
16
True '''

# 10.  Find  outputs
def  f1():
	global  a
	if  a:
		print(a)
		a = a - 1
		f1()
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
a = 3
f1()
print('End')
'''
3
2
1
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
End'''

# 11. Find  outputs  
def  f1():
	print('f1  function')
	#f2()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	# f1()
	print('End  of  f2  function')
f1()

'''
f1 function 
f2 function 
each statement are called infintely 

'''#1  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))

d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))

g = (x * x   for   x   in   range(5))
print(g)
print(type(g))


[0, 1, 4, 9, 16]
<class 'list'>
{0, 1, 4, 9, 16}
<class 'set'>
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
<class 'dict'>
<generator object <genexpr> at 0x000001F5A5A620A0>
<class 'generator'>

#2 Find  outputs (Home  work)
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
#print(next(g))

10
10
10

10
20
30
