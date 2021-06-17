#!/usr/bin/env python
# coding: utf-8

# ####  Write a function which takes two arguments: a list of customers and the number of open cash registers. Each customer is represented by an integer which indicates the amount of time needed to checkout. Assuming that customers are served in their original order, your function should output the minimum time required to serve all customers.
# Example:
# get_checkout_time([5, 1, 3], 1) should return 9
# get_checkout_time([10, 3, 4, 2], 2) should return 10 because while the first register is busy serving customer[0] the second register can serve all remaining customers.

# In[5]:


def checkout_time(customers, cash_registers):
    if cash_registers == 1:
        return sum(customers)
    elif len(customers) <= cash_registers:
        return max(customers)

    registers = {}
    for i in range(cash_registers):
        registers[i] = customers.pop(0)

    count = 0
    while any(registers.values()):
        for j in registers.copy():

            registers[j] -= 1
            if registers[j] <= 0:
                try:
                    registers[j] = customers.pop(0)
                except IndexError:
                    registers[j] = 0
        count += 1
    return count


print(checkout_time([5, 1, 3], 1))
print(checkout_time([10, 3, 4, 2], 2))


# #### Write a function that satisfies the following rules:
# #### Return true if the string in the first element of the list contains all of the letters of the string in the second element of the list.
# examples
# ["hello", "Hello"]
# should return true because all of the letters in the second string are present in the first, ignoring case.
# ["hello", "hey"]
# should return false because the string "hello" does not contain a "y".
# ["Alien", "line"]
# should return true because all of the letters in "line" are present in "Alien".

# In[7]:


def func(lst):
    x=lst[0].lower()
    y=lst[1].lower()
    c=0
    c2=0
    for j in y:
        if j in x:
            c+=1
        else:
            c2+=1
    if c2>=1:
        print("False")
    else:
        print("True")
        
#lst = []
#for i in range(0,2):
#    lst.append(input()) 
#print(lst)
func(["hello", "Hello"])
func(["hello", "hey"])
func(["Alien", "line"])


# In[ ]:




