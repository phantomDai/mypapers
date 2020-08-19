#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/10/29
# @Anthor   : phantomDai
"""
为分区模式分配测试用例
"""
import linecache
from constant import constantNumber as constant


def allocation_testcases():
    """
    为每一个分区模式分配测试用例
    :return:
    """
    partition_testcases = {}

    # 存放所有的分区模式
    partition_scheme = []
    partition_map = {}

    # 读取所有的分区模式
    with open(constant.partition_scheme_path, 'r') as temp_file:
        for temp_line in temp_file:
            temp_list = temp_line.strip().split(';')
            temp_set = set(ele for ele in temp_list)
            partition_scheme.append(temp_set)
    temp_file.close()

    data_dict = {}
    line_number = 0
    for i in range(0, len(partition_scheme)):
        ascheme = partition_scheme[i]
        indexs = []
        with open(constant.partition_scheme_testframes_path, 'r') as file:
            counter = 0
            for line in file:
                counter = counter + 1
                temp_list = line.strip().split(';')
                # 只保留感兴趣的选项
                filtration_temp_list = [ele for ele in temp_list if ele != '#']
                flag = True
                if len(filtration_temp_list) != len(ascheme):
                    flag = False
                    continue
                for ele in filtration_temp_list:
                    if ele not in ascheme:
                        flag = False
                if flag:
                    indexs.append(counter)
        line_number += 1
        temp_str = linecache.getline(
            constant.partition_scheme_path, line_number).strip()
        partition_map[line_number] = indexs
        data_dict[temp_str] = indexs

    partition_scheme_testcases_file = open(
        constant.partition_scheme_testcases_file_path, 'w+')
    for ele in data_dict.items():
        partition_scheme_testcases_file.write(str(ele) + '\n')
    partition_scheme_testcases_file.close()

    partition_map_file = open(constant.partition_map_file_path, 'w+')
    for item in partition_map.items():
        partition_map_file.write(str(item) + '\n')
    partition_map_file.close()

    return partition_map


def get_partition_map():
    partition_map = {}
    with open(constant.partition_map_file_path, 'r') as file:
        for aline in file:
            aline = aline.strip().replace('(', '').replace(
                ')', '').replace('[', '').replace(']', '')
            temp_list = aline.split(', ')
            index = temp_list[0]
            temp_list.remove(index)
            partition_map[int(index)] = temp_list
    file.close()

    return partition_map
