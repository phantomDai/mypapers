#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/16
# @Anthor   : phantomDai
"""
"""
import numpy as np
import random


class mapt(object):

    def __init__(self):
        self.__number_partitions = 550
        self.__test_profile = [
            [1 / self.__number_partitions for i in range(0, 550)]] * 550

        self.__mapt_gamma = 0.1
        self.__mapt_tau = 0.1

    def get_next_partition_index(self, ex_partition):
        """
                获取下一次测试的分区
        :param ex_prtition:　上一个分区，注意实际的分区值比得到的值大１
        :return:
        """
        ex_partition -= 1
        array = self.__test_profile[ex_partition]
        index = -1

        random_number = random.random()
        sum = 0

        while(index < len(array) and random_number >= sum):
            index += 1
            sum += array[index]
            if index == 449:
                break

        # 为了符合文本partition_sheme_testcase_file中的分区编号是从１开始的所以需要在返回值的基础上增加１
        return index + 1

    def adjust_profile(self, ex_source_partition, ex_follow_partition, is_killed_mutant):
        """
        根据测试结果调整测试用剖面
        """
        # 实际的分区数是从１开始的，而算法是从０开始的，因此需要将原始测试用例和衍生测试用例的分区数值减１
        ex_source_partition -= 1
        if ex_follow_partition is None:
            ex_follow_partition = ex_source_partition
        else:
            ex_follow_partition -= 1

        old_i = self.__test_profile[ex_source_partition][ex_source_partition]
        old_f = self.__test_profile[ex_follow_partition][ex_follow_partition]

        # source and follow test cases belong to same partition
        if ex_source_partition == ex_follow_partition:
            # 揭示了故障
            if is_killed_mutant:
                sum = 0
                threadhold = self.__mapt_gamma * \
                    old_i / (self.__number_partitions - 1)
                for i in range(0, self.__number_partitions):
                    if i != ex_source_partition:
                        if self.__test_profile[ex_source_partition][i] > threadhold:
                            self.__test_profile[ex_source_partition][i] -= threadhold
                        else:
                            pass
                    else:
                        pass
                    sum += self.__test_profile[ex_source_partition][i]
                self.__test_profile[ex_source_partition][ex_source_partition] = 1 - sum
            else:  # 没有揭示故障
                threadhold = self.__mapt_tau * \
                    (1 - old_i) / (self.__number_partitions - 1)
                for i in range(0, self.__number_partitions):
                    if i != ex_source_partition:
                        if self.__test_profile[ex_source_partition][i] > threadhold:
                            self.__test_profile[ex_source_partition][i] += self.__mapt_tau * \
                                self.__test_profile[ex_source_partition][i] / \
                                (self.__number_partitions - 1)
                        else:
                            pass
                    else:
                        if self.__test_profile[ex_source_partition][i] > threadhold:
                            self.__test_profile[ex_source_partition][i] -= threadhold
                        else:
                            pass
        else:  # 原始测试用力与衍生测试不属于同一个分区
                # 揭示了故障
            if is_killed_mutant:
                sum_source = 0
                sum_follow = 0
                threadhold_source = self.__mapt_gamma * \
                    old_i / (self.__number_partitions - 1)
                threafhold_follow = self.__mapt_gamma * \
                    old_f / (self.__number_partitions - 1)

                for i in range(0, self.__number_partitions):
                    if i != ex_source_partition:
                        if self.__test_profile[ex_source_partition][i] > threadhold_source:
                            self.__test_profile[ex_source_partition][i] -= threadhold_source
                        else:
                            pass

                    if i != ex_follow_partition:
                        if self.__test_profile[ex_follow_partition][i] > threafhold_follow:
                            self.__test_profile[ex_follow_partition][i] -= threafhold_follow
                        else:
                            pass
                    sum_source += self.__test_profile[ex_source_partition][i]
                    sum_follow += self.__test_profile[ex_follow_partition][i]
                self.__test_profile[ex_source_partition][ex_source_partition] = 1 - sum_source
                self.__test_profile[ex_follow_partition][ex_follow_partition] = 1 - sum_follow
            else:  # 没有揭示故障
                threadhold_source = self.__mapt_tau * \
                    (1 - old_i) / (self.__number_partitions - 1)
                threadhold_follow = self.__mapt_tau * \
                    (1 - old_f) / (self.__number_partitions - 1)

                for i in range(0, self.__number_partitions):
                    if i != ex_source_partition:
                        if self.__test_profile[ex_source_partition][i] > threadhold_source:
                            self.__test_profile[ex_source_partition][i] += threadhold_source
                        else:
                            pass
                    else:
                        if old_i > threadhold_source:
                            self.__test_profile[ex_source_partition][i] -= threadhold_source
                        else:
                            pass

                    if i != ex_follow_partition:
                        if self.__test_profile[ex_follow_partition][i] > threadhold_follow:
                            self.__test_profile[ex_follow_partition][i] += threadhold_follow
                        else:
                            pass
                    else:
                        if old_f > threadhold_follow:
                            self.__test_profile[ex_follow_partition][i] -= threadhold_follow
                        else:
                            pass


if __name__ == '__main__':
    apt = mapt()
