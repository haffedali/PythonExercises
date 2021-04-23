lumpSum = 800000
interestRate = 0.06
minimumPayment = 103

def monthGoesBy(lumpSum,interestRate,minimumPayment):
    interesetGrowth = interestRate / 12
    lumpSum = (interesetGrowth * lumpSum) + lumpSum
    lumpSum -= minimumPayment
    print(lumpSum)

monthGoesBy(lumpSum, interestRate, minimumPayment)




# Write a program which will find all 
# such numbers which are divisible by 7 
# but are not a multiple of 5,between 2000 
#  3200 (both included).The numbers obtained 
#  should be printed in a comma-separated 
#  sequence on a single line

def divisbleBySevenNotByFive():
    results = []
    x = range(2000,3000)
    for n in x:
        if not n % 7 and n % 5:
            results.append(n)
    print(results)

# Write a program which can compute the factorial of a 
# given numbers.The results should be printed in a 
# comma-separated sequence on a single line

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


# Your goal in this programming exercise is to
#  determine, whether the phrase represents a 
#  palindrome or not.Input datacontains number 
#  of phrases in the first line.Next lines contain 
#  one phrase each.Answershould have a single 
#  letter (space separated) for each phrase:Y 
#  if it is a palindrome andNif not.

def isPalindrome(string):
    place = -1
    flag = 0
    for i in string:
        if i.lower != string[place].lower:
            place = place - 1
            flag = 1
            break
        place = place - 1
    if flag == 1:
        return("N ")
    else:
        return("Y ")

def checkPhrases(listOfPhrases):
    returnString = ""
    for i in listOfPhrases:
        returnString += isPalindrome(i)
    print(returnString)


print(factorialRecursive(8))
allIntegrals(10)

checkPhrases(["racecar", "president", "Some men interpret nine memos"])


# Three is a Crowd
class Crowd():
    def __init__(self):
        self.room = ["Haffed", "Becca", "Jessica", "Joseph"]

    def isRoomCrowded(self):
        if len(self.room) >= 6:
            print("There is a heckin mob up in there!!!")
        elif len(self.room) >= 3 and len(self.room)< 6:
            print("Sorry, The room is pretty crowded")
        else:
            print("We have space, come on in!")
            print("What's your name hun?")
            self.room.append(input())
    
    def bootABish(self):
        self.room.pop()

    def giveTheGuestList(self):
        print(self.room)

    def makeItAMob(self):
        self.room.append("Tyler")
        self.room.append("Jacob")
        self.room.append("Dylan")
        self.room.append("Alex")



coffeeHouse = Crowd()

coffeeHouse.bootABish()
coffeeHouse.bootABish()
coffeeHouse.isRoomCrowded()
coffeeHouse.giveTheGuestList()
coffeeHouse.makeItAMob()
coffeeHouse.isRoomCrowded()
coffeeHouse.giveTheGuestList()

