def even_numbers(number):
    """This function returns
        if a number is even
    """

    if number%2 ==0:
        return number

numbers = range(50)
evenNumList = list(filter(even_numbers,numbers))
print(evenNumList)


"""Using **kwargs as argument to the function"""

def helloProg(**kwargs):
    """
    This function is used to understand the functionality of kwargs
    :param kwargs:
    :return:
    """
    print("Hello {0}, {1}".format(kwargs['name'],kwargs['msg']))

helloProg(name='Dhiraj',msg='Welcome to the world of Data Science')


"""Using arbitary arguments in python"""

def helloNames(*names):
    for name in names:
        print("Welcome {0}".format(name))

helloNames('Dhiraj','Priyanka','Hrisha','Dhanashri')


listOfNames = ['Dhiraj','Priyanka','Hrisha','Dhanashri']

def printNames(listOfNames):
    for nm in listOfNames:
        print("Welcome {}".format(nm))

printNames(listOfNames)