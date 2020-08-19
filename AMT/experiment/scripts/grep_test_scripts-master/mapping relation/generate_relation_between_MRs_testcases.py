#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/10/29
# @Anthor   : phantomDai

import re
import os
from myutl.Utl import Utl

test_frame_path = os.path.join(os.path.abspath('..'), 'mapping relation', 'TestFrames_grep_no_repeat_1.2')

test_case_path = os.path.join(os.path.abspath('..'), 'mapping relation', 'partition_scheme_testcases_1.2')

parent_path = os.path.join(os.path.abspath('..'), 'mapping relation')

# 实例化工具类的对象
tool = Utl()

def genrate_MR4():
    """
    从all_range_sets中去掉MAX_{ASC} - MIN_{ASC} < 2 的测试用例
    """

    all_range_sets_file = os.path.join(parent_path, 'all_range_sets')

    file_range_sets = tool.get_file_object(all_range_sets_file)

    #　存放无效的范围值，例如[1-2]
    invalid_range_sets = []


    for aline in file_range_sets:
        aline = aline.strip().replace('[', '').replace(']', '')
        min_asc = ord(aline.split('-')[0])
        max_asc = ord(aline.split('-')[1])
        if (max_asc - min_asc) < 2:
            invalid_range_sets.append(aline.strip())

    MR4_relation_path = os.path.join(parent_path, 'MR4_relation')
    file_MR4_relation = tool.get_file_object(MR4_relation_path)

    valid_test_cases = []

    for aline in file_MR4_relation:
        flag = True
        for item in invalid_range_sets:
            if item in aline.strip():
                flag = False
        if flag:
            valid_test_cases.append(aline)


    MR4_file_path = os.path.join(parent_path, 'MR4')

    tool.write_test_cases(MR4_file_path, valid_test_cases)

def generate_MR7():

    # 获取有效地范围值
    all_range_sets_path = os.path.join(parent_path, 'all_range_sets')

    range_set_file = tool.get_file_object(all_range_sets_path)

    valid_range_set = []

    for item in range_set_file:
        index = item.split(':')[0]
        item = item.split(':')[1].strip().replace('[', '').replace(']', '')
        min_asc = ord(item.split('-')[0])
        max_asc = ord(item.split('-')[1])
        if (max_asc - min_asc) >= 2:
            valid_range_set.append(index)

    range_set_file.close()

    # 获取有效的测试用例
    test_case_file = tool.get_file_object(test_case_path)

    valid_test_case = []

    tricktrock = 1

    for aline in test_case_file:
        if str(tricktrock) in valid_range_set:
            valid_test_case.append(str(tricktrock) + ":" + aline)
        tricktrock += 1
    test_case_file.close()

    MR7_path = os.path.join(parent_path, 'MR7')
    tool.write_test_cases(MR7_path, valid_test_case)

def generate_MR8():

    # 获取有效地范围值
    all_range_sets_path = os.path.join(parent_path, 'all_range_sets')

    range_set_file = tool.get_file_object(all_range_sets_path)

    valid_range_set = []

    for item in range_set_file:
        index = item.split(':')[0]
        item = item.split(':')[1].strip().replace('[', '').replace(']', '')
        max_asc = ord(item.split('-')[1])
        if max_asc != 57 and max_asc != 90 and max_asc != 122:
            valid_range_set.append(index)

    range_set_file.close()

    # 获取有效的测试用例
    test_case_file = tool.get_file_object(test_case_path)

    valid_test_case = []

    tricktrock = 1

    for aline in test_case_file:
        if str(tricktrock) in valid_range_set:
            valid_test_case.append(str(tricktrock) + ":" + aline)
        tricktrock += 1
    test_case_file.close()

    MR8_path = os.path.join(parent_path, 'MR8')
    tool.write_test_cases(MR8_path, valid_test_case)

def generate_MR9():

    test_case_file = tool.get_file_object(test_case_path)

    invalid_meta_charaters = ['[[:digit:]]', '[^[:digit:]]', '\w', '\W']

    valid_test_cases = []

    tricktrock = 1
    for aline in test_case_file:
        flag = True
        for item in invalid_meta_charaters:
            if item in aline.strip():
                flag = False
                break
        if flag:
            valid_test_cases.append(str(tricktrock) + ':' + aline)
        tricktrock += 1

    MR9_path = os.path.join(parent_path, 'MR9')
    tool.write_test_cases(MR9_path,valid_test_cases)

