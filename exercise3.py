print("Please fill in the blanks below: ")
print("____(name)____'S favorite subject in school is ___(subject)___.")

def mad_libs(input1, input2):
    return print((f"{input1}'s favorite subject in school is {input2}."))

user_name = input("What is the name? ")
user_subject = input("What is the subject? ")

mad_libs(user_name, user_subject)