__author__ = 'Colleen Toth'

# DFA runner program for Dan LeBlancs's CS311 by Colleen Toth
# This program will take user input for states, the delta function,
# final states, and the language and determine whether or not the
# given string is accepted by the DFA provided

def main ():

    lang = [] #array that holds elements of language (sigma)
    states = [] #array that holds the states contained in DFA
    start = ""  #string for start state
    final = [] #array for final states
    transitions = []  #array to hold the transition statements before splitting
    dTransitions = []
    fTransitions = []
    toCompute = ""
    currentState = ""
    response = "Y"

    #counter variables
    i = 0
    k = 0
    j = 0

    print ("Welcome to Colleen's DFA Runner Program\n\n")
    print("This program will determine whether a string you input")
    print("will be accepted by the DFA you specify. Please follow the")
    print("directions below.\n\n\n")


    i = getInput() #gets the length for the number of elements in the language

    #stores elements
    for x in range(0,i):
        element = raw_input("Please enter an element in the language: ")
        lang.append(element)


    print("\n\n")

    #gets number of states
    k = getStates()

    #stores states
    for x in range(0 , k):
        aState = raw_input("Please enter the designation for each state: ")
        states.append(aState)

    print("\n\n")

    DFA = dict.fromkeys(states, None)
    for x in DFA:
        DFA[x] = dict.fromkeys(lang, None)

    print("\n\n")

    start = raw_input("Please enter the start state: ")

    print("\n\n")

    #gets number of final states
    j = getFinalStates()

    #stores final states
    for x in range (0 , j):
        fState = raw_input("Please enter each accepting state: ")
        final.append(fState)

    print("\n\nPlease enter the transition function for each state (i.e. q(n): a-q): ")
    print("The state and the transition on an element are provided. Enter only the new state: \n\n")

    #gets individual transition states from user for each state declared in states array (a(element of sigma)-q(new state))
    for x in states:
        for t in lang:
            aTransition = raw_input("At state: " + x + " : " + " on " + t + " : " )
            while aTransition not in states:
                print("State provided not in set of states. ")
                aTransition = raw_input("At state: " + x + " : " + " on " + t + " : " )
            DFA[x][t] = aTransition


    #displays DFA definition
    print("The DFA you entered is defined as: \n")
    print("Sigma: ")
    print(lang)
    print("States: ")
    print(states)
    print("Start state: ")
    print(start)
    print("Delta function: ")
    print(transitions)
    print("F: ")
    print(final)
    print("\n\n")


    print "\n\n Your DFA looks like\n\n "
    for x in DFA:
        print x + "\t" + str(DFA[x])


    while response == "Y":

        toCompute = raw_input("\nPlease enter a string to check: \n")

        currentState = start

        for x in range(0, len(toCompute)):
            currentState = DFA[currentState][toCompute[x]]

        print("\nThe final state is: " + currentState + " and the accepting state(s) are: " + str(final) + "\n\n")

        if currentState in final:
            print("String accepted")
        else:
            print("String rejected")

        response = raw_input("Would you like to check another string? ")
        response.upper(response)

def getInput():
    while True:
        try:
            i = int(raw_input("How many elements are in the language? (sigma): "))
            return i
        except ValueError:
            print("Incorrect. Please try again")

def getStates():
    while True:
        try:
            i = int(raw_input("Enter the number of states: "))
            return i
        except ValueError:
            print("Incorrect. Please try again")

def getFinalStates():
    while True:
        try:
            i = int(raw_input("Enter the number of accepting states: "))
            return i
        except ValueError:
            print("Incorrect. Please try again")

if __name__ == '__main__':
    main()
