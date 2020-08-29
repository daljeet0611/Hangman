import random # Library to generate a random number

class Hangman:
    # Array to store the predefined words
    Random_words = ["SEARCH", "VOLVO", "QUERY", "MATCH", "UPLOAD", "CURSOR", "FOLLOW", "UPDATE", "SCREEN", "REMOVE", "MEMBER", "PLACE", "NAVIGATE"]

    # Fields
    WrongLettersGuessedByUser = "" 
    randomly_selected_word = ""
    LettersGuessedByUser = ""
    Result = ""
    Lives = 0

    # ****** Select Random Word *********************
    #                                               *
    #   This function selects one word randomly      *
    #   and return                                  *
    #                                               *
    #************************************************

    def GetRandomWord(self):
        # Get random number to choose on word from words collection
        random_number = random.randint(0, 12)   
        # Select the one word from collection of words
        return self.Random_words[random_number]

    # ****** Calculate lives  ************************
    #                                               *
    #   This function return lives                  *
    #                                               *
    #************************************************

    def GetUserLives(self, randomly_selected_word):
        #Lives, given to user. equal to letters in words
        return len(randomly_selected_word)
        

    # ****** FillBlankSpaces ************************
    #                                               *
    #   This function search the location of        *
    #   letters and place them on correct position  *
    #   Fill the _ on the place of not guessed      *
    #   letters.                                    *
    #                                               *
    #************************************************

    def FillBlankSpaces(self, LettersGuessedByUser, LetterGuessByUser, RandomlySelectedWord, Result):
 
        # Making collection of guessed letters from user, to filled the guessed letters
        LettersGuessedByUser += LetterGuessByUser

        self.LettersGuessedByUser = LettersGuessedByUser
        # Clear previous result
        Result = ""
        # Selecting one letter from randomly selected word.
        for c in RandomlySelectedWord:
            # Finding selected letter in guessed letters string and filling the correct letters in blank spaces. 
            if c in self.LettersGuessedByUser:
                # Filling guessed letter
                Result += c+" "
            else: # Not guessed letter/s postion 
                Result += "_ "
        return Result
        
    # ****** IsAllSpacesFilled **********************
    #                                               *
    #   Checking the empty spaces                   *
    #   return true if no empty spaces left         *
    #   otherwise false                             *
    #                                               *
    #************************************************

    def IsAllSpacesFilled(self, Result):
        # Checking, are the all letters guessed by user?    
            if "_" not in Result: # True = All the letters guessed by user and won the game. 
                print("******* You Won *******\n\n")
                return True 
            else:
                return False # returned false if 

    # **************** RunGame **********************
    #                                               *
    #   Calling the functions in sequence to run    * 
    #   the game in stable state                    *
    #                                               *
    #                                               *
    #************************************************

    def RunGame(self):

        # While loop, to keep program runing until the end of gamel
        while True:
            if self.Lives == 0: # if user loose all the lives means end of game
                print("**** You Lose ****\n\n")
                break   # Terminate the while loop, end of game

            # Taking input from user and store into string for further use
            LetterGuessByUser = input()

            # Here upper() function is use to make letter, upper case. Reason, all the random words are in upper case.
            LetterGuessByUser = LetterGuessByUser.upper() 

            # Finding letter in randomly selected word. If exist fill the blank space
            if LetterGuessByUser in self.randomly_selected_word:
                # Calling FillBlankSpaces and LetterGuessByUser is argument.
                self.Result = self.FillBlankSpaces(self.LettersGuessedByUser, LetterGuessByUser, self.randomly_selected_word, self.Result)
                # Print the result
                print("\n"+self.Result+"\n") # Printing result after letter entered by user.
                # Searching, is there any empty space.
                if self.IsAllSpacesFilled(self.Result) == True:
                    break # Terminate the while loop, end of game. Beacuse there is no empty space.
            else: # If letter gueesed by user is not exist in randomly selected word.
                self.Lives -= 1  # User loose the one live.
                print("Live/s: "+str(self.Lives)+"\n")
                # Storing wrong letter guessed by user and print all the wrong letters in next line.
                # User can see wrong words.
                self.WrongLettersGuessedByUser += LetterGuessByUser+" "
                print("Wrong letter/s guessed by you : "+self.WrongLettersGuessedByUser+"\n")
                # Printing result after letter guessed by user.
                print("\n"+self.Result+"\n") 

    # **************** __init__ *********************
    #                                               *
    #   This function initialize the class object   *
    #   and fields                                  * 
    #                                               *
    #************************************************

    def __init__(self):

            self.WrongLettersGuessedByUser = ""
            
            self.randomly_selected_word = self.GetRandomWord()

            print(self.randomly_selected_word)
            self.Lives = self.GetUserLives(self.randomly_selected_word)
            
            print("\n\n******* Hangman by Diljeet Bains *******\n\n")
            # Print the count of lives given to user
            print("You have "+str(self.Lives)+" lives\n")

            #Preparing black spaces, equal to letters in word
            for _ in range(0, self.Lives):
                self.Result += "_ "
            #print Blank Spaces
            print(self.Result)

# >>>>>>>>>>> End of class <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Creating class object and calling RunGame function            
han = Hangman()
han.RunGame()