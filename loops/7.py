items = ['apple', 'orange', 'banana','apple','mango', 'orange']
u_items = []

for i in items:
    if i in u_items:
        print("Duplicate item found: ", i)
        # break ## first dupilicate found and stop the loop
    else:
        u_items.append(i)