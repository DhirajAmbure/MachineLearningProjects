def hello_wrd(strVar):
    """
    This function is used to print the passed value
    :param strVar: Name of the person
    :return: Nothing
    """
    print("Hello",strVar)


hello_wrd('Dhiraj')
print(hello_wrd.__doc__)


def sumOfNumbers(numbers):
    """
    :param numbers: numbers to find Sum of
    :return: Sum of passed numbers
    """
    sumVal = 0
    for number in numbers:
        sumVal += number

    return sumVal

print("Sum is:",sumOfNumbers([2.3,1,7,4.3,9.2]))
print(sumOfNumbers.__doc__)