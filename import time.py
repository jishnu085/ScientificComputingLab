
# importing libraries
from matplotlib.pyplot import *
from numpy import *
# import matplotlib.pyplot as plt
# import numpy as np
x = linspace(0, 2, 10) # assigning the values of x
y=x**2 # assigning the values of x^2
z=x**3 # assigning the values of x^3
fig1=figure()
plot(x, x,label='linerar') 

stem(x, y, label='quadratic') #stemploting

plot(x, z, label='cubic') #plotting x vs x^3 graph
xlabel('x label') # labeling x axis
ylabel('y label') # labeling y axis
title("Simple Plot") #titling the graph
axis([0,2,0,5]) #giving plot limit
legend() # enabling the legend
show() # displaying figure