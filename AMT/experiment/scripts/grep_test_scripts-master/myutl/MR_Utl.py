#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/5
# @Anthor   : phantomDai
"""
一些蜕变关系实现过程中的工具接口
"""
import re
import os

class MyUtl(object):

    def get_range_charaters_MR1(self, source_test_case):
        """
        从一个字符串中获取一个范围字符集合，例如[1-3]
        :param aline: 一个ｐａｔｔｅｒｎ
        :return: 范围集合
        """
        target_str = re.findall(r'\[\w-\w\]', source_test_case)
        return target_str[0]

    def get_collection_characters_MR3(self, source_test_case):
        """
        从一个字符串中获取一个范围字符集合，例如[abc]
        :param aline: 一个ｐａｔｔｅｒｎ
        :return: 范围集合
        """
        target_str = re.findall(r'\[\w*\]', source_test_case)
        return target_str[0]





    def verify_equal(self, repetitive_index, testing_index, mutant_name):

        """
        验证原始测试用例与衍生测试用例的执行结果
        :param repetitive_index: 重复试验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_file = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index, testing_index + '_source_' + mutant_name)
        follow_file = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index, testing_index + '_follow_' + mutant_name)



        if not os.path.exists(source_file) or not os.path.exists(follow_file):
            return False
        else:
            pass

        shell_command = 'diff ../testingResults/repetitive' + repetitive_index + '/' + testing_index + '_source_' + mutant_name + \
                        ' ../testingResults/' + '/repetitive' + repetitive_index + '/' + testing_index + '_follow_' + mutant_name

        result = os.popen(shell_command).read()

        if len(result) == 0:
            return False
        else:
            return True

    def verify_appertain(self, repetitive_index, testing_index, mutant_name):
        """
        验证原始测试用例的执行结果是否都出现在衍生测试用例的结果中
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index, testing_index + '_source_' + mutant_name)
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index, testing_index + '_follow_' + mutant_name)

        if not os.path.exists(source_result_path) or not os.path.exists(follow_result_path):
            return False
        else:
            pass

        if os.path.getsize(source_result_path) == 0 and os.path.getsize(follow_result_path) == 0:
            return False





        flag = False

        follow_content = []
        with open(follow_result_path, 'r') as follow_file:
            for aline in follow_file:
                follow_content.append(aline)

        with open(source_result_path, 'r') as source_file:
            for line in source_file:
                if line not in follow_content:
                    flag = True
                    break
        source_file.close()

        return flag


    def verify_includ(self, repetitive_index, testing_index, mutant_name):
        """
        验证原始测试用例的执行结果是否包含衍生测试用例的结果
        :param repetitive_index: 重复实验的编号
        :param testing_index: 执行的测试序号（执行了第几个测试用例）
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index,
                                          testing_index + '_source_' + mutant_name)
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index,
                                          testing_index + '_follow_' + mutant_name)

        if not os.path.exists(source_result_path) or not os.path.exists(follow_result_path):
            return False
        else:
            pass


        if os.path.getsize(source_result_path) == 0 and os.path.getsize(follow_result_path) == 0:
            return False





        flag = False

        with open(follow_result_path, 'r') as follow_file:
            for line in follow_file:
                with open(source_result_path, 'r') as source_file:
                    if line.strip() not in source_file.readlines():
                        flag = True
                        break
                source_file.close()
        follow_file.close()

        return flag


    def verify_result_MR9(self, repetitive_index, testing_index, mutant_name):
        """
        验证MR10的执行结果：原始测试用例的执行结果出现在衍生测试用例的执行结果中，并且包含２１８１１１
        :param repetitive_index:　重复实验的编号
        :param testing_index:　测试用力执行的个数
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index,
                                          testing_index + '_source_' + mutant_name)
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index,
                                          testing_index + '_follow_' + mutant_name)

        if not os.path.exists(source_result_path) or not os.path.exists(follow_result_path):
            return False
        else:
            pass


        flag = False
        source_results = []
        follow_results = []

        if os.path.getsize(source_result_path) != 0:
            with open(source_result_path, 'r') as source_file:
                for aline in source_file:
                    source_results.append(aline)
            source_file.close()

            if os.path.getsize(follow_result_path) == 0:
                flag = True
            else:
                with open(follow_result_path, 'r') as follow_file:
                    for aline in follow_file:
                        follow_results.append(aline)
                follow_file.close()

            if '218111\n' not in follow_results:
                flag = True
            else:
                for aline in source_results:
                    if aline not in follow_results:
                        flag = True
                    else:
                        pass
        else:
            if os.path.getsize(follow_result_path) == 0:
                flag = True
            else:
                with open(follow_result_path, 'r') as follow_file:
                    for aline in follow_file:
                        follow_results.append(aline)
                follow_file.close()
                if '218111\n' not in follow_results:
                    flag = True
                else:
                    pass
        return flag


    def verify_result_MR11(self, repetitive_index, testing_index, test_case_index, mutant_name):
        """
        验证MR11的执行结果：原始测试用例的执行结果出现在衍生测试用例的执行结果中
        :param repetitive_index:　重复实验的编号
        :param testing_index:　测试用力执行的个数
        :param test_case_index: the index of test case
        :return: 是否揭示了故障：Ｔｒｕｅ，表示揭示故障；Ｆａｌｓｅ表示没有揭示故障
        """
        source_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index,
                                          testing_index + '_source_' + mutant_name)
        follow_result_path = os.path.join(os.path.abspath('..'), 'testingResults', 'repetitive' + repetitive_index,
                                          testing_index + '_follow_' + mutant_name)

        if not os.path.exists(source_result_path) or not os.path.exists(follow_result_path):
            return False
        else:
            pass


        target_file_path = os.path.join(os.path.abspath('..'), 'targetFiles', 'MR11_' + test_case_index)

        # 出现以下任意一种情况，则表明违反了蜕变关系：（１）原始和衍生测试用例的执行结果一样；（２）原始测试
        # 用例和衍生测试用例的结果加起来和目标文件不一样
        target_file_content = []
        with open(target_file_path, 'r') as file:
            for aline in file:
                target_file_content.append(aline)
        file.close()

        source_result = []

        with open(source_result_path, 'r') as file:
            for aline in file:
                source_result.append(aline)
        file.close()

        follow_result = []

        with open(follow_result_path, 'r') as file:
            for aline in file:
                follow_result.append(aline)
        file.close()

        # 判断原始结果与衍生结果是否相等
        if len(source_result) != 1 or len(follow_result) != 1:
            return True
        elif source_result[0] == follow_result[0]:
            return True
        elif len(source_result) + len(follow_result) != len(target_file_content):
            return True
        elif source_result[0] not in target_file_content or follow_result[0] not in target_file_content:
            return True
        else:
            return False










if __name__ == '__main__':
    utl = MyUtl()
    # print(utl.verify_appertain('mutant1', '1'))
    print(utl.get_range_charaters_MR1(r"\<\s|\d(^[[:alnum:]])(\b.\b)\2\!(\W+)([^6-8])"))