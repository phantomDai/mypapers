#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/5
# @Anthor   : phantomDai
"""
记录揭示the second fault需要的测试用例数目
"""
import numpy as np

class F2(object):
    F2_measure = []

    def __init__(self):
        pass

    def append(self, f2measure):
        self.F2_measure.append(f2measure)


    def get_average(self):

        return np.mean(self.F2_measure)


    def get_variance(self):

        return np.var(self.F2_measure)

    def get_all_F2(self):
        return self.F2_measure

