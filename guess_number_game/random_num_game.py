from random import randint


def get_guess(low, high, current_attempt_num):
    while True:
        try:
            user_guess = int(input(f"try {current_attempt_num} - Your guess: "))
        except ValueError:
            print(
                f"You entered a string please enter a whole number between {low} and {high}, (this try did not count)"
            )
            continue

        if user_guess >= low and user_guess <= high:
            return user_guess
        print(
            f"Number out of range pleas enter a number between {low} and {high} (this try did not count)"
        )


def play_game(low, high, current_attempt, secret):
    guess = get_guess(low, high, current_attempt)
    if guess == secret:
        return "won"
    elif guess > secret:
        return "high"
    elif guess < secret:
        return "low"


def show_result(status, tries_left, attempts):
    if status == "won":
        print(f"You won! you found the number in {attempts} tries.")
        return True
    elif status == "high":
        print(f"Too high! {tries_left} tries left. ")
        return False
    elif status == "low":
        print(f"Too low! {tries_left} tries left. ")
        return False


def game_start_message():
    print("Welcome to guess the Number!")
    print(
        f"i have picked a number between {minimum_number} and {maximum_number}. you have {max_attempts} tries."
    )


def set_difficulty():
    while True:
        difficulty = input("input your desired difficulty (easy, normal, hard): ")
        if (
            difficulty.strip().lower() == "easy"
            or difficulty.strip().lower() == "normal"
            or difficulty.strip().lower() == "hard"
        ):
            break
        print("please enter one of the correct options. ")

    if difficulty == "easy":
        return 1, 50, 5
    elif difficulty == "normal":
        return 1, 100, 7
    else:
        return 1, 1000, 10


def give_hint(secret):
    if secret % 2 == 0:
        print("Here is a hint, the number is even.")
    else:
        print("Here is a hint, the number is odd.")


# main

minimum_number, maximum_number, max_attempts = set_difficulty()
attempts_so_far = 1

secret = randint(minimum_number, maximum_number)

game_start_message()

hint_round = 3

while attempts_so_far <= max_attempts:
    won_flag = show_result(
        play_game(minimum_number, maximum_number, attempts_so_far, secret),
        max_attempts - attempts_so_far,
        attempts_so_far,
    )
    attempts_so_far += 1

    if attempts_so_far == hint_round + 1 and not won_flag:
        give_hint(secret)

    if attempts_so_far == max_attempts + 1 and not won_flag:
        print("You Lost!")
        print(f"The secret number was {secret}.")
        won_flag = True

    if won_flag:
        play_again = input("Play again? (y/n): ")
        if play_again.strip().lower() != "n":
            attempts_so_far = 1
            minimum_number, maximum_number, max_attempts = set_difficulty()
            secret = randint(minimum_number, maximum_number)
            game_start_message()

        else:
            print("Thank you for playing! Goodbye.")
            break
