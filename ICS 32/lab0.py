"""
Name: Kelvin Zhao
UCINetID: kelvinyz
"""

''' This functions asks the user for the number of steps
they want to climb, gets the value provided by the user
and returns it to the calling function'''
def getUserInput():
    #your code belongs here
    user_input = int(input("How many steps do you want to move?\n"))
    return user_input

''' This function takes the number of steps as an unput parameter,
creates a string that contains the entire steps based on the user input
and returns the steps string to the calling function
'''
def createSteps(stepCount):
    #your code belongs here
    result = ""
    if (stepCount < 0):
        return "Invalid staircase size provided."
    elif (stepCount == 0):
        return "Your staircase has no steps."
    elif (stepCount >= 500):
        return "I can't build a staircase that tall."
    else:
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
        
        

'''Within this condition statement you are to write the code that
calls the above functions when testing your code the code below this
should be the only code not in a function and must be within the if
statement. I will explain this if statement later in the course.'''
if __name__ == "__main__": 
    #your code belongs here
    user_input = getUserInput()
    print(createSteps(user_input))
