import speech_to_text as s2t
import sentiment as sen

programLoop = True

while programLoop:
    # Clearing old 'output.txt' by opening it in "w" mode, which truncates the file to zero length
    with open("output.txt", "w") as clearOldFile:
        print("Old file cleared")


    # Loop until valid option is entered
    while True:
        try:
            # Prompting a user to enter 'num'
            num = int(input("\nEnter a number of sentences you want to analyze: "))
            if num >= 1:
                # Ending loop if input is natural number greater or equel 1
                break
            else:
                # Raising an error in other case
                raise ValueError
        except ValueError as e:
            # Prompting a user if he entered something else than natural number greater or equel 1
            print("\nPlease enter a natural number greater or equel 1.\n")

    s2t.speech_to_text(num)

    with open("output.txt", "r") as rdyToAnalyze:
        for line in rdyToAnalyze:
            sen.analyze_sentiment(line)

    while True:
        try:
            programAns = input("Continue?[y/n]")

            if programAns.lower() == "y":
                programLoop = True
            elif programAns.lower() == "n":
                programLoop = False
            else:
                raise ValueError
            break
        except ValueError:
            print("\nInvalid response. Please enter 'y' or 'n'\n")
