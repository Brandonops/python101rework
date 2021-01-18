def yell_return(input):
    count = 0
    if len(input) > count:
        print("HELLO, " + input.upper() + "!")
        return print("YOUR NAME HAS " + str(len(input)) + " LETTERS IN IT! AWESOME!")
    else:
        return print("Oops please run the program again and enter a name!")


user_input = input("WHAT IS YOUR NAME? ")
yell_return(user_input)