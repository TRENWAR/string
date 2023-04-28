import os
import time


# COLOR
WHITE = "\033[37m"
CYAN = "\033[36m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
PINK = "\033[95m"
RED = "\033[91m"


def len_in_python():
    print("The len() function returns the number of items in an object")
    time.sleep(0.5)
    print(
        "When the object is a string, the len() function returns the number of characters in the string"
    )
    user = input("Want to try it Y/n: ")
    if user in ["y", "yes", "Y"]:
        print("Type something")
        user = input("~~> ")
        calculate_typed_users = len(user)
        time.sleep(0.4)
        print(calculate_typed_users)
        print(f"the characters you type are {calculate_typed_users} characters")
        time.sleep(0.4)
        print("spaces are also counted")

    else:
        print("oke")
        time.sleep(0.6)
        main_menu()


def main_menu():
    os.system("clear")
    time.sleep(0.3)
    print(10 * "=" + "Welcome" + 10 * "=")
    print("Welcome to this tools\r\nThis tools can manipulate string (using Python)")
    print("1.Use len()")
    user_input = input("~~> ")
    if user_input == "1":
        len_in_python()
    else:
        pass


def choose_color():
    os.system("clear")
    print(10 * "=" + "Welcome" + 10 * "=")
    print("Before we start, please select the color first")
    print(
        "1.Original (white (cuz you're original & simple boy)\r\n2.Red (cuz you like Red..??)\r\n3.Yellow (cuz idk why)\r\n4.Pink (cuz u watched Barbie or something)\r\n5.Cyan (cuz that a nice color???)\r\n6.Green (cuz u want to look like Hacker (fck)"
    )
    user_input = input("~~> ")

    if user_input == "1":
        print(WHITE + "Nice, this is what i've been waiting for 20 years...Nice :)")
        time.sleep(0.8)
        main_menu()

    elif user_input == "2":
        print(RED + "Nice, i mean pretty nice :)")
        time.sleep(0.9)
        main_menu()

    elif user_input == "3":
        print(YELLOW + "Oke")
        time.sleep(0.4)
        main_menu()

    elif user_input == "4":
        print(PINK + "Nice fcking choise :D")
        time.sleep(0.8)
        main_menu()

    elif user_input == "5":
        print(CYAN + "Cool mode on i mean Cyan")
        time.sleep(0.6)
        main_menu()

    elif user_input == "6":
        print(
            GREEN
            + "if u like green & u choose this Np\r\nbut if u wan't to look like Hacker this is not hacking tools Wtf\r\nbut Np u can use this tools Xd"
        )
        time.sleep(0.4)

        user_input = input("So do u wan't to use my tool Y/n: ")
        if user_input == "Y":
            print("Oke")
            time.sleep(0.4)
        else:
            print("Oke")

    else:
        print("Im serious")
        time.sleep(0.5)
        choose_color()


if __name__ == "__main__":
    choose_color()
