day = input("Enter Day for Movie====>")
age = int(input("Enter age===>"))

if day == "wednesday":
   if age >= 18:
      print("You can watch the movie. Movie tickets pRice is $10")
   else:
      print("You can watch the movie. Movie tickets price is $6")
else:
   if age >= 18:
      print("You can watch the movie. Movie tickets pRice is $12")
   else:
      print("You can watch the movie. Movie tickets price is $8")