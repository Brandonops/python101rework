user_input = int(input("Day (0-6)? "))
def days(input1):
    if input1 <= 6:
        if user_input == 0:
            print("Sunday")
        elif user_input == 1:
            print("Monday")
        elif user_input == 2:
            print("Tuesday")
        elif user_input == 3:
            print("Wednesday")
        elif user_input == 4:
            print("Thursday")
        elif user_input == 5:
            print("Friday")
        elif user_input == 6:
            print("Saturday")
    else:
        print("Please rerun the program and enther a number! ")

days(user_input)