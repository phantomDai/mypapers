#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:26:39 2019
this script is responsible to identify all valid combinations of 
choices that belong to defferent categories of group A.

@author: phantom
"""

# all choices of categories belonging to B
choices_categoriesB = ["NB", "CB", "QM", "ST", "PL", "RM",
                       "BR", "PR", "N0", "BL", "EL", "LL",
                       "BW", "EW", "WW", "YB", "YE", "YY",
                       "EN", "NE", "NN", "CO", "AL"]

# this set records all valid combinations of choices
valid_combinations = []

with open ('TestFrames_grep_no_repeat', 'r') as f:
    # get each line
    for line in f:
        # get each line
        temp_choices = line.strip().split(';')
        # replace choices of B with '#'
        modify_temp_choices = [ele if ele in choices_categoriesB else '#' for ele in temp_choices]
        # converts the list to a string
        temp_test_frame = ';'.join(ele for ele in modify_temp_choices)
        # add the new test frame into the set
        if temp_test_frame not in valid_combinations:
            valid_combinations.append(temp_test_frame)
f.close()


new_file = open('partition_scheme_2.1', 'w')

for ele in valid_combinations:
    new_file.write(ele + '\n')
new_file.close
print("OK!")




