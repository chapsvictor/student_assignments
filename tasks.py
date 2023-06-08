'''
User will enter a floating type number.Your task is to find out the integer portion of the number
 before the point and then check if that number is an even portion or not?
'''
x = float(input('Enter any real number: '))
y = round(x)
if x > 0:
    if  y > x:
        intp = y+1
    else:
        intp = y
else:
    if y < x:
        intp = y + 1
    else:
        intp = y
if intp%2 == 0:
    print('Integer is even,Bravo')
else:
    print('Not Correct')






