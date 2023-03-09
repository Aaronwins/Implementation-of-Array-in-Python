# -*- coding: utf-8 -*-
"""Array

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nNCee1EbRxKpiBJWRqWAd6ALZl1Viu1u

.py file creating our own module, import and use it

This Array implementation is like a list, but we can only use 
[], len, and str
"""

class Array(object): 
  #represents an array init helps with setting attributes
  def __init__(self, capacity, fillValue=None): #fill value being none makes it empty
    #capacity is the static size of the array 
    #fillValue is placed at each position 
    self.items = list() #creating array class based on lists, and methods 
    for count in range(capacity):
      self.items.append(fillValue) #add values in fill 
  def __len__(self):
    #capacity of the array returned
    return len(self.items)
  def __str__(self):
    return str(self.items) #self is a convention 2 pages
  def __iter__(self): #use python function
    return iter(self.items) 
  def __getitem__(self,index):
    return self.items[index] #getting the item at the given index
  def __setitem__(self, index, newItem):#setting new item to this
    self.items[index] = newItem