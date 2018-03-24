#!/usr/bin/python3
#Google Jam Round 1A 2008
#Problem A

import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def minimum_scalar_product():
    num = int(input()) #turn around time
    
    v1 = [int(n) for n in input().split()]
    v2 = [int(n) for n in input().split()]
    
    v1.sort()
    v2.sort()
    v2.reverse()
    
    msp = 0
    
    for i in range(num):
        msp += v1[i] * v2[i]
    
    return msp
    
for i in range(int(input())):
    print("Case #{}: {}".format(i+1, minimum_scalar_product()))
     
    