print("This program converts Celsius to Fahrenheit!")
user_input = float(input("Please enter a temperature in Celsius: "))


def celc(num1):
    F = (num1 * 9/5) + 32
    return print(str(F) + " F")


celc(user_input)