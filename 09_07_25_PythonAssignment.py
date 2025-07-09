# Find  outputs (Home  work)
from threading import *
def   disp():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = disp)
child . start()
child . join()
for  i  in  range(10):
	print('main  thread')
'''output:  child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
 '''	
#  Find  outputs (Home  work)
from  threading  import *
import  time
def   disp():
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
child = Thread(target = disp)
child . start()
child . join(10)
for  i  in  range(10):
	print('main  thread')
'''output:  child  thread
			child  thread
			child  thread
			child  thread
			child  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
			main  thread
'''	
'''  (Home  work)
Modify  following  program  such  that  child  thread  should  wait  for  main  thread  expiry
'''
from threading import *
import time

def main_task():
    for i in range(10):
        print('main thread')
        time.sleep(0.5)

def disp(main_thread):
    main_thread.join()  # child waits until main task thread is done
    for i in range(10):
        print('child thread')

main_thread = Thread(target=main_task)
child = Thread(target=disp, args=(main_thread,))

main_thread.start()
child.start()

# Wait for both to finish
main_thread.join()
child.join()

# Find  outputs (Home work)
from threading import *  
main = main_thread()  
name = main.name  
print(name, 'is started')    # MainThread is started
main.join()                  # RuntimeError: cannot join current thread
print(name, 'is ended')      # (This line won't execute due to the error above)

# Find  outputs (Home  work)
from threading import *
import time

def double():
    for i in range(1, 7):
        print('Double : ', 2 * i)
        time.sleep(1)  # Waits 1 second per iteration (6 seconds total)

def square():
    for i in range(1, 7):
        print('Square : ', i * i)
        time.sleep(1)  # Waits 1 second per iteration (6 seconds total)

start = time.time()

double()        # Output: Double : 2 ... Double : 12 (6 seconds total)
square()        # Output: Square : 1 ... Square : 36 (6 seconds total)

end = time.time()

print('Execution time of 2 functions : ', end - start)
# Execution time of 2 functions :  12.0 (approximately, varies slightly)

# Find  outputs  (Home  work)
from  threading  import  *
import  time
def   display():
        name = current_thread() . name
        print(name , ' is  started')
        time . sleep(3)
        print(name , ' is  ended')
print(active_count())
t1 = Thread(target = display , name = 'Child Thread 1')
t2 = Thread(target = display , name = 'Child Thread 2')
t3 = Thread(target = display , name = 'Child Thread 3')
print(active_count())
t1 . start()
t2 . start()
t3 . start()
print(active_count())
t1 . join()
t2 . join()
t3 . join()
print(active_count())
'''output:  Child Thread 1 is started
			Child Thread 2 is started
			Child Thread 3 is started
			Child Thread 1 is ended
			Child Thread 2 is ended
			Child Thread 3 is ended
'''
# is_alive()  method   demo  program
from threading import *
import time

def disp():
    name = current_thread().name
    print(name, 'is started')            # One is started / Two is started / Three is started (order may vary)
    time.sleep(3)
    print(name, 'is ended')              # One is ended / Two is ended / Three is ended (order may vary)

t1 = Thread(target=disp, name='One')
t2 = Thread(target=disp, name='Two')
t3 = Thread(target=disp, name='Three')

t1.start()
t2.start()
t3.start()

print(t1.is_alive())   # True (Thread is running)
print(t2.is_alive())   # True (Thread is running)
print(t3.is_alive())   # True (Thread is running)

t1.join()
t2.join()
t3.join()

print(t1.is_alive())   # False (Thread has finished)
print(t2.is_alive())   # False (Thread has finished)
print(t3.is_alive())   # False (Thread has finished)

# Find  outputs (Home  work)
from threading import *
import time

def disp(s):
    print('[', s, end='')       # Output: [ Hyd[ Sec[ Cyb  (Order may vary)
    time.sleep(3)
    print(']')                  # Output: ]    ]    ]        (After 3 sec, in any order)

