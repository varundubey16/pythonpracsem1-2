#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


data = {'name': ['John', 'Marie', 'Bob', 'Alice'],
        'age': [32, 24, 45, 27],
        'country': ['USA', 'Canada', 'UK', 'Australia']}

dict_df = pd.DataFrame(data)
print(dict_df)


# In[14]:


data = [['John', 32, 'USA'],
        ['Marie', 24, 'Canada'],
        ['Bob', 45, 'UK'],
        ['Alice', 27, 'Australia'],
        ['Tom', 25, 'Germany'],
        ['Sandy', 31, 'Ireland'],
        ['Alex', 29, 'UK'],
        ['Jackson', 38, 'China'],
        ['Mark', 37, 'South Korea'],]

list_df = pd.DataFrame(data, columns=['name', 'age', 'country'])
print(list_df)

#df = list_df


df1=pd.read_csv("iris.csv")
print(df1)
print(df1.head())

print(df1.head(6))

# In[15]:

'''
print("First five datasets")
df.head()


# In[ ]:


print("Last five datasets")
df.tail()


# In[23]:


print("Column names:")
df.columns


# In[22]:


print("Data types:")
df.dtypes


# In[21]:


print("DataFrame Shape:")
df.shape


# In[25]:


# Select a single column from the DataFrame
df['name']

# Select multiple columns from the DataFrame
df[['name', 'age']]

# Select a row from the DataFrame using the index
df.loc[0]

# Select rows from the DataFrame based on a condition
df[df['age'] > 30]


# In[29]:


# Add a new column to the DataFrame
df['profession'] = ['doctor', 'teacher', 'engineer', 'artist','doctor', 'teacher', 'engineer', 'artist', 'doctor']
print(df)

print()

# Delete a column from the DataFrame
df.drop('profession', axis=1, inplace=True)
print(df)


# In[31]:


# Add a new row to the DataFrame
# new_row = {'name': 'Tom', 'age': 36, 'country': 'Germany'}
# df = df.append(new_row, ignore_index=True)
# print(df)

# Delete a row from the DataFrame
df.drop(0, inplace=True)
print(df)

'''