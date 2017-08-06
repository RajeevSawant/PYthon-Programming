l = [1,2,3,4,5,6,7,8]

print "\nList: "
for num in l:
    print num
print "\n"

print "Even: \n"
for num in l:
   if num % 2 == 0:
	print num
print "\n"

list_num = 0
for num in l:
    list_num += num

print "Sum: %s\n" %(list_num)


my_l = [(1,2), (2,3), (3,4)]
print "Tuple: "
for tup in my_l:
    print tup
print "\n"

for (t1, t2) in my_l:
    print "First: %s" %(t1)
    print "Second: %s\n" %(t2)
  
 

  
