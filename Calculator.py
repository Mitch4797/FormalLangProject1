#Mitchell humphries
#This is my python Script to inturprit numebrs
##################################################
#Imports
from enum import Enum
import enum

##################################################
#Enum State Class
class STATE:
    ERROR = 0
    START = 1

    INTEGERFIRST = 2
    INTEGER = 3
    INTERGERUNDER = 4 #Integer part underscore

    DECIMALFIRST = 5
    DECIMAL = 6
    DECIMALUNDER = 7 #Decimal part underscore
    
    EXPONENTSIGN = 11
    EXPONENTFIRST =  8
    EXPONENT = 9
    EXPONENTUNDER = 10 #exponent part underscore

    FORCEDEND = 12
    


##################################################
def stringInterpreter(inputString):
    #For Value
    #for base
    sign = 1
    value = 0
    power = 0.1

    #fpr exp
    exponent = 0
    expSign = 1

    #For State
    i = 0
    currentState = STATE.START
    currentCharcter = inputString[i]

    #Enter Loop to start solving
    while currentState != STATE.ERROR:
        match currentState:

            #Start State
            case STATE.START:
                if currentCharcter == '.':
                    power = 0.1
                    currentState = STATE.DECIMALFIRST
                elif currentCharcter.isdigit():
                    value = ord(currentCharcter) - ord('0')
                    currentState = STATE.INTEGER
                else:
                    currentState = STATE.ERROR

            #Integer Portion
            case STATE.INTEGER:
                if currentCharcter == '.':
                    power = 0.1
                    currentState = STATE.DECIMALFIRST
                elif currentCharcter == '_':
                    currentState = STATE.INTERGERUNDER
                elif currentCharcter.isdigit():
                    value = 10 * value + ord(currentCharcter) - ord('0')
                elif currentCharcter == 'e' or currentCharcter == 'E':
                    currentState = STATE.EXPONENTSIGN
                elif currentCharcter =='f' or currentCharcter == 'F':
                    currentState = STATE.FORCEDEND
                else:
                    currentState = STATE.ERROR

            case STATE.INTERGERUNDER:
                if currentCharcter.isdigit():
                    value = 10 * value + ord(currentCharcter) - ord('0')
                    currentState = STATE.INTEGER
                elif currentCharcter == '_':
                    pass
                else:
                    currentState = STATE.ERROR

            #Decimal Portion
            case STATE.DECIMALFIRST:
                if currentCharcter.isdigit():
                    value = value + power * (ord(currentCharcter) - ord('0'))
                    power = power/10 
                    currentState = STATE.DECIMAL
                else:
                    currentState = STATE.ERROR

            case STATE.DECIMAL:
                if currentCharcter.isdigit():
                    value = value + power * (ord(currentCharcter) - ord('0'))
                    power = power/10
                elif currentCharcter == '_':
                    currentState = STATE.DECIMALUNDER
                elif currentCharcter == 'e' or currentCharcter == 'E':
                    currentState = STATE.EXPONENTSIGN
                elif currentCharcter =='f' or currentCharcter == 'F':
                    pass
                else:
                    currentState = STATE.ERROR

            case STATE.DECIMALUNDER:
                if currentCharcter.isdigit():
                    value = value + power * (ord(currentCharcter) - ord('0'))
                    power = power/10
                    currentState = STATE.DECIMAL
                elif currentCharcter == '_':
                    pass
                else:
                    currentState = STATE.ERROR

            #Exponent Portion
            case STATE.EXPONENTSIGN:
                if currentCharcter == '-':
                    expSign = -1
                    currentState = STATE.EXPONENTFIRST
                elif currentCharcter == '+':
                    expSign = 1
                    currentState = STATE.EXPONENTFIRST
                elif currentCharcter.isdigit():
                    exponent = ( ord(currentCharcter) - ord('0') )
                    currentState = STATE.EXPONENT
                else:
                    currentState = STATE.ERROR

            case STATE.EXPONENTFIRST:
                if currentCharcter.isdigit():
                    exponent = ( ord(currentCharcter) - ord('0') )
                    currentState = STATE.EXPONENT
                else:
                    currentState = STATE.ERROR

            case STATE.EXPONENT:
                if currentCharcter.isdigit():
                    exponent = 10 * exponent + (ord(currentCharcter) - ord('0'))
                elif currentCharcter =='f' or currentCharcter == 'F':
                    pass
                elif currentCharcter == '_':
                    currentState = STATE.EXPONENTUNDER
                else:
                    currentState = STATE.ERROR

            case STATE.EXPONENTUNDER:
                if currentCharcter.isdigit():
                    exponent = 10 * exponent + (ord(currentCharcter) - ord('0'))
                    currentState = STATE.EXPONENT
                elif currentCharcter =='_':
                    pass
                else:
                    currentState = STATE.ERROR
            
            case default:
                print("Error this should not be reached")
        
        #CHECK IF IN ERROR STATEMENT
        if currentState == STATE.ERROR:
            return "ERROR, Invalid Form"

        #Handle Finishing/Done State
        elif(i + 1 >= len(inputString)):
            #If in none except State
            if(currentState == STATE.INTERGERUNDER or currentState ==STATE.INTEGER or currentState==STATE.DECIMALUNDER or currentState==STATE.EXPONENTUNDER):      
                return "ERROR, Invalid Form"
            else:
                return sign * value * pow(10,(expSign * exponent ))
        else:
            i = i + 1
            currentCharcter = inputString[i]

##################################################

#To Run Program
print("Mitchell H. Calculator.")
print("Type 'exit' or 'q' to close program.")

while True:
    inputString = input("Please enter float literal: ")

    if inputString == "exit" or inputString == "Exit" or inputString == "q":
        break

    newNum = stringInterpreter(inputString)
    print(newNum)


