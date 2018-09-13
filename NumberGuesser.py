import re

int_regex = re.compile("[+-]?[\d]+$")
def ensure_integer(curInput):
    if int_regex.match(curInput) is not None:
        return True
    else:
        return False

def ensure_one_hundred(curInput):
    num = int(curInput)
    return (num>0 and num<=100)

yn_regex = re.compile("[yn]$")
def ensure_y_n(curInput):
    return yn_regex.match(curInput) is not None

greatlessequal_regex = re.compile("[\>\<\=]$")
def ensure_greatlessequal(curInput):
    return greatlessequal_regex.match(curInput) is not None

###
### Silly version: ###
###

def silly():
    over = False
    print("Welcome to Number Guesser!\n")
    print("Enter a number from 1 to 100, and I'll guess it in 7 or fewer tries!")

    flag = True
    while (flag):
        userNum = input("\nYour number is: ")

        if not ensure_integer(userNum):
            print("You should have input an integer...")
        elif not ensure_one_hundred(userNum):
            print("It has to be between 1 and 100...")
        else:
            flag = False

    flag = True
    while (flag):
        print("\nIs your number -12?")
        ans = input("y/n: ")

        if ensure_y_n(ans):
            flag = False
        else:
            print("That wasn't y or n. What's wrong with you?")

    if(ans.lower()=="y"):
        print("Yay! I got it!")
        over = True
    elif(ans.lower()=="n"):
        print("Hmm...")
        print("")

    if(not over):
        flag = True
        while (flag):
            print("\nWas your number " + userNum + "?")
            ans = input("y/n: ")

            if ensure_y_n(ans):
                flag = False
            else:
                print("That wasn't y or n. What's wrong with you?")


        if(ans.lower()=="n"):
            print("LIAR.")
        elif(ans.lower()=="y"):
            print("I win!")
        else:
            print("That wasn't y or n. What's wrong with you?")

###
### Real version: ###
###

def real():
    print("Welcome to Number Guesser!\n")
    print("Enter a number from 1 to 100, and I'll guess it in 7 or fewer tries!")

    numGuesses = 0
    curGuess = 50
    minGuess = 1
    maxGuess = 100
    over = False
    while (not over):
        flag = True
        while (flag):
            print("\nIs your number "+str(curGuess)+"? Or is it > or <?")
            ans = input("Enter >, <, or =: ")
            if ensure_greatlessequal(ans):
                flag = False
            else:
                print("Please enter \">,\" \"<,\" or \"=.\"")
        
        numGuesses+=1
        
        if ans == "=":
            over = True
        elif ans == ">":
            minGuess = curGuess + 1
            curGuess = (curGuess + maxGuess)//2
            if curGuess < minGuess:
                curGuess = minGuess
            if curGuess > maxGuess:
                curGuess = maxGuess
        else:
            maxGuess = curGuess - 1
            curGuess = (curGuess + minGuess)//2
            if curGuess < minGuess:
                curGuess = minGuess
            if curGuess > maxGuess:
                curGuess = maxGuess
    
    if numGuesses>1:
        print("Yay, I got it! It took " + str(numGuesses) + " guesses!")
    else:
        print("Yay, I got it! It took 1 guess!")
