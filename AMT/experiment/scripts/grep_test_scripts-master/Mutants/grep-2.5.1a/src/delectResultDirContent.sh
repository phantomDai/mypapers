#!/bin/bash

counter=`ls -l ./result | grep "^-" | wc -l`
echo ${counter}

for((i=1;i<=${counter};i++))
do
    rm ./result/testresult${i}
done





    
