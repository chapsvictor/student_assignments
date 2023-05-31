my_list = [5, 3 , 7]
newlist = []
while my_list:
    min = my_list[0]
    for i in my_list:
        if i < min:
            min = i

    my_list.remove(min)
    newlist.append(min)

print(newlist)