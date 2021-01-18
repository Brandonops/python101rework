print("This program counts all numbers between your start and end number!")
user_start = int(input("Start from: "))
user_end = int(input("End on: "))


def num_counta(num1, num2):
    while (num1 <= num2):
        print(num1)
        num1 += 1
        if num1 == num2 +1:
            break


num_counta(user_start, user_end)