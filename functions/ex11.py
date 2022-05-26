#recursive sum of natural numbers

def Sum(num):
    if num <= 1:
       return num
    else:
       return num + Sum(num-1)

# change this value for a different result
number = 16

print(Sum(7))