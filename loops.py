#While loops used when the number of iterations is not known
count = 0
print('starting')
while count < 10:
    print(count, ' ', end='')
    count += 1

#outside the loop
print()
print('Done!')
print()
#For loop used when the number of iterations is known
#Loop over a set of values in arange
print("print out values in arange")
for i in range (0, 10):
     print(i, ' ', end='')
print()
print('Done!')
    
for _ in range(0, 10):
    print(_, end=' ')
print()
print(type(_))
    