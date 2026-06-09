#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rd


# In[ ]:


import random as rd
brayden_food=["alfredo","Lasanga","country rib","gumbo","jambalaya","shrimp", "fried rice","breakfast burritos","spaghetti","salmon","sausage egg and cheese sndwch","bravado","stroganoff","turkey leg"]
randoresult=rd.sample(brayden_food,2)

while True:
    command = input("type:'run':")
    if command == "run":
        print(randoresult,"make a lot")
        break
    else:
        print("that is not run,try again")

