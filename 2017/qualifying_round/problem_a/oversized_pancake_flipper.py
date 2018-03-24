#!/usr/bin/python3
#Google Jam Qualification Round 2017
#Problem A

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def flip_pancakes():
    flips = 0
    data = input().split()
    pancakes = list(data[0])
    flipper_size = int(data[1])
    pancakes_count = len(pancakes)
    
    for i in range(pancakes_count):
        #last set of pancakes, check if all +/- or mixed
        if i + flipper_size == pancakes_count:
            if pancakes[i:] and all(pcake == "+" for pcake in pancakes[i:]):
                return flips
            elif pancakes[i:] and all(pcake == "-" for pcake in pancakes[i:]):
                return flips + 1
            else: 
                return "IMPOSSIBLE"
        #iterate through pancakes and flip to happy
        if pancakes[i] == "+":
            continue
        else:
            flips += 1
            pancakes[i:i+flipper_size] = ["+" if x == "-" else "-" for x in pancakes[i:i+flipper_size]]
            
    return flips

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, flip_pancakes()))
     
    