t1 = Thread(target=disp, args=('Hyd',))
t2 = Thread(target=disp, args=('Sec',))
t3 = Thread(target=disp, args=('Cyb',))

t1.start()                      # Starts thread 1
t2.start()                      # Starts thread 2
t3.start()                      # Starts thread 3

#  Find  outputs (Home  work)
from threading import *
import time

class Account:
    def __init__(self, acno1, bal1):  
        self.acno = acno1
        self.bal = bal1

    def credit(self, amt):
        s = current_thread().name
        print(f'{s} is depositing Rs. {amt} into account {self.acno}')
        x = self.bal
        time.sleep(1)
        self.bal = x + amt

ac = Account(25, 1000.0)
print('Initial Balance : ', ac.bal)   # Initial Balance : 1000.0

t1 = Thread(target=ac.credit, args=[100], name='Rama')
t2 = Thread(target=ac.credit, args=(200,), name='Sita')

t1.start()
t2.start()

t1.join()
t2.join()

print('Final Balance : ', ac.bal)     # Error May be 1100.0 or 1200.0 or 1300.0 due to race condition

#  Find  outputs  (Home  work)
from threading import RLock

r = RLock()

r.acquire()                    # 1st acquire
print('Locked')               # Locked

r.acquire()                    # 2nd acquire (RLock allows reentrant locking)
print('Locked')               #  Locked

r.release()                    # Releases 1 lock
print('Unlocked')            #  Unlocked

r.release()                    # Releases 2nd lock
print('Unlocked')            #  Unlocked

r.release()                    #  ERROR: no lock to release now
print('End')

# Find  outputs  (Home  work)
from threading import *
l = Lock()
l.acquire()
print('Locked') # Locked
l.acquire()
print('Locked') # program hangs here and no further output
l.release()
print('Unlocked')
l.release()
print('Unlocked')
print('End')

# Find   outputs (Home  work)
from threading import *
import time
def disp():
	main_thread().join(10)                   # child thread waits up to 10 seconds for main thread
	for i in range(10):
		print('child  thread')              # prints after 10 seconds if main thread hasn't ended
child = Thread(target = disp)
child.start()
for i in range(10):
	print('main  thread')                   # main thread prints this 10 times with 2 sec delay
	time.sleep(2)

#  Find  outputs  (Home  work)
from threading import *
import time
def disp():
	main_thread().join()                      # deadlock: child waits for main to end
	for i in range(10):
		print('child  thread')
child = Thread(target = disp)
child.start()
child.join()                                  # main waits for child to finish
for i in range(10):
	print('main  thread')

'''
Modify  following  program  such  that   t1  should  execute  double()  function  and
t2  should  execute  square()  function
'''
from threading import *
import time

def double():
    for i in range(1, 7):
        print('Double :', 2 * i)
        time.sleep(1)

def square():
    for i in range(1, 7):
        print('Square :', i * i)
        time.sleep(1)

start = time.time()

