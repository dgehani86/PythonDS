# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
#-------Number data type-----
value1 = 12
value2 = 10
resultsum = value1+ value2
resultdiv = value1 / value2
resultexp = value1**value2
resultmul = value1*value2
result_float = float(value1*value2)
salary = 1000.00
intsal = int(salary)
#-------String data type single or double quotes-----
name = "Deepak Gehani"
print(name[0])
print(name[1:5]) #sliceoperator
print(name[1:])
print(name*2)
string2= name[-1] + name[+1]
"G" in name
age = 32
print(name + " has age " + str(age))
sample = """it is very good day today
            we enjoyed"""
print(sample)

a,b,c = 1,2,"Dpk"

print(str(b) + c)

#-------List data type-----
students = ["Rishab", "Kumar","Maria", "Nitin", "Rahul"]
list1 = ['deepak', 716 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print (list1)
print (students[0] + list1[0]) 
print (list1[2:])

students.append("Amit")
print (students)
students.extend([1,23,34,55,67])
print (students)
tinylist.pop
print(tinylist)


print(list1)
list1[3] = "Rahul"
print(list1)

tinylist.clear
print(tinylist)

students.append("Rahul")
print(students)
x = students.count("Rahul")
print (x)

student2 = ["abc", "defk", "geh", "ijk","Rahul"]
student2.remove("Rahul")
student2.sort()
print(student2)

student2.reverse()
print(student2)

allstudent = students + student2

print(allstudent)

marks = [5, 99,11, 32,44]

print (max(marks))

#-------Tuple data type-----immutable cannot changed in paranthesis---
tuple1 = ("a", "b", "c")
tuple2 = (1,2,3)
tuple3 = tuple1 + tuple2 #concatenation
print(tuple3) 
print(tuple1*2) #repetition 
print(tuple2[1]) #indexing
print(tuple1[1:]) #slicing

#tuple1[1] = "f"
print (tuple1)


#----------python dictionary-------
#hashtype, curly brackets

tinydict = {'name': 'john','empid': 6234, 'dept': 'sales'}
dictblk = {}
print (tinydict.keys())
print (tinydict.values())

dictblk["age"] = 31
dictblk["college"] = "hindu_college"
print(dictblk)

del dictblk["college"]
print(dictblk)

print(len(tinydict))
type(tinydict)

tinydict.update(dictblk)
print(tinydict)

dictblk.clear
print(dictblk)

print(tinydict['dept'])

len(tinydict)
