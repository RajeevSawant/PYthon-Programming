s = 'String'
f = 12.098

print "\nThe String to be printed is %s\n"%(s)

print "Digit = 1, Decimal Places = 2  %1.2f \n"%(f)


# WhiteSpace will be filled if u dont have enough character in that floating point number
print "Digit = 3, Decimal Places = 5  %10.5f \n"%(f)


# Use format function

print "Using the format function {x} with the addition of string {y} \n".format(x = 100.2345, y = 'Hello World')
