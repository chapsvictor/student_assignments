""" wrote a code that print out age above 20 in a dictionary of some persons using function"""
def print_ages_above_20(dictionary):
    for name, age in dictionary.items():
        if age > 20:
            print(f"{name}: {age}")
dict1 = {'victor': 20, 'frank': 30, 'uche': 35}
print_ages_above_20(dict1)