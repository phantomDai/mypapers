#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/12/8
# @Anthor   : phantomDai
"""

"""
import os

dir_path = os.getcwd();

for index in range(1, 31):
    target_dir = os.path.join(dir_path, "repetitive" + str(index))
    files = os.listdir(target_dir)
    if len(files) == 0:
        continue
    else:
        for f in files:
            temp_file = os.path.join(target_dir, f)
            os.remove(temp_file)



