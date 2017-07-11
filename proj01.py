n = raw_input("enter your name: ")
a = raw_input("enter your age: ")
b = raw_input("have you had a birthday this year? ")
if a > 100:
    print n, "turned 100 in the year", 2017-int(a)+100
elif b == "yes":
    print n, "will turn 100 in the year", 2017-int(a)+100
elif b == "no":
    print n, "will turn 100 in the year", 2017-int(a)+99
