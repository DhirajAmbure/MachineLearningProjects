import math as m


def findfact(number):
    if number == 1:
        return number
    elif number != 0:
        return number * findfact(number - 1)


number = int(input("Enter number to find Factorial: "))

if number < 0:
    print("factorial can not be found for negative numbers")
elif number ==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of {} is {}".format(number,findfact(number)))

print("Factorial of {} using function from math package is {}".format(number,m.factorial(number)))


# def findFact(number):
#     if(number==0 | number==1):
#         return 1
#     elif (number > 1):
#         return number * findFact(number-1)
#
# varFact = int(input("Please Enter the number to find Factorial"))
# fact = 0
# if(varFact < 0):
#     print("Please enter +ve number to find factorial")
# else:
#     print("factorial of {} is {}".format(varFact,findFact(varFact)))
#

"""Using while loop"""

def factUsingWhile(number):
    """To find the factorial of given parameter"""
    factr = 1

    while(number>0):
        factr *= number
        number -= 1
    return factr


factr_vari = int(input("Enter the number: "))
print(factUsingWhile(factr_vari))