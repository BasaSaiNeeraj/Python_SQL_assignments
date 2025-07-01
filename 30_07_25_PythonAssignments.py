'''
Write  a  program  to  merge  two  strings  to  form  a  new  string
1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->   HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0     'H'        'V'           '' + 'H' + 'V' = 'HV'
1     'Y'         'A'           'HV' + 'Y' + 'A' =  'HVYA'
2     'D'         'M'          'HVYA' + 'D' + 'M' =  'HVYADM'
--------------------------------------------------------
1) What  action  to  be  made  when  1st  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  2nd    string  to  object  'c'

2) What  action  to  be  made  when  2nd  string  got  exhausted ?  --->  Concatenate  remaining  chars  of  1st  string  to  object  'c'

3) Hint:  Use  while  loop  and  slice (outside)
'''
a=input("enter the string:")
b=input("enter the string:")
c=""
i=0
while i < len(a) and i < len(b):
    c += a[i] + b[i]
    i += 1
c += a[i:] + b[i:]
print(c)


#2
'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
    What  is  the  output ? --->  RAM<space>O

2) out = '' + 'R' + 'A' + 'M' + ' ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																						Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->  Ignore  the  character

5) Hint:  Use  not  in   operator
'''

k,c=input("enter the string:"),""
for i in range(len(k)):
    if k[i] not in c:
        c=c+k[i]
print(c)

#3
# len()  function  demo  program  (Home  work)
print(len('Hyd'))  #  3
print(len('Rama Rao'))#8
print(len('9247'))#4
print(len('+-$'))#3
print(len(''))#0
print(len(' '))#1
print(len('A2#'))#3
#print(len(3456))#error
#print('Sec'. len())#error 'str' object has no attribute 'len'



'''
What  does  len(str)  do  ?  --->  Returns  number  of  characters  in  the  string
'''

#4
# chr()  function  demo  program
print(chr(65)) #  A   becoz  65  is  unicode  value  of  'A'
print(chr(90))#Z
print(chr(97))#a
print(chr(122))#z
print(chr(48))#0
print(chr(57))#9
print(chr(36))#$
print(chr(32))#<space>


#5
# ord()  function  demo  program
print(ord('A'))  #  Unicode  value  of  'A'  i.e.  65
print(ord('Z'))#90
print(ord('a'))#97
print(ord('z'))#122
print(ord('0'))#48
print(ord('9'))#57
print(ord('$'))#36
print(ord(' '))#32

#6
'''
Let  input  be  A4M3Z5D2

What  is  the  output ?  --->  AEMPZ_DF

 0     1     2     3    4    5    6     7
 A    4     M    3    Z    5    D     2


Iteration        i       a[i]      a[i + 1]         out
--------------------------------------------------------------------------------
                                                              ''
     1               0       'A'         '4'             '' + 'A' + 'E' = 'AE'

	 2              2       'M'         '3'             'AE' + 'M' + 'P' = 'AEMP'

	 3              4       'Z'         '5'             'AEMP' + 'Z' + '' = 'AEMPZ'

	 4              6       'D'         '2'             'AEMPZ_' + 'D' +'F' = 'AEMPZ_DF'
-----------------------------------------------------------------------------------
Hint: Use  chr()  and  ord()  functions
'''

k=input("enter the string with numbers:")
l=""
if len(k)%2!=0:
    print("the length must be even")
else:
    for i in range(0,len(k),2):
        l+=k[i]+chr(ord(k[i])+int(k[i+1]))
    print(l)


#1
k= input("enter the string:")
vowels='AEIOU'
c=""
for i in k:
    i=i.upper()
    if i in vowels and i not in c:
        c=c+i
print(c)


#2
'''
Modify  following  program  with  walrus  operator

Hint:  Combine  lines  7 , 8  and  10  to  a  single  line  with  walrus  operator
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index=-1
while  (index:=a.find('Hyd',index+1)) != -1:
	print(index)
print('End')

#3
'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')
	while  index != -1:
		print(index)
		index = a .index('is' , index + 1)
	print('End')
except ValueError:
	print("substring not found")

'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error  when  string  is  not  found  (but  not  -1)

Syntax  is  same  as   find()  method
'''

#4
'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a.rfind('is')
while  index != -1:
	print(index)
	index = a.rfind('is',0,index)
print('End')

#5
'''
(Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
try:
	index = a . rindex('is')
	while  index != -1:
		print(index)
		index = a . rindex('is',0 , index )
	print('End')
except ValueError:
	pass

#6
#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))#4
print(a . count('is' , 19 , 48))#3
print(a . count('was'))#0
#7
#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'

print(a . count(' '))#3
print(a . count('\t'))#3
print(a . count('\n'))#3

#8
'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
k=input("enter the string:")
if len(k)>0:
    first=k[0]
    result=first+k[1:].replace(first,'*')
print(result)

#9
#  Find  outputs  (Home  work)
a = '15:36:48'
print(a . split(':'))
print(a)#'15:36:48'

#10
# Find  outputs  (Home  work)
a = 'Hyd\nis green\tcity'
print(a . split(' '))#['Hyd\nis', 'green\tcity']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split('green'))#['Hyd\nis ', '\tcity']
print(a . split(''))#empty seperator

#11
# Find  outputs  (Home  work)
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t'))#['Hyd', 'is', 'green', 'city']
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd\tis\tgreen\tcity']

#12
# Find  outputs (Home  work)
a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())#['Hyd', 'is', 'green', 'city']
print(a . split(' '))#['Hyd', '', '', 'is', '', '', 'green', '', '', 'city']