t1 = Thread(target=double)
t2 = Thread(target=square)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print('Execution time of 2 functions :', end - start)
'''
-- Numeric Functions Demo Script
-- ABS: Absolute value
SELECT ABS(15) AS abs_example;

-- CEIL / CEILING: Round up
SELECT CEIL(4.3) AS ceil_example;

-- FLOOR: Round down
SELECT FLOOR(4.99) AS floor_example;

-- ROUND: Round to nearest integer or specified decimals
SELECT ROUND(4.5678) AS round_example;
SELECT ROUND(4.5648, 2) AS round_2_decimals_1, ROUND(4.5668, 2) AS round_2_decimals_2;

-- MOD: Modulo (remainder)
SELECT MOD(31, 5) AS mod_example;

-- POWER / POW: Exponentiation
SELECT POWER(2, 5) AS power_example;

-- SQRT: Square root
SELECT SQRT(50) AS sqrt_example;

-- SIGN: Sign of number (-1, 0, 1)
SELECT SIGN(-1005) AS sign_negative, SIGN(0) AS sign_zero, SIGN(15) AS sign_positive;

-- TRUNCATE: Truncate to specific decimals without rounding
SELECT TRUNCATE(4.5678, 3) AS truncate_example;

-- String Functions Demo Script

-- CONCAT
SELECT CONCAT('Hello', ' ', 'World') AS concat_example;           -- Hello World

-- SUBSTRING / SUBSTR
SELECT SUBSTRING('MySQLDatabase', 6, 4) AS substring_example;     -- Data
SELECT SUBSTR('MySQLDatabase', 6, 4) AS substr_example;           -- Data

-- LENGTH vs CHAR_LENGTH
SELECT LENGTH('Résumé') AS length_bytes;                          -- 7 (1 byte for ASCII, 2 bytes for é in UTF-8)
SELECT CHAR_LENGTH('Résumé') AS length_chars;                     -- 6 (counts characters, not bytes)

-- TRIM, LTRIM, RTRIM
SELECT TRIM('  hello world ') AS trim_example;                    -- hello world
SELECT LTRIM('  hello   ') AS ltrim_example;                      -- hello   
SELECT RTRIM('  hello  ') AS rtrim_example;                       --   hello

-- REPLACE
SELECT REPLACE('a1b1c', '1', '+') AS replace_example;             -- a+b+c

-- INSTR & LOCATE
SELECT INSTR('analyticslt', 'lt') AS instr_example;               -- 10
SELECT LOCATE('e', 'water', 2) AS locate_example;                 -- 5

-- LOWER, UPPER, LCASE, UCASE
SELECT LOWER('MySQL') AS lower_example;                           -- mysql
SELECT UPPER('MySQL') AS upper_example;                           -- MYSQL
SELECT LCASE('MySQL') AS lcase_example;                           -- mysql
SELECT UCASE('MySQL') AS ucase_example;                           -- MYSQL
'''
# Modify  following  program  such  that  final  balance  should  be  1300
from threading import *   
import time   
l = Lock()  

class Account:  
    def __init__(self, acno1, bal1):  
        self.acno = acno1  
        self.bal = bal1  

    def credit(self, amt):  
        s = current_thread().name   
        print(f'{s} is depositing Rs. {amt} into account {self.acno}')  # Rama... then Sita...
        with l:  # lock critical section
            x = self.bal  
            time.sleep(1)  # simulate delay
            self.bal = x + amt  # update balance safely

ac = Account(25, 1000.0)   
print('Initial Balance :', ac.bal)  # Initial Balance : 1000.0

t1 = Thread(target=ac.credit, name='Rama', args=(100,))   
t2 = Thread(target=ac.credit, name='Sita', args=(200,))  

t1.start()  # starts Rama thread
t2.start()  # starts Sita thread
t1.join()  # wait for Rama to complete
t2.join()  # wait for Sita to complete

print('Final balance :', ac.bal)  # Final balance : 1300.0

#  Find  outputs (Home  work)
from threading import *
import time
def   f1():
        sem . acquire()
        name = current_thread() . name
        print(name , 'is   under   execution')
        time . sleep(1)
        print(name , 'finished  execution')
        sem . release()
sem = Semaphore(3)
t1 = Thread(target = f1 , name = 'One')
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t4 = Thread(target = f1 , name = 'Four')
t5 = Thread(target = f1 , name = 'Five')
t6 = Thread(target = f1 , name = 'Six')
t7 = Thread(target = f1 , name = 'Seven')
t8 = Thread(target = f1 , name = 'Eight')
t9 = Thread(target = f1 , name = 'Nine')
t1 . start()
t2 . start()
t3 . start()
t4 . start()
t5 . start()
t6 . start()
t7 . start()
t8 . start()
t9 . start()
'''output:  One is   under   execution
			Two is   under   execution
			Three is   under   execution
			One finished  execution
			Four is   under   execution
			Two finished  execution
			Five is   under   execution
			Three finished  execution
			Six is   under   execution
			Four finished  execution
			Seven is   under   execution
			Five finished  execution
			Eight is   under   execution
			Six finished  execution
			Nine is   under   execution
			Seven finished  execution
			Eight finished  execution
            Nine finished  execution
'''
#  Find  outputs
from threading import *  
import time  
def fact(n):  
	sem.acquire()  # acquires a semaphore permit  
	if n > 0:  
		x = n * fact(n - 1)  
	else:  
		x = 1  
	sem.release()  # releases the permit  
	return x  
# end of the function  
def disp(n):  
	print(n , '!=' , fact(n))  # 4 != 24 or 7 != 5040 (order may vary due to thread execution)  
sem = Semaphore(8)  
t1 = Thread(target=disp, args=(4,))  
t2 = Thread(target=disp, args=(7,))  
t1.start()  # starts thread t1  
t2.start()  # starts thread t2  

# Possible outputs:
# 4 != 24  
# 7 != 5040  
# (or)
# 7 != 5040  
# 4 != 24  

#  Find  outputs  (Home  work)
from queue import Queue
from threading import *
q = Queue()

for i in [10, 20, 30, 40, 50]: q.put(i)  # inserts 10,20,30,40,50 into queue

print('Deleted elements')  # Deleted elements

while not q.empty(): print(q.get())  # 10 20 30 40 50

print(active_count())  # 1 (only main thread is running)

print(q.get())  # blocks forever or raises exception if queue is empty (program hangs here)

print('End')  # won't be reached if above line blocks

#  Find  outputs  (Home  work)
from queue import LifoQueue
stack = LifoQueue()

for i in [10, 20, 30, 40, 50]: stack.put(i)  #inserts 10,20,30,40,50 into stack

print('Deleted elements')  #Deleted elements

while not stack.empty(): print(stack.get())  #50 40 30 20 10

print(stack.get())  #blocks forever or raises exception (program hangs here)

print('End')  #won't be reached due to blocking get()

#  Find  outputs  (Home  work)
from queue import PriorityQueue
pq = PriorityQueue()
for i in [10, 20, 30, 40, 50]: pq.put(i)  #insert 10, 20, 30, 40, 50 into pq
print('Deleted elements')  #Deleted elements
while not pq.empty(): print(pq.get())  #10 20 30 40 50
print('End')  #End

# Find  outputs  (Home  work)
from queue import Queue
q = Queue()
q.put(('Hyd', 10))       # inserted ('Hyd', 10)
q.put(('Delhi', 20))     # inserted ('Delhi', 20)
q.put(('Chennai', 15))   # inserted ('Chennai', 15)
q.put(('Pune', 5))       # inserted ('Pune', 5)
q.put(('Mumbai', 12))    # inserted ('Mumbai', 12)

while not q.empty(): print(q.get())  
# ('Hyd', 10)
# ('Delhi', 20)
# ('Chennai', 15)
# ('Pune', 5)
# ('Mumbai', 12)

#  Find  outputs  (Home  work)
from queue import LifoQueue
stack = LifoQueue()
stack.put(('Hyd', 10))       # inserted ('Hyd', 10)
stack.put(('Delhi', 20))     # inserted ('Delhi', 20)
stack.put(('Chennai', 15))   # inserted ('Chennai', 15)
stack.put(('Pune', 5))       # inserted ('Pune', 5)
stack.put(('Mumbai', 12))    # inserted ('Mumbai', 12)

while not stack.empty(): print(stack.get())
# ('Mumbai', 12)
# ('Pune', 5)
# ('Chennai', 15)
# ('Delhi', 20)
# ('Hyd', 10)

#  Find  outputs
from queue import PriorityQueue
pq = PriorityQueue()
pq.put(('Hyd', 10))       # inserted ('Hyd', 10)
pq.put(('Delhi', 20))     # inserted ('Delhi', 20)
pq.put(('Chennai', 15))   # inserted ('Chennai', 15)
pq.put(('Pune', 5))       # inserted ('Pune', 5)
pq.put(('Mumbai', 12))    # inserted ('Mumbai', 12)

