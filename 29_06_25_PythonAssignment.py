'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0 + 1.1 * 1 + 1.1 * 2 + 1.1* 3 +  ......

2) What  is  added  to  sum  in  general ?  ---> 1.1 * i   where  'i'  varies  from  1  to  n
'''
n = int(input("How many terms would you like to add   : "))

sum = 0.0
for i in range(1, n + 1):
    sum += 1.1 * i

print("Sum  :  ", sum)
o/p: How many terms would you like to add   : 5
     Sum  :   16.5

'''
Write  a  program  to  determine  sum  of  first  20  even  numbers

1) sum =  0 + 2 * 1 + 2 * 2 + 2 * 3 + .... + 2 * 20

2) What  is  added  to  sum  in  general ? ---> 2 * i   where 'i'  varies  from   1  to  20
'''
sum = 0
for i in range(1, 21):
    sum += 2 * i

print("Sum of first 20 even numbers :", sum)

o/p : Sum  of  first  20  even  numbers :   420
'''
Write  a  program  to  determine  sum  of  first  20  odd  numbers

1) sum =  0 + 2 * 1 - 1 + 2 * 2 - 1 + 2 * 3 - 1 +  ... + 2 * 20 - 1

2) What  is  added  to  sum  in  general ? --->  2 * i - 1   where 'i'  varies  from   1  to  20
'''
sum = 0
for i in range(1, 21):
    sum += 2 * i - 1

print("Sum of first 20 odd numbers :", sum)

o/p: Sum  of  first  20  odd  numbers :   400
'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n
'''
n = int(input("How many terms would you like to add   : "))

sum = 0
for i in range(1, n + 1):
    sum += i

print("Sum : ", sum)

o/p: How  many  terms  would  you  like  to  add   :  10
o/P: Sum :   55

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3
	4
	Sec
	Hello
	5
	Sec
	Hello
	6
	7
	Sec
	Hello
	Outside loop

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')
o/p: Error  if () is invalid.
     continue is invalid outside loops.
# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')	
# End  of  the  loop
print('Outside loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3
	Outside loop

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
o/p: SyntaxError: 'break' outside loop
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3
	Hyd
	Hello
	4
	Sec
	Hello
	5
	Sec
	Hello
	6
	Hyd
	Hello
	7
	Sec
	Hello
	Outside loop

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3
	4
	Sec
	Hello
	5
	Sec
	Hello
	6
	7
	Sec
	Hello
	else suite
	Outside loop

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3
	Outside loop

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')
o/p:    1
	Sec
	Hello
	2
	Sec
	Hello
	3
	Sec
	Hello
	4
	Sec
	Hello
	5
	Sec
	Hello
	6
	Sec
	Hello
	7
	Sec
	Hello
	else suite
	Outside loop

'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Note:  Do  not  use  index()  method

Let  list  be   [10 , 20 , 15 , 12 , 18]

lst = [10, 20, 15, 12, 18]
x = int(input("Enter value to search: "))

found = False
for i in range(len(lst)):
    if lst[i] == x:
        print("Found at index", i)
        found = True
        break
if not found:
    print("Not found")
																	  don't   search  in  rest  of  the  list

5) W…
#  Walrus   operator (:=)  demo  program
print(a := 25) # valid
print(a = 25) # Error 
print(a) # 25
print(a := 6 + 7) # valid
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
print((a = 6) + 7) # Error
# Find  outputs  (Home  work)
a = 0
if a == 0:
    print('Hyd')          # o/p: Hyd

if (b := 0):              # Assigns b=0, condition is False
    print('Hyd')
else:
    print('Sec :', b)     # Output: Sec : 0

if c = 0:                 # Error invalid assignment in if
    print('Hyd')

