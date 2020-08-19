#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/12/3
# @Anthor   : phantomDai
"""

"""
from myutl.Utl import Utl
from execute.utl.Utl import execute_utl

import os
import linecache

class mutant_failure_rate(object):
    test_cases_2_mrs_path = os.path.join(os.path.abspath('..'), 'mapping relation', 'testcase_2_MRs')

    # 获得测试用例的具体信息，索引是行号
    test_cases = []

    wrong_test_cases = []

    # 获取测试用例与蜕变关系的映射关系,键是测试用例的编号，值是可以作用的蜕变关系列表
    test_case_2_MRs = {}

    # 执行测试用例的工具类
    exec_utl = execute_utl()

    partition_rate = []

    def __init__(self):
        """
        初始化测试信息
        """
        tool = Utl()
        self.test_cases = tool.get_concrete_test_case()
        self.test_case_2_MRs = tool.get_test_case_2_MRs()
        self.wrong_test_cases = self.exec_utl.get_wrong_patterns()
    def execute(self, seed, mutant_name_list):

        killed_test_case_indexs = []
        #开始遍历测试用例
        for test_case_index in range(1, 101194):

            num_test_case_counter = test_case_index

            if test_case_index in self.wrong_test_cases:
                continue
            else:
                pass

            # 获取正则表达式
            source_pattern = self.test_cases[int(test_case_index)]

            # MRs = self.exec_utl.get_test_case_MR_list(test_case_index)
            MRs = linecache.getline(self.test_cases_2_mrs_path, int(test_case_index)).\
                replace('\'', '').replace('\'', '').strip().split(':')[1].replace('[', '').replace(']', '')
            MRs_list = MRs.split(', ')

            for selected_MR in MRs_list:
                # 获取衍生测试用例
                follow_pattern = self.exec_utl.generate_follow_test_case(selected_MR,
                                                                         source_pattern, test_case_index)
                # 遍历变异体
                for mutant_name in mutant_name_list:
                    print(str(test_case_index) + selected_MR + mutant_name)
                    source_command = ''
                    follow_command = ''
                    if selected_MR != 'MR11' and selected_MR != 'MR9':
                        source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern \
                              + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(seed) \
                              + "/" + str(num_test_case_counter) + "_source_" + mutant_name

                        follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern \
                              + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(seed) \
                              + "/" + str(num_test_case_counter) + "_follow_" + mutant_name
                    elif selected_MR == 'MR11':
                        source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern \
                                  + "\" " + "../targetFiles/MR11_" + str(test_case_index) + "> ../testingResults/repetitive" \
                                  + str(seed) + "/" + str(num_test_case_counter) + '_source_' + mutant_name

                        follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern \
                                  + "\" " + "../targetFiles/MR11_" + str(test_case_index) + "> ../testingResults/repetitive" \
                                  + str(seed) + "/" + str(num_test_case_counter) + '_follow_' + mutant_name
                    else:
                        source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern \
                                         + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(seed) \
                                         + "/" + str(num_test_case_counter) + "_source_" + mutant_name

                        follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern \
                                         + "\" " + "../targetFiles/file.test_MR9_follow > ../testingResults/repetitive" + str(seed) \
                                         + "/" + str(num_test_case_counter) + "_follow_" + mutant_name


                    terminal_source = os.popen(source_command)
                    terminal_source.close()
                    terminal_follow = os.popen(follow_command)
                    terminal_follow.close()


                    # 标志位：判断测试用例是否揭示故障，默认没有揭示故障
                    isKilledMutant = False
                    # 调用ＭＲ的验证结果的方法，判断是否揭示故障
                    if selected_MR != 'MR11':
                        isKilledMutant = self.exec_utl.verify_result_not_MR11(selected_MR, str(seed), str(num_test_case_counter), mutant_name)
                    else:
                        isKilledMutant = self.exec_utl.verify_result_MR11(str(seed), str(num_test_case_counter), str(test_case_index), mutant_name)

                    # 判断是否揭示故障
                    if isKilledMutant:
                        if str(test_case_index) not in killed_test_case_indexs:
                            killed_test_case_indexs.append(str(test_case_index))
                    else:
                        continue

        self.partition_rate.append(mutant_name + " failure rate: " + str(len(killed_test_case_indexs) / 101193) + '\n')


    def write_partition_rate(self):
        f = open('mutant_failure_rate', 'w+')
        for aline in self.partition_rate:
            f.write(aline)
        f.close()

if __name__ == '__main__':
    mutant_rate = mutant_failure_rate()
    all_mutants = [["grep_v16"]]
    for alist in all_mutants:
        mutant_rate.execute(1, alist)
    mutant_rate.write_partition_rate()