#keyword arguments

def greetings(name, title, message):
    greet = f'{message} {title} {name}!'
    print(greet)


#calling by keyword arguments
greetings(message = 'Good morning', title='Mr.', name= 'Kenneth')

#calling by positional arguments

greetings('Kenneth', 'Mr.', 'Good Morning')