#13
# Find  outputs  (Home  work)
a = 'www.gmail.com'
print(a . split('.'))#['www','gmail','com']


#14
'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be  3+2+4+5+6+21+4+5+8+12.....
Print  the  sum  result

Hint:  Use  split()  method
'''
k=input("enter the input:").split('+')
sum=0
for i in range(len(k)):
    sum=sum+eval(k[i])
print(sum)

#15
#  Find  outputs  (Home  work)
a = ['15' , '36' , '48']
print(':' . join(a))#15:36:48

b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b))#Hyd is green city

c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c))#25,10,52,15,20

d = ['www' , 'gmail', 'com']
print('.' . join(d))#www.gmail.com

e = [15 , 36 , 48]
#print(':' . join(e))all are integer values

f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f))#SankarDayalSarma

g = range(5)
print('-' . join(g))#error

#16
# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))#true
print(a . endswith('town'))#False
print(a . endswith('green' , 3 , 12))#True
print(a . endswith('green' , 3 , 13))#False
print(a . endswith(' ' , 3 , 13))#True

#17
'''
Write  a  program  to  append  'ing'  to  input  string.
Append  'ly'  to  the  string  if  the  string  already  ends  with  'ing'.
Leave  the  string  unchanged  if  string  has  lessthan  three  characters

1) What  is  the  output  if  input  is  'interest' ?  --->  interesting

2) What  is  the  output  if  input  is  'interesting' ? --->  interestingly

3) What  is  the  output  if  input  is  Hi ?  --->  Hi  itself

4) Hint:  Use  endswith()  method
'''
k=input("enter the input:")
if len(k)<3:
    print(k)
elif k.endswith("ing"):
    result=k+"ly"
    print(result)
else:
    result=k+'ing'
    print(result)

#18
#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #   True
print('Rama  Rao'  . isalpha()) #  False  due  to  space
print('Hyd4'  . isalpha())#True
print('Hyd$'  . isalpha())#FAlse
print('9247'  .  isalpha())#Flase
print('+-$'    .  isalpha())#False
print('A2#'  .   isalpha())#False
print(''  .  isalpha())#False
print(' '  .  isalpha())#false

#19
# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #   True
print('92a47' . isdigit())  #  False  due  to  'a'
print('92$47' . isdigit())#False
print('Hyd' . isdigit())#False
print('+-$' . isdigit())#False
print('A2#' . isdigit())#False
print('' . isdigit())#flase
print(' ' . isdigit())#False
#print(9247 . isdigit())#ERROR method not define




'''
isdigit()  method
--------------------
1) When  does  it  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  alphabet  (or) special  character
																					   (or)
															  When  there  are  no  digits  in  the  string
'''

#20
# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  becoz  there  are  no  lowercase  alphabets
print('9247' . isupper())#false
print('RAMA  RAO' . isupper())#TRUE
print('+-$' . isupper())#False
print('HYD123' . isupper())#TRUE
print('HYD+-$' . isupper())#TRUE
print('' . isupper())#False
print('A2#' . isupper())#True

#21
# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True  becoz  there  are  no  uppercase  alphabets
print('9247' . islower())#False
print('rama  rao' . islower())#True
print('+-$' . islower())#False
print('hyd+-$' . islower())#True
print('abc123' . islower())#True
print('' . islower())#False
print('a2#' . islower())#True

#22
# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  becoz  there are  no  special  chars
print('+-$' . isalnum())#False
print('hyd' . isalnum())#true
print('hYd' . isalnum())#true
print('9247' . isalnum())#true
print('' . isalnum())#false
print('A7g9'  . isalnum())#true    

#1
# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())#False
print('\n  \t' . isspace())#True
print('\n  7\t' . isspace())#False
print('\n' . isspace())#True
print('\n  $\t' . isspace())#False
print('\t' . isspace())#true
print('' . isspace())#false
print(' ' . isspace())#true
#2
# Find  outputs  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print('a  :  {}  \t  b  :  {}  \t  c  :  {}  '  .  format(a , b , c))#a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {0}  \t  b  :  {1}  \t  c  :  {2}  ' . format(a , b , c))#a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {2}  \t  b  :  {1}  \t  c  :  {0}  ' . format(a , b , c))#a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {2}  \t  b  :  {2}  \t  c  :  {2}  ' . format(a , b , c))#a  :  Hyd  	  b  :  Hyd  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(x = a , y = b , z = c))#a  :  25  	  b  :  10.8  	  c  :  Hyd
print('a  :  {x}  \t  b  :  {y}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  Hyd  	  b  :  10.8  	  c  :  25
print('a  :  {z}  \t  b  :  {z}  \t  c  :  {z}  ' . format(z = a , y = b , x = c))#a  :  25  	  b  :  25  	  c  :  25

#3
'''
Write  a  program  to  determine  user  input  is  alphabet , digit , white space  or  special  character

1) What  are  the  three  outputs  if  input  is  'A' ?  ---> Alphanumeric  character , Alphabet character , Upper case  alphabet

