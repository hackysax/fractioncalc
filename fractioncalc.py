import os
import sys
import re
import math
import testData

# Ask user for input...
# if 'h', print intructions, go back to start
# if 'q', quit
# If invalid input, print error, go back to start
# If valid inputs, run the calculator
#If test, run tests
#
___author___ = "Devon Summers"

### Main ###


def main():

    clear()

    print("############################################################################################")
    print("### Welcome to the fraction calculator! (Enter '?' for instructions, enter 'Q' to quit.) ###")
    print("############################################################################################\n")

    userInput = input("Please enter your problem: ")
    # print(userInput)
    checkUserInput(userInput)


def checkUserInput(input):
    if input.strip().lower() == 'h':
        showHelp()
    elif input.strip().lower() == 'q':
        runQuit()
    elif input.strip().lower() == 'test':
        runTest()
    else:
        validateInput(input)


def validateInput(input):
    # config for later if wanting to handle more terms or operators...
    config = {"minTerms": 2, "maxTerms": 2, "validOps": ["+", "-", "*", "/"]}
    errorMessages = []

    expressionArray = input.split()

    errorMessages.append(checkNumberOfTerms(
        config['minTerms'], config['maxTerms'], expressionArray))

    for index, value in enumerate(expressionArray):
        if index % 2 == 0:
            errorMessages.append(checkForInvalidCharactersInTerm(value))
            errorMessages.append(checkZeroDenominatorInTerm(value))
            errorMessages.append(checkOneSlashUnderInTerm(value))
            errorMessages.append(checkInvalidNegativesInTerm(value))
            errorMessages.append(checkProperWholeNumberInTerm(value))
        else:
            errorMessages.append(checkOperatorTerm(value, config['validOps']))

    errorMessages = list(filter(None, errorMessages))

    if len(errorMessages) == 0:
        runCalc(expressionArray)
    else:
        sendErrors(errorMessages)


"""Begin Input Error Handling Functions"""


def checkForInvalidCharactersInTerm(term):
    result = ""
    regexString = '^[\d,\/,\_, \-]*$'
    if not re.search(regexString, term):
        result = "Term contain invalid characters: " + term
    return result


def checkForInvalidCharactersInTerms(expressionArray):
    result = ""
    regexString = '^[\d,\/,\_, \-]*$'
    for index, value in enumerate(expressionArray):
        if index % 2 == 0:
            if not re.search(regexString, value):
                result = "Terms contain invalid characters."
    return result


def checkOneSlashUnderInTerm(term):
    result = ""
    slashes = term.count("/")
    unders = term.count("_")
    if unders > 1 or slashes > 1:
        result = "Term '" + term + "' contains more than one special character '/' and/ or '_'."
    return result


def checkInvalidNegativesInTerm(term):
    result = ""
    if len(term) == 1 and term is "-":
        result = "Invalid negative found."
    else:
        for index, value in enumerate(term):
            if index != 0 and value == "-":
                result = "Invalid negative found in term '" + term + "'"
    return result


def checkProperWholeNumberInTerm(term):
    result = ""
    under = term.find("_")
    slash = term.find("/")
    if (under > 0 and slash > 0) and under > slash:
        result = "Whole number detected after fraction in term '" + term + "'"
    elif(slash < 0 and under > 0):
        result = "Missing fraction declaration detected after whole number in term '" + term + "'"
    return result


def checkNoLeadingUnderSlash(term):
    result = ""
    under = term.find("_")
    slash = term.find("/")
    if under == 0 or slash == 0:
        result = "Invalid start to an expression in term '" + term + "'"
    return result


def checkNumberOfTerms(minTerms, maxTerms, expressionArray):
    result = ""
    numTerms = math.ceil(len(expressionArray)/2)
    # print("Number of Terms found: ", numTerms, len(expressionArray))
    if (numTerms < minTerms):
        result = "Not enough terms in the expression."
    elif (numTerms > maxTerms):
        result = "Too many terms in the expression."
    return result


def checkOperatorTerm(term, validops):
    result = ""
    term = term.strip()
    valid = False
    for op in validops:
        if term == op:
            valid = True
    if not valid:
        result = "'" + term + "' is an invalid operator."
    return result


def checkZeroDenominatorInTerm(term):
    result = ""
    check = term.split("/")
    if len(check) > 1 and check[-1][0:] == '0':
        result = "Leading zero detected in a denominator. Cannot divide by zero. See term '" + term + "'"
    return result

