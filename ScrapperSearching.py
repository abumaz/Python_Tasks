# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:36:34 2019

@author: User
"""
import csv
def search(t):
    with open('new_quotes.csv', 'r') as reader:
        read=csv.reader(reader)
        for i in read:
            if i==[]:
                continue
            if t in i[2]:
                print("\n"+i[0])
                

n=int(input("Enter the number of tags to search for: "))
for i in range(n):
    tag=input("Enter the tag to search for: ")
    search(tag)