2) What  are  the  three  outputs  if  input  is  'a' ?  --->  Alphanumeric  character , Alphabet character , lower case  alphabet

3) What  are  the  two  outputs  if  input  is  '7' ?  --->  Alphanumeric  character , digit  character

4) What  is  the  output  if  input  is  '$' ?  --->  Special  character

5) What  is  the  output  if  input  is  <spacebar> ?  --->  White  space

6) What  is  the  output  if  input  is  <tab>  key ?  --->   White  space

7) What  is  the  output  if  input   is   <enter>   key ?  --->  White  space

8) Hint1:  Use  isalnum() , isalpha() , isupper() , islower() , isdigit()   and  isspace()  methods

9) Hint2:  Use  nested  if  and   elif
'''
a=input("enter the no:")
if len(a)==1:
    if a.isalnum():
        print("Alphanumeric  character")
        if a.isalpha():
            print("Alphabet character")
            if a.isupper():
                print("Upper case  alphabet")
            elif a.islower():
                print("lower case  alphabet")
        elif a.isdigit():
            print("Digit character")
    elif a.isspace():
        print("White  space")
    else:
        print("special character")
else:
    print("enter only one input")

#4
'''
Write  a  program  to  reverse  a  string  without  slice

1) Let  input  be   Hyd
    What  is  the  output ?  ---> dyH

2)   H       y      d
      -3     -2     -1

      i       a[-i]            b
    ---------------------------------------
                                ''
     1         'd'            '' + 'd' = 'd'
     2         'y'            'd' + 'y' = 'dy'
     3         'H'            'dy' + 'H' = 'dyH'
  ---------------------------------------------
'''

k=input("enter the string:")
sum=''
for i in range(1,len(k)+1):
    sum+=k[-i]
print(sum)

#5
'''
Write  a  program  to  reverse  order  of  words  in  the  sentence  without  slice

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> city   green   is   Hyd

2) What  is  the  result  of  input . split() ?  --->  ['Hyd' , 'is' , 'green' , 'city']   --->   Assume  that  it  is  'b'

3) i        b[-i]           c
   ---------------------------------------------
                              ''
    1         'city'       '' + 'city' + ' ' =  'city '
    2         'green'    'city ' + 'green' + ' ' =  'city green '
    3         'is'           'city green ' + 'is' + ' ' = 'city green is '
    4         'Hyd'       'city green is ' + 'Hyd' + ' ' = 'city green is Hyd '
   --------------------------------------------------------
'''
k= input("input:")
b=k.split()
sum=''
for i in range(1,len(b)+1):
    sum+=b[-i]+' '
print(sum)

#6
'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
k= input("input:")
b=k.split()
sum=''
for i in b:
    sum=sum+i[::-1]+" "
print(sum)

#7
'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS

Hint:  Use   sorted()  function  and   join()  method
'''

k=input("enter the string:")
b="".join(sorted(k))

#8
'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  ---> ADKPZ13579