while not pq.empty(): print(pq.get())
# ('Chennai', 15)
# ('Delhi', 20)
# ('Hyd', 10)
# ('Mumbai', 12)
# ('Pune', 5)

# Find  outputs
from  queue  import   PriorityQueue
pq = PriorityQueue()
pq . put(('Hyd' , 10))
pq . put(('Hyd' , 20))
pq . put(('Hyd' , 15))
pq . put(('Hyd' , 5))
pq . put(('Hyd' , 12))
print('Deleted tuples')
while not pq.empty():
    print(pq.get()) #How  to  remove  each  tuple  of  object  pq  until  it  is  empty
'''output:  Deleted tuples
			('Hyd', 5)
			('Hyd', 10)
			('Hyd', 12)
			('Hyd', 15)
			('Hyd', 20)
'''
'''
-- Find all employees along with their department names
SELECT e.emp_id, e.dept_id, d.dept_name
FROM emp e
LEFT JOIN dept d ON e.dept_id = d.dept_id;

-- Find employees whose department doesn't exist in dept table
SELECT e.emp_id, e.dept_id
FROM emp e
LEFT JOIN dept d ON e.dept_id = d.dept_id
WHERE d.dept_id IS NULL;

-- Find duplicate dept_ids in dept table (only for demo2)
SELECT dept_id, COUNT(*) as count
FROM dept
GROUP BY dept_id
HAVING COUNT(*) > 1;

-- Count of employees per department
SELECT e.dept_id, COUNT(*) as emp_count
FROM emp e
GROUP BY e.dept_id;
'''
#  Find  outputs  (Home  work)
from threading import *
import time
def f1():
	l1.acquire() # 1st thread locks object l1
	print('1st  thread  locks  object  l1') # 1st  thread  locks  object  l1
	time.sleep(1)
	l2.acquire() # Deadlock occurs here (t1 waits for l2, held by t2)
	print('1st  thread  is  under  execution')
	l2.release()
	l1.release()
	print('End  of  the  1st  thread')
def f2():
	l2.acquire() # 2nd thread locks object l2
	print('2nd   thread  locks  object  l2') # 2nd   thread  locks  object  l2
	time.sleep(1)
	l1.acquire() # Deadlock occurs here (t2 waits for l1, held by t1)
	print('2nd   thread  is  under  execution')
	l1.release()
	l2.release()
	print('End  of  the  2nd   thread')
l1 = Lock()
l2 = Lock()
t1 = Thread(target = f1)
t2 = Thread(target = f2)
t1.start()
t2.start()
time.sleep(1)
print('Deadlock') # Deadlock
'''
USE demo1; SELECT * FROM salesdata;

-- Optional: Rename column if special characters exist
ALTER TABLE salesdata RENAME COLUMN `ï»¿SaleID` TO saleid;

-- LEAD & LAG by saledate
SELECT saleid, salesperson, saleamount, saledate,
LEAD(saleamount, 1) OVER (ORDER BY saledate) AS lead_1,
LEAD(saleamount, 2) OVER (ORDER BY saledate) AS lead_2,
LAG(saleamount, 1) OVER (ORDER BY saledate) AS lag_1,
LAG(saleamount, 2) OVER (ORDER BY saledate) AS lag_2
FROM salesdata;

-- SELF JOIN to get consecutive sale dates
SELECT s1.*, s2.* FROM salesdata AS s1 JOIN salesdata AS s2 ON s1.saledate = DATE_SUB(s2.saledate, INTERVAL 1 DAY);

-- LEFT JOIN version
SELECT s1.*, s2.* FROM salesdata AS s1 LEFT JOIN salesdata AS s2 ON s1.saledate = DATE_SUB(s2.saledate, INTERVAL 1 DAY);

-- LEAD & LAG by salesperson
SELECT saleid, salesperson, saleamount, saledate,
LEAD(saleamount, 1) OVER (PARTITION BY salesperson ORDER BY saledate) AS lead_1,
LEAD(saleamount, 2) OVER (PARTITION BY salesperson ORDER BY saledate) AS lead_2,
LAG(saleamount, 1) OVER (PARTITION BY salesperson ORDER BY saledate) AS lag_1,
LAG(saleamount, 2) OVER (PARTITION BY salesperson ORDER BY saledate) AS lag_2
FROM salesdata;

USE employees;

-- Employees hired in 1999
SELECT emp_no FROM employees WHERE YEAR(hire_date) = 1999;

-- Salaries of employees hired in 1999
SELECT * FROM salaries WHERE emp_no IN (SELECT emp_no FROM employees WHERE YEAR(hire_date) = 1999) LIMIT 100;

-- Avg salary of employees NOT hired in 1999 using IN
SELECT emp_no, AVG(salary) AS avg_salary FROM salaries WHERE emp_no IN (SELECT emp_no FROM employees WHERE YEAR(hire_date) <> 1999) GROUP BY emp_no ORDER BY emp_no LIMIT 50;

-- Alternate using NOT IN
SELECT emp_no, AVG(salary) AS avg_salary FROM salaries WHERE emp_no NOT IN (SELECT emp_no FROM employees WHERE YEAR(hire_date) = 1999) GROUP BY emp_no ORDER BY emp_no LIMIT 50;
'''
# How  to  resolve  deadlock ?
# Resolved Deadlock by consistent lock order
from threading import *
import time

