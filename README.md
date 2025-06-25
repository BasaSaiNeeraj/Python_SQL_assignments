# 25-06-2025
# Find  outputs (Home  work)
a = 0O6247
print(a) # converting octal 0O6247 to decimal no i.e 3239
print(type(a)) # <class'int'>
print(id(a)) # address of a
b = 0o6247 
print(id(b)) # same address as a
print(b) # 3239
c = 3239
print(c) # 3239
print(id(c)) # same address as a 
print(0o9248) # Error becoz 9 digit in octal number.

# Find  outputs  (Home  work)
a = 0XA7B9
print(a) # converting hexadecimal to decimal no i.e 42937
print(type(a)) # <class'int'>
b = 0xBEEF
print(b) # 48879
print(A7B9) # Error becoz not defined as hexadecimal before A7B9
print('A7B9') # A7B9
print(0XBEER) # Error becoz the R is there in hexa decimal it allows only from (0-F(15))
print(0XHYD) # Error becoz of Y
print(0xA7G9B) # Error becoz of G

# Find outputs (Home  work)
a = 9248 
print(a) # 9248
print(type(a)) # <class'int'>
#  Find  outputs  (Home  work)
a = "Rama Rao"
print(a) # Rama Rao
print(type(a)) # <class'str'>
print(id(a)) # address of a
b = 'Hyd'
print(b) # Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c) # Hyd is green city. <nxt line> Hyd is hitec city. <nxt line> Hyd is beautiful city.

# Index   demo  program  (Home  work)
a = 'Hyd'
print(a[0])# How  to  print  'H'  of  object  'a'
print(a[1]) # How  to  print  'y'  of  object  'a'
print(a[2]) # How  to  print  'd'  of  object  'a'
print(a[3]) # Error becoz no index 3 in a
print(a[-1]) # How  to  print  'd'  of  object  'a'  with  -ve  index
print(a[-2]) # How  to  print  'y'  of  object  'a'  with  -ve  index
print(a[-3]) # How  to  print  'H'  of  object  'a'  with  -ve  index
print(a[-4]) # Error becoz no exceeding the index count
print(a[0] ==  a[-3]) # True becoz a[0] is H and a[-3] is also H.
a[2] = 'c' # Error becoz str is immutable cannot modify
print(25[0]) # Error becoz there is no index for int datatype
print('25'[0]) # 2
print(True[1]) # Error becoz there is no index for bool datatype
print('True'[1]) # r
#  Find  outputs  (Home work)
a = 'Hyd'
print(a * 3) # HydHydHyd
print(a * 2) # HydHyd
print(a * 1) # Hyd
print(a * 0) # Empty string
print(a * -1) # Empty string
print(25 * 3) # 75
print('25' * 3) # 252525
print('25' * 4.0) # Error becoz the repeating can be done by only int datatype not float 4.0
print(3 * 'Hyd') # HydHydHyd
# len()  function  (Home  work)
print(len('Hyd')) # 3
print(len('Rama Rao')) # 7
print(len('9247')) # 4
print(len('')) # 0
print(len(' ')) # 1
print(len(689)) # Error becoz no len function for int datatype 689
# Find  outputs  (Home  work)
a = """"Hyd"""
print(a) # "Hyd
print(len(a)) # 4
print(a[0]) # "
print("""Hyd"""") # Error becoz of last "
b = """""Hyd"""
print(b) # ""Hyd
print(len(b)) # 5
# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) # Dayal
print(a[7 : ]) # Dayal Sarma
print(a[ : 6]) # Sankar
print(a[ : ]) #   a[ 0 :  18 :  1]  --->  string  from  indexes  0  to   17  in  steps  of   1   ---> Sankar  Dayal  Sarma
print(a[:  : ]) # Sankar Dayal Sarma 
print(a[1 : 10 : 2]) # akrDy
print(a[0 : : 2]) # Sna aa am
print(a[1 : : 2]) # akrDylSra
print(a[-5 : -1]) # Sarm
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  1-  to   18  in  steps  of   -1   ---> Reverse string 
print(a[-1:-5:-1]) # amra
print(a[ : : -2]) # arSlyDrka
print(a[3 : -3]) # kar Dayal Sa
print(a[2 : -5])   #  a[2 : -5 :  1]  --->  string  from  indexes  2  to  -6   in  steps  of   1   --->  nkar<space>Dayal<space>
print(a[-1:-5]) # Empty string
print(a[3 : 3]) # Empty string

#  Find  outputs  (Home  work)
a =  'A'
print(a[1]) # Error becoz no index 1 in a
print(a[1:]) # empty string

# int()  function  demo  program
print(int(10.8)) #  Converts  10.8  to  10
print(int(True))  #  Converts  True  to  1
print(int(False)) # Converts False to 0
print(int('25')) # '25' to 25
print(int(False)) # Converts False to 0
print(int('25')) # '25' to 25
print(int('0075')) # '0075' to 75
print(int(0B11010)) # 26
print(0B11010) # 26
print(int(0O6247)) # 3239
print(0O6247) # 3239
print(int(0XA7B9)) # 42937
print(0XA7B9) # 42937
#print(int(3 + 4j)) # Error becoz it is complex not int
#print(int('25.4')) # Error becoz it is float
print(int('Ten')) # Error becoz ten is not int



'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer
# float()  function  demo  program
print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False)) # Convert False to 0.0
print(float('92')) # Converts '92' to 92.0
print(float('36.4')) # Converts '36.4' to 36.4
print(float('0075')) # Converts '0075' to 75.0
print(float(0B1010101)) # Converts to float 85.0
print(float(0O6247)) # 3239.0
print(float(0XA7B9)) # 42937.0
print(float(3 + 4j)) # Error becoz complex cannot convert to float
print(float('Ten')) # Error becoz ten cannot convert to float