def genrate_MR10():
    """
    读取最后得到normal_literals_4_MR10_lines文件得到最后的ＭＲ１０文件
    :return:
    """
    file_path = os.path.join(parent_path, 'MR10Relation', 'normal_literals_4_MR10_lines')
    valid_test_cases_index = []

    for aline in tool.get_file_object(file_path):
        valid_test_cases_index.append(aline.strip().split(':')[0])

    # 判断normal_literal后面存不存在{1}或者＋
    repetive_indexs = []
    normal_literals_path = os.path.join(parent_path, 'MR10Relation', 'normal_literals_4_MR10_lines')
    MR10_path = os.path.join(parent_path, 'MR10Relation', 'MR10')
    for i in range(1, 98722):
        complete_test_case = tool.get_line_content(MR10_path, i).split(':')[1]
        normal_literal = tool.get_line_content(normal_literals_path, i).split(':')[1]
        temp_str = normal_literal + '{'
        if normal_literal + '{' in complete_test_case or normal_literal + '+' in complete_test_case:
            repetive_indexs.append(tool.get_line_content(MR10_path, i).split(':')[0])

    for item in repetive_indexs:
        if item in valid_test_cases_index:
            valid_test_cases_index.remove(item)


    valid_test_cases = []
    tricktrock = 1
    for aline in tool.get_file_object(test_case_path):
        if str(tricktrock) in valid_test_cases_index:
            valid_test_cases.append(str(tricktrock) + ':' + aline)
        tricktrock += 1

    tool.write_test_cases(os.path.join(parent_path, 'MR10'), valid_test_cases)


def generate_MR11():
    valid_choices = ['\w', '\W', '\s', '\S', '[[:digit:]]', '[^[:digit:]]', '[[:alnum:]]', '[^[:alnum:]]']

    test_case_file = tool.get_file_object(test_case_path)

    valid_test_cases = []

    counter = 1
    for aline in test_case_file:
        tricktrock = 0
        for item in valid_choices:
            if item in aline.strip():
                tricktrock += 1

        if tricktrock == 1:
            valid_test_cases.append(str(counter) + ":" + aline)
        counter += 1

    MR11_path = os.path.join(parent_path, 'MR11')
    tool.write_test_cases(MR11_path, valid_test_cases)

def generate_MR12():
    """
    筛选出适用于该ＭＲ的pattern的过程如下：
    读取normal_literals中内容，筛选非ＮＵＬＬ的行
    :return:
    """
    test_case_indexs = []

    normal_literals_path = os.path.join(parent_path, 'normal_literals')

    normal_literals_file = tool.get_file_object(normal_literals_path)

    tricktrock = 1

    for aline in normal_literals_file:
        if aline.strip() != 'NULL':
            test_case_indexs.append(str(tricktrock))
        else:
            pass
        tricktrock += 1

    print("wancheng")

    test_cases = []

    counter = 1

    test_case_file = tool.get_file_object(test_case_path)

    for aline in test_case_file:
        if str(counter) in test_case_indexs:
            test_cases.append(str(counter) + ":" + aline)
        counter += 1
    print("wancheng")

    MR12_path = os.path.join(parent_path, 'MR12Relation', 'MR12')

    tool.write_test_cases(MR12_path, test_cases)






def generate_testcase_2_MRs():
    """
    产生测试用例与ＭＲ之间的映射关系，即测试用例可以在哪些蜕变关系上使用
    １：ＭＲｓ
    2:MRs
    １，２表示ｐａｒｔｉｔｉｏｎ_scheme_testcases_1.2中的测试用例编号
    :return:
    """

    testcase_2_MRs = {}

    # 初始化字典，键为测试用例的编号，值为列表，该列表存储该测试用例可以作用到的蜕变关系
    for index in range(1, 101194):
        testcase_2_MRs[str(index)] = []

    #　便利每一个ＭＲｘ获得每一个测试用例
    for i in range(1, 13):
        path = os.path.join(parent_path, 'MR' + str(i) + 'Relation', 'MR' + str(i))

        file = tool.get_file_object(path)

        # 便利当前的文件内容
        for aline in file:
            index = aline.split(":")[0]
            temp_list = testcase_2_MRs[index]
            temp_list.append('MR' + str(i))
            testcase_2_MRs[index] = temp_list
        file.close()

    # 输出结果
    testcase_2_MRs_file_path = os.path.join(parent_path, 'testcase_2_MRs')
    tool.write_info_from_dict(testcase_2_MRs_file_path, testcase_2_MRs)
    # for key, value in testcase_2_MRs.items():
    #     print('{key}:{value}'.format(key=key,value=value))

def check_testcases_2_MRs():
    """
    检测testcase_2_MＲs中是否存在测试用例没有对应的蜕变关系
    :return:
    """
    testcase_2_MRs_file = os.path.join(parent_path, 'testcase_2_MRs')
    file = tool.get_file_object(testcase_2_MRs_file)

    tricktrock = 1
    for aline in file:
        MRs = aline.strip().split(':')[1].split(', ')
        if len(MRs) == 0:
            print(tricktrock)
        tricktrock += 1

    file.close()

# generate_testcase_2_MRs()
check_testcases_2_MRs()
# genrate_MR10()

# generate_MR12()














