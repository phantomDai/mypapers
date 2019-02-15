#!/bin/bash

#将Major生成的变异体改名字，其格式为：程序名+序号

#获取变异体的个数
#numSimpleLinear=`ls -l ./SimpleLinear | grep "^d" | wc -l`
#
numSimpleTree=`ls -l ./simpleTree | grep "^d" | wc -l`
#
#numFineGrainedHeap=`ls -l ./fineGrainedHeap | grep "^d" | wc -l`
#
#numSequentialHeap=`ls -l ./sequentialHeap | grep "^d" | wc -l`

#numSkipQueue=`ls -l ./skipQueue | grep "^d" | wc -l`

#改文件的名字

#for ((i=1;i<=$numSimpleLinear;i++))
#do
#    `mv ./SimpleLinear/$i/ ./SimpleLinear/simpleLinear$i/`    	
#done
#
#for ((i=1;i<=$numSimpleTree;i++))
#do		
#    `mv ./SimpleTree/$i/ ./SimpleTree/simpleTree$i/`    	
#done
#
#for ((i=1;i<=$numFineGrainedHeap;i++))
#do
#    `mv ./fineGrainedHeap/$i/ ./fineGrainedHeap/fineGrainedHeap$i/`    	
#done
#
#for ((i=1;i<=$numSequentialHeap;i++))
#do
#    
#    `mv ./sequentialHeap/$i/ ./sequentialHeap/sequentialHeap$i/`    	
#done
#
#for ((i=1;i<=$numSkipQueue;i++))
#do
#    `mv ./skipQueue/$i/ ./skipQueue/skipQueue$i/`    	
#done

#更新SkipQueue类import的部分
#
#for ((i=1;i<=$numSkipQueue;i++))
#do
#    `sed -ie "s/import mutants.skipQueue.skipQueue$i.PrioritySkipList.Node/import mutants.skipQueue.skipQueue$i.PrioritySkipList.Node;/g" ./skipQueue/skipQueue$i/SkipQueue.java`    	
#done


#处理SimpleTree中缺少Bin类的问题
for ((i=1;i<=$numSimpleTree;i++))
do
#	`sed -i "12i import priority.Bin;" ./simpleTree/simpleTree$i/SimpleTree.java`
`sed '12d' ./simpleTree/simpleTree$i/SimpleTree.java`
`cp ./Bin.java ./simpleTree/simpleTree$i/`
`sed -i "10i package mutants.simpleTree.simpleTree$i;" ./simpleTree/simpleTree$i/Bin.java`
done







