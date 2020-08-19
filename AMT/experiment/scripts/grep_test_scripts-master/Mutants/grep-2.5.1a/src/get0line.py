#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/14
# @Anthor   : phantomDai
"""

"""
import linecache
import os



def get(line):
    path = os.path.join(os.getcwd(), 'partition_scheme_testcases_1.2')
    aline = linecache.getline(path, line).strip()
    command_line = "./grep -E \"" + aline + "\"" + " ./file.test"
    print(command_line)

get(25538)