### End Error Handling functions ###


# @runCalc()  Right now this only handles two terms.
# TO DO: Handle n number of terms and apply PEMDAS.


def runCalc(input):
    result = ""
    goodResult = True
    num_a = toNumDen(input[0])
    num_b = toNumDen(input[2])
    if type(num_a) is list and type(num_b) is list:
        if(input[1].strip() is "*"):
            #print("Product true!")
            result = getProduct(num_a, num_b)
        elif(input[1] is "/"):
            result = getQuotient(num_a, num_b)
        elif(input[1] is "+"):
            result = getSum(num_a, num_b)
        elif(input[1] is "-"):
            result = getDifference(num_a, num_b)
        else:
            #print("input 1: ", input[1])
            result = "Invalid operator found."
            goodResult = False
    else:
        result = "Invalid input found, missing numerator or denominator."
        goodResult = False

    if goodResult:
        sendResults(result)
    else:
        sendErrors([result])

# @reduce([int], [int]) is the workhorse. Enter the numerator and denomintaro and it will spit out a string as mixed number with reduced fraction.
# handles GCD problems by factoring primes, pretty fast.


def reduce(n, d):
    if abs(d) == 0:
        return "NaN"
    sign = getSign(n, d)
    n = abs(n)
    d = abs(d)
    answer = "0"
    mixed = False
    if n > d:
        mixed = True
        newN = n % d
    elif n == d:
        newN = 0
    else:
        newN = n
    whole = int(math.floor(n/d))

        #this was a simple (terrible) brute force reducing function. Worked very well on smaller problems and was simple.
        # decided to replace with getGCF() function
        # i = 2
        # while i <= newN:
        #    if (newN % i == 0) and (d % i == 0):
        #        comfactor = i
        #    i += 1
        #

    #print("Getting GCF")
    #print("newN: ", newN, "D: ", d)
    comfactor = getGCF(newN, d)
    newN = int(newN/comfactor)
    newD = int(d/comfactor)
    #print("newN: ", newN, "D: ", newD)
    if whole > 0:
        answer = sign + str(whole)
        mixed = True
    if newN > 0:
        if mixed:
            answer = answer + "_" + str(int(newN)) + "/" + str(int(newD))
        else:
            answer = sign + str(int(newN)) + "/" + str(int(newD))

    return answer


def getGCF(small, big):
    smallPrimes = getPrimeFactors(small)
    bigPrimes = getPrimeFactors(big)
    commons = []
    gcf = 1
    #goes through the primes and find common factors 
    for i, sprime in enumerate(smallPrimes):
        for j, bprime in enumerate(bigPrimes):
            if sprime == bprime:
                commons.append(bprime)
                bigPrimes.pop(j)
                break
    if len(commons) > 0:
        for n in commons:
            gcf = n*gcf
    #print(commons, gcf)
    return gcf


def getPrimeFactors(n):
    factors = []
    d = 2
    while(d*d <= n):
        while(n > 1):
            while n % d == 0:
                factors.append(d)
                n = n/d
            d += 1
    if n > 1: factors.append(n)
    #print(n, factors)
    return factors


# @sign([int], [int]) returns string indicated if fraction is negative or positve.


def getSign(n, d):
    sign = ""
    if n*d < 0:
        sign = "-"
    return sign

# @get[OPERATION]([str,str], [str, str]) expects two arrays of length 2 representing two fractions.
# Performes multiplcation to get new numerator and denominator.
# calls reduce, returns result.


def getProduct(a, b):
    n = int(a[0])*int((b[0]))
    d = int(a[1])*int((b[1]))
    result = reduce(n, d)
    return result


def getQuotient(a, b):
    checkZero = reduce(int(b[0]), int(b[1]))
    if checkZero == "0":
        result = "NaN"
    else:
        n = int(a[0])*int((b[1]))
        d = int(a[1])*int((b[0]))
        result = reduce(n, d)
    return result


def getSum(a, b):
    n = (int(a[0])*int(b[1])) + (int(a[1])*int(b[0]))
    d = int(a[1])*int(b[1])
    result = reduce(n, d)
    return result

# @getProduct([str,str], [str, str]) expects two arrays of length 2 representing two fractions.
# Performes substraction to get new numerator and denominator.
# calls reduce, returns result.


