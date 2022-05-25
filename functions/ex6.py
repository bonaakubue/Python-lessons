#A function that prompts the user for a number

def check_odd_even(num):
    if (num % 2) == 0:
        print (num, 'is even')
    else:
        print(num, 'is odd')

number = int(input('enter any number: '))

check_odd(number)