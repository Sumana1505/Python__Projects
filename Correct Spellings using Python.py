#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install pyspellchecker


# In[5]:


from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))


# In[ ]:





# In[ ]:




