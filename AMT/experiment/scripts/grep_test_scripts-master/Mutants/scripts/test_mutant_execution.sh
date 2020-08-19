#!/bin/bash

# 设置当前目录
current_dir="/home/phantom/dmt-paper/grep/Mutants/scripts/"

# 设置target file的位置
target_file_path="/home/phantom/dmt-paper/grep/inputfile/file.test"

# 设置测试用例的位置
testpool_path="/home/phantom/dmt-paper/grep/scripts/removeRepeatTestFrames/TestPool_grep_no_repeat"

# 设置变异体的目录
mutant_parent_dir="/home/phantom/dmt-paper/grep/Mutants"


# 遍历所有的变异体
#for i in {1..20}
for i in {1..2}
do
    #　每一个变异体的可执行文件的位置
    mutant_dir="${mutant_parent_dir}/grep_v${i}/bin"
    
    # 将所有的patterns和target file放进每一个mutant_dir所在的目录
    cp ${testpool_path} ${mutant_dir}
    cp ${target_file_path} ${mutant_dir}
done