1) Hint:  sorted()  function , isalpha() , isdigit()  and   join()  method
'''
k=input("enter the string:")
sum=''
m=''
for i in range(len(k)):
    if k[i].isalpha():
        sum=sum+k[i]
    elif k[i].isdigit():
        m=m+k[i]
    else:
        print("enter only alpha and numeric:")
o=sorted(sum)+sorted(m)
r="".join(o)
print(r)

#9
a = input('Enter  list  :  ')#1
print(type(a))#<class'string'>
print(a)#1
b = eval(a)
print(b)#1
print(type(b))#<class'int'>

#10
#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a
print(a  is  b)#true
print(a  ==  b)#true
b[2] = 12
print(a)#[10, 20, 12, 18]

#11
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
b = [100 , 200 , 150]
print(a + b)#[10,20,15,18,100,200,150
#print(a + 5)#error
#print(a + '5')#error
#print([10 , 20] + (30 , 40))#error only list to list not tuple to list

#12
# Find  outputs
list = [25 , 10.8 , 'Hyd' ,  True]
a , *b , c = list  #  Unpacks  list  into  3  elements
print('a : ' , a) #  a :  25
print('b : ' , b)#   b : [10.8 , 'Hyd']
print('c : ' , c) #  c : True
print(type(b))#  <class  'list'>
x , *y = list
print('x : ' , x)#25
print('y : ' , y)#[10.8,hyd,True]
*p , q = list
print('p : ' , p)#[25, 10.8, 'Hyd']
print('q : ' , q)#True

#13
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , c , d , e = list#list error not enough tp unpack
#a , b , *c , d , e = list error not enough tp unpack
print('a : ' , a)#25
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
print('e : ' , e)
a , b , *c , d , e , f = list

#14
# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
a , b , _  , d = list
print('a : ' , a)#25
print('b : ' , b)#10.8
print('_ :  ' , _)#Hyd
print('d : ' , d)#True

#15
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b , a , d , a = list
print('a : ' , a)#3+4j
print('b : ' , b)#10.8
print('d : ' , d)#True

#16
# Find  outputs (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , b ,  _ , d , _  = list
print('a : ' , a)#25
print('b : ' , b)#10.8
print('_ : ' , _)#3+4j
print('d : ' , d)#True
print('_: ' , _)#3+4j

#17
# Identify  error (Home  work)
list = [25 , 10.8 , 'Hyd' , True , 3 + 4j]
a , *b , c , *d , e  = list# multiple stars

#18
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
a , b , c = list
print('a :  ' , a)#[25 , 10.8]
print('b :  ' , b)#'Hyd'
print('c :  ' , c)#True

#19
# Find  outputs  (Home  work)
list = [[25 , 10.8] , 'Hyd' , True]
[a , b] , c , d = list
print('a : ' , a)
print('b : ' , b)
print('c : ' , c)
print('d : ' , d)
a , b , c , d = list

#20
# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b)#true
print(a  is   b)#False
print(a < c)#True
print(a > d)#True
print(a >= c)#False
print(a <= d)#False
print(a != c)#True
print(a != b)#False
print(a == c)#False

#21
# Comparing  Lists  (Home  work)
a = [10 , 20 , 15 , 18]
b = [20 , 18 , 15 , 10]
print(a == b)#False
print(a  is   b)#False

#22
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3

#23
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#8+10j
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#39.8+4j
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error str is not supported

#24
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a))#error
print(sum(a[0]))#63
print(sum(x for x in a[0]))#63

#25
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#vamsi
print(min(b))#Amar
c = [25 , 10.8 ,  3 + 4j , True]
#print(max(c))#not supported
d = [25 , '35']
#print(max(d))#error not supported
#print(max([]))#error argument is empty
#print(min([]))#error argument is empty

#26
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10, 20, 15, 18]
print(type(b))#<class 'list'>
print(a  is  b)#False
print(a == b)#False

#27
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4, 6, 8]
print(type(b))#<class 'list'>
a = list('Vamsi')
print(a)#['V', 'a', 'm', 's', 'i']
a = list()
print(a)#[]
#print(list(25))#int object is not interable
#print(list(10.8))#int object is not interable
#print(list(True))#bool object is not interable
#print(list(None))#bool object is not interable

#28
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10, 20), (30, 40, 50), (60, 70, 80, 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(30, 40, 50), (60, 70, 80, 90), (10, 20)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[[10, 20], (30, 40), {50, 60}]

#29
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar', 'Kiran', 'Rajesh', 'Rama', 'Rama  Rao', 'Sita', 'Vamsi']
c = sorted(a , reverse = True)
print(c)#['Vamsi', 'Sita', 'Rama  Rao', 'Rama', 'Rajesh', 'Kiran', 'Amar']
['
print(a)#['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

#30
# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#True

#31
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False

#1
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . append(19)
print(list)#[10 , 20 , 15 , 18,19]

#2
#  Find  outputs (Home  work)
list = []
print(list)#[]
list . append(25)
list . append(10.8)
list . append('Hyd')
list . append(True)
print(list)#[25, 10.8, 'Hyd', True]

#3
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)#[0, 10, 20, 30, 40]

#4
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])

#5
#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)#[10,20,[50,60,70],30,40]
print(len(a))
print(a[2])
print(a[2][0])
print(a[2][1])
print(a[2][2])

# clear() method  demo program  (Home  work)
'''
list = [10 , 20 , 15 , 18]
print(list) # [10,20,15,18]
list . clear() 
print(list) # []
'''

# reverse()  method  demo  program (Home  work)
'''
a = [10 , 20 , 15 , 18]
print(a) # [10,20,15,18]
a . reverse()
print(a) # [18,15,20,10]
'''

#  sort()  method  demo  program (Home  work)
'''
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10,20,15,18,5]
list . sort()
print(list) # [5,10,15,18,20]
list . sort(reverse = True)
print(list) # [20,18,15,10,5]
'''

# Find  outputs (Home  work)
'''
a = ['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a.sort()
print(a) # ['Amar' , 'Kiran' , 'Rajesh' ,  'Rama' ,  'Rama Rao' , 'Sita' , 'Vamsi']
a.sort(reverse = True)
print(a) # ['Vamsi' , 'Sita' , 'Ramo Rao' , 'Rama' , 'Rajesh' , 'Kiran' , 'Amar']
'''

# Identify  error (Home  work)
'''
a = [25,10.8,'Hyd',True] # it does not support 'Hyd'
a.sort() 
'''

#  count()  method  demo    program (Home  work)
'''
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9
'''

# Gift

# Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
# Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
# What  is  the  output ?  ---> [15 , 14 , 18 , 19]
# Hint: Use count() and append() methods
'''
a = [10,20,15,10,14,10,18,20,19]
result = []
for x in a:
	if a.count(x) == 1:
		result.append(x)
print(result)
'''

# index()  method  demo  program  (Home  work)
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
'''
# Gift

# Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
# True  if  it  is  a  sublist  and  False  otherwise
'''
a = eval(input('enter the first list : '))
b = eval(input('enter the second list : '))
try:
	i = -1
	for x in a :
		b.index(x,i+1)
	print(True)
except:
	print(False)
'''

# copy()  method  demo program  (Home  work)
'''
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10,20,15,18]
print(a is b) # 
print(a == b) # True
c = a   
print(c)
print(a is c)
print(a == c)
d = a
print(d)
print(a is d)
print(a == d)
'''

'''
x=eval(input("enter the list"))
if len(x)==x.count((x[0])):
	print("elemnts identical")
else:
	print("elements unidentical")
'''

'''
x=eval(input("enter the list: "))
y=int(input("enter the element:"))
while x.count(y)!=0:
	x.remove(y)
print(x)
''' 

'''          
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))     #3
print(a[0])       #[10 , 20 , 30 ,  40]  
print(a[1])        #[50 , 60 ,  70 , 80]  ,  ]
print(a[2])       # [90 , 100 , 110 , 120]
print(a[0][2])  #30
print(a[1][3])  #80
print(a[2][1])  #100
'''

'''
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) #[10 , 20]
print(a[1])  # [30 , 40 , 50]
print(a[2])  # [60 , 70 , 80 , 90]
print(len(a[0])) #2
print(len(a[1])) #3
print(len(a[2])) #4
'''

'''
a=[x**3 for x in range(2,12,2)]
print(a)   #[8, 64, 216, 512, 1000]
'''

'''
a=['hyd','pune','chennai','vijayawada']
y=[]
for x  in range(len(a)):
	y+=(a[x][0]).upper()
print(y)
'''

'''
a=['hyd','pune','chennai','vijayawada','mumbai']
y=[(a[x][0]).upper() for x  in range(len(a))]
print(y)
'''

'''
a=input("enter the string : ")
x=a.split(" ")
y=[]
z=[]
for i in range(len(x)):
	y=[x[i].upper(),len(x[i])]
	z.append(y)
print(z)
'''

'''
a=input("enter the string : ")
x=a.split(" ")
z=[[x[i].upper(),len(x[i])] for i in range(len(x))]
print(z)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[]
for i in range(num):
	y+=[a[i]+b[i]]
print(y)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[a[i]+b[i] for i in range(num)]
print(y)
'''

'''
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[]
for i in range((x)):
	out=[[0]*y]*x
print(out)
'''

'''
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[[[0]*y] for i in range((x))]
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for x in range(len(a)):
	if a[x] not in b:
		out.append(a[x])
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
out=[(a[x]) for x in range(len(a)) if a[x] not in b]
print(out)
'''

'''
a=[i for i in range(1,21) if i%2==0]
print(a)
'''

'''
a=[i for i in range(2,21,2) ]
print(a)
'''

'''
a=[i**2 for i in range(1,21) if i%2==0 ]
print(a)
'''

'''
a=[i**2 for i in range(2,21,2) ]
print(a)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for i in range(len(a)):
	for x in range(len(b)):
		out+=[a[i]+b[x]]
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''

'''
a=(input("enter the string 1: "))
b=(input("enter the string 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''

'''
x=(input("enter the list"))
z=[]
for x in (x):
	z.append(x)
print(z)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[x for x in a for y in x]
print(b)
 output
 [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
'''

'''
a=[[j for j in range (i)] for i in range(5)]
print(a)
output
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
print(a)
for x in a:
	print(x)
for x in a:
	for i in x:
		print(i)
'''

'''
a=[[10,20],[30,40],[50,60],[70,80]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
output
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
'''

'''
a=[[10,20,30],[40,50,60],[70,80,90]]
for x in a:
	print(x)
print()
for x,y ,z in a:
	print(x,y,z,sep='...')
output
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
'''

'''
a=[[]]
print(a[0])
print(F'{a[0]}')
'''

'''
a=[[0,'Rama',1000.0],[20,'Sita',2000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[5,'Amar',5000.0]]
print(sorted(a))
print(sorted(a,reverse=True))
print(a)
output:
[[0, 'Rama', 1000.0], [5, 'Amar', 5000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [5, 'Amar', 5000.0], [0, 'Rama', 1000.0]]
[[0, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[]
for x in a:
	list.extend(x)
print(list)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[list.extend(x) for x in a]
print(list)
'''

'''
a=[10,20,15,18]
b=a.copy()
print(b)
print(a is b)
print(a == b)
c=a[:]
print(c)
print(a is c)
print(a == c)
d=a
print(d)
print(a is d)
print(a == d)
#output:
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
True
True
'''

'''
a=eval(input("enter the list:"))
cont=0
b=set(a)
for x in b:
	freq =a.count(x)
	if freq>cont:
		cont =freq
		mode=x
print("mode:",mode)
'''

'''
try:
	a=eval(input("enter the list 1:"))
	b=eval(input("enter the list 2:"))
	i=-1
	for x in a:
		i=b.index(x,i+1)
	print(True)
except:
	print(False)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
i=0
for i in range(len(a[i])):
	for j in range(len(a[i])):
		print(a[i][j],end='\t')
	print()
'''

'''
a=eval(input("enter the list 1:"))
print("mode:", max(a, key = a.count))
'''
# clear() method  demo program  (Home  work)
'''
list = [10 , 20 , 15 , 18]
print(list) # [10,20,15,18]
list . clear() 
print(list) # []
'''

# reverse()  method  demo  program (Home  work)
'''
a = [10 , 20 , 15 , 18]
print(a) # [10,20,15,18]
a . reverse()
print(a) # [18,15,20,10]
'''

#  sort()  method  demo  program (Home  work)
'''
list = [10 , 20 , 15 , 18 , 5]
print(list) # [10,20,15,18,5]
list . sort()
print(list) # [5,10,15,18,20]
list . sort(reverse = True)
print(list) # [20,18,15,10,5]
'''

# Find  outputs (Home  work)
'''
a = ['Rama','Rajesh','Amar','Sita','Vamsi','Kiran','Rama Rao']
print(a) # ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a.sort()
print(a) # ['Amar' , 'Kiran' , 'Rajesh' ,  'Rama' ,  'Rama Rao' , 'Sita' , 'Vamsi']
a.sort(reverse = True)
print(a) # ['Vamsi' , 'Sita' , 'Ramo Rao' , 'Rama' , 'Rajesh' , 'Kiran' , 'Amar']
'''

# Identify  error (Home  work)
'''
a = [25,10.8,'Hyd',True] # it does not support 'Hyd'
a.sort() 
'''

#  count()  method  demo    program (Home  work)
'''
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15)) # 3
print(a . count(25)) # 0
print(len(a)) # 9
'''

# Gift

# Write  a  program  to  remove  all  duplicate  elements  of  list  (Not  even  single  occurance)
# Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
# What  is  the  output ?  ---> [15 , 14 , 18 , 19]
# Hint: Use count() and append() methods
'''
a = [10,20,15,10,14,10,18,20,19]
result = []
for x in a:
	if a.count(x) == 1:
		result.append(x)
print(result)
'''

# index()  method  demo  program  (Home  work)
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
'''
# Gift

# Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
# True  if  it  is  a  sublist  and  False  otherwise
'''
a = eval(input('enter the first list : '))
b = eval(input('enter the second list : '))
try:
	i = -1
	for x in a :
		b.index(x,i+1)
	print(True)
except:
	print(False)
'''

# copy()  method  demo program  (Home  work)
'''
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) # [10,20,15,18]
print(a is b) # 
print(a == b) # True
c = a   
print(c)
print(a is c)
print(a == c)
d = a
print(d)
print(a is d)
print(a == d)
'''

'''
x=eval(input("enter the list"))
if len(x)==x.count((x[0])):
	print("elemnts identical")
else:
	print("elements unidentical")
'''

'''
x=eval(input("enter the list: "))
y=int(input("enter the element:"))
while x.count(y)!=0:
	x.remove(y)
print(x)
''' 

'''          
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))     #3
print(a[0])       #[10 , 20 , 30 ,  40]  
print(a[1])        #[50 , 60 ,  70 , 80]  ,  ]
print(a[2])       # [90 , 100 , 110 , 120]
print(a[0][2])  #30
print(a[1][3])  #80
print(a[2][1])  #100
'''

'''
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) #[10 , 20]
print(a[1])  # [30 , 40 , 50]
print(a[2])  # [60 , 70 , 80 , 90]
print(len(a[0])) #2
print(len(a[1])) #3
print(len(a[2])) #4
'''

'''
a=[x**3 for x in range(2,12,2)]
print(a)   #[8, 64, 216, 512, 1000]
'''

'''
a=['hyd','pune','chennai','vijayawada']
y=[]
for x  in range(len(a)):
	y+=(a[x][0]).upper()
