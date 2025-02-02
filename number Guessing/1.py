import random

print('Hi. Welcome to Number Guessing Game. \nYou got 7 chances to guess the number.Lest start the Game,shall we? ')

chances=7

while True:
    
    number_to_guess=random.randrange(1,101)

    guess_counter=0
    
    while guess_counter < chances:
        guess_counter+=1
        try:
            my_guess=int(input("please enter your guess: "))
        except ValueError:
            print("enter a valid number")
            guess_counter -=1 #dont count invalid numbers 
            continue
        
        if my_guess==number_to_guess:
            print(f'You won! you guessed the number {number_to_guess} with {guess_counter} attemps')
            break
        
        elif my_guess > number_to_guess:
            print("your guess is to high.try again")
            
        elif my_guess < number_to_guess:
            print("go higher , you guessed less")
            
    if guess_counter > chances and my_guess != number_to_guess:
        print(f'Better luck next time. The number is {number_to_guess}.')
        
    next_game=input("do another guessing? (yes/no)").strip().lower()
    if next_game=="no":
        print("See you next time . Ciao")
        break

    

    