# Question 1 Fibbonacci series
import timeit
from memoize import memoize                          
@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

t1 = timeit.Timer("fib(35)", "from __main__ import fib")
print t1.timeit(1)

# Question 2
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"