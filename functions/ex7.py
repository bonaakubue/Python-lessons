# non-keyword arguments *args

def func(*args):
    for value in args:
        print(value)

#calling the function with variable number of positional arguments
func('yellow', 'blue', 'green', 'purple')

#calling the function with a tuple
countries = ('Spain', 'Brazil', 'Mexico')
func(*countries)