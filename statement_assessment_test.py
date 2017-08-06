st = 'Print only the words that start with s in this sentence'
for word in st.split():
  if word[0] == 's':
    print word	



for x in range(11):
  if x % 2 == 0:
    print x






lst =[x for x in range(51) if x%3 == 0]

print lst






str = 'Print every word in this sentence that has an even number of letters'
letter = [x for x in str.split() if len(x)%2 == 0]
print letter

y = len(letter)
while y > 0:
  print "even!"
  y -= 1






for x in range(101):

  if x%3 == 0 and x%5 == 0:
    print "FizzBuzz"

  elif x%3 == 0:
      print "Fizz"
    
  elif x%5 == 0:
      print "Buzz"

  else:
    print x 





stri = 'Create a list of the first letters of every word in this string'


lstr = [word[0] for word in stri.split()]

print lstr
