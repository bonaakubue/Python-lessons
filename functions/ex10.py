#function scopes
#Global scope
num = 20

def func():
    #local scope
    num = 10
    print(num)


func()

print(num)