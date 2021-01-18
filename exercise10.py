print("This program prints a square NxN")
user_input = int(input("How big is the square??"))

def NxN(input1):
    count = 0
    star = "*"
    while (count <= input1):
        print(star * input1)
        count += 1
        

NxN(user_input)

