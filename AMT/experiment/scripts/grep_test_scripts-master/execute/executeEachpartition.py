#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/12/2
# @Anthor   : phantomDai
"""
executing each partition and calcuting partition failure rate and mutants failure rate
"""
from execute.utl.Utl import execute_utl
from constant import constantNumber as constant
from partition import allocation_testcases_4_partitions as allocation_object
from myutl.Utl import Utl
import linecache
import os
import time

partition_map = allocation_object.get_partition_map()


tool = Utl()
test_cases = tool.get_concrete_test_case()
exec_utl = execute_utl()
content = []
wrong_test_cases = exec_utl.get_wrong_patterns()

def execute(partition_index):
    partition_info = "partition: " + str(partition_index) + ";"

    # add a list
    temp_list = []

    partition_test_cases = partition_map[partition_index]
    partition_info += "number of test cases: " + str(len(partition_test_cases)) + ';'

    killed_test_case_indexs = []
    killed_mutanmts = []
    for test_case_index in partition_test_cases:
        if int(test_case_index) in wrong_test_cases:
            continue

        source_pattern = test_cases[int(test_case_index)]
        MRs = linecache.getline(constant.test_cases_2_mrs_path, int(test_case_index)). \
            replace('\'', '').replace('\'', '').strip().split(
            ':')[1].replace('[', '').replace(']', '')
        MRs_list = MRs.split(', ')
        for aMR in MRs_list:

            follow_pattern = exec_utl.generate_follow_test_case(aMR, source_pattern, int(test_case_index))

            source_command = ''
            follow_command = ''

            for mutant_name in constant.mutant_names_list:
                if aMR != 'MR11' and aMR != 'MR9':
                    source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(
                        1) \
                                     + "/" + str(test_case_index) + "_source_" + mutant_name

                    follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(
                        1) \
                                     + "/" + str(test_case_index) + "_follow_" + mutant_name
                elif aMR == 'MR11':
                    source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern + "\" " + "../targetFiles/MR11_" + str(
                        test_case_index) + "> ../testingResults/repetitive" \
                                     + str(1) + "/" + str(test_case_index) + '_source_' + mutant_name

                    follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern + "\" " + "../targetFiles/MR11_" + str(
                        test_case_index) + "> ../testingResults/repetitive" \
                                     + str(1) + "/" + str(test_case_index) + '_follow_' + mutant_name
                else:
                    source_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + source_pattern + "\" " + "../targetFiles/file.test > ../testingResults/repetitive" + str(
                        1) \
                                     + "/" + str(test_case_index) + "_source_" + mutant_name

                    follow_command = r"../Mutants/" + mutant_name + "/bin/grep -E " + "\"" + follow_pattern + "\" " + "../targetFiles/file.test_MR9_follow > ../testingResults/repetitive" + str(
                        1) \
                                     + "/" + str(test_case_index) + "_follow_" + mutant_name
                terminal_source = os.popen(source_command)
                terminal_source.close()
                terminal_follow = os.popen(follow_command)
                terminal_follow.close()

                time.sleep(0.1)

                isKilledMutant = False
                # 调用ＭＲ的验证结果的方法，判断是否揭示故障
                if aMR != 'MR11':
                    isKilledMutant = exec_utl.verify_result_not_MR11(aMR, str(1), str(test_case_index), mutant_name)
                else:
                    isKilledMutant = exec_utl.verify_result_MR11(str(1), str(test_case_index), str(test_case_index),
                                                                 mutant_name)

                if isKilledMutant:
                    if str(test_case_index) not in killed_test_case_indexs:
                        killed_test_case_indexs.append(str(test_case_index))
                    killed_mutanmts.append(mutant_name)
                else:
                    pass
        print("execute a test case")
    print("execute all test cases in one partition")
    partition_info += "enable killed mutants: " + ','.join(ele for ele in killed_test_case_indexs) + ";"
    partition_info += "killed mutants: " + ','.join(ele for ele in killed_mutanmts) + ";"
    partition_info += "partition failure rate: " + str(len(killed_test_case_indexs) / len(partition_test_cases))
    content.append(partition_info + '\n')

for partition_index in range(1, 551):
    execute(partition_index)

f = open('partition_killed_info', 'w+')
for aline in content:
    f.write(aline)
f.close()
















