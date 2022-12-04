"""
Name: Kelvin Zhao
UCINetID: kelvinyz
"""

class IntegerOutOfRangeException(Exception):
    pass

class NoStaircaseSizeException(Exception):
    pass

''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function. This function will
raise any exceptions related to none integer user inputs.'''
def getUserInput():
    #your code belongs here
    user_input = input("Please input your staircase size:")
    
    try:
        temp = float(user_input)
        if (temp.is_integer() == True):
            raise ValueError
    except ValueError:
        if (user_input == "DONE"):
            return user_input
        elif (user_input.isnumeric == False):
            raise ValueError
        else:
            return user_input
    return float(user_input)
            
    
    
        

''' This function takes the number of steps as an input parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function. This function will raise
any exceptions resulting from invalid integer values.
'''
def printSteps(stepCount):
    #your code belongs here
    if (stepCount == 0):
        raise NoStaircaseSizeException
    elif (stepCount < 1 or stepCount >= 1000):
        raise IntegerOutOfRangeException
    else:
        result = ""
        for i in range(stepCount, 0, -1):
            if (i == stepCount):
                result += " " * (i * 2 - 2)
                result += "+-+\n"
                result += " " * (i * 2 - 2)
                result += "| |\n"
            else:
                result += " " * (i * 2 - 2)
                result += "+-+-+\n"
                result += " " * (i * 2 - 2)
                result += "| |\n"
        result += "+-+"
        return result

'''This function kicks off the running of your program. Once it starts
it will continuously run your program until the user explicitly chooses to
end the running of the program based on the requirements. This function returns
the string "Done Executing" when it ends. Additionally, all exceptions will be
handled (caught) within this function.'''
def runProgram():
    #your code belongs here
    quit_key = ""
    while quit_key != "DONE":
        try:
            stepCount = getUserInput()
            if (stepCount == "DONE"):
                quit_key = "DONE"
                break
            elif (float(stepCount) < 1 and float(stepCount) > 0):
                stepCount = float(stepCount)
            elif (int(stepCount) != float(stepCount)):
                stepCount = 0.1
            elif (stepCount.isdigit):
                stepCount = int(stepCount)
            
            print(printSteps(stepCount))
            
        except ValueError:
            print("Invalid staircase value entered.")
            
        except NoStaircaseSizeException:
            print("I cannot draw a staircase with no steps.")
            
        except IntegerOutOfRangeException:
            print("That staircase size is out of range.")
    
    return "Done Executing"
    
'''Within this condition statement you are to write the code that kicks off
your program. When testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    #your code belongs here
    print(runProgram())
   