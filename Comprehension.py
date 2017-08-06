l = [letter for letter in 'word']

print l

sq = [ x**2 for x in range(11)]

print sq


even = [number for number in range(11) if number%2 == 0]

print even



ev_num = []
for number in range(11):
   if number%2 == 0: 
    {
      ev_num.append(number)
    }   


print ev_num 




celsius = [0, 10, 20.1, 34.5]

fahrenheit = [((temp*9)/5 + 32) for temp in celsius]

print fahrenheit


final_nest = [nest**2 for nest in [x**2 for x in range(11)]]

print final_nest



