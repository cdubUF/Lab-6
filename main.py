def encoder(password):
    final_res = ""
    for n in password:
        if n == "1":
            res = str(4)
        elif n == "2":
            res = str(5)
        elif n == "3":
            res = str(6)
        elif n == "4":
            res = str(7)
        elif n == "5":
            res = str(8)
        elif n == "6":
            res = str(9)
        elif n == "7":
            res = str(0)
        elif n == "8":
            res = str(1)
        elif n == "9":
            res = str(2)
        elif n == "0":
            res = str(3)
        final_res += res
    return final_res


def decoder(password):
    new_password = ""
    for char in password:
        new_char = (int(char) + 7) % 10
        new_password += str(new_char)
    return new_password


def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


def main():

    game_continue = True
    print_menu()
    option = int(input("Please enter an option: "))
    password = input("Please enter your password to encode: ")
    if option == 1:
        print("Your password has been encoded and stored!\n")
    elif option == 2:
        print(f"The encoded password is {encoder(password)}, and the original password is {decoder(encoder(password))}.")
        pass
    elif option == 3:
        game_continue = False
    while game_continue:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoder(password)}, and the original password is {decoder(encoder(password))}.")
        elif option == 3:
            game_continue = False


if __name__ == "__main__":
    main()