# -*- coding: utf-8 -*-
"""
in previous materials of Arlinta, there is a mistake about the category 10. 
More specificallly, category 10 has the same choices as category 7.
To identify the choices of categiry 10, I code this script.

@author: phantom
"""

right_choices = ["NA", "NP", "YW", "NW", "YD", "ND", "YS", "NS", "N1", "N2", "N3","N4","N5","N6","N7","N8","N9","N10",
               "N11","N12", "DOT", "UR", "LR", "NR", "NB", "CB", "QM", "ST", "PL", "RM", "BL", "EL", "LL", "BW", "EW",
               "WW", "YB", "YE", "YY", "EN", "NE", "NN", "CO", "AL"]

non_right_choices = []

with open("TestFrames_grep", 'r') as file:
    for line in file:
        temp_choices = line.strip('\n').split(';')
        temp_list = [item for item in temp_choices if item not in right_choices]
        non_right_choices += temp_list

file.close
print(set(non_right_choices))









