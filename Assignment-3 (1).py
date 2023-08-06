#!/usr/bin/env python
# coding: utf-8

# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the 
# range of 1 to 25.

# In[4]:


l1 = list(range(1,26))         


# In[6]:


def odd_no(x):
    l2 = []
    for i in x:
        if i%2!=0:
            l2.append(i)
    return l2


# In[9]:


odd_no(l1)


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs 
# to demonstrate their use.

# #Ans.
# *Args:- If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# 
# **kwargs:- If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#     
#     

# In[13]:


def my_function(*kids):                            #example of *args
  print("The youngest child is " + kids[0])

my_function("kunal", "Tihar", "Lalu")


# In[12]:


def my_function(**kid):                              #example of **kwargs
  print("His last name is " + kid["lname"])

my_function(fname = "Kunal", lname = "kumar")


# Q3.  What is an iterator in python? Name the method used to initialise the iterator object and the method 
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 
# 16, 18, 20].

# In[16]:


#Ans.
# An iterator is an object that contains a countable number of values. Insitialise method is iter() & next() to use for iteration.

s1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
s2 = iter(s1)





# In[17]:


next(s2)


# In[18]:


next(s2)


# In[19]:


next(s2)


# In[20]:


next(s2)


# In[21]:


next(s2)


# Q4.  What is a generator function in python? Why yield keyword is used? Give an example of a generator 
# function.

# In[4]:


# # A generator function in Python is a function that uses the yield keyword to return a sequence of values. 
# Yield is inbuild function, it must use to return the value while using generator function.

def inf_sequence(n):
    a = 0
    while a<=n:
        yield a
        a += 1


# In[8]:


for i in inf_sequence(20):
    print(i)


# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the 
# first 20 prime numbers.

# In[26]:


#a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.
def primes():
    """Create a generator function for prime numbers less than 1000."""
    yield 2
    primes_list = [2]
    for i in range(3, 1000):
        is_prime = True
        for prime in primes_list:
            if i % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes_list.append(i)
            yield i

prime_gen = primes()
# the next() method to print the first 20 prime numbers.
for i in range(20):
    print(next(prime_gen))


# Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

# In[28]:


#a python program to print the first 10 Fibonacci numbers using a while loop.
def fibonacci(n):
    """This function will print fibonacci sequence"""
    a, b = 0, 1
    count = 0
    while count < n:
        print(a)
        a, b = b, a + b
        count += 1

fibonacci(10)
    


# Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# 
# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']

# In[38]:


s = 'pwskills'
l2 = []
for i in s:
    l2.append(i)
print(l2) 


# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

# In[4]:


#a python program to check whether a given number is Palindrome or not using a while loop.
i = int(input("Please give a number : "))
x = i
r = 0
while i>0:
    r = r*10+i%10
    i=i//10
    
if x == r:
    print("Given number is a palindrome")
else:
    print("Given number is a not palindrome") 


# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# 
# Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter 
# out odd numbers.

# In[14]:


l2 = list(range(1,101))


# In[19]:


def odd_no(x):                                 #create a function to filter odd nos from the given list.
    a=list(filter(lambda x : x%2!=0,x))
    return a


# In[20]:


odd_no(l2)


# In[ ]:




