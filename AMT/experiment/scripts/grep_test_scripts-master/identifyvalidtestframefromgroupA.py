#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:26:50 2019

this script is responsible to identify all valid combinations of 
choices that belong to defferent categories of group A.

@author: phantom
"""


# all choices of categories belonging to A
choices_categoriesA = ["NA", "NP", "YW", "NW", "YD", "ND", "YS", "NS",
                       "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8",
                       "N9", "N10","N11","N12", "DOT", "UR", "LR", "NR"]

# this set records all valid combinations of choices
valid_combinations = []

# reading the test frame file
with open ('TestFrames_grep_no_repeat', 'r') as file:
    for line in file:
        # get each line
        temp_choices = line.strip().split(';')
        # replace choices of B with '#'
        modify_temp_choices = [ele if ele in choices_categoriesA else '#' for ele in temp_choices]
        # converts the list to a string
        temp_test_frame = ';'.join(ele for ele in modify_temp_choices)
        # add the new test frame into the set
        if temp_test_frame not in valid_combinations:
            valid_combinations.append(temp_test_frame)
file.close

new_file = open('partition_scheme_1.1', 'w+')

for ele in valid_combinations:
    new_file.write(ele + '\n')
new_file.close
print("OK!")











