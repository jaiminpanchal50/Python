age = int(input("Enter age"))

if age < 15:
    print("You can play video games!")
elif age<19:
    print("You can watch movies!")
elif age>21 & age<60:
    print("You can drink alcohol!")
else:
    print("You can't play video games, watch movies, or drink alcohol.")