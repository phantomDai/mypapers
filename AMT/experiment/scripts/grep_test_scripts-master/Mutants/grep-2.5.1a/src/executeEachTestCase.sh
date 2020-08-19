#!/bin/bash

file_name="TestPool_grep_no_repeat"

rm -rf ./result/*

# 读取testPool中的每一行
i=1
 while read -r line
 do
    # 如果包含"\d -a \D"那么就使用perl解释器来执行正则表达式，
    # 否则使用扩展的正则表达式解释器
    if [[ ${line} =~ '\d' -a ${line} =~ '\D']]
    then
        ./grep -P "$line" ./file.test > ./result/testresult${i} 2>&1 
    else
        ./grep -E "$line" ./file.test > ./result/testresult${i} 2>&1
    fi

   let i+=1
 done < ./${file_name}
