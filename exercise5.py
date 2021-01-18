user_input = int(input("Day (0-6)? "))
def days(input1):
    if input1 <= 6:
        if (input1 == 0) or (input1 == 6):
            print("Sleep in! It's the weekend!")
        else: 
            print("You need to go to work!")
    else:
        print("Please rerun the program and enter a number 0-6! ")

days(user_input)