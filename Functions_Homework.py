
# Question 1

def vol(rad):
  return((4.0/3)*3.14159*(rad*rad*rad))
  pass

print "\nThe Volume of the Sphere is: %1.3f\n" %(vol(3))



# Question 2

def ran_check(num,low,high):
  if num > low and num < high:
    return True
  else:
    return False
  
print "Is the Number in Range? %s\n"%(ran_check(4,2,7))


# Question 3 
upp, loow = 0,0

def up_low(s):
  global upp, loow
  for x in s:
    if x.isupper():
      upp += 1
    elif x.islower():
      loow += 1      

  print "No. of Upper Case Characters: %d" %(upp)
  print "No. of Lower Case Characters: %d" %(loow)


s = "Hello Mr. Rogers, how are you doing this fine Tuesday?"
up_low(s)          



# Question 4
l = [1,1,1,1,2,2,2,3,3,3,3,3,4,5]

def unique_list(l):
   return set(l)

print "The Unique List is: {x}\n".format(x = unique_list(l))



# Question 5

numbers = [1,2,3,-4]

def multiply(numbers):
  mul = 1
  for x in numbers:
    mul *= x 
  return mul


print "The Result is: %d\n" %(multiply(numbers))



# Questions 6

s = "nursesrun"
def palindrome(s):
  y = s[::-1]
  if s == y:
    return True
  else:
    return False

print "Is this a Palindrome? %s \n"%(palindrome(s))


 
# Question 7

str = "The quick brown fox jumps over the lazy dog"

import string 

count = 0
def ispangram(str):
  global count
  y = str.lower()
  trn = [word[0] for word in y.split()]
  
  for x in trn:
    for z in string.ascii_lowercase:
      if x == z:
         count += 1
      else:
         continue
    
    if count == 26:
      return True
    else:
      return False

print "The value of the count: %d" %(count)   

 
'''
  for x in y:
     print "The value of x: %s"%(x)
     for z in string.ascii_lowercase:
        print "The value of z: %s"%(z)
        if x == z:  
          count += 1   
        else:
          continue 

  if count == 26:
    return True
  else:
    return False
print "The value of count is %d" %(count)
'''




print"Is the statement Pangram? %s\n" %(ispangram(str))   
  
   

