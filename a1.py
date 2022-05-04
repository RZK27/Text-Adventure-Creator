"""
Student Last Name: Sekandar
Student First Name: Rahabar
Student Number: 501100634
Ryerson email: rsekandar@ryerson.ca
The following code uses text files to run a text based "choose your own adventure" type game.
It is simple to use and solves the issue of having to code differently for different games,
supporting a virtually unlimited number of levels. The READ ME.txt file attached goes into depth
with the rules of writing the game.txt file that is used, as well as a couple functions that the
author of the story can use. The text files this code requires are game.txt and title.txt.
created 09 29 2021
"""
from time import sleep

#this handles reading the text file, making sure the number of lines fits the formatting of the code. For every next 2^n (where n begins at 0), there is a level of choices.
#it's a simple, readable way of storing a binary choice tree
#An example text file is attached, you can edit in your own story (following the rules in READ ME.txt)
with open('game.txt') as f:
    numOfLines = len(f.readlines())
    if numOfLines == 0:
        input("game.txt is empty, this code will self-destruct.")
    if int(str(bin(numOfLines + 1))[3:]) == 0:
        numOfLevels = len(str(bin(numOfLines + 1))[3:])
    else:
        input("The number of lines in game.txt are not 1 less than a power of 2, this code will self-destruct.")

#prints but cooler and also takes an input which can be ignored and instead used as a "Press enter to continue"
def coolPrint(text):
    #this is used to send a path back into another path
    reroute = False
    reroutePath = ""
    #this is used to clear the screen if the user puts # in game.txt (explained with READ ME.txt)
    toClear = False
    for letter in text:
        #if ^ is written at the end of a line, the story is ended there (early end) with ooga (error on purpose)
        #the rest of game.txt MUST STILL HAVE NON-EMPTY LINES WHERE EXTRA CHOICES WOULD HAVE GONE (explained with READ ME.txt)
        if letter == "^":
            return -1
        #if @ is written, will clear after printing sentence
        elif letter == "@":
            toClear = True
        # if # is found at the end of a line, we jump to the line number written afterwards
        elif letter == "#":
            reroute = True
        elif reroute:
            reroutePath += letter
        #else we print all cool with delay
        else:   
            print (letter, end = "")
            sleep(0.03)

    
    if reroute:
        return int(reroutePath)

    #handy in case i want it (which i will)
    if not reroute:
        toReturn = input().lower()
    print("")
    if toClear:
        print("\033c")
    return toReturn
#outputs a line from game.txt and returns the int value of the next line to be read
def outputGameLine(lineNumber):
    #clear console
    print("\033c")
    #separate the line of text into sentences based on backslashes
    with open('game.txt') as f:
        text = f.readlines()[lineNumber - 1].split("\\")
    #here we use coolPrint to print the lines that we have separated above in the function
    #also time to take input (if there are any to be taken, otherwise if we are on the last row of lines (8 or more) its just like a press to continue sort of deal)
    for fragment in text:
        userChoice = coolPrint(fragment.strip() + " ")
    
    #checks if rerouting to a different line
        
    if type(userChoice) == int and userChoice > 0:
        return userChoice

    #checks for if early ending or final line
    if userChoice == -1 or lineNumber >= 2 ** (numOfLevels - 1):
        return -1

    #reads input and returns next lineNumber
    while(True):
        if userChoice == "a":
            return lineNumber * 2
        elif userChoice == "b":
            return lineNumber * 2 + 1
        else:
            userChoice = coolPrint("Input must be A or B: ").lower()

if __name__ == "__main__":

    #this is the title screen, title.txt, can also be edited
    print("\033c")
    with open('title.txt') as t:
        for letter in t.read(): 
            print (letter, end = "")
            sleep(0.03)

    input()

    #replay is used to allow the user to play the game again and attempt a different ending
    replay = "a"
    while(replay == "a"):
        #this is the number for the line in the game text file that is to be read next
        gameLineNumber = 1
        #recursion? here is to update the line the user is reading 
        while(gameLineNumber != -1):
            gameLineNumber = outputGameLine(gameLineNumber)

        #checking if user wants to replay
        replay = coolPrint("A: try again?\nB: quit game\n").lower()
        while(not (replay == "a" or replay == "b")):
            replay = coolPrint("Input must be A or B: ").lower()