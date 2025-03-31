import math
import random


def get_user_name():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(game_logic, game_description):
    name = get_user_name()
    print(game_description)

    for _ in range(3):  # Три раунда
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def game_lcm():
    numbers = [random.randint(1, 100) for _ in range(3)]
    question = " ".join(map(str, numbers))
    answer = math.lcm(*numbers)  # Считаем НОК
    return question, answer


def game_progression():
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


def main():
    print("Choose a game:\n1 - Least Common Multiple (LCM)\n2 - Geometric Progression")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        run_game(game_lcm, "Find the smallest common multiple of given numbers.")
    elif choice == "2":
        run_game(game_progression, "What number is missing in the progression?")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()