print(y)
'''

'''
a=['hyd','pune','chennai','vijayawada','mumbai']
y=[(a[x][0]).upper() for x  in range(len(a))]
print(y)
'''

'''
a=input("enter the string : ")
x=a.split(" ")
y=[]
z=[]
for i in range(len(x)):
	y=[x[i].upper(),len(x[i])]
	z.append(y)
print(z)
'''

'''
a=input("enter the string : ")
x=a.split(" ")
z=[[x[i].upper(),len(x[i])] for i in range(len(x))]
print(z)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[]
for i in range(num):
	y+=[a[i]+b[i]]
print(y)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
num=min(len(a),len(b))
y=[a[i]+b[i] for i in range(num)]
print(y)
'''

'''
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[]
for i in range((x)):
	out=[[0]*y]*x
print(out)
'''

'''
x=int(input("enter the no of list: "))
y=int(input("enter the no of elemts in list: "))
out=[[[0]*y] for i in range((x))]
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for x in range(len(a)):
	if a[x] not in b:
		out.append(a[x])
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
out=[(a[x]) for x in range(len(a)) if a[x] not in b]
print(out)
'''

'''
a=[i for i in range(1,21) if i%2==0]
print(a)
'''

'''
a=[i for i in range(2,21,2) ]
print(a)
'''

'''
a=[i**2 for i in range(1,21) if i%2==0 ]
print(a)
'''

'''
a=[i**2 for i in range(2,21,2) ]
print(a)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[]
for i in range(len(a)):
	for x in range(len(b)):
		out+=[a[i]+b[x]]
