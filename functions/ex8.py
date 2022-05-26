# keyword arguments **kwargs

def func(**kwargs):
    #if you want to get keys
    for kwarg in kwargs:
        print(kwarg)
    #if you want to get values
    for kwarg in kwargs.values():
        print(kwarg)


#calling the function with keyword arguments
func(a='apple', b='mango', c='orange', d='pineapple', e='pawpaw')


#calling the function with dictionary

dict = {'name':'Paul', 'age':25, 'gender':'male'}
func(**dict)