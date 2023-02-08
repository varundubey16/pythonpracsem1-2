# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:30:15 2023

@author: Dr.Anuja B
"""

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import numpy as n

import pandas as pd
'''
#histogram
y=[10,6,8,4,2]
plt.hist(y)
plt.show()

x=n.random.randn(1000)
plt.hist(x)
plt.show()

#line plot
x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.plot(x,y)
plt.show()

#Bar plot
x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.bar(x,y)
plt.show()

my_df=pd.DataFrame(n.random.rand(10,4),columns=['a','b','c','d'])
my_df.plot.bar()

#Scatter plot
x=[5,2,9,4,7]
y=[10,5,8,4,2]
plt.scatter(x,y)
plt.show()


fig=plt.figure()
fig, ax=plt.subplots()
x=n.linspace(-1,1,50)
y=n.random.randn(50)
ax.scatter(x,y)
plt.show()
'''
#functional approach
x=n.linspace(0,10,20)
y=x**2
plt.plot(x,y)


plt.title('our first plot')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.show()


plt.subplot(1,2,1)
plt.plot(x,y,'red')
plt.subplot(1,2,2)
plt.plot(y,x,'green')
#plt.subplot(1,3,3)
#plt.plot(y,x,'blue')