print(out)
'''

'''
a=eval(input("enter the list 1: "))
b=eval(input("enter the list 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''

'''
a=(input("enter the string 1: "))
b=(input("enter the string 2: "))
out=[a[i]+b[x] for i in range(len(a)) for x in range(len(b))]
print(out)
'''

'''
x=(input("enter the list"))
z=[]
for x in (x):
	z.append(x)
print(z)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
b=[x for x in a for y in x]
print(b)
 output
 [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]
'''

'''
a=[[j for j in range (i)] for i in range(5)]
print(a)
output
[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
print(a)
for x in a:
	print(x)
for x in a:
	for i in x:
		print(i)
'''

'''
a=[[10,20],[30,40],[50,60],[70,80]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
output
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
'''

'''
a=[[10,20,30],[40,50,60],[70,80,90]]
for x in a:
	print(x)
print()
for x,y ,z in a:
	print(x,y,z,sep='...')
output
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
for x in a:
	print(x)
print()
for x,y in a:
	print(x,y,sep='...')
'''

'''
a=[[]]
print(a[0])
print(F'{a[0]}')
'''

'''
a=[[0,'Rama',1000.0],[20,'Sita',2000.0],[15,'Rajesh',3500.0],[18,'Kiran',2800.0],[5,'Amar',5000.0]]
print(sorted(a))
print(sorted(a,reverse=True))
print(a)
output:
[[0, 'Rama', 1000.0], [5, 'Amar', 5000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [5, 'Amar', 5000.0], [0, 'Rama', 1000.0]]
[[0, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[]
for x in a:
	list.extend(x)
print(list)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
list=[list.extend(x) for x in a]
print(list)
'''

'''
a=[10,20,15,18]
b=a.copy()
print(b)
print(a is b)
print(a == b)
c=a[:]
print(c)
print(a is c)
print(a == c)
d=a
print(d)
print(a is d)
print(a == d)
#output:
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
False
True
[10, 20, 15, 18]
True
True
'''

'''
a=eval(input("enter the list:"))
cont=0
b=set(a)
for x in b:
	freq =a.count(x)
	if freq>cont:
		cont =freq
		mode=x
print("mode:",mode)
'''

'''
try:
	a=eval(input("enter the list 1:"))
	b=eval(input("enter the list 2:"))
	i=-1
	for x in a:
		i=b.index(x,i+1)
	print(True)
except:
	print(False)
'''

'''
a=[[10,20],[30,40,50],[60,70,80,90]]
i=0
for i in range(len(a[i])):
	for j in range(len(a[i])):
		print(a[i][j],end='\t')
	print()
'''

'''
a=eval(input("enter the list 1:"))
print("mode:", max(a, key = a.count))
'''
#1
# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)
print(c)#{10,20}
print(type(c))#<class 'set'>
d = a - b
print(d)#{10,20}
print(type(d))#<class 'set'>
print(c  is  d)#False
print(c  ==  d)#True

#2
# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)
print(c)#{10,20,30,40}
print(type(c))#<type "class">
d = a ^ b
print(d)#{10, 50, 20, 60}
print(type(d))#<class 'set'>
print(c   is   d)#False
print(c  ==   d)#True

#3
# Find  outputs  (Home  work)
a = {x * x  for   x   in   range(10)}
print(a)#{{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
print(type(a))#<class "set">

#4
'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? --->  Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''

a=input("enter the string:")
b=set(a)
print(b)
print("".join(b))

#5
'''
List
----
insertion --->  append() , extend() , insert()
deletion  --->  pop() , remove() , clear()
modification  --->  sort() , reverse()
Access  --->  index() , count() , copy()
----------------------------------------------------
set
----
insertion --->  add() , update()
deletion  --->  pop() , remove() ,  discard() , clear()
Set  theory  --->  union() , intersection() , difference() , symmetic_difference()
Access  --->   copy()
'''

#6
'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
   What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a=input("enter the string:")
b=a.upper()
k="AEIOU"
set=set()
for i in b:
    if i in k:
        set.add(i)
print("".join(set))


#7
'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a=eval(input("ente rthe input:"))
b=set(a)
c=list(b)
print(c)

#8
'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

a,b=eval(input("enter the list 1:")),eval(input("enter the list 2:"))
c,d=set(a),set(b)
print(list(k:=c.intersection(d)))

#9
#  How  to  access  values  of  dictionary (Home  work)
a  =  {'Empno'  :  25 ,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a['Empno'])
print(a['Ename'])
print(a['Sal'])

#10
# How  to  modify  values  of  dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
print(id(a))
a['Sal']= 2000
a['Ename']='Sita'
a['Empno']=35
print(a)
print(id(a))

#11
#  How  to  append  key : value  pairs  to dictionary  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a['Gender']='M'
a['Married' ]=True
print(a)

#12
# Find  outputs (Home  work)
a = { }
a[10]='Rama'
a[20]='Sita'
a[15]='Rajesh'
a[18]='Kiran'
print(a)

#13
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
a.pop('Sal')
print(a)

#14
#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
a.pop("Sal")
print(a)

#15
#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())#TRue
print(60  in  a . keys())#False
print(60  in  a . values())#True
print(30  in  a . values())#False
print(50  in  a)#True
print(20  in  a)#False
print(70  not  in  a . keys())#false
print(40  not  in  a . values())#False
print(25  not  in  a)#true


#16
#  What  are  the  outputs  if  input  is  {10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
a = input('Enter  dictionary  :  ')
print(a)#{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a))#<class 'str'>
b = eval(a)
print(b)#{10: 'A', 20: 'D', 15: 'C'}
print(type(b))#<class 'dict'>

#17
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh' , 18 : 'Kiran'}
b = {**a}
print(b)#{10: 'Rama', 20: 'Sita', 15: 'Rajesh', 18: 'Kiran'}
print(a  is  b)#False
print(a  ==  b)#true
c = a
print(a  is   c)#true
print(a  ==  c)#True

#18
#Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
b = {18 : 'Kiran' , 14 : 'Amar' , 20  : 'Manohar'}
c = {25 : 'Ramesh' , 19 : 'Krishna' , 15 : 'Radha' , 14 : 'Srinivas'}
d = {*a , *b , *c}
print(d)#{10, 14, 15, 18, 19, 20, 25}
print(type(d))#<class 'set'>
e = {**a , **b , **c}
print(e)#{10: 'Rama', 20: 'Manohar', 15: 'Radha', 18: 'Kiran', 14: 'Srinivas', 25: 'Ramesh', 19: 'Krishna'}
print(type(e))#<class 'dict'>

#19
#  Find  outputs  (Home  work)
a = {10 : 20 , 30 : 40}
b = {30 : 50 , 10 : 60}
#print(a + b)#error
c = {**a , **b}
print(c)#{10: 60, 30: 50}
d = a | b
print(d)#{10: 60, 30: 50}


#20
'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
a=int(input("enter the no of emp:"))
b={}
for i in range(a):
    k=input("enter the empname:")
    p=int(input("enter the salary:"))
    b[k]=p
print(b)

#21
''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''

a=input("enter the list:")
b=a.split(",")
result={}
for i in b:
    key, value = i.split('=')
    key = key.strip()
    value = value.strip()
    result[key] = value
print(result)

#22
# len()  function  demo  program  (Home  work)
a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))#3
b = {}
print(len(b))#0


