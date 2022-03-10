#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[1]:


print(pow(7,4))


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[2]:


text="Hi there dad!"


# In[3]:


print(text.split())


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[4]:


s="The diameter of {} is {} kilometers"


# In[5]:


print(s.format("Earth",12742))


# ** Given this nested list, use indexing to grab the word "hello" **

# In[8]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[10]:


print(lst[3][1][2][0])


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[12]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[13]:



print(d['k1'][3]["tricky"][3]['target'][3])


# ** What is the main difference between a tuple and a list? **

# # tuple is immutable,and list is mutable

# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[15]:


def domainGet(email):
    print("Your domain is:" + email.split('@')[-1])


# In[16]:


email = input("Please enter your email:>")
domainGet(email)


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[17]:


def findDog(st):
    if 'dog' in st.lower():
        print("True")
    else:
        print("False")


# In[19]:


st=input("please key a string:>")
findDog(st)


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[ ]:


def countdogs(string):
    count=0
    for word in string.lower().split():
        if word=='dog' or word=='dogs':
            count=count+1
            print(count)
countdogs(string)            


# In[ ]:


string=input("please enter the string:")


# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[ ]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[ ]:


speeding=input("enter the speed:")
caught_speeding(speed,is_birthday)


# In[ ]:


speeding=input("enter the speed:")
caught_speeding(speed,is_birthday)


# # Great job!
