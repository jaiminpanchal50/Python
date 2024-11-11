#  way-1

nums = [1,-2,3,-4,5,6,-7,-8,9,10]

negative_nums = []
positive_nums = []

for i in nums:
    if i < 0:
        negative_nums += [i]
    else:
        positive_nums += [i]


print("count of positive number is ",len(positive_nums)  ,positive_nums)
print("count of negative number is ",len(negative_nums)  ,negative_nums)



#  way-2
# nums = [1,-2,3,-4,5,6,-7,-8,9,10]

# positive_nums_count = 0

# for i in nums:
#     if i > 0:
#        positive_nums_count +=1
#     else:
#         positive_nums_count

# print(positive_nums_count)