#23
#  sum()  function demo  program  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))#90
print(sum(a . values()))#120
print(sum(a))90
print(sum(a . items()))#error

#24
# max()  and  min()   functions  demo  program  (Home  work)
a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys()))#40
print(min(a . keys()))#7
print(max(a . values()))#50
print(min(a . values()))#5
print(max(a . items()))#(40,5)
print(min(a . items()))#(7,28)
print(max(a))#40
print(min(a))#7

#25
#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]  #  List of  tuples
b = dict(a) #  Converts  list  of  tuples  to  dict
print(b)  #  {10 : 'Hyd', 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
print(dict(e))
f = [[10] , [20] , [30]]
print(dict(f))
print(dict([10 , 20]))
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g))
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
print(dict(h))
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i))

#26
# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b)##[5, 10, 15, 18, 20]
c = sorted(a . values())
print(c)#['Blue', 'Green', 'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d)#[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True)
print(f)#[20, 18, 15, 10, 5]
print(a)#{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

#27
'''
Gift
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function

4) a = {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    b = sorted(a . items())  --->  [(5 , 'D' ) , (10 , 'A') , (12 , 'E') , (15 , 'C') , (20, 'B')]
    dict(b)  --->  {5 : 'D' , 10 : 'A' , .....}
'''

a=eval(input("enter the dict1:"))
c=sorted(a.items())
print(dict(c))

