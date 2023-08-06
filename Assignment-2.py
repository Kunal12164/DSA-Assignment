#!/usr/bin/env python
# coding: utf-8

# Q1. How do you comment code in Python? What are the different types of comments?

# In[6]:


#Ans.

# Two types of comments- single line & multi-line comment

a = print('Hello Kunal !')    #this is single line comment.

"""you can add a multiline string (triple quotes) in your code,
and place your comment inside it:"""

# """ Python program to demonstrate
#  multiline comments"""


# Q2. What are variables in Python? How do you declare and assign values to variables?

# In[ ]:


#Ans.
Variables in python like containers that stores values.

a = 5  #a is variable that stores value of 5.
b = 4



# Q3. How do you convert one data type to another in Python?

# In[9]:


#Ans. 
a = 5
print(type(a))    # data type of a is int, we want to change its datatype we can do typecast for that.

b = str(a)
print(type(b))


# Q4. How do you write and execute a Python script from the command line?

# In[10]:


#Ans.
C:\>python "d:\Python Tutorials\tut1.py"


# Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].

# In[15]:


#Ans.
my_list = [1, 2, 3, 4, 5]

sub_lst = my_list[1:3]
print(sub_lst)


# Q6. What is a complex number in mathematics, and how is it represented in Python?

# In[21]:


#Ans.

# The complex number is basically the combination of a real number and an imaginary number.
a = 45+6j
print(a.real)    #that's how we can get real number
print(a.imag)     #that's how we can get imaginary no


# Q7. What is the correct way to declare a variable named age and assign the value 25 to it?

# In[22]:


age = 25
print(age)


# Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable 
# belong to?

# In[23]:


#Ans.
price = 9.99
print(type(price))


# Q9. Create a variable named name and assign your full name to it as a string. How would you print the 
# value of this variable?

# In[24]:


name = 'kunal kumar'
print(name)


# Q10. Given the string "Hello, World!", extract the substring "World".

# In[26]:


#Ans.
a = 'Hello, World!'
a.index('World') #use to find from which index World starts with
a[7:12]


# Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are 
# currently a student or not.

# In[34]:


#Ans.

is_student = int(input("Enter 1 if you're a student else 0:\n "))

if is_student==True:
    print("You're a student")
else:
    print("You're not a student")


# In[ ]:




