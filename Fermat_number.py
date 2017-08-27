#! -*- coding:utf-8 -*-
# This program finds a solution of Fermat equation.
# You input an integer n at the first.
import sys
import math
print('Put an integer n : ',end='')
n = int(input())

c = 3
k = 3
while(True):
    for b in range(1,c):
        for a in range(1,b):
            for k in range(3,15):
                if math.copysign(c - math.pow(a**k + b**k, 1/k), 0.0) < 0.1**n:
                    if c < math.pow(a**k + b**k, 1/k):
                        print('[a,b,c] = ' + str([a,b,c]))
                        print('k = ' + str(k))
                        print(str(a) + '^' + str(k) + ' + ' + str(b) + '^' + str(k)+ ' =' + str(math.pow(a**k + b**k, 1/k)) + '^' + str(k))
                        sys.exit()                    
    c += 1    
