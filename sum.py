collins2
"""A list of numbers were great woth both positive numbers and negative numbesr. 
I wrote a program to sum the positive numbers and break out when negative number is reach .  """
mylist= [-1, 2,-3,4,5]
sum_list=0
for num in mylist:
    if num < 0:
        break
    if num>=0:
        sum_list=num+num
print(sum_list)

