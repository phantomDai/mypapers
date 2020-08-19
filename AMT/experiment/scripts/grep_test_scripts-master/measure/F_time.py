#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/13
# @Anthor   : phantomDai
"""
F标准的时间记录者

"""
import numpy as np
class Ftime(object):
    F_select_test_case_time = []
    F_generate_test_case_time = []
    F_execute_test_case_time = []


    def __init__(self):
        pass

    def append_select_test_case(self, f_select):
        self.F_select_test_case_time.append(f_select)

    def append_generate_test_case(self, f_generate):
        self.F_generate_test_case_time.append(f_generate)

    def append_execute_test_case_(self, f_execute):
        self.F_execute_test_case_time.append(f_execute)

    def get_F_select_average(self):
        return np.mean(self.F_select_test_case_time)

    def get_F_select_variance(self):
        return np.var(self.F_select_test_case_time)

    def get_F_generate_average(self):
        return np.mean(self.F_generate_test_case_time)

    def get_F_generate_variance(self):
        return np.var(self.F_generate_test_case_time)

    def get_F_execute_average(self):
        return np.mean(self.F_execute_test_case_time)

    def get_F_execute_variance(self):
        return np.var(self.F_execute_test_case_time)

    def get_all_F_select(self):
        return self.F_select_test_case_time

    def get_all_F_generate(self):
        return self.F_generate_test_case_time

    def get_all_F_execute(self):
        return self.F_execute_test_case_time


