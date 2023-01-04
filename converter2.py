#
# converter.py: convert between temperature formats - Fahrenheit, Celsius and Kelvin
#

from conversions import *

class InvalidSelectionError(Exception):
    pass


class NoValueError(Exception):
    pass


def input_number(message):
    while True:
        try:
            userInput = int(input(message))
            while userInput < 1 or userInput > 7:
                print("Invalid index! Try again.\n")
                userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again.\n")
            continue
        else:
            return userInput
            break


def main_menu(conversion_style):
    print("\n=== TEMPERATURE CONVERSION MACHINE ===\n")
    for index, conv in enumerate(conversion_style):
        print(f"{index+1} -", conv)
    user_input = input_number("Choose your conversion: ")
    return float(user_input)


def main():
    conversion_style = ["Fahrenheit to Celsius", "Fahrenheit to Kelvin",
                        "Celsius to Fahrenheit", "Celsius to Kelvin",
                        "Kelvin to Fahrenheit", "Kevin to Celsius", "Exit..."]
    user_input = main_menu(conversion_style)
    if user_input != 7:
        input_valueS = input("\nEnter temperature: ")
    else:
        exit()
    
    while input_valueS:
        input_value = float(input_valueS)
        if user_input == 1:
            result = fahr2cel(input_value)
            
        elif user_input == 2:
            result = fahr2kel(input_value)

        elif user_input == 3:
            result = cel2fahr(input_value)

        elif user_input == 4:
            result = cel2kel(input_value)

        elif user_input == 5:
            result = kel2fahr(input_value)

        elif user_input == 6:
            result = kel2cel(input_value)

        elif user_input == 7:
            input_valueS = False
            break
        
        print(f"Converted temperature: {result}")
        input_valueS = input("\nEnter temperature: ")

    print("\nGoodbye!\n")


if __name__ == "__main__":
    main()
