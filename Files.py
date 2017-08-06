
f = open('test.txt', 'a+')
f.write("My name is Rajeev")
f.seek(0)

print "\nRead: %s\n"%(f.read())

print "Again Read: %s\n"%(f.read())

print "Seek: \n"
f.seek(0)

print "Read: %s\n"%(f.read())
f.seek(0)


print "Readline: %s\n"%(f.readline())

f.write("\nWelcome to the World!!\n")
f.seek(0)


print "Read: %s\n" %(f.read())
f.seek(0)
f.truncate()
f.close()


