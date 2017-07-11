sum=0
loop_control = True
while loop_control is True:
    u = raw_input("enter a number above zero, or add zero to finish")
    sum = sum + int(u)
    if int(u) == 0:
        print "your total is", sum
        loop_control = False
    elif int(u) > 0:
        m = raw_input("enter a number above zero, or add zero to finish")
        sum = sum + int(m)
    if int(m) == 0:
        print "your total is", sum
        loop_control = False
