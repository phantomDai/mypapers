#!/bin/bash

file_name="TestPool_grep_no_repeat"

rm -rf ./result/*

# 读取testPool中的每一行
i=1
 while read -r line
 do
   echo ${i}
   ./grep "$line" ./file.test > ./result/testresult${i}
   let i+=1
 done < ./${file_name}
