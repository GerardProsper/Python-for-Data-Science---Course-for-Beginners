#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def notnumeric(*args):
    for x in args:
        if not(isinstance(x,(int,float))):
            return False
        return True

def addallNumerics(*args):
    s = 0
    for x in args:
        s += x
    return s

myName = "Python Course"

