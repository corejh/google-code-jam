#!/usr/bin/python3
#Google Jam Qualification Round 2017
#Problem B

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def find_tidy(start_number="missing"):
    if start_number == "missing":
        number = list(input()) #input as list for convenience
    else:
        number = start_number
    digits = len(number)

    #Scan each digit left->right for tidiness
    #When you find a spot that is greater than the next digit,
    #subtract enough such that the remaining digits turn into something
    #like XXX999. At this point the back half is gauranteed to be tidy.
    #Run tidiness subroutine again in case subtraction changed previous nums.
    for i in range(digits):
        if i + 1 == digits: #last digit
            if number[i] == "0":
                number = str(int(number)-1)
                return find_tidy(number)
            return ''.join(number) #is tidy
        if number[i] > number[i+1]:
            number = list(str(int(''.join(number)) - (int(''.join(number[i+1:])) + 1)))
            return find_tidy(number)

    return ''.join(number) #is tidy

# def is_tidy(number = 0):
#     n = list(number)
#     for i in range(len(number)):
#         if n[i] > n[i+1] and n[i+1]:
#             return false
#     return true

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, find_tidy()))
     
    