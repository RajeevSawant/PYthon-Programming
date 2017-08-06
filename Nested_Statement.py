'''
When u create a variable in python the name is stored in namespace.

U can use globals() and locals() a build in funtion to check the current local and global variable is 
 
'''


# Local Variable 

x = 50 

def printer():
  x = 10
  print "The current value of the x: %d\n" %(x)   
  
print "\nThe value of the x: %d" %(x)
printer()




# String 
name = "This is a Global name"

def greet():
  name = "Rajeev"
  
  def hello():
    print "Hello " +name

  hello()
  print"The name is : %s\n" %(name)

print"The name is : %s" %(name) 

greet()




# Global Variable in Local function

y = 50

def modify():
  global y
  print"The value of y: %d" %(y)
  y = 17 
  print "Now the value of y: %d" %(y)

modify()
print "The final value of y: %d\n" %(y)



globals()
locals()
