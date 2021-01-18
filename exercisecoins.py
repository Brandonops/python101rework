print("This program will give you coins if you want another one! You start with no coins!")
print("You have 0 coins:)")
user_input = (input("Do you want another coin?"))

count = 0
while count >= 0:
    if user_input == "yes":
        print("You have %s coins." % (count))
        count += 1
        more_coins = input("Do you want another coin? ")
        if more_coins == "no":
            break
            
else:
    print("Bye")