#finding factorial using recursive function
def factorial(num):  
   if num == 1:  
       return num  
   else:  
       return num*factorial(num-1)  

number = 7
result = factorial(number)

print('The factorial of', number, 'is', result)