'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float
# complex()  function  demo  program
print(complex(3 , 4)) # 3+4j
print(complex(0 , 4)) # 4j
print(complex(3)) # 3+0j
print(complex(3.8 , 4.6)) # 3.8 + 4.6j
print(complex(3.8)) # 3.8 + 0.0j
print(complex(3 , 4.5)) # 3 + 4.5j
print(complex(True , False)) # 1 + 0j
print(complex(True)) # 1 + 0j
print(complex(False)) # 0 + 0j
print(complex(True , 4)) # 1 + 4j
print(complex('3')) # 3.0 + 0j
print(complex('3.8')) # 3.8 + 0j
#print(complex(3 , '4')) # Error becoz second arg can't be string
#print(complex('3' , 4)) # Error Can't take second arg when first arg is string
#print(complex('3' , '4')) # Error Can't take second arg when first arg is string
print(complex('Ten')) # Error becoz Ten is not commplex datatype
#  bool()  function  demo  program
print(bool(0))         # False (0 is considered False)
print(bool(10))        # True  (non-zero)
print(bool(-25))       # True  (non-zero)
print(bool(0.0))       # False
print(bool(0.1))       # True
print(bool(0 + 0j))    # False (both real and imaginary parts zero)
print(bool(10 + 20j))  # True
print(bool(-15j))      # True
print(bool('False'))   # True (non-empty string)
print(bool(''))        # False (empty string)
print(bool('Hyd'))     # True
print(bool(' '))       # True becoz space is a character
print(bool('True'))    # True



'''
bool()  function
------------------
1) What  does  bool(x)  do  ?  --->  Converts  object  'x'  to  True / False

2) Is  0  True  (or)  False ?   ---> False
    What  about  non-zero ?   ---> True

3) Is  ''(i.e.  Empty  string)  True  (or) False ?  --->  False
    What  about  non-empty  string ?  --->  True

4) When  is  x + yj  treated  as  False ?  ---> When  both  'x'  and  'y'  are  zeroes
     When  is  x + yj  treated  as True ?  --->  When  either  'x'  is   non-zero  (or)  'y'  is  non-zero
'''
# str()  function  demo  program
print(str(25))  #  Converts   25  to  '25'
print(str(10.8)) # Converts 10.8 to '10.8'
print(str(3 + 4j)) # '3+4j'
print(str(True)) # 'True'
print(str(False)) # 'False'
print(str(None)) # 'None'


'''
What  does  str(x)  do ?  --->  Converts  object  'x'  to  string
'''
# oct()  function  demo  program
print(oct(195))               # '0o303'
print(oct(0B10101110010))     # '0o1272'
print(oct(0xA7B9))            # '0o24771'


'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where  
								                    'x'  can  be  binary / decimal / hexa-decimal  number
# hex()  function  demo  program
print(hex(25))                # '0x19'
print(hex(0B10101111010111))  # '0xafd7'
print(hex(0O6247))            # '0xCAF'



'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number
# Find  outputs    (Home  work)
a = range(10 , 50 , 5)
print(type(a))         # <class 'range'>
print(a)               # range(10, 50, 5)
print(*a)              # 10 15 20 25 30 35 40 45
print(id(a))           # (some memory id)
print(len(a))          # 8
print(*a[2 : 7] , sep = ' , ')  # 20 , 25 , 30 , 35 , 40
print(*a[ : : -1])     # Empty (step -1 not valid forward)
a[4] = 32  # no assignment is allowed for range becoz it is immutable
print(a * 2) # no repeatation becoz it not resuable
#  Find  outputs  (Home  work)
a = range(10 , 20)
print(*a , sep = ',')         # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)                     # 0 1 2 3 4
c = range(10 , 1 , -1)
print(*c , sep = '...')       # 10...9...8...7...6...5...4...3...2
d = range(-10 , 0)
print(*d)                     # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)                     # Empty
f = range(2 , 2)
print(*f)                     # Empty
g = range(10 , 11 , 0.1) # Error: step must be integer
h = range('A' , 'F') # Error: 'str' object cannot be interpreted as an integer

