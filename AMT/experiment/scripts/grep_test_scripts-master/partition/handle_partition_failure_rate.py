#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/12/10
# @Anthor   : phantomDai
"""
提取partition_failure_rate中信息
"""

content = []


def get_partition_failure_rate():
    """
    从partition_failure_rate中获得分区以及分区对应的失效率
    """
    with open("partition_failure_rate", 'r') as file:
        for aline in file:
            temp = ""
            temp += aline.strip().split(';')[0] + ";"
            temp += aline.strip().split(';')[4]
            content.append(temp)
    file.close()


def get_max_failure_rate():
    get_partition_failure_rate()
    failure_rates = []

    for aline in content:
        temp_line = aline.split(';')[1]
        arate = temp_line.split(': ')[1]
        failure_rates.append(float(arate))

    # 对所有的失效率进行排序
    # sorted(failure_rates, reverse=True)
    # print(failure_rates)
    # print(failure_rates[0])
    # print(failure_rates[1])
    max_failrure_rate = 0.0
    for rate in failure_rates:
        if rate >= max_failrure_rate:
            max_failrure_rate = rate
        else:
            pass

    print("max:" + str(max_failrure_rate))

    second_failure_rate = 0.0
    for rate in failure_rates:
        if rate == max_failrure_rate:
            continue
        else:
            if rate >= second_failure_rate:
                second_failure_rate = rate
            else:
                pass
    print("second:" + str(second_failure_rate))

    # 计算RAPT的delta参数
    delta = 0.05 / ((1 / max_failrure_rate - 1) +
                    (1 / second_failure_rate - 1 / max_failrure_rate) * 0.8)
    print("delta:" + str(delta))


get_max_failure_rate()
