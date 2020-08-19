#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/22
# @Anthor   : phantomDai
"""

"""

from partition import allocation_testcases_4_partitions as allocation_object

import random
import math


class rapt(object):
    """
    test case selecting strategy
    """

    def __init__(self):
        """
        initial varians
        """
        # test profile
        self.__test_profile = [1 / 550 for i in range(0, 550)]

        # number of partitions
        self.__number_partitions = 550

        # set boundaries for all paritions
        self.__boundary = self.__initial_boundary()

        # record the reward for each partution
        self.__reward = [0] * 550

        # record the punishment for each partition
        self.__punishment = [0] * 550

        self.__epsilon = 0.05
        self.__delta = 0.42

    def __initial_boundary(self):
        partition_map = allocation_object.get_partition_map()
        boundaries = [0] * 550
        for index in range(0, 550):
            boundaries[index] = int(len(partition_map[index + 1]) * 0.7)
        return boundaries

    def get_next_partition_index(self):
        """
        randomly select the next partition according to the test profile
        :return: the index of selected partition
        """
        index = -1
        sum = 0
        random_number = random.random()
        while (index < self.__number_partitions and random_number >= sum):
            index += 1
            sum += self.__test_profile[index]
            if index == 449:
                break
        return index + 1

    def add_punishement(self, source_partition_index, follow_partition_index):
        """
        update the punishement array
        :param source_partition_index:
        :param follow_partition_index:
        :return:
        """
        source_partition_index -= 1
        if follow_partition_index is None:
            follow_partition_index = source_partition_index
        else:
            follow_partition_index -= 1

        c = self.__punishment
        a = self.__punishment[source_partition_index]
        b = self.__punishment[follow_partition_index]

        if source_partition_index == follow_partition_index:
            self.__punishment[source_partition_index] += 1
        else:
            self.__punishment[source_partition_index] += 1
            self.__punishment[follow_partition_index] += 1

    def add_reward(self, source_partition_index, follow_partition_index):
        """
        update the reward array
        :param source_partition_index:
        :param follow_partition_index:
        :return:
        """
        source_partition_index -= 1
        if follow_partition_index is None:
            follow_partition_index = source_partition_index
        else:
            follow_partition_index -= 1
        if source_partition_index == follow_partition_index:
            self.__reward[int(source_partition_index)] += 1
        else:
            self.__reward[int(source_partition_index)] += 1
            self.__reward[int(follow_partition_index)] += 1

    def clear_punishement(self, source_partition_index, follow_partition_index):
        """
        当原始测试用例以及衍生测试用例揭示故障时，清空原始测试用例以及衍生测试用力所在分区的惩罚
        :param source_partition_index:
        :param follow_partition_index:
        :return:
        """
        source_partition_index -= 1
        if follow_partition_index is None:
            follow_partition_index = source_partition_index
        else:
            follow_partition_index -= 1

        if source_partition_index == follow_partition_index:
            self.__punishment[source_partition_index] = 0
        else:
            self.__punishment[source_partition_index] = 0
            self.__punishment[follow_partition_index] = 0

    def adjust_profile(self, ex_source_partition, ex_follow_partition, isKilledMutant):
        """
        update test profile
        :param ex_source_partition:
        :param ex_follow_partition:
        :param isKilledMutant:
        :return:
        """

        ex_source_partition -= 1
        if ex_follow_partition is None:
            ex_follow_partition = ex_source_partition
        else:
            ex_follow_partition -= 1

        if isKilledMutant:  # detect a fault
            if ex_source_partition == ex_follow_partition:  # source and follow-up test cases belong to same partition

                sum = 0
                for index in range(0, 550):
                    if index != ex_source_partition:
                        same_hit_i_shreshold = (
                            1 + math.log(self.__reward[index])) * self.__epsilon / (self.__number_partitions - 1)
                        if self.__test_profile[index] > same_hit_i_shreshold:
                            self.__test_profile[index] -= same_hit_i_shreshold
                            sum += self.__test_profile[index]
                        else:
                            self.__test_profile[index] = 0
                    else:
                        pass

                self.__test_profile[ex_source_partition] = 1 - sum
            else:  # detect a fault, moreover, source and follow test cases do not belong same partition
                old_s = self.__test_profile[ex_source_partition]
                old_f = self.__test_profile[ex_follow_partition]
                sum = 0
                not_same_hit_i_shreshold = (
                    1 + math.log(self.__reward[ex_source_partition])) * self.__epsilon / (self.__number_partitions - 2)
                for index in range(0, 550):
                    if index != ex_source_partition and index != ex_follow_partition:
                        not_same_hit_i_shreshold = (1 + math.log(
                            self.__reward[index])) * self.__epsilon / (self.__number_partitions - 2)
                        if self.__test_profile[index] > not_same_hit_i_shreshold:
                            self.__test_profile[index] -= not_same_hit_i_shreshold
                            sum += self.__test_profile[index]
                        else:
                            self.__test_profile[index] = 0
                    else:
                        pass

                self.__test_profile[ex_source_partition] = old_s + \
                    ((1 - sum - old_s - old_f) / 2)
                self.__test_profile[ex_follow_partition] = old_f + \
                    ((1 - sum - old_s - old_f) / 2)

            # 分区奖励结束，需要对分区的奖励清零
            self.__reward[ex_source_partition] = 0
            self.__reward[ex_follow_partition] = 0
        else:  # does not detect a fault
            old_s = self.__test_profile[int(ex_source_partition)]
            old_f = self.__test_profile[int(ex_follow_partition)]
            # source test case and follow test case belong to same partition
            if ex_source_partition == ex_follow_partition:
                for index in range(0, 550):
                    if index == ex_source_partition:
                        if self.__test_profile[ex_source_partition] > self.__delta:
                            self.__test_profile[ex_source_partition] -= self.__delta
                        elif self.__test_profile[ex_source_partition] <= self.__delta or self.__boundary[ex_source_partition] == self.__punishment[ex_source_partition]:
                            self.__test_profile[ex_source_partition] == 0
                        else:
                            pass
                    else:
                        if self.__test_profile[ex_source_partition] > self.__delta:
                            self.__test_profile[index] += self.__delta / \
                                (self.__number_partitions - 1)
                        elif self.__test_profile[ex_source_partition] <= self.__delta or self.__boundary[ex_source_partition] == self.__punishment[ex_source_partition]:
                            self.__test_profile[index] += old_s / \
                                (self.__number_partitions - 1)
                        else:
                            pass
            else:  # source test case and follow test case does not belong to same partition
                if self.__test_profile[ex_source_partition] > self.__delta:
                    self.__test_profile[ex_source_partition] -= self.__delta
                elif self.__test_profile[ex_source_partition] <= self.__delta or self.__boundary[ex_source_partition] == self.__punishment[ex_source_partition]:
                    self.__test_profile[ex_source_partition] = 0
                else:
                    pass
                if self.__test_profile[ex_follow_partition] > self.__delta:
                    self.__test_profile[ex_follow_partition] -= self.__delta
                elif self.__test_profile[ex_follow_partition] <= self.__delta or self.__boundary[ex_follow_partition] == \
                        self.__punishment[ex_follow_partition]:
                    self.__test_profile[ex_follow_partition] = 0
                else:
                    pass
                for i in range(0, 550):
                    if i != ex_source_partition and i != ex_follow_partition:
                        self.__test_profile[i] += ((old_s - self.__test_profile[ex_source_partition]) + (
                            old_f - self.__test_profile[ex_follow_partition])) / (self.__number_partitions - 2)
            if self.__punishment[ex_source_partition] == self.__boundary[ex_source_partition]:
                self.__punishment[ex_source_partition] = 0
            elif self.__punishment[ex_follow_partition] == self.__boundary[ex_follow_partition]:
                self.__punishment[ex_follow_partition] = 0
            else:
                pass


if __name__ == '__main__':
    apt = rapt()

