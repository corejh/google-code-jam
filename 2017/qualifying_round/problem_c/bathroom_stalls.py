#!/usr/bin/python3
#Google Jam Qualification Round 2017
#Problem C

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def fill_stalls():
    num_stalls, num_people = map(int, input().split())    
    stalls = ['.'] * num_stalls
    
    for i in range(num_people):
        return 0
    
    #print(stalls,"|",num_people)
    return 0

# def is_tidy(number = 0):
#     n = list(number)
#     for i in range(len(number)):
#         if n[i] > n[i+1] and n[i+1]:
#             return false
#     return true

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, fill_stalls()))
     
    