myPrimeNumList = []

lowLimit = input("Enter Lower Lomit of the Prime Numbers List: ")
numLimit = input("Enter Upper limit of the Prime Numbers List: ")

if numLimit.isdigit():
    for num in range(int(lowLimit),int(numLimit)+1):
        if num > 1:
            for deno in range(2,num):
                if (num % deno) == 0:
                    break
            else:
                print(num)

#print(myPrimeNumList)