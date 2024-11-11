
even = 0
for i in range(1, 51):
  if i % 2 == 0:
    even += i
    print("Even number", i)
  else:
    print("Odd number", i)

print("Sum of even numbers from 1 to 50:", even)