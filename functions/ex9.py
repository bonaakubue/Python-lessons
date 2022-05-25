def power (value, exponentiation = 2):

    result = 1

    if exponentiation is None:

        result = value ** 2

    else:

        result = value ** exponentiation

    print (result)

#Calling the function

power (2, 3)
power (2)