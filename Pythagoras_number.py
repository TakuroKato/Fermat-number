#! -*- coding:utf-8 -*-
# This program finds nth Pyuthagoras Number.
# You input an integer n at the first.
import sys
print('Put an integer n :',end='')
n = int(input())
print('Here is ' + str(n) + ' sets of  Pyuthagoras Numbers.\n')
print('n : [a, b, c]\n')

a = 1
b = 2
c = 3
i = 0
while(True):
    for b in range(c):
        for a in range(b):
            if a**2 + b**2 == c **2:
                print(str(i+1) + ' : ' + str([a,b,c]))
                i += 1
                if(i == n):
                    sys.exit()                    
    c += 1
    
