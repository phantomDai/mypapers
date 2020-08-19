import numpy as np
import os
from myutl.Utl import Utl
from MRs.MR import *
import linecache
import random
from constant import constantNumber as constant


class execute_utl(object):
    """
    为执行测试提供常用的接口
    """

    mapping_relation_path = os.path.join(
        os.path.abspath('../..'), 'mapping relation')

    tool = Utl()

    def __init__(self):
        self.__choices_add = dict().fromkeys(['MR1', 'MR2', ], [])
        self.__partition_scheme = self.__get_partition_scheme()

    def __get_partition_scheme(self):

        partition_scheme = []

        a = constant.partition_scheme_path

        with open(constant.partition_scheme_path, 'r') as file:
            for aline in file:
                temp_list = aline.strip().split(';')
                temp_set = set(ele for ele in temp_list)
                partition_scheme.append(temp_set)
        file.close()
        return partition_scheme

    def generate_random_number(self, seed):
        """
        根据指定的随机数种子生成一系列的随机数，并返回一个列表
        """
        # 设置随机数的种子
        # start_time = int(round(time.time() * 1000))
        np.random.seed(seed)
        random_list = [np.random.randint(1, 101194) for i in range(100)]

        # ended_time = int(round(time.time() * 1000))
        return random_list

    def get_test_case_MR_list(self, test_case_index):
        """
        获取测试用例所有可能作用的蜕变关系
        :test_case_index是测试用例的编号 (int)
        """
        test_cases_2_mrs_path = os.path.join(
            self.mapping_relation_path, 'testcase_2_MRs')

        # 读取一行的内容
        aline = linecache.getline(test_cases_2_mrs_path, int(test_case_index))
        aline = aline.replace('\'', '').replace('\'', '').strip().split(':')[
            1].replace('[', '').replace(']', '')
        MRs = aline.split(', ')

        return MRs

    def random_select_MR(self, MR_list):
        """
        randomly select a MR from the MR list
        :param MR_list:
        :return: the name of selected MR
        """
        index = random.randint(0, len(MR_list) - 1)

        return MR_list[index]

    def generate_follow_test_case(self, MR_name, source_test_case, source_test_case_index):
        """
        根据选择的蜕变关系以及原始测试用例生成衍生测试用例
        :param MR_name: 　选择的蜕变关系的名称
        :param source_test_case: 原始测试用例
        :return: 衍生测试用例
        """
        factory = MR_factory()
        MR_obj = factory.choose_MR(MR_name)
        return MR_obj.generate_follow_test_case(source_test_case, source_test_case_index)

    def verify_result_not_MR11(self, MR_name, repetivite_index, testing_index, mutant_name):
        return MR_factory().verify_result_no_MR11(MR_name, repetivite_index, testing_index, mutant_name)

    def verify_result_MR11(self, repetitive_index, testing_index, test_case_index, mutant_name):
        return MR_factory().verify_MR11_result(repetitive_index, testing_index, test_case_index, mutant_name)

    def get_wrong_patterns(self):
        """
        fanhui cuowu de patterns
        :return:
        """
        wrong_patterns = [897, 4020, 7172, 12207, 13065, 14292, 14558, 19179, 20295, 20651, 22651,
                          23804, 25538, 30545, 32414, 33642, 33908, 34762, 36159, 42623, 49107,
                          50461, 52338, 52402, 53975, 56767, 58235, 59879, 63682, 63867, 64494,
                          70266, 71852, 77634, 79335, 81911, 82506, 83695, 84299, 85994, 86212, 86298,
                          88781, 91300, 93940, 98676, 5922]
        file_path = os.path.join(os.path.abspath(
            '..'), 'files', 'executed_wrong_test_cases')
        with open(file_path, 'r') as file:
            for aline in file:
                if int(aline.strip()) not in wrong_patterns:
                    wrong_patterns.append(int(aline.strip()))
        file.close()

        return wrong_patterns

    def __get_follow_test_case_test_frame(self, source_test_frame, MR_name):

        follow_test_frame = source_test_frame

        if MR_name == 'MR1':
            temp_list = ['NR', 'UR', 'LR']
            for item in temp_list:
                if item in follow_test_frame:
                    follow_test_frame = follow_test_frame.replace(item, '')
                    break
                else:
                    pass
            if 'NA' in follow_test_frame:
                pass
            else:
                follow_test_frame += ';NA'
        elif MR_name == 'MR2':
            temp_list = ['NR', 'UR', 'LR']
            for item in temp_list:
                if item in follow_test_frame:
                    follow_test_frame = follow_test_frame.replace(item, '')
                    break
                else:
                    pass

            if 'NA' not in follow_test_frame:
                follow_test_frame += (';NA')
            else:
                pass
        elif MR_name == 'MR3':
            pass
        elif MR_name == 'MR4':
            pass
        elif MR_name == 'MR5':
            pass
        elif MR_name == 'MR6':
            pass
        elif MR_name == 'MR7':
            pass
        elif MR_name == 'MR8':
            pass
        elif MR_name == 'MR9':
            if 'N3' not in follow_test_frame:
                follow_test_frame += ';N3'
            else:
                pass
        elif MR_name == 'MR10':
            pass
        elif MR_name == 'MR11':
            pass
        else:
            if 'DOT' not in follow_test_frame:
                follow_test_frame += ';DOT'
            else:
                pass
        return follow_test_frame

    def get_follow_test_case_partition(self, source_test_case_index,
                                       ex_source_partition, MR_name):
        """
        判断衍生测试用例所在的分区
        """

        # 获取原始测试用例的测试帧
        aline = linecache.getline(
            constant.test_frame_file_path, source_test_case_index).strip()
        # 获取衍生测试用例的测试帧
        follow_test_frame = self.__get_follow_test_case_test_frame(
            aline, MR_name)
        if aline == follow_test_frame:
            return ex_source_partition
        else:
            # 去掉测试帧中的"#"
            temp_list = []
            for ele in follow_test_frame.split(';'):
                if ele != '#' and ele != '':
                    temp_list.append(ele)
                else:
                    pass
            follow_test_frame = ';'.join(ele for ele in temp_list)
            follow_set = set(ele for ele in temp_list)
            # 判断衍生测试用例所在的分区
            partion_index = 0
            for aset in self.__partition_scheme:
                partion_index += 1
                if follow_set == aset:
                    return partion_index

    def PBMR_select_MR(self, MR_list):
        """
        select a MR according to the PBMR strategy
        :param test_case_index: source test case index
        :param MR_list: condicate MRs
        :return: MR
        """
        return MR_list[random.randint(0, len(MR_list) - 1)]
        list2 = []
        list3 = []
        list1 = []
        list0 = []
        if 'MR1' in MR_list:
            list2.append('MR1')
        elif 'MR9' in MR_list:
            list2.append('MR9')
        elif 'MR2' in MR_list:
            list3.append('MR2')
        else:
            pass
        for item in MR_list:
            if item == 'MR3' or item == 'MR4' or item == 'MR5' or item == 'MR6' or item == 'MR10' or item == 'MR12':
                list1.append(item)
            elif item == 'MR7' or item == 'MR8' or item == 'MR11':
                list0.append(item)
            else:
                pass
        if 0 != len(list3):
            return 'MR2'
        elif 0 != len(list2):
            return list2[random.randint(0, len(list2) - 1)]
        elif 0 != len(list1):
            return list1[random.randint(0, len(list1) - 1)]
        elif 0 != len(list0):
            return list0[random.randint(0, len(list0) - 1)]
        else:
            pass





if __name__ == '__main__':
    utl = execute_utl()
    print(utl.get_test_case_MR_list(98540))
    # utl.generate_random_number(1)
    # utl.get_wrong_patterns()