def getDifference(a, b):
    n = (int(a[0])*int(b[1])) - (int(a[1])*int(b[0]))
    d = int(a[1])*int(b[1])
    result = reduce(n, d)
    return result


# @toNumDe([str]) gets a term fomr the validated input and breaks it up into a numberator and denominator.
# there is some additional error handling happening in here as well just in case anything slips through.
# puts all inputs in terms of a numerator and denominator


def toNumDen(input):
    #print("input: ", input)
    worker = [None, None, None]
    result = ["0", "0"]
    negative = 1
    if "-" in input:
        negative = -1
        input = input.strip("-")
    if "_" in input:
        worker[0] = input.split("_")[0]
        input = input.split("_")[1]
    if "/" in input:
        worker[1] = input.split("/")[0]
        worker[2] = input.split("/")[1]
    if not ("/" in input or "_" in input):
        worker[0] = input
        worker[1] = "0"
    if (worker[2] == None or worker[2] == '' or worker[1] == '') and ("/" in input or "_" in input):
        result = False
    # whole number case
    elif (worker[1] == "0" or worker[1] == None):
        result = [str(negative*int(worker[0])), "1"]
    # mixed number
    elif (worker[0] != "0" and worker[0] != None):
        a = str(negative*(int(worker[0])*int(worker[2]) + int(worker[1])))
        result = [a, worker[2]]
    else:
        result = [str(negative*int(worker[1])), worker[2]]

    #print ("num/den results: ", result)
    return result

###End Buslogic###

### Flow and interface ####


def showHelp():
    print("############################  INSTRUCTIONS  #################################")
    print("### * Enter your input as two fractions with an operator between the two. ###")
    print("### * All terms must be separated by whitespace.                          ###")
    print("### * Mixed numbers should be connected by an underscore.                 ###")
    print(
        "### * Valid operators are: [*, +, /, -]                                   ###")
    print("### * Improper fractions are allowed.                                     ###")
    print("### * Whole numbers are allowed.                                          ###")
    print("### * Negative numbers are allowed.                                       ###")
    print("### * Decimal numbers are NOT allowed.                                    ###")
    print("### * Examples (ignore single quotes): '3_1/4 * 5/6' or '10 - -21/5'      ###")
    print("#############################################################################")
    userInput = input("Please enter your problem: ")
    checkUserInput(userInput)


def clear(): return os.system('cls')


def runQuit():
    print("Check you later!")
    sys.exit()

# result handler, loops back to start on enter.


def sendResults(results):
    output = "Here is the answer: [ " + results + " ]"
    print(output)
    input("Press enter to try again...")
    restart()

# hanldes the error messages, loops back on enter.


def sendErrors(errorMessages):
    result = "The following input error(s) have occured: \n"
    for message in errorMessages:
        result += "-> " + message + "\n"
    print(result)
    input("Press enter to try again...")
    restart()


def restart():
    clear()
    userInput = input("Please enter your problem (Q to quit, H for help): ")
    print(userInput)
    checkUserInput(userInput)

### End flow and interface ###

### TEST ###


def runTest():
    testType = input("Enter test type ('Reduce', 'Primes', 'GCF'): ")
    if testType.strip().lower() == 'reduce':
        unitTestReduce()
    if testType.strip().lower() == 'primes':
        unitTestPrimes()
    if testType.strip().lower() == 'gcf':
        unitTestGCF()
    runQuit()


def unitTestPrimes():
    print(getPrimeFactors(21))
    print(getPrimeFactors(45))
    print(getPrimeFactors(111))
    print(getPrimeFactors(110))
    print(getPrimeFactors(7365273))
    print(getPrimeFactors(98876270))


def unitTestGCF():
    print(getGCF(144, 48))
    print(getGCF(1440, 348))
    print(getGCF(415634, 24708))


def unitTestReduce():
    inTest = testData.testInput
    checkData = testData.testCheck
    for i in range(len(inTest)):
        result = reduce(inTest[i][0], inTest[i][1])
        if result == checkData[i]:
            pass
            print("Line " + str(i + 1) + " PASS.")
            #print("Result: " + str(result) + " Test Value: " + checkData[i])
        else:
            print("Line ", i + 1, "---------------  FAIL -----------------")
            print(inTest[i][0], inTest[i][1])
            print("Result: ", result, " Test Value: ", checkData[i])


### MAIN ###

if __name__ == "__main__":
    main()
