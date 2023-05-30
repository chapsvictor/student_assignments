lst = [1,-2,3,4,-7,5]
sum_num = 0
for num in lst:
    if num > 0:  
        sum_num += num
    else:
        break

print(sum_num)
