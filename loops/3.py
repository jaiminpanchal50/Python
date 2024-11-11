
for i in range(1 , 10+1):
    if i == 5:
        print("Skipped printing multiplication table for", i)
        continue
    print("Multiplication Table of", i)
    for j in range(1, 10+1):
        print(i ,"*", j,"=" ,i*j)

