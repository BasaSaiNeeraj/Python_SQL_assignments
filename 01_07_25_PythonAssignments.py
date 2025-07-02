# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) #  a : 10 <tab> b : 20
f1(b = 30 , a = 40) #  a : 40 <tab> b : 30
#f1(50 , 60) # Error becoz after * it will take key word argmnts only
f1(70 , b = 80) # Error becoz after * it will take key word argmnts only
#f1(a = 15 , 25) # Error: positional argument follows keyword argument
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a : 10 <tab> b : 20 <tab> c : 30
f1(a = 40 , b = 50 , c = 60) # a : 40 <tab> b : 50 <tab> c : 60
f1(c = 100 , b = 90 , a = 80) # a : 80 <tab> b : 90 <tab> c : 100
f1(70 , 80 , c = 90) # Error becoz b must be Keyword Argmt
f1(70 , 80 , 90) # Error beco b and c must be Keyword Argmt
f1(c = 15 , b = 25 , 35) # Error becoz Positional Argmnt after Keyword Argmnt
# Identify error (Home  work)
def   f1(a  , b , *): # Error becoz after * atleast one Keyword argmt should be there
        pass
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}') 
# End  of   the  function
f1(10 , 20) # a : 10 <tab> b : 20
f1(a = 30 ,  b = 40) # Error becoz it only supports Postional Argmnts becoz of /
f1(50 , b = 60) # Error becoz of b
f1(a = 70 , 80) # Error becoz of P.A after K.A
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a : 10 <tab> b : 20 <tab> c : 30
f1(40 , 50 , c = 60) # a : 40 <tab> b : 50 <tab> c : 60
f1(a = 70 , b = 80 , c = 90) # Error becoz of a and b are k.A 
f1(a = 100 , b = 110 , 120) # Error becoz of P.A after k.A
f1(a = 130 , 140 , c = 150) # Error beoz of P.A after K.A
f1(160 , b = 170 , 180) # Error becoz of P.A after K.A
f1(190 , b = 200 , c = 210) # Error becoz of b is K.A
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a : 10 <tab> b : 20 <tab> c : 30 <tab> d : 40 <tab> e : 50 <tab> f : 60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error becoz of b is K.A 
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error becoz e is P.A
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error becoz P.A after K.A
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a : 10 <tab> b : 20 <tab> c : 30 <tab> d : 40 <tab> e : 50 <tab> f : 60
# Identify error (Home  work)
def  f1(/ , a , b ,  c): # Error becoz of atleast one P.A before /
        pass
def   f2(a , b , c , *): # Error becoz one K.A after *
        pass
# Identify  error  (Home  work)
def  f4(* , a , b , c , /): # Error becoz P.A / is after K.A *
	        pass
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x) 
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd  function : 10
f1(y = 20) # Error becoz of same function name 
f1(x = 30) # Error becoz of same function name
# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): # Error becoz P.A after a
	pass 
def   f2(b , d , a = 10 , c = 20): # No Error
	pass
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a) # 20 <next line> 10 <next line> 30
# End  of  the  function
f1(20)
f1()
f1(a = 30)
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 100 + 200 + 10 + 20 = 330
print(add(100 , 200 , 300)) # 100 + 200 + 300 + 20 = 620
print(add(100 , 200 , 300 , 400)) # 100 + 200 + 300 + 400 = 1000
print(add(b = 100 , a = 200)) # 200 + 100 + 10 + 20 = 330
print(add(100 , 200 , d = 300)) # 100 + 200 + 10 + 300 = 610
print(add(d = 100 , a = 200 , b = 300)) # 100 + 200 + 300 + 10 = 610
print(add(c = 100 , d = 200 , 300 , 400)) # Error becoz of P.A after K.A
print(add(100 , 200 , c = 300 , x = 400)) # Error becoz of x is not there
print(add()) # Error becoz there is no default parameters for a and b
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x # 10 <next line> 25
def   f2(x):
        return  x # 20 <next line> Error becoz no default parameter
# End  of  the  function
print(f1(10))
print(f1())
print(f2(20))
print(f2())
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # 20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
disp(ch = '!' ,  5) # Error becoz P.A after K.A
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 4.5 ** 3 = 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
def   power(b = 2 , a): # Error becoz K.A after P.A
 	 pass
