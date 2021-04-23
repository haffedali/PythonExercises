lumpSum = 800000
interestRate = 0.06
minimumPayment = 103

def monthGoesBy(lumpSum,interestRate,minimumPayment):
    interesetGrowth = interestRate / 12
    lumpSum = (interesetGrowth * lumpSum) + lumpSum
    lumpSum -= minimumPayment
    print(lumpSum)

monthGoesBy(lumpSum, interestRate, minimumPayment)


def divisbleBySevenNotByFive():
    results = []
    x = range(2000,3000)
    for n in x:
        if not n % 7 and n % 5:
            results.append(n)
    print(results)


def factorialRecursive(n):
    if n < 2:
        return 1
    else:
        return n * factorialRecursive(n - 1)





# With a given integral number n, write a program to generate a 
# dictionary that contains (i, i*i) such that is an integral number 
# between 1 and n (both included). and then the program should print 
# the dictionary

def allIntegrals(number):
    integralDictionary = {}
    x = range(1,number)
    for n in x:
        integralDictionary[n] = n*n
    print(integralDictionary)


class StringClass():
    def __init__(self):
        self.string = ""

    def setString(self):
        self.string = input()

    def printString(self):
        print(self.string)




# stringRetriever = StringClass()
# stringRetriever.setString()
# stringRetriever.printString()

print(factorialRecursive(8))
allIntegrals(10)