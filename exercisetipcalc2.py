print("This program is a tip calculator!")
user_bill = float(input("Please enter the total bill amount: "))
user_service_input = (input("Please enter the level of service(ex: good, fair, or bad): "))
split_bill = int(input("Split how many ways? "))

if user_service_input == "good":
    tip1 = user_bill * .2 
    print("Tip amount: $%.2f " % (tip1))
    total_amount1 = tip1 + user_bill
    print("Total amount: $%.2f " % (total_amount1))
    amount_per1 = total_amount1 / split_bill
    print("Amount per person: $%.2f " % (amount_per1))

elif user_service_input == "fair":
    tip2 = user_bill * .15 
    print("Tip amount: $%.2f " % (tip2))
    total_amount2 = tip2 + user_bill
    print("Total amount: $%.2f " % (total_amount2))
    amount_per2 = total_amount2 / split_bill
    print("Amount per person: $%.2f " % (amount_per2))


elif user_service_input == "bad":
    tip3 = user_bill * .10 
    print("Tip amount: $%.2f " % (tip3))
    total_amount3 = tip3 + user_bill
    print("Total amount: $%.2f " % (total_amount3))
    amount_per3 = total_amount3 / split_bill
    print("Amount per person: $%.2f " % (amount_per3))
