#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/14
# @Anthor   : phantomDai
"""
execute each test case
"""
import os
import time


def execute_test_case():
    indexs = []
    wrong_contents = ["grep: malformed repeat count",
                      "grep: unfinished repeat count",
                      "grep: 无效的向后引用",
                      "grep: 不匹配的 ( 或 \(",
                      "grep: 不匹配的 ) 或 \)",
                      "grep: 尾端的反斜线"
                      ]
    with open('partition_scheme_testcases_1.2', 'r') as file:
        counter = 0
        for aline in file:
            counter += 1
            aline = aline.strip()
            shell_command = r'./grep -E ' + "\"" + aline + "\" ./file.test"
            # print(str(counter) + ":    " + shell_command)
            content = os.popen(shell_command).read()
            if content in wrong_contents:
                indexs.append(counter)

    file.close()

    print(indexs)


def get_all_results():
    parent_path = os.path.join(os.getcwd(), 'result')
    all_results = []
    for i in range(1, 101194):
        file_path = os.path.join(parent_path, str(i))
        if os.path.getsize(file_path) == 0:
            continue
        else:
            temp_str = ''
            with open(file_path, 'r') as file:
                for aline in file:
                    temp_str += aline
            file.close()
            if temp_str not in all_results:
                all_results.append(temp_str)

    file = open('all_kind_results', 'w+')
    file.writelines(all_results)
    file.close()


def whether_extis():
    indexs = []
    parent_path = os.path.join(os.getcwd(), 'result')
    for i in range(1, 101194):
        file_path = os.path.join(parent_path, str(i))
        if os.path.exists(file_path):
            pass
        else:
            indexs.append(i)
    print(len(indexs))

    for index in indexs:
        comman = "touch ./result/" + str(index)
        os.popen(comman)


def read_results_get_wrongs_test_cases():
    """
    从每个测试用例的执行结果中，获取空白执行结果以及报错的测试用例执行结果
    """
    wrong_contents = ["grep: malformed repeat count",
                      "grep: unfinished repeat count",
                      "grep: 无效的向后引用",
                      "grep: 不匹配的 ( 或 \(",
                      "grep: 不匹配的 ) 或 \)",
                      "grep: 尾端的反斜线"
                      ]
    # 存放产生错误结果的测试用例的编号
    wrong_results_test_cases = []
    # 存放不输出任何结果的测试用例的编号
    block_result_test_cases = []
    # 存放file.test文件的内容，不删除换行符
    target_file_content = []

    with open('file.test', 'r')as file:
        for aline in file:
            target_file_content.append(aline)
    file.close()
    for index in range(0, 101194):
        file_path = os.path.join(os.getcwd(), 'result', str(index))
        if os.path.getsize(file_path) == 0:
            block_result_test_cases.append(str(index) + '\n')
        else:
            with open(file_path, 'r') as file:
                for aline in file:
                    if aline.strip() in wrong_contents:
                        wrong_results_test_cases.append(str(index) + '\n')
                        break
            file.close()
        index += 1

    file1 = open('block_test_cases', 'w+')
    file1.writelines(block_result_test_cases)
    file1.close()

    file2 = open('wrong_test_cases', 'w+')
    file2.writelines(wrong_results_test_cases)
    file2.close()


# get_all_results()
# whether_extis()
# execute_test_case()
read_results_get_wrongs_test_cases()
