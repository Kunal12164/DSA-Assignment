#!/usr/bin/env python
# coding: utf-8

# Q1. Create one variable containing following type of data:
# 
# (i)	string
# 
# (ii)	list
# 
# (iii)	float
# 
# (iv)	tuple

# In[6]:


#Ans.

s = 'kunal kumar'
l = [1,5,5,7,2,45.6,'kunal']
f = 45.6
t = (1,4,5,6,'kunal',9,11)


# Q2. Given are some following variables containing data:
# 
# (i)	var1 = ‘ ‘
# 
# (ii)	var2 = ‘[ DS , ML , Python]’
# 
# (iii)	var3 = [ ‘DS’ , ’ML’ , ‘Python’ ]
# 
# (iv)	var4 = 1.
# 
# What will be the data type of the above given variable

# In[9]:


#Ans.

var1 = ''
var2 = '[DS,ML,Python]'
var3 =  ['DS','ML','Python']
var4 = 1.

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


# Q3. Explain the use of the following operators using an example:
# 
# (i)	/
# 
# (ii)	% 
# 
# (iii)	//
# 
# (iv)	*

# In[10]:


a = 2
b = 10

k1 = a/b
print(k1)

k2 = a%b
print(k2)

k3 = a//b
print(k3)

k4 = a*b
print(k4)


# Q4. Create a list of length 10 of your choice containing multiple types of data. Using for loop print the 
# element and its data type.

# In[17]:


#Ans.
l1 = [1,6,45.4,'kunal','sudhanshu',45+7j,'ram babu',67.8,90,6+8j]

for i in l1:
    print(i, type(i))


# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many 
# times it can be divisible.

# In[ ]:


a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd number:'))

while a<=b:
    if a%b == 0:
        print('Divisible by',a//b)
        a +=1
        
        
# Note:- Please provide me solution for this


# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is 
# divisible by 3 or not.

# In[4]:


#Ans.

l2 = [2,4,3,5,7,8,9,11,22,45,78,65,90,112,45,117,18,10,29,115,117,127,130,133,135]
for i in l2:
    if i%3 ==0:
        print(i,'This number is divisible by 3')
    else:
        print(i,'This number is not divisible by 3')


# Q7. What do you understand about mutable and immutable data types? Give examples for both showing 
# this property.

# #Ans.
# Mutable:- Mutability refers to the capability of an object to be changed or modified after its creation.
#         
# Nonmutable:- An immutable object can’t be changed after it is created. 

# In[6]:


s = 'kunal'  #string & tuple both are immutable, you can't item assignment.
s[0]='m'


# In[7]:


l3 = [2,55,67,11,23]
l3[0]=29                 #list is mutable, you can item assignment in that.


# In[8]:


l3


# In[ ]:




