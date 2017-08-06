#They are mappings in Python, they donot retain any sequence. 

my_dict = {'key1': 'Rajeev', 'key2': 'Sawant' }

print "\nKey1 Value: %s\n" %(my_dict['key1'])

print "Upper: %s\n" %(my_dict['key2'].upper())

print "Reverse: %s\n" %(my_dict['key2'][::-1])

print "Items: %s\n" %(my_dict.items())  

my_dict['key3'] = 'NewKey'

print "Dictionary: %s\n" %(my_dict)

print "Keys: %s\n" %(my_dict.keys())

print "Values: %s\n" %(my_dict.values())

my_dict['key4'] = [1,123,1234]

print "Dictionary: %s\n" %(my_dict)

