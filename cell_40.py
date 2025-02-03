#!/usr/bin/env python
# coding: utf-8

# In[ ]:


y = 0
n = 1
while True:
  y = int(input(" Please enter positive number, greater than 1: "))
  x = int(input("Please enter base to check: "))
  if y > 1 and x > 1:
    break
def power_of_int(y,n,x):
  if n > y:
    return False
  elif n == y:
    return True
  else:
    n = n * x
    return power_of_int(y,n,x)
print(power_of_int(y,n,x))

