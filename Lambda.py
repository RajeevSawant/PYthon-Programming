# Use def for larger functions ,  but use lambda fro fucntions that are only going to be used once or going to have less statements.

'''
num = input("Enter the number you want the square of: ")

def square(num):
  return num*num
print "The square of {x} is {y}\n".format(x=num, y=square(num)) 



x = input("\nEnter the number: ")
squ = lambda x: x*x 
print "The square of {x} is {y}\n".format(x=x, y = squ(x))



even = input("\nEnter the number: ")
isEven = lambda even: even%2 == 0

print isEven(even)
print "\n"

'''

r = raw_input('Enter the string: \n')
#print 'The Entered string is %s'%(r)
First = lambda r: r[0]
reverse = lambda r: r[::-1]
print "The 1st character of the string is {}\n".format(First(r))
print "The Reverse of the string entered is {}".format(reverse(r))




