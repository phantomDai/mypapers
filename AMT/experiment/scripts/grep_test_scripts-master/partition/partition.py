#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/10/28
# @Anthor   : phantomDai
"""
this script is responsible for dividing the input domain into partitions.
We combine choices with different categories belonged to the group A.
"""
import os

import constant.constantNumber as constant


def partition_step_one():
    """
    the first step to divide the input domain
    :return: generate a file named partition_scheme_1.0
    """
    # the choices of group A
    considered_choices = ["NA", "NP", "YW", "NW", "YD", "ND", "YS", "NS",
                          "N1", "N2", "N3", "N4", "N5", "N6", "N7", "N8",
                          "N9", "N10", "N11", "N12", "DOT", "UR", "LR", "NR"]

    # new test frames
    new_test_frame_list = []

    with open('TestFrames_grep_no_repeat', 'r') as source_file:
        # read each line of source_file
        for line in source_file:
            # a temp array
            temp_choices = line.strip().split(";")
            # replace choices that not belong to the group a with '#'
            modify_temp_choices = [
                ele if ele in considered_choices else '#' for ele in temp_choices]
            new_test_frame = ';'.join(ele for ele in modify_temp_choices)

            new_test_frame_list.append(new_test_frame)

    source_file.close()

    # write result
    write_result('partition_scheme_testframes_1.1', new_test_frame_list)


def identify_test_frames():
    """
    identify those test frames whose all of choices are belonging to group b
    :return:
    """
    indexs_list = []
    with open('partition_scheme_testframes_1.1', 'r') as file:
        counter = 1
        for line in file:
            temp_choices = line.strip().split(';')
            flag = True
            for ele in temp_choices:
                if ele != '#':
                    flag = False
                    break
            if flag:
                indexs_list.append(counter)
            counter = counter + 1
    file.close()
    print(indexs_list)


def delete_invalide_testframes():
    """
    delete invalide test frames and test cases
    :return:
    """
    new_testframes = []

    invalide_indexs = [18, 71, 168, 197, 214, 255, 257,
                       277, 299, 335, 355, 543, 598, 609, 647, 672, 732]

    with open('partition_scheme_testframes_1.1', 'r') as file_testframes:
        counter = 1
        for line in file_testframes:
            if counter in invalide_indexs:
                counter = counter + 1
                continue
            new_testframes.append(line.strip())
            counter = counter + 1

    file_testframes.close()
    write_result('partition_scheme_testframes_1.2', new_testframes)

    new_testcases = []
    with open('partition_scheme_testcases_1.1', 'r') as file_testcases:
        counter_star = 1
        for line_star in file_testcases:
            if counter_star in invalide_indexs:
                counter_star = counter_star + 1
                continue
            new_testcases.append(line_star.strip())
            counter_star = counter_star + 1
    file_testcases.close()
    write_result('partition_scheme_testcases_1.2', new_testcases)

    new_testframes_star = []
    with open('TestFrames_grep_no_repeat_1.1', 'r') as file_testframes_star:
        counter_star_1 = 1
        for line_star_1 in file_testframes_star:
            if counter_star_1 in invalide_indexs:
                counter_star_1 = counter_star_1 + 1
                continue
            new_testframes_star.append(line_star_1.strip())
            counter_star_1 = counter_star_1 + 1
    file_testframes_star.close()
    write_result('TestFrames_grep_no_repeat_1.2', new_testframes_star)


def partition_step_two():
    """
    忽略选项的顺序
    :return:
    """

    partition_scheme_testcases = []
    partition_scheme_testframes = []
    testframes_grep_no_repeat = []
    # 需要删除的测试帧和测试用例的编号
    indexs = []

    # 存放所有的测试帧的选项
    choices = []
    final_scheme = []

    with open('partition_scheme_testframes_1.2', 'r') as temp_file:
        counter = 1
        for temp_line in temp_file:
            temp_choices = temp_line.strip().split(';')
            temp_list = [ele for ele in temp_choices if ele != '#']
            temp_set = set(ele for ele in temp_choices if ele != '#')

            if temp_set in choices:
                indexs.append(counter)
                counter = counter + 1
                continue
            else:
                choices.append(temp_set)
                final_scheme.append(temp_list)
                counter = counter + 1
    temp_file.close()

    partition_scheme = []
    for aSet in final_scheme:
        temp_str = ';'.join(ele for ele in aSet)
        partition_scheme.append(temp_str)
    write_result('partition_scheme', partition_scheme)


def write_result(file_name, li=[]):
    """
    write elements to file
    :param file_name: file name
    :param li: elements
    :return:
    """

    file_path = os.path.join(constant.partition_dir_path, file_name)

    new_file = open(file_path, 'w+')

    new_li = [ele + '\n' for ele in li]

    new_file.writelines(new_li)

    new_file.close()



# partition_step_one()
# identify_test_frames()
# delete_invalide_testframes()
partition_step_two()