def f1():
    l1.acquire()
    time.sleep(1)
    l2.acquire()
    print('1st thread is under execution')
    l2.release()
    l1.release()
    print('End of the 1st thread')

def f2():
    l1.acquire()  # acquire in the same order as f1
    time.sleep(1)
    l2.acquire()
    print('2nd thread is under execution')
    l2.release()
    l1.release()
    print('End of the 2nd thread')

l1 = Lock()
l2 = Lock()

t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()

t1.join()
t2.join()

print('End of main thread')

'''
Producer-Consumer  problem  with  synchronization

1) Add  one  more  variable  to  buffer  object  i.e.  write  variable

2) What  does  write = True  indicate ?  --->  Thread  'p'  can  write  a  value  to  the  buffer  object
    What  does  write = False  indicate ?  --->  Thread  'p'  can  not  write  a  value  to  the  buffer  object

3) Initialize  write  = True  in  the  constructor  of  buffer  class

4) What  are  the  four  events  for  thread  'p' ?  --->  a) Write  a  value  to  buf . x  when  buf . write = True
     b) Modify  buf . write = False  becoz  thread  'p'  can  not  write  another  value  to  object  buf   immediately
	 c) Notify  thread  'c'  that  a  new  value  is  available  in  object   buf
	 d) Thread  'p'  waits  due  to  …'''
from threading import Thread, Condition
import time
import random

# Shared Buffer Class
class Buffer:
    def __init__(self):
        self.x = None               # shared data
        self.write = True           # True => producer can write, False => wait
        self.cond = Condition()     # condition for synchronization

# Producer Thread
class Producer(Thread):
    def __init__(self, buf):
        super().__init__()
        self.buf = buf

    def run(self):
        for i in range(5):
            with self.buf.cond:
                while not self.buf.write:           # wait if write is False
                    self.buf.cond.wait()
                val = random.randint(1, 100)
                self.buf.x = val                    # write to buffer
                print(f'Producer writes: {val}')
                self.buf.write = False              # prevent next write
                self.buf.cond.notify()              # notify consumer
                time.sleep(1)

# Consumer Thread
class Consumer(Thread):
    def __init__(self, buf):
        super().__init__()
        self.buf = buf

    def run(self):
        for i in range(5):
            with self.buf.cond:
                while self.buf.write:               # wait if write is True
                    self.buf.cond.wait()
                print(f'Consumer reads: {self.buf.x}')
                self.buf.write = True               # allow next write
                self.buf.cond.notify()              # notify producer
                time.sleep(1)

# Create shared buffer and start threads
buf = Buffer()
p = Producer(buf)
c = Consumer(buf)
p.start()
c.start()
p.join()
c.join()