#  Find  outputs  (Home  Work)
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(a)                  # [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Hyd' , 25]
print(*a)                 # 25 10.8 Hyd True (3+4j) None Hyd 25
print(type(a))            # <class 'list'>
print(id(a))              # Some memory ID
print(len(a))             # 8
a[2] = 'Sec'
print(a)                  # [25 , 10.8 , 'Sec' , True , 3 + 4j , None , 'Hyd' , 25]
print(a[2 : 5])           # ['Sec', True, (3+4j)]

# append()  and  remove()  methods  (Home  work)
a = [ ]
print(a) # [ ]
a . append(25) # 25 appended to empty list
a . append(10.8) # 10.8 appended to list
a . append('Hyd') # 'Hyd' appended to list
a . append(True) # True appended to list
print(a) # [25, 10.8, 'Hyd', True]
a . remove('Hyd') # 
print(a) # [25, 10.8, True]
a . remove('25')
print(a) # Error becoz no string 25 is in list there is int 25
#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd']
print(a * 3)             # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 2)             # [25 , 10.8 , 'Hyd', 25 , 10.8 , 'Hyd']
print(a * 1)             # [25 , 10.8 , 'Hyd']
print(a * 0)             # []
print(a * -1)            # []
print(a * 4.0)           # Error: can't multiply sequence by non-int of type 'float'

# list()  function  demo  program
a = list('Hyd')
print(a)                # ['H', 'y', 'd']
print(type(a))          # <class 'list'>
print(len(a))           # 3

b = (10 , 20 , 15 , 18)
print(list(b))          # [10, 20, 15, 18]

print(list(range(5)))   # [0, 1, 2, 3, 4]

print(list(25))         # Error: int is not iterable



'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list

2) Is  list(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only

3) What  does  list(No  args)  do ?  --->  Returns  an  empty  list  i.e.  []

4) Finally  list()  function  does  typecasting
'''
# Find  outputs
a = [ ]
print(type(a)) # <class'list'>
print(a) # [ ]
print(len(a)) # 0
b = list()
print(b) # []
print(len(b)) # 0
# Slice  demo  program (Home  work)
#        0      1          2         3           4         5       6          7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8      -7       -6          -5        -4       -3      -2         -1
print(list[2 : 7])           # [(3+4j), 'Hyd', True, None, 10.8]
print(list[ : : ])           # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])               # [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1])         # ['Hyd' , 10.8 , None , True , 'Hyd' , 3+4j , 10.8 , 25]
print(list[ : : 2])          # [25, (3+4j), True, 10.8]
print(list[1 : : 2])         # [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2])         # ['Hyd', None, 'Hyd', (3+4j)]
print(list[-2 : : -2])       # ['10.8', True, (3+4j), 10.8]
print(list[1 : 4])           # [10.8, (3+4j), 'Hyd']
print(list[-4 : -1])         # [True, None, 10.8]
print(list[3 : -3])          # ['Hyd', True]
print(list[2 : -5])          # [(3+4j)]
print(list[-1:-5])           # []

#  Find  outputs  (Home  work)
#        0      1         2        3          4         5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]
print('x : ' , x) # 'Hyd'
print('y : ' , y) # True
for  x  in  list[2:7]:
	print(x) # 3+4j <nxt line> 'Hyd' <nxt line> True <nxt line> None <nxt line> 10.8 
#  Find  outputs  (Home  work)
#     0    1      2     3     4
a = [10 , 20 , 30 , 40 , 50]
print(a) # [10 , 20 , 30 , 40 , 50]
a[1 : 4] = [60 , 70 , 80]
print(a) # [10, 60, 70, 80, 50]
#  Find  outputs  (Home  work)
a =  [25]
print(a[1]) # Error becoz no index 1
print(a[1:]) # Empty string
#  Find  outputs (Home  work)
list = [10 , 20 , 15 , 12 , 18]
print(15 in list)        # True
print(19 in list)        # False
print(14 not in list)    # True
print(12 not in list)    # False

'''
1) x  in   list
   What  does   in  operator  do ?  --->  Returns  True  when  'x'  is  in  the  list  and  False  otherwise

2) x  not  in   list
    What  does   not  in  operator  do ?  ---> Returns  True  when  'x'  is  not  in  the  list  and  False  otherwise
'''
--------