#28
#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b)#dict_keys([10, 20, 15, 18])
print(type(b))#<class 'dict_keys'>
for  x  in   b:
        print(x)

"""
10
20
15
18
"""

#29
# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))
for  x   in   b:
	print(x)

"""
Hyd
Sec
Cyb
Pune
"""

#30
#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b)#dict_items([(10, 'Hyd'), (20, 'Sec'), (15, 'Cyb'), (18, 'Pune')])
print(type(b))#<class 'dict_items'>
for  x   in   b:
        print(x)
for  x , y   in  b:
        print(x , y , sep = ' ... ')

'''
(10, 'Hyd')
(20, 'Sec')
(15, 'Cyb')
(18, 'Pune')
10 ... Hyd
20 ... Sec
15 ... Cyb
18 ... Pune
'''

#31
# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')
'''for  x , y   in  a . keys():
       print(x , y , sep = ' ... ')'''#error
'''for  x , y   in  a . values():
       print(x , y , sep = ' ... ')'''#error
'''for  x , y   in  a:
       print(x , y , sep = ' ... ')'''#error

#32
# clear()  method  demo  program (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
print(a)#{10 : 20 , 30 : 40 , 50 : 60}
a . clear()
print(a)#{}
del  a
#print(a)error

#33
# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()
print(b)
print(a  is  b)#False
print(a  ==  b)#Truue

#34
#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)#10
print(y)#20
print(z)#30
print()

x , y , z = a . values()
print(x)#Rama
print(y)#sita
print(z)#Rajesh
print()
x , y ,  z = a . items()
print(x)#(10, 'Rama')
print(y)#(20, 'Sita')
print(z)#(15, 'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1)#10 Rama
print(rno2 , sname2)#20 Sita
print(rno3 , sname3)#15 Rajesh


#35
'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  ---> {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method
'''
a=input("enter the srtring:")
b=a.upper()
for i in a:
    set = {}
    if i.isalpha():
        set[i]=set.get(i,0)+1
sorted_set=dict(sorted(set.items()))
print(sorted_set)

#36
# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)
print(b)#{'Y': 'Yellow', 'G': 'Green', 'R': 'Red', 'B': 'Blue'}
#a . update(b)#error

#37
#  Find  outputs  (Home  work)
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
#b.update(a)#error
print(b)#{}
c = [(10,) , (20,) , (30,)]
#b . update(c)#error
print(b)#{}

#38
#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}
print(d)#{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
print(type(d))#<class 'dict'>

#39
# Find outputs   (Home  work)
d = { x :  2 * x    for    x   in   range(5) }
print(d)#{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

#40
# Find outputs  (Home  work)
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)#
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)#{10: 'Rama', 18: 'Rajesh', 12: 'Rama Rao'}
