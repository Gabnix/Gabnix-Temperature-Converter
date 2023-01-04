#
# conversions.py: module with functions to convert between units
#
# fahr2cel : Convert from Fahrenheit to Celsius.
#

import random


def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius.
    Argument: fahr - the temperature in Fahrenheit
    """
    celsius = (fahr-32) * (5/9)
    return celsius


def cel2fahr(cel):
    """Convert from Fahrenheit to Celsius.
    Argument: cel - the temperature in Celsius
    """
    fahr = (cel*1.8) + (32)
    return fahr


def fahr2kel(fahr):
    """Convert from Fahrenheit to Kelvin.
    Argument: fahr - the temperature in Fahrenheit
    """
    kel = ((fahr-32) * (5/9) + 273.15)
    return kel


def kel2fahr(kel):
    """Convert from Kelvin to Fahrenheit.
    Argument: kel - the temperature in Kelvin
    """
    fahr = (1.8 * (kel-273)) + 32
    return fahr


def cel2kel(cel):
    """Convert from Celsius to Kelvin.
    Argument: cel - the temperature in Celsius
    """
    kel = cel + 273.15
    return kel


def kel2cel(kel):
    """Convert from Kelvin to Celsius.
    Argument: kel - the temperature in Kelvin
    """
    cel = kel - 273.15
    return cel


def test():
    test_fahr = random.randint(0, 100)
    test_cel = fahr2cel(test_fahr)
    print(f"Fahrenheit: {test_fahr}\nCelsius: {test_cel}\n")


def yes_no():
    print("Do you want another conversion? ", end="")
    answer = input().upper()
    return answer


def main():
    index = 1
    while True:
        print(f"\nConversion {index}")
        test()
        index += 1
        answer = yes_no()
        if answer == "Y":
            continue
        else:
            break
    print('\n---> Testing complete')


if __name__ == '__main__':
    main()
