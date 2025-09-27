#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 12:50:40 2025

@author: dinhbatan
"""

from collections import deque 

dq = deque([1,2,3,4])

print(f"The intial values are{dq}")

dq.append(6)


print (f"the values are {dq}")

dq.pop()
print(f"The values are {dq}")
dq.popleft()
print(f"The values are {dq}")

dq.extend([6,7,8])
print(f"The values are {dq}")
dq.extendleft([-1,-2,])    
print(f"The values are {dq}")

queue =deque()
queue.extend(["customer1", "customer2","customer3", "customer4"])
print(queue)

while queue:
    served =queue.popleft()
    print(f"Served: {served}---Inquee{queue}")
print("the queue is empty", queue)