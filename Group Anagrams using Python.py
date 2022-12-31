#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        dfdict[sorted_i].append(i)
    return dfdict.values()


# In[2]:


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))


# In[ ]:




