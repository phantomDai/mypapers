#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/4
# @Anthor   : phantomDai
"""
记录揭示第一个故障需要的测试用例数目
"""
import numpy as np

class F(object):

    F_measures = []

    def __init__(self):
        pass


    def append(self, f_measure):
        self.F_measures.append(f_measure)


    def get_average(self):
        """
        获取平均数
        :return: 平均数
        """
        return np.mean(self.F_measures)


    def get_variance(self):
        """
        获取方差
        :return:　方差
        """

        return np.var(self.F_measures)

    def get_all_F(self):
        return self.F_measures


