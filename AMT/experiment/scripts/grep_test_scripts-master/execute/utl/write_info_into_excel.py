#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time     : 2019/11/18
# @Anthor   : phantomDai
"""
Measure	    F-measure	F2-measure	FSelectTime	FGenerateTime	FExecuteTime	F2SelectTime	F2GenerateTime	F2ExecuteTime
均值：
方差：
repetitive1
repetitive2
.
.
.
repetitive30
"""
import xlwt
import xlrd
import os
from xlutils.copy import copy


header = ['Measure', 'F-measure', 'F2-measure', 'FSelectTime', 'FGenerateTime', 'FExecuteTime',
          'F2SelectTime', 'F2GenerateTime', 'F2ExecuteTime']

def write_info(file_name, all_averages, all_variance, all_F, all_F2, all_F_select, all_F_generate,
               all_F_execute, all_F2_select, all_F2_generate, all_F2_execute):

    workbook = None
    sheet = None
    row = 0
    if os.path.exists(file_name):
        old_workbook = xlrd.open_workbook(file_name)
        workbook = copy(old_workbook)
        sheet = workbook.get_sheet("sheet1")
        row = sheet.nrows + 1
    else:
        workbook = xlwt.Workbook(encoding='utf-8')
        sheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)



    for i in range(0, len(header)):
        sheet.write(row, i, header[i])

    row += 1
    sheet.write(row, 0, '均值：')
    for i in range(1, len(header)):
        sheet.write(row, i, all_averages[i - 1])

    row += 1
    sheet.write(row, 0, '方差：')
    for i in range(1, len(header)):
        sheet.write(row, i, all_variance[i - 1])

    for i in range(1, 31):
        sheet.write(row + i, 0, 'repetitive' + str(i))
        for col in range(1, len(header)):
            sheet.write(row + i, 1, all_F[i - 1])
            sheet.write(row + i, 2, all_F2[i - 1])
            sheet.write(row + i, 3, all_F_select[i - 1])
            sheet.write(row + i, 4, all_F_execute[i - 1])
            sheet.write(row + i, 5, all_F_generate[i - 1])
            sheet.write(row + i, 6, all_F2_select[i - 1])
            sheet.write(row + i, 7, all_F2_generate[i - 1])
            sheet.write(row + i, 8, all_F2_execute[i - 1])

    workbook.save(file_name)