# Find  outputs
b = 10
a = b += 5  # SyntaxError: cannot assign to assignment
print(a)
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
'''
sum = 0
count = 0

while True:
    val = input("Enter input (-1 to stop)  : ")
    if val == '-1':
        break
    sum += eval(val)
    count += 1

if count > 0:
    print("Average : ", sum / count)
else:
    print("No values entered.")
i/p:    25
	10.8
	True
	46.2
	False
	92
	-1

o/p:    Average :   29.166666666666668

#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a 
print(a) # Error
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a # ref a is lost
print(b , c) # 25 25
print(a) # Error 
del   b # ref b is lost
print(c) # 25
print(b) # Error
del   c # ref c is lost
print(c) # Error
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 'Hyd'
del   a , b , c
print(a) # Error becoz  ref a is lost
print(b) # Error becoz  ref b is lost
print(c) # Error becoz  ref c is lost
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2] # [10 , 20 , 18]
print(a) # [10 , 20 , 18]
del  a # list is del
print(a) # Error ref a is gone
print(a[0]) # Error ref is gone
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] # can't modify Error
del  a # deletes whole tuple
print(a) # Error becoz ref is deleted
print(a[0]) # Error no ref

#search for an element in list without in operator
lst=[10,20,15,12,18,15,19,14,15,14]
x = 15
count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(f'{x} is {i}')
        count += 1
if count>0:
    print(f'{x} is found {count}')
else:
    print(f'{x} is not found')           
'''o/p: 15 is 2
        15 is 5
        15 is 8
        15 is found 3''' 
#modify  prgm with walrus 
try:
    sum = ctr = 0
    while (x := eval(input('Enter input (-1 to stop): '))) != -1:
        sum += x
        ctr += 1
    print('Avg:', sum / ctr)
except ZeroDivisionError:
    print('At least one valid input is required.')
except (NameError, TypeError, SyntaxError):
    print('Input cannot be a string or invalid expression.')
        

#find the Largest cmd line input
import sys
try:
    if len(sys.argv)<2:
        print('Please send inputs:')
    else:
        a = [eval(i) for i in sys.argv[1:]]
        print('Largest input:',max(a))
except(ValueError,TypeError):
    print('Inputs cannot be mix of nos and strings')      

'''o/p: python 05_03_25_PracticePython.py 10 20 30.8 7 40 35.6
        Largest input: 40         '''


#check if cmd line input even or odd
import sys
try:
    if len(sys.argv)<2:
        print('Please send inputs:')
    else:
        n = int(sys.argv[1])
        print('Even no' if n%2==0 else 'odd no')
except ValueError:
    print('Please send integer:')

'''o/p:  py 05_03_25_PracticePython.py 60
         Even no         '''

#calculate avg of cmd line 
import sys
try:
    if len(sys.argv)<2:
        print('Please send no')
    else:
        a = [eval(i) for i in sys.argv[1:]]    
        print('Avg',sum(a)/len(a))
except (ValueError,TypeError):
    print('Please send no input:')        

'''o/p:  py 05_03_25_PracticePython.py 10.8 25 True 14.6 19 False 7.4
         Avg 11.114285714285716       '''
#PROGRAM
'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  the  first  two  characters  of each string.
Assume  that  each  string  contains  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
CODE:
a=input("enter first input:")
b=input("enter second input:")
print(a[0:2]+b[2:6])
print(b[0:2]+a[2:4])

OUTPUT:
enter first input:Java
enter second input:Python
Jathon
Pyva


#PROGRAM
'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  contains  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
CODE:
str=input("enter first input:")
if len(str)<4:
		print("Nothing")
else:
		print(str[:2]+str[-2:])

OUTPUT:
enter first input:PYTHON
PYON
enter first input:hyd
Nothing


#PROGRAM
'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                  Character  at  index  1  :  A
								                  Character  at  index  2  :  M
							                      Character  at  index  3  :  S
								                  Character  at  index  4  :  I

								                  Character  at  index  -1  :  I
								                  Character  at  index  -2  :  S
								                  Character  at  index  -3  :  M
								                  Character  at  index  -4  :  A
								                  Character  at  index  -5  :  V

Hint:  Use  two  for  loops
'''
CODE:
a = input("Enter string: ")
for i in range(len(a)):  
    print(f"Character at index {i} : {a[i]}")
print()
for i in range(-1, -len(a) - 1, -1):  
    print(f"Character at index {i} : {a[i]}")

OUTPUT:
Enter string: VAMSI
Character at index 0 : V
Character at index 1 : A
Character at index 2 : M
Character at index 3 : S
Character at index 4 : I

Character at index -1 : I
Character at index -2 : S
Character at index -3 : M
Character at index -4 : A
Character at index -5 : V


#PROGRAM
'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' ' + 'a' =  'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->  Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  ---> Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop
'''
CODE:
a = input("Enter string: ")
even = ""  
odd = ""  
for i in range(len(a)):  
    if i % 2 == 0:  
        even += a[i]
    else:  
        odd += a[i]
print("Even index characters:", even)
print("Odd index characters:", odd)

OUTPUT:
Enter string: Rama Rao
Even index characters: Rm a
Odd index characters: aaRo



'''
Let  input  be    A   4   B   3   C   2   $   5
                          0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

1) What  is  the  result  of  'A' * 4  ?  --->  'AAAA'

2) Iteration    i        a[i]       a[i + 1]          out
   -------------------------------------------------------------------------------------------------
                                                                 ''
            1         0        'A'          '4'             '' + 'A' * 4 = 'AAAA'
            2        2        'B'           '3'             'AAAA' + 'B' * 3  = 'AAAABBB'
            3        4        'C'           '2'             'AAAABBB' + 'C' * 2 = 'AAAABBBCC'
            4        6        '$'           '5'             'AAAABBBCC' + '$' * 5 = 'AAAABBBCC$$$$$'
----------------------------------------------------------------------------------------------------
What  is  the  difference  between  a[i]   and  a[i + 1] ?  ---> a[i]  is  ith  char  of  string  and  a[i + 1]  is  (i + 1)th  char  of  string
'''
CODE:
try:
   a=input("enter string:")
   for i in range(0,len(a),2):
	      print(a[i]*int(a[i+1]),end='')
   print()
except:
	print("Pls  enter  alternate  char  and  digit")

OUTPUT:
enter string: A4B3C2$5
AAAABBBCC$$$$$


# Find outputs  
print( 'green'   in   'Hyd  is  green  city') # True
print('day'   in   'Sankar  dayal  sarma') # True
print('Green'   in   'Hyd  is  green  city') # False
print('d  is'   in   'Hyd  is  green  city') # True
print('dis'   in   'Hyd  is  green  city') # False
print('iniv'   in   'Srinivas') # True
print('iniv'   not   in   'Srinivas') # False


