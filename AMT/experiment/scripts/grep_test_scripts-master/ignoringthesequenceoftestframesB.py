#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:05:43 2019

based on the parition_scheme_2.1, this script is 
responsible to get new partition scheme by ignoring
the sequence of interested choices. 

@author: phantom
"""

# the list that cotains the set of choices for each test frame
choices_list = []

# the index of test frames are going to be removed
indexs = []


with open('partition_scheme_2.1', 'r') as file:
    for line in file:
        temp_line_choices = line.strip().split(';')
        temp_set = set(temp_line_choices)
        temp_set1 =set(ele for ele in temp_set if ele != '#')
        flag = False
        for one_set in choices_list:
            if one_set == temp_set1:
                flag = True
        
        if flag == False:
           choices_list.append(temp_set1)
           indexs.append(';'.join(ele for ele in temp_set1))
file.close

with open('partition_scheme_2.2', 'w+') as f:
    for temp_str in indexs:
        f.write(str(temp_str + '\n'))
f.close
print('OK!')