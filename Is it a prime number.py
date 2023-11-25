def isPrimeNumber(): #new function 
 x = int(input("Enter a number: ")) #ask for user input by (Enter a number)
 current_number = 1  # Starting number
 divison_count = 0  # Starting number
 while current_number <= x:  # Change the condition to run until current_number reaches x
    division_reminder = x % current_number # division by modulo operator
    if division_reminder == 0 :
     divison_count += 1
    current_number += 1
 if divison_count == 2 or divison_count == 1 :
   return True
 return False
if(isPrimeNumber()):
  print('IT IS PRIME NUMBER')
else :print('NOT A PRIME NUMBER')


