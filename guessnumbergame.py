import os
import random
import time

def game(a):
    global count
    ans = random.randint(1, a)
    used_number = []
    count = 1
    def guessing():
        global count
        print(f"Guess the number between 1 and {a}")
        num = int(input())
        while num != ans:
            if num in used_number:
                print("You've guessed this number!")
                time.sleep(1)
            if num == str:
                print("You can only type number!")
                time.sleep(1)
                os.system("cls")
            if num not in used_number:
                used_number.append(num)
            if ans > num:
                print("Higher!")
            elif ans < num:
                print("Lower!")
            print(f"Guess the number between 1 and {a}")
            num = int(input())
            count += 1
        else:
            print(f"Correct! The number was {num} and you've guessed {count} times")
        replay = str(input("Do you want to replay? : ").lower())
        if replay == "y" or "yes":
            os.system("cls")
            menu()
        elif replay == "n" or "no":
            os.system("cls")
            quit()
        else:
            print("That not in option!")
            time.sleep(1)
            os.system("cls")
    guessing()

def menu():
    print("Select Difficulty\n\"E\" for Easy\n\"M\" for Medium\n\"H\" for Hard\n\"N\" for Nightmare\n\"I\" for Impossible")
    difficulty = str(input(": ").lower())
    if difficulty == "e":
        os.system("cls")
        game(10)
    elif difficulty == "m":
        os.system("cls")
        game(50)
    elif difficulty == "h":
        os.system("cls")
        game(100)
    elif difficulty == "n":
        os.system("cls")
        game(1000)
    elif difficulty == "i":
        os.system("cls")
        game(10000)
    else:
        print("That not in option!")
        time.sleep(1)
        os.system("cls")
        menu()

menu()