# Find outputs  (Home  work)
def   add(a , b):
	print('2-argument  function') 
	return a + b 
def  add(a , b , c):
	print('3-argument  function') 
	return a + b + c  
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function') 
	return a + b  + c + d 
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40)) # 4-argument  function <next line> 100
print(add(50 , 60 , 70)) # 4-argument  function <nxt line> 184
print(add(80 , 90)) # 4-argument  function <nxt line> 177
print(add(100)) # 4-argument  function <nxt line> 109
print(add()) # 4-argument  function <nxt line> 10
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b) 
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :   10 20 30
#disp(40 , 50 , 60 , 70) # Error becoz of 4 P.A
disp(80 , 90) # 3-argument  function  :   80 90 25
# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b # 70 <nxtt line> 30 <nxt line> 70 <nxt line> 130 <nxt line> Error becoz of P.A
# End of  the  function
print(add(a = 30 , b = 40)) 
print(add())
print(add(a = 50))
print(add(b = 60 , a = 70))
print(add(80 , 90))
# Find  outputs(Home  work)
def   add(a = 10 , b , c): # Error becoz of default Parameters after non-default Parameters
        pass
def   add( * , a = 10 , b , c ): 
        return  a + b + c # 120 <xt line> 140 <nxt line> 270 <nxt line> Error becoz b is not given <nxt line> Error becoz P.A is given after * <nxt line> P.A after K.A
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))
print(add(b = 60 , c = 70))
print(add(c = 80 , b = 90 , a = 100))
print(add(c = 25 , a = 43))
print(add(1 , 2 , 3))
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
		pass
# Find  output (Home  work)
def   f1(a = []):
        pass
print(f1 . __defaults__) # ([],)
# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a) # List : [3] <nxt line> List : [1, 2, 3, 4] <nxt line> List : [3,9] <nxt line> List : [10, 20, 30, 40] <nxt line> List : [3, 9, 5] <nxt line> List : [3, 9, 5, [6, 7, 8]]
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([],)
f1(3)
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([3],)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([3],)
f1(9)
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([3,9],)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([3,9],)
f1(5)
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([3,9,5],)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_) # _defaults_  :   ([3, 9, 5, [6, 7, 8]],)
#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_)
f1(3)
print('_defaults_  :  ' , f1._defaults_)
f1(4 , [1 , 2 , 3])
print('_defaults_  :  ' , f1._defaults_)
f1(4)
print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)
f1(5)
print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)
# Find  outputs(Home  work)
def     f1(x , a = []):
	for  i  in  range(x):
		a . append(i * i)
	return  a
# End  of  the  function
print('_defaults  :  ' , f1._defaults_)
print(f1(3))
print('_defaults  :  ' , f1._defaults_)
print(f1(4 , [10 , 20 , 15 , 18]))
print('_defaults  :  ' , f1._defaults_)
print(f1(5))
print('_defaults  :  ' , f1._defaults_)
print(f1(a = [100 , 200 , 300],   x = 6 ))
print('_defaults  :  ' , f1._defaults_)
print(f1(6))
print('_defaults  :  ' , f1._defaults_)
# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))
print(f1(4 , [10 , 20 , 15 , 18]))
print(f1(5))
print(f1(a = [100 , 200 , 300],   x = 6 ))
print(f1(6))
# Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b += [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()
print('Default Values  :  ' , f1 . _defaults_)
f1()

#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)   #  Tuple  of  4  elements  is  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
#f1(t = (10 , 20 , 30))  #  Error  :  var-arg  param  can  not be  ka


'''
(10,20,15,18)
<class  'tuple'>
4
'''
#  Write  a  function  to  determine  average  of  arguments  passed  from  function  call (Home  work)
def avg(*a):
    return sum(a) / len(a) if a else 0 #Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
# End  of  the  function
print(avg(10 , 20 , 15 , 18)) #  Average  of  10 , 20 , 15  and  18 is 15.75
print(avg(25 , 10.8 , True)) # 25+10.8+1.0 = 36.8/3 = 12.266666666666667
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) # 71.3/5 = 14.26
print(avg()) # 0
print(avg(25)) # 25.0
print(avg(3 + 4j , 5 + 6j)) # 4+5j
tpl = (10 , 20 , 15 , 18) 
print(avg(tpl))  # Error becoz no sum for tuple it can done by unpacking tuple
'''
Gift
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def concat(*a):
    return ' '.join(str(x) for x in a) #Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))  # Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City')) # Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Python Is A Great Language
print(concat()) # empty string
print(concat('Python')) # Python
print(concat(1, 2, 3)) # 1 2 3
#Find  outputs (Home  work)
def   f1(a = 25  , *b):	
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 25 <tab> b : (20,30,40)
f1(50 , 60) # a : 50 <tab> b : 60
f1(70) # a : 70 <tab> b : ()
f1(a = 80) # a : 80 <tab> b : ()
f1(b = (10 , 20 , 30) , a = 40) # Error becoz b got unexpect argmnt 
f1() # a : 25 <tab> b : ()
f1(a = 10 , (20 , 30 , 40)) # Error becoz P.A after K.A
f1(25 , b = (10 , 20 , 30)) # Error becoz b got unexpect argmnt
f1(25 , a = (10 , 20 , 30)) # Error becoz a got unepect argmnt
f1((10 , 20 , 30) , 10 , 20 , 30) # a : (10,20,30) <tab> b : (10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30) # Error becoz P.A after K.A
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)
f1(50 , b = 60)
f1(b = 70)
#f1(b = 10 , a = (20 , 30 , 40)) # Error: f1() got an unexpected keyword argument 'a'
#f1(b = 10 , (20 , 30 , 40)) Error becoz P.A after K.A
#f1()#Error: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , (10 , 20 , 30)) # Error: f1() missing 1 required keyword-only argument: 'b'
#f1(10 , 20 , 30 , 40)#Error: f1() missing 1 required keyword-only argument: 'b'
#f1(25)#Error: f1() missing 1 required keyword-only argument: 'b'

f1(10 , 20 , 30 , b = (10 , 20 , 30)) # a  :  (10, 20, 30)   	   b  :  (10, 20, 30)
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) # a : 10 <tab> b : (20,30,40) <tab> c : 50
f1(60 , 70 , c = 80) # a : 60 <tab> b : 70 <tab> c : 80
f1(90 , c = 100)  # a : 90 <tab> b : () <tab> c : 100
#f1(a = 1 , 2 , c = 3) # Error becoz P.A after K.A
#f1(1 , 2 , 3) # Error: f1() missing 1 required keyword-only argument: 'c'
#f1(a = 1 , b = 2 , c = 3) # Error: f1() got an unexpected keyword argument 'b'
#f1(a = 25 , 100 , 200 , 300 , c = 35) # Error becoz of P.A after K.A
# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b): # Error: * argument may appear only once
        pass
def  f2(*a , b): # Valid b must be K.A
        pass
def  f3(a , *b): # Valid
        pass
def  f4(a , b): # Valid
        pass
def    f5(a , *b , c): # Valid but c must be K.A
        pass
def   f6( * , a , *b , c): # Error: * argument may appear only once
       pass
def   f7(a , *b , c ,  /): #     Error: positional-only marker (/) may appear only once
       pass
# Find  outputs  (Home  work)
def   f1(*a):
	print(a) # ([10, 20], {40, 30}, (50, 60))
	print(type(a)) # <class 'tuple'>
	for  x  in  a:
		print(x) # [10,20] <nxt line> {40,30} <nxt line> (50,60)
		print(type(x)) # <class 'list'> <nxt line> <class 'set'> <nxt line> <class 'tuple'>
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results') # Results
	print(type(a)) # <class 'dict'>
	print(a) 
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  #  {'RollNo': 10, 'StudName': 'Rama  Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0) # {'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm') # {'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}
disp() # {}
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results') # Results
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ') # Empno ... 25 <nxt line> Empname ... Rama  Rao <nxt line> Salary ... 10000.0 <nxt line> Gender ... m
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
f1() # Results
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a)) # <class 'tuple'>
	print(a) # (25, 10.8, 'Hyd', True)
def   f2(**a):
	print(type(a)) # <class 'dict'>
	print(a) # {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a) # Emp  Number  :  25  	  Emp  Name  :  Sita  	  Salary  :	10000.0 <nxt line> Error becoz of there is no eno <nxt line> {'empno': 25, 'ename': 'Sita', 'sal': 10000.0} <nxt line> {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0)
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a) # 25 <nxt line> Hyd <nxt line> 10.8
	if   b:
		print(b) # (10,20,30) <nxt line> (25, 'Hyd', True)
	if  c:
		print(c) # {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
# End  of  the  function
f1(25)
print()
f1('Hyd' , 10 , 20 , 30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) # a : 10
	print('b : ' , b) # b : 20
	print('c : ' , c) # c : 30
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a) # a :  11
	print('b : ' , b) # b :  40
	print('c : ' , c) # c :  31
# End  of  f2()  function
c = 30
print('a : ' , a) # a :  50
print('b : ' , b) # b :  22
print('c : ' , c) # c :  32
print()
a +=  1
b +=  1
c +=  1
f1()
a +=  1
b +=  1
c +=  1
f2()
print('Bye') # Bye
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # 20
	a += 1
#End  of  the  function
a = 10
print(a) # 10
a += 1
f1()
print(a) # 11
# Find  outputs  (Home  work)
def   f1():
	a = 20
	print(a) # 20 
	dict = globals()
	print(dict['a']) # 11
	a = 30
	dict['a'] = 40
#  End  of  f1()  function
a = 10
print(a) # 10
a += 1
f1() 
print(a) # 40
# Find  outputs (Home  work)
x = 10
def   f1():
	print(x) # 10
	print(globals()['x']) # 10
# end of the function
f1()
# Find  outputs (Home  work)
def  f1():
	x = 20
	print(x) # 20
	print(globals()['x']) # Error: 'x'
# End  of  the  function
f1()
# Find outputs (Home  work)
def  f1():
	a = 40
	b = 50
	c = 60
	print(a , b , c) # 40 50 60
	dict = globals()
	print(dict['a'] , dict['b'] , dict['c']) # 10 20 30
	dict['a'] = 100
	dict['b'] = 200
	dict['c'] = 300
def  f2():
	print(a , b , c) # 100 200 300
# End  of  f2  function
a = 10
b = 20
c = 30
f1()
f2()
# global  keyword  demo  program (Home  work)
def    f1():
	x = 20
	print(x) # 20
def   f2():
	global  x
	x = 30
	print(x) # 30
	x += 1
def   f3():
	global  y
	y = 40
	print(y) # 40
	y += 1
def   f4():
	x = 50
	#global   x # Error: name 'x' is assigned to before global declaration
#  End  of  the  functions
x = 10
print(x) # 10
x += 1
f1() 
print(x) # 11
f2()
print(x) # 31
x += 1
f3()
print(y) # 41
f4()
print(x) # 32
# Find outputs (Home  work)
def  f1():
	global  a
	a = 20
	print(a) # 20
	print(globals()['a']) # 20
	a = 30
# End of the function
a = 10
print(a) # 10
f1()
print(a) # 30
# Find  outputs(Home  work)
def  f1():
	global  a
	#print(a) # Error: name 'a' is not defined
	a = 10
	print(globals()['a']) # 10
	a = 20
	print(a) # 20
	a = 30
def  f2():
	print(a) # 30
# End  of   f2   function
f1()
f2()
print(a) # 30
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 10
	a = 20
def  f2():
	global  a
	print(a) # 20
	a = 30
def  f3():
	print(a) # 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a) # 40
# Find outputs (Home  work)
def  f1():
	global   a
	a = 10
	print(a) # 10 
	a = 20
def  f2():
	#print(a) # Error: cannot access local variable 'a' where it is not associated with a value
	a = 30
	print(a) # 20
def  f3():
	print(a) # 30
	globals()['a'] = 40
# End  of  the  function
f1()
f2()
f3()
print(a) # 40
#  Find  outputs (Home  work)
def  f1():
        a = 10
        #global  a # Error: name 'a' is assigned to before global declaration
        print(a) # 10
        global  b
        b = 20
# End  of  f1()  function
f1()
#print(a) # Error: name 'a' is not defined
print(b) #20
# Find outputs (Home  work)
def  f1():
        global  a
        print(a) # 11
        a += 1
def  f2():
        global  a
        print(a) # 13
        a += 1
# End  of  the  function
a = 10
print(a) # 10
a += 1
f1()
print(a) # 12
a += 1
f2() 
print(a) # 14
# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a) # 20
def  f2():
	#print(a) #Error: cannot access local variable 'a' where it is not associated with a value
	#a += 1 #Error: cannot access local variable 'a' where it is not associated with a value

# End of the function
a = 10
print(a) # 10
f1()
a += 1
f2()
print(a)
# Find outputs (Home  work)
def  f1():
	a = 20
	#global   a #Error: name 'a' is assigned to before global declaration
	print(a) # 20
	print(globals()['a']) # 11
	a = 30
	globals()['a'] = 40
#  End  of  f1()   function
a = 10
print(a) # 10
a += 1
f1()
print(a) #40
#  Find   outputs
def   f1():
	#x = x + 5 # Error: cannot access local variable 'x' where it is not associated with a value
	pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5
	print(x) # 15
# End of f2  function
x = 10
f1()
f2()
print(x) # 10

#  Find  outputs  (Home  work)
def  change(b):
	b . append(25)
	b[2] = 17
	del  b[1]
# End  of  the  function
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
change(a) 
print(a) # [10, 17, 18, 25]

# Find  outputs  (Home  work)
def  change(b):
	b  = [50 , 60 , 70 , 80]
	print(b) # [50 , 60 , 70 , 80]
# End  of  the  function
a = [10 , 20 , 30 , 40]
print(a) # [10 , 20 , 30 , 40]
change(a)
print(a) # [10 , 20 , 30 , 40]
#  Find  outputs  (Home  work)
def   f1(x):
	x = 20
	print(x) # 20
# End  of   the   function
x = 10
print(x) # 10
f1(x)
print(x) # 10
#  Find  outputs  (Home  work)
def  f1(b):
	#b[2] = 25 #Error: 'tuple' object does not support item assignment
	pass
#end  of  the  function
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
f1(a)
print(a) # (10 , 20 , 15 , 18)

# Find  outputs (Home  work)
square = lambda  x = 10  :   x * x
print(square(5)) # 25
print(square()) # 100
# Find  output (Home  work)
add = lambda a=1, b=2: a + b #How  to  define  lambda  function   to  return  sum   of  two  arguments
print(type(add))  # <class 'function'>
print(add(10, 20))  # 30
print(add(10.6, 20.8))  # 31.4
print(add('Hyder', 'abad'))  # Hyderabad
print(add(True, False))  # 1 (True=1, False=0)
print(add(25, 10.8))  # 35.8
print(add(3+4j, 5+6j))  # (8+10j)
print(add(10, '20'))  # Error: unsupported operand types
print(add())  # 3 (default: 1 + 2)
print(add)  # <function object>

#  Find  outputs (Home work)
print((lambda x, y: x + y)(10, 20))  # 30
print((lambda x, y: x + y)(10.8, 20.6))  # 31.4
print((lambda x, y: x + y)('Hyder', 'abad'))  # Hyderabad
print(lambda x, y: x + y ('Hyder', 'abad'))  # Error (missing parentheses)

#  Find  outputs (Home  work)

large = lambda a, b: a if a > b else b #How  to  define  lambda  to  detrmine  largest  of  two  arguments
print(large(10, 20))  # 20
print(large(10.7, 5.6))  # 10.7
print(large('g', 's'))  # 's' (lexical comparison)
print(large('Rama', 'Rajesh'))  # 'Rama' < 'Rajesh' → 'Rajesh'
print(large(True, False))  # True (1 > 0)

#Find  outputs (Home  work)
power = lambda a=3.5, b=2: a ** b
print(power(2, 3))  # 8
print(power(4.5, 4))  # 410.0625
print(power())  # 12.25 (3.5 ** 2)
print(power(9))  # 81 (9 ** 2)

# Find  outputs
all = lambda a, b: (a + b, a - b, a * b, a / b)
x = all(10, 7)
print(type(x))  # <class 'tuple'>
print(x)  # (17, 3, 70, 1.428...)
p, q, r, s = all(9, 2)
print(p, q, r, s)  # 11 7 18 4.5

#  Find  outputs
a = lambda: 'Hyd'
print(a())  # Hyd
print(a)  # <function ...>

# Find  outputs
a = lambda: print('Hyd'); print('Sec'); print('Cyb')  # Only 'Hyd' in lambda
a()  # prints: Hyd, Sec, Cyb (but 'Sec', 'Cyb' outside lambda)
# Find  outputs
a = lambda: print('Hyd'), print('Sec'), print('Cyb')
print(type(a))  # <class 'tuple'> (each print is evaluated first!)
print(a)  # (None, None, None)
# a is now a tuple — not callable!

