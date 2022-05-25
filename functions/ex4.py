#mixed arguments

def greetings(name, title, message):
    greet = f'{message} {title} {name}!'
    print(greet)


#This is correct

greetings('Kenneth',title= 'Mr.', message='Good Morning')


#This is wrong

# greetings('Kenneth', title= 'Mr.', 'Good Morning')

#This is also wrong
greetings(name='Kenneth', title= 'Mr.', 'Good Morning')