#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/16
# @Anthor   : phantomDai
"""

"""
import re


all_test_cases = []

with open('MR1_1', 'r') as file:
    for aline in file:
        if len(re.findall(r"\[\^+\w+-\w+\]", aline.strip())) != 0:
            pass
        else:
            all_test_cases.append(aline)
file.close()

file = open('MR1', 'w+')
file.writelines(all_test_cases)
file.close()