#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/4
# @Anthor   : phantomDai
"""
传统的蜕变测试技术：随机选择测试用例随机选择蜕变关系
"""
from myutl.Utl import Utl
from measure.F_time import Ftime
from measure.F2_time import F2time
from measure.F_Measure import F
from measure.F2_Measure import F2
from execute.utl.Utl import execute_utl
from execute.MAPT import mapt
from partition import allocation_testcases_4_partitions as allocation_object
from constant import constantNumber as constant

import execute.utl.write_info_into_excel as writer

import time
import os
import linecache
import random


class AMT_MAPT_random(object):

    def __init__(self):
        # 创建工具类
        tool = Utl()
        self.__exec_utl = execute_utl()

        # 获取测试用例的具体信息，索引是行号，从１考试
        self.__test_cases = tool.get_concrete_test_case()

        # 获取测试用例与蜕变关系之间的关系，键是测试用例的编号，值是可以作用的蜕变关系列表
        self.__test_case_2_MRs = tool.get_test_case_2_MRs()

        # 获取分区与测试用例的编号，键是分区编号（１－５５０），值是该分区的测试用例
        self.__partition_map = allocation_object.get_partition_map()

        # 获取执行错误的测试用例的编号
        self.__wrong_test_cases = self.__exec_utl.get_wrong_patterns()

        # 初始化测试信息记录对象
        self.__F_time_recorder = Ftime()
        self.__F2_time_recorder = F2time()
        self.__F_measure_recorder = F()
        self.__F2_measure_recorder = F2()

        # 获取分区与测试用例之间的关系
        self.__partition_map = allocation_object.get_partition_map()

        # 初始化控制测试执行的策略
        self.__mapt = mapt()

    def execute(self, seed):
        """
        执行测试用例
        :param seed:　指定的随机数种子
        :return:
        """

        # mutant names
        mutant_names_list = ['grep_v2', 'grep_v4', 'grep_v6',
                             'grep_v13', 'grep_v15', 'grep_v17', 'grep_v18', 'grep_v19']

        # 初始化度量标准
        F_select_time = int(0)
        F_generate_time = int(0)
        F_execute_time = int(0)
        F2_select_time = int(0)
        F2_generate_time = int(0)
        F2_execute_time = int(0)
        F = int(0)
        F2 = int(0)

        # 杀死的变异体数目
        num_killed_mutants = int(0)

        # 统计测试用例的执行数目
        num_test_case_counter = int(0)

        # 获取该种子下所有的测试用例的序列
        random_list = self.__exec_utl.generate_random_number(seed)

        # record ex partition
        ex_source_partition = int(0)
        ex_follow_partition = int(0)

        for pure_cycle in range(1, 10000):

            # 执行的测试用例数目＋１
            num_test_case_counter += 1

            # 测试用例的编号
            test_case_index = 0

            #　记录选择测试用例需要的时间
            started_select_source_test_case_time = int(
                round(time.time() * 1000000))

            # 选择一个分区
            partition_index = 0
            if num_test_case_counter == 1:
                partition_index = random.randint(1, 550)
                ex_source_partition = partition_index
                ex_follow_partition = partition_index
            else:
                partition_index = self.__mapt.get_next_partition_index(
                    ex_source_partition)
                ex_source_partition = partition_index
                ex_follow_partition = partition_index

            if partition_index == 551:
                partition_index = 550

            # 获得选中的分区中所有的测试用例
            selected_partition_test_cases = self.__partition_map[partition_index]

            test_case_index = int(selected_partition_test_cases[random.randint(0, len(selected_partition_test_cases) - 1)])

            ended_select_source_test_case_time = int(
                round(time.time() * 1000000))

            # 记录选择测试用例需要的时间
            if num_killed_mutants == 0:
                F_select_time += (ended_select_source_test_case_time -
                                  started_select_source_test_case_time)
            else:
                F2_select_time += (ended_select_source_test_case_time -
                                   started_select_source_test_case_time)

            if test_case_index in self.__wrong_test_cases:
                continue
            else:
                pass

            # 获取正则表达式
            source_pattern = self.__test_cases[test_case_index]

            # 统计测试用来的生成时间
            started_generating_follow_test_case_time = int(
                round(time.time() * 1000000))

            # 获取该正则表达式可以作用的蜕变关系的集合，然后随机选择一个蜕变关系
            MRs = linecache.getline(constant.test_cases_2_mrs_path, test_case_index). \
                replace('\'', '').replace('\'', '').strip().split(
                    ':')[1].replace('[', '').replace(']', '')
            MRs_list = MRs.split(', ')

            # randomly select a MR
            selected_MR = self.__exec_utl.random_select_MR(MRs_list)

            # 获取衍生测试用例
            follow_pattern = self.__exec_utl.generate_follow_test_case(
                selected_MR, source_pattern, test_case_index)

            ended_generating_follow_test_case_time = int(
                round(time.time() * 1000000))

            # 生成衍生测试用例的时间
            generate_follow_test_case_time = ended_generating_follow_test_case_time - \
                started_generating_follow_test_case_time

            # 判断衍生测试用例所在的分区
            ex_follow_partition = self.__exec_utl.get_follow_test_case_partition(test_case_index, ex_source_partition, selected_MR)
            # record test case generating time
            if num_killed_mutants == 0:
                F_generate_time += generate_follow_test_case_time
            else:
                F2_generate_time += generate_follow_test_case_time

            # 遍历变异体
            for mutant_name in mutant_names_list:
                source_command = ''
                follow_command = ''

                if selected_MR != 'MR11' and selected_MR != 'MR9':
                    source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern \
                                     + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(seed) \
                                     + "/" + str(num_test_case_counter) + \
                        "_source_" + mutant_name

                    follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern \
                                     + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(seed) \
                                     + "/" + str(num_test_case_counter) + \
                        "_follow_" + mutant_name
                elif selected_MR == 'MR11':
                    source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern \
                                     + "\" " + "../targetFiles/MR11_" + str(
                                         test_case_index) + "> ../testingResults/repetitive" \
                        + str(seed) + "/" + str(num_test_case_counter) + \
                        '_source_' + mutant_name

                    follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern \
                                     + "\" " + "../targetFiles/MR11_" + str(
                                         test_case_index) + "> ../testingResults/repetitive" \
                        + str(seed) + "/" + str(num_test_case_counter) + \
                        '_follow_' + mutant_name
                else:
                    source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern \
                                     + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(seed) \
                                     + "/" + str(num_test_case_counter) + \
                        "_source_" + mutant_name

                    follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern \
                                     + "\" " + "../targetFiles/file.test_MR9_follow > ../testingResults/repetitive" + str(
                                         seed) \
                        + "/" + str(num_test_case_counter) + \
                        "_follow_" + mutant_name

                # executing source and follow-up test cases
                started_executing_cases_time = int(
                    round(time.time() * 1000000))
                terminal_source = os.popen(source_command)
                terminal_source.close()
                terminal_follow = os.popen(follow_command)
                terminal_follow.close()
                ended_executing_cases_time = int(round(time.time() * 1000000))
                execute_test_cases_time = ended_executing_cases_time - started_executing_cases_time

                # record source and follow-up test cases executing time
                if num_killed_mutants == 0:
                    F_execute_time += execute_test_cases_time
                else:
                    F2_execute_time += execute_test_cases_time


                # 标志位：判断测试用例是否揭示故障，默认没有揭示故障
                isKilledMutant = False
                # 调用ＭＲ的验证结果的方法，判断是否揭示故障
                if selected_MR != 'MR11':
                    isKilledMutant = self.__exec_utl.verify_result_not_MR11(selected_MR, str(seed),
                                                                            str(num_test_case_counter), mutant_name)
                else:
                    isKilledMutant = self.__exec_utl.verify_result_MR11(str(seed), str(num_test_case_counter),
                                                                        str(test_case_index), mutant_name)

                # 调整测试剖面
                self.__mapt.adjust_profile(ex_source_partition, ex_follow_partition, isKilledMutant)

                # 判断是否揭示故障
                if isKilledMutant:
                    print("killed a mutant: repetitive:" + str(seed) + "; mutant_name: " + mutant_name
                          + "; selected_MR: " + selected_MR +
                          "; testing_index:" + str(num_test_case_counter)
                          + "; test_case_index:" + str(test_case_index))

                    mutant_names_list.remove(mutant_name)
                    num_killed_mutants += 1
                    if num_killed_mutants == 1:
                        F = num_test_case_counter * 2
                        break

                    elif num_killed_mutants == 2:
                        F2 = num_test_case_counter * 2 - F
                        break
                    else:
                        break

                else:
                    continue

            if num_killed_mutants == 2:
                break

        # record testing informtion
        self.record_result_info(F, F2)
        self.record_time_info(F_select_time, F_generate_time, F_execute_time,
                              F2_select_time, F2_generate_time, F2_execute_time)

    def record_result_info(self, f_mesure, f2_mesure):
        """
        记录F和F2的实验结果
        :param f_mesure:　ｆ标准的值
        :param f2_mesure:　f2标准的值
        :return: Null
        """
        self.__F_measure_recorder.append(f_mesure)
        self.__F2_measure_recorder.append(f2_mesure)

    def record_time_info(self, f_select, f_generte, f_execute, f2_select, f2_generte, f2_execute):
        """

        :param f_select: f标准选择测试用例的时间
        :param f_generte: f标准选择测试用例的时间
        :param f_execute: f标准选择测试用例的时间
        :param f2_select: f２标准选择测试用例的时间
        :param f2_generte: f２标准选择测试用例的时间
        :param f2_execute: f２标准选择测试用例的时间
        :return:
        """
        self.__F_time_recorder.append_select_test_case(f_select)
        self.__F_time_recorder.append_generate_test_case(f_generte)
        self.__F_time_recorder.append_execute_test_case_(f_execute)
        self.__F2_time_recorder.append_select_test_case(f2_select)
        self.__F2_time_recorder.append_generate_test_case(f2_generte)
        self.__F2_time_recorder.append_execute_test_case_(f2_execute)

    def write_results_time_info(self):
        content = []
        content.append("F-average: " +
                       str(self.__F_measure_recorder.get_average()) + '\n')
        content.append("F2-average: " +
                       str(self.__F2_measure_recorder.get_average()) + '\n')
        content.append("F-variance: " +
                       str(self.__F_measure_recorder.get_variance()) + '\n')
        content.append("F2-variance: " +
                       str(self.__F2_measure_recorder.get_variance()) + '\n')
        content.append("F-select-average: " + str(self.__F_time_recorder.get_F_select_average())
                       + ";F-generate-average: " +
                       str(self.__F_time_recorder.get_F_generate_average())
                       + ";F-execute-average: " + str(self.__F_time_recorder.get_F_execute_average()) + '\n')

        content.append("F-select-variance: " + str(self.__F_time_recorder.get_F_select_variance())
                       + ";F-generate-variance: " +
                       str(self.__F_time_recorder.get_F_generate_variance())
                       + ";F-execute-variance: " + str(self.__F_time_recorder.get_F_execute_variance()) + '\n')

        content.append("F2-select-average: " + str(self.__F2_time_recorder.get_F2_select_average())
                       + ";F2-generate-average: " +
                       str(self.__F2_time_recorder.get_F2_generate_average())
                       + ";F2-execute-average: " + str(self.__F2_time_recorder.get_F2_execute_average()) + '\n')

        content.append("F2-select-variance: " + str(self.__F2_time_recorder.get_F2_select_variance())
                       + ";F2-generate-variance: " +
                       str(self.__F2_time_recorder.get_F2_generate_variance())
                       + ";F2-execute-variance: " + str(self.__F2_time_recorder.get_F2_execute_variance()) + '\n')

        parent_path = os.path.join(os.getcwd(), 'test_results')

        file_path = os.path.join(parent_path, 'AMT_MAPT_random')
        file = open(file_path, 'w+')
        file.writelines(content)
        file.close()

        writer.write_info('AMT_MAPT_random.xlsx', self.get_all_average_list(), self.get_all_variance_list(),
                          self.__F_measure_recorder.get_all_F(),
                          self.__F2_measure_recorder.get_all_F2(), self.__F_time_recorder.get_all_F_select(),
                          self.__F_time_recorder.get_all_F_generate(), self.__F_time_recorder.get_all_F_execute(),
                          self.__F2_time_recorder.get_F2_all_select(), self.__F2_time_recorder.get_F2_all_generate(),
                          self.__F2_time_recorder.get_F2_all_execute())

    def get_all_average_list(self):
        all_average = [0] * 8
        all_average[0] = self.__F_measure_recorder.get_average()
        all_average[1] = self.__F2_measure_recorder.get_average()
        all_average[2] = self.__F_time_recorder.get_F_select_average()
        all_average[3] = self.__F_time_recorder.get_F_generate_average()
        all_average[4] = self.__F_time_recorder.get_F_execute_average()
        all_average[5] = self.__F2_time_recorder.get_F2_select_average()
        all_average[6] = self.__F2_time_recorder.get_F2_generate_average()
        all_average[7] = self.__F2_time_recorder.get_F2_execute_average()
        return all_average

    def get_all_variance_list(self):
        all_variance = [0] * 8
        all_variance[0] = self.__F_measure_recorder.get_variance()
        all_variance[1] = self.__F2_measure_recorder.get_variance()
        all_variance[2] = self.__F_time_recorder.get_F_select_variance()
        all_variance[3] = self.__F_time_recorder.get_F_generate_variance()
        all_variance[4] = self.__F_time_recorder.get_F_execute_variance()
        all_variance[5] = self.__F2_time_recorder.get_F2_select_variance()
        all_variance[6] = self.__F2_time_recorder.get_F2_generate_variance()
        all_variance[7] = self.__F2_time_recorder.get_F2_execute_variance()
        return all_variance


if __name__ == '__main__':
    amt = AMT_MAPT_random()
    for seed in range(1, 31):
        amt.execute(seed)
    amt.write_results_time_info()
