my_list = ['First item', 12, 4.0, [14, 10.0, 'matrix']]


print "\nDisplay the value of my_list %s\n"%(my_list)

print "my_list[:3] %s\n"%(my_list[:3])

print "my_list[3:] %s\n"%(my_list[3:])

print "my_list[3][0] %s\n"%(my_list[3][0])


my_list.append('New Item')
print "Append:  %s\n"%(my_list)


print "Pop: %s\n"%(my_list.pop(1))

print "New List: %s\n"%(my_list)

my_list.reverse()
print "Reverse: %s\n"%(my_list)

my_list.sort()
print "Sort: %s\n"%(my_list)


first_collumn = [row[0] for row in my_list]
print "First_collumn: %s\n"%(first_collumn)   
