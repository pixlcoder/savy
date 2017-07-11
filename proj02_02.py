# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
print "the first numbers are both 1"
f = 1
m = 1
q = raw_input("do you want to start?")
if q == "yes":
    s = True
    while s == True:
        f = f + m
        m = m + f
        print f, m, "(current numbers)"
        s = False
        q = raw_input("do you want to start again?")
        if q == "yes":
            s = True
else:
    print "that's OK"
