#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/13
# @Anthor   : phantomDai
"""
Ｆ２标准的时间记录者
"""
import numpy as np
class F2time(object):
    F2_select_test_case_time = []
    F2_generate_test_case_time = []
    F2_execute_test_case_time = []

    def __init__(self):
        pass

    def append_select_test_case(self, f2_select):
        self.F2_select_test_case_time.append(f2_select)

    def append_generate_test_case(self, f2_generate):
        self.F2_generate_test_case_time.append(f2_generate)

    def append_execute_test_case_(self, f2_execute):
        self.F2_execute_test_case_time.append(f2_execute)

    def get_F2_select_average(self):
        return np.mean(self.F2_select_test_case_time)

    def get_F2_select_variance(self):
        return np.var(self.F2_select_test_case_time)

    def get_F2_generate_average(self):
        return np.mean(self.F2_generate_test_case_time)

    def get_F2_generate_variance(self):
        return np.var(self.F2_generate_test_case_time)

    def get_F2_execute_average(self):
        return np.mean(self.F2_execute_test_case_time)

    def get_F2_execute_variance(self):
        return np.var(self.F2_execute_test_case_time)

    def get_F2_all_select(self):
        return self.F2_select_test_case_time

    def get_F2_all_generate(self):
        return self.F2_generate_test_case_time

    def get_F2_all_execute(self):
        return self.F2_execute_test_case_time