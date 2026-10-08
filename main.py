import random  # get random number

random_number = random.randint(1, 10)  # pick number from 1 to 10
previous_guesses = []  # store guesses
tries_remaining = 5  # 5 tries
correct_answer_picked = False  # check if they won

while tries_remaining > 0 and not correct_answer_picked:  # loop until win or no tries
    print(f"You have {tries_remaining} tries remaining.")  # show tries left
    valid_guess = False  # check if guess is valid
    while not valid_guess:  # keep asking until valid
        try:  # check input
            user_guess = int(input("Enter a number between 1 - 10: "))  # get guess
        except ValueError:  # if its not a number
            print("Invalid input! Please enter a whole number.")  # tell them its invalid
            continue  # ask again
        if user_guess < 1 or user_guess > 10:  # check range
            print("Invalid input! Please enter a number between 1 and 10.")  # invalid range
        elif user_guess in previous_guesses:  # check if guessed already
            print(f"You already guessed {user_guess}!")  # tell them its a repeat
            print("Choose a different number.")  # ask for new number
            print(f"Previous guesses: {previous_guesses}")  # show old guesses
        else:  # valid guess
            valid_guess = True  # accept guess
    previous_guesses.append(user_guess)  # add guess to list
    if user_guess == random_number:  # check if correct
        print(f"You guessed correctly! The number was {random_number}.")  # win message
        print(f"Your guesses: {previous_guesses}")  # show all guesses
        correct_answer_picked = True  # end game
    elif user_guess > random_number:  # check if too high
        print("Try again! The random number is lower!")  # tell them to go lower
        tries_remaining -= 1  # lose a try
    else:  # otherwise its too low
        print("Try again! The random number is higher!")  # tell them to go higher
        tries_remaining -= 1  # lose a try
    if not correct_answer_picked:  # if they havent won
        print(f"Previous guesses: {previous_guesses}")  # show guesses
        print(f"You have {tries_remaining} tries remaining.\n")  # show tries left
if not correct_answer_picked:  # check if they lost
    print("You ran out of tries!")  # out of tries
    print(f"Your guesses were: {previous_guesses}")  # show guesses
    print(f"The correct number was {random_number}.")  # reveal number
    print("Game over!")  # end message
