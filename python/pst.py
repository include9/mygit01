#coding: utf-8 

import math
'''
def quadratic(a, b, c):
    x1=(math.sqrt(b*b-4*a*c)-b)/2/a
    x2=(-math.sqrt(b*b-4*a*c)-b)/2/a
    return x1,x2

classmate = ['Michael', 'Bob', 'Tracy']
classmates = ['Michael', 'Bob', 'Tracy',classmate]
print(classmates.pop(-1))
print(classmates)

L = ['Bart', 'Lisa', 'Adam']
while len(L)!=0 and 1!=2:
    print(L.pop())

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d.pop('Bob'))
print(d)
'''
'''
x=5000
i=0

def s(s1,s2=60000):
    return s1*1.035+s2
while x<10000000:
    i=i+1
    x=s(x)
    print("NO",i,"year:",x)
    print("                                   total interest:",x-5000*(1.02**i)-i*60000)
'''
import random

for tt in range(100):
    
    j = 0

    for i in range(5):
       s = random.choice("abc")  # 随机选择1个
       if s == "c" and j:
           break
       print(s, end="")
       j += 1
    print()
