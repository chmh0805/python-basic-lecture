# winner_number = 10

# if winner_number > 10:
#     print("Winner_number is greater than 10")
# elif winner_number < 10:
#     print("Winner_number is less than 10")
# else:
#     print("Winner is 10")

age = int(input("how old are you?"))

print("user answer :", age)
print(type(age))

if age < 18:
    print("You can't drink.")
elif age >= 18 and age <= 35:
    print("You drink beer!")
elif age == 60 or age == 70:
    print("Birthday party!")
elif age > 70:
    print("Don't drink for health!")
else:
    print("Go ahead!")

True and True == True
False and True == False
True and False == False
False and False == False

True or True == True
False or True == True
True or False == True
False or False == False