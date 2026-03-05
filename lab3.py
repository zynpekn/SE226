#TASK1
x = int (input ('Please enter a positive integer greater than 1: '))
if int ( x <= 1 ) :
    print('Invalid number please enter a number greater than 1.')
else :

 totalsteps = 0
print (x , end = '')

while ( x > 1 ) :
    if ( x % 2 == 0 ) :
       x =  x // 2 
    else :
        x = x * 3 + 1  
    print ('->', x , end= '' )
    
totalsteps = totalsteps + 1
print ('\nTotal steps:' , totalsteps)

#TASK2
y = int (input ('Please enter a positive integer between 10-100: '))

while( y > 100 or y < 10 ) :
   y = int (input ('Invalid Input. Please enter a positive integer between 10-100:' ))

fizz_count = 0 
buzz_count = 0
fizzbuzz_count = 0

for i in range (1 , y+1) :
    if i % 7==0:
       continue

    if i % 15 == 0 :
     print('FizzBuzz ' )
     fizzbuzz_count += 1 
    elif i % 3 == 0 :
     print ( 'Fizz ')
     fizz_count += 1 
    elif i % 5 == 0 :
     print ( 'Buzz ' )
     buzz_count += 1
    else :
       print (i) 


print(' \n --- Summary ---')
print('Fizz Count: ' , fizz_count)
print('Buzz Count: ' , buzz_count)
print('FizzBuzz Count: ' , fizzbuzz_count)

#TASK3


n = int ( input ('Please enter a number bewteen 3 and 9: '))
while n < 3 or n> 9 :
   n = int ( input ( 'Invalid Input. Please enter a number between 3 and 9: '))

for i  in range (1, n+1) :
   print ( '*' * i)


for i in range (n-1 , 0 , -1 ):
   print ('*' * i )
