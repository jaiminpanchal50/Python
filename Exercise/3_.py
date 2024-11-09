marks = 919

if marks >= 101:
   print("Invalid Marks")
   exit()   # Exit early or stop executing code 

if marks >= 90:
   grade = "A"
elif marks >= 80:
   grade = "B"
elif marks >= 70:
   grade = "C"
elif marks >= 60:
   grade = "D"
else:
   grade = "F"


print(grade)