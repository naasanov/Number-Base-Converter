# This class is used for the main function of the program.
class BaseConverter:
    def __init__(self):

        self.is_negative = False

        self.orgBase = self.tryBaseInput("Enter the base of your number: ")
        self.orgNum = self.tryNumberInput("Enter your number (enter with spaces between digits if base is greater than 10): ")
        if self.orgNum[0] == "-":
            self.orgNum = self.orgNum[1:]
            self.is_negative = True

        self.newBase = self.tryBaseInput("Enter the base you want to convert to: ")
        self.decNum = self.convertToDec(self.orgNum, self.orgBase)

    """
    To change base, we use the following algorithm:
    Starting with the highest exponent n such that base^n will go into the decimal number at least once,
    find how many times base^n goes into the decimal number. This is the value at the current digit.
    Repeat this process on the remainder with n-1.
    """
    def convertNumber(self):       
        convertedNum = []
        if self.is_negative is True:
            convertedNum.append("-")

        changingNum = self.decNum # copy decNum into another variable to avoid changing decNum
        newBaseDigits = self.getNewBaseDigits(self.decNum, self.newBase) # number of digits that will be in the converted number
        for i in reversed(range(newBaseDigits)): # iterate through each power of base from high to low
            currPlace = pow(self.newBase, i)
            convertedNum.append(int(changingNum / currPlace)) # find how many times base^n goes into the decimal number
            changingNum = changingNum % currPlace # set the working variable to the remainder
        
        return convertedNum
    
    # Finds the number of digits a decimal number will need to be represented in a new base.
    # Used to find the highest exponent of the base that will go into the decimal number
    def getNewBaseDigits(self, num, base):
        places = 0
        while (num - pow(base, places) >= 0):
            places += 1

        return places
    
    # Converts a number of any base to a decimal number
    def convertToDec(self, num, base):
        final = 0
        i = 0
        for n in reversed(num):
            final += int(n) * pow(base, i)
            i += 1

        return final

    # Gets user input for a standard integer input.
    # Returns a valid integer user input
    def tryBaseInput(self, message):
        userInput = input(message)
        while True:
            if self.validateInt(userInput) is not True:
                print("Incorrect input, please try again")
                userInput = input(message)
            elif int(userInput) < 2:
                print("Please provide a base greater than 1")
                userInput = input(message)
            else:
                break

        return int(userInput)
    
    # Gets user input for a list of digits used for numbers in bases higher than 10.
    # Returns a valid digit list user input
    def tryNumberInput(self, message):
        userInput = input(message)

        if (self.orgBase > 10):
            userInput = userInput.split(" ")
            while self.validateDigitList(userInput) is not True:
                print("Incorrect input, please try again")
                userInput = input(message)
                
            returnList = []
            for item in userInput:
                if item == "-":
                    returnList.append(item)
                else:
                    returnList.append(int(item))
            return returnList
        else:
            while self.validateInt(userInput) is not True:
                print("Incorrect input, please try again")
                userInput = input(message)
            return userInput
            
        
    # Validates a user input meant for a standard integer
    # Returns True if valid, False if not
    def validateInt(self, input):
        if len(input) == 0:
            return False
        
        try:
            int(input)
        except:
            return False
        
        return True

    
    # Validates a user input meant for a digit list
    # Returns True if vaild, False if not
    def validateDigitList(self, inputList):
        if inputList[0] == "-":
            if len(inputList) == 1:
                return False
            else:
                inputList = inputList[1:]
            
        for item in inputList:
            if self.validateInt(item) is not True:
                return False
            if int(item) >= self.orgBase:
                return False
            if int(item) < 0:
                return False

        return True