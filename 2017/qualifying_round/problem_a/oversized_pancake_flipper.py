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
    
    #print(pancakes, flipper_size)
    
    for i in range(pancakes_count):
        if i + flipper_size == pancakes_count:
            #last set of pancakes
            if pancakes[i:] and all(pcake == "+" for pcake in pancakes[i:]):
                return flips
            elif pancakes[i:] and all(pcake == "-" for pcake in pancakes[i:]):
                return flips + 1
            else: 
                return "IMPOSSIBLE"    
        if pancakes[i] == "+":
            #print(pancakes[0:i], pancakes[i], pancakes[i+1:])
            continue
        else:
            flips += 1
            pancakes[i:i+flipper_size] = ["+" if x == "-" else "-" for x in pancakes[i:i+flipper_size]]
            #pancakes[i:i+flipper_size] = pancakes[i:i+flipper_size].replace("+","x").replace("-","+").replace("x","-")
            #print(pancakes[0:i], pancakes[i:i+flipper_size], pancakes[i+flipper_size-1:])
            #print(''.join(pancakes))
            
    return flips

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, flip_pancakes()))
     
    