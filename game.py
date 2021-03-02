"""A number-guessing game."""
# Put your code here
#The computer will choose a random number between 1-100 and ask the user to guess the number
#Once the user guesses, the computer will tell the user if their guess was too high or too low
#The game is over once the user guesses the computer's number. When the game is over, 
#the computer the total number of guesses the user made before guessing the right answer
print('Hi')
name = input('What is your name? ')
print(name)
game_winning_number = 23
guess_container = [] #stores all the users responses
print("I'm thinking of a number between 1 - 100")
guess_count = 0
guess = 0

    
while guess != game_winning_number : #If the user does not guess the number correctly, then they will have t
    guess = int(input("Enter guess: "))
    if guess != game_winning_number: #
        if guess < 1 or guess > 100:
            print("invalid number")
            break
        guess_container.append(guess)
        if guess < game_winning_number: #
            print("Your guess is too low, try again")
            guess_count += 1  #
        elif guess > game_winning_number: #
            print("Your guess is too high, try again")
            guess_count += 1
    else:
        print("You won! Your lucky number was " + str(guess))
        guesses_printout = str(len(guess_container))
        print(guesses_printout + " guesses")

