#!/bin/bash
numSimpleLinear=`ls -l ./SimpleLinear | grep "^d" | wc -l`

numSimpleTree=`ls -l ./SimpleTree | grep "^d" | wc -l`

numFineGrainedHeap=`ls -l ./fineGrainedHeap | grep "^d" | wc -l`

numSequentialHeap=`ls -l ./sequentialHeap | grep "^d" | wc -l`

numSkipQueue=`ls -l ./skipQueue | grep "^d" | wc -l`

#for ((i=1;i<=$numSimpleLinear;i++))
#do
#
#`sed -i "10i package mutants.simpleLinear.simpleLinear$i;" ./SimpleLinear/$i/Bin.java`	
#
#`sed -i "10i package mutants.simpleLinear.simpleLinear$i;" ./SimpleLinear/$i/PQueue.java`	
#
#`sed -i "10i package mutants.simpleLinear.simpleLinear$i;" ./SimpleLinear/$i/SimpleLinear.java`	
#done
#
#for ((i=1;i<=$numSimpleTree;i++))
#do
#
#`sed -i "10i package mutants.simpleTree.simpleTree$i;" ./SimpleTree/$i/SimpleTree.java`	
#
#`sed -i "10i package mutants.simpleTree.simpleTree$i;" ./SimpleTree/$i/PQueue.java`		
#done
#
#for ((i=1;i<=$numFineGrainedHeap;i++))
#do
#
#`sed -i "10i package mutants.fineGrainedHeap.fineGrainedHeap$i;" ./fineGrainedHeap/$i/ThreadID.java`	
#
#`sed -i "10i package mutants.fineGrainedHeap.fineGrainedHeap$i;" ./fineGrainedHeap/$i/PQueue.java`	
#
#`sed -i "10i package mutants.fineGrainedHeap.fineGrainedHeap$i;" ./fineGrainedHeap/$i/FineGrainedHeap.java`	
#done
#
#for ((i=1;i<=$numSequentialHeap;i++))
#do
#
#`sed -i "10i package mutants.sequentialHeap.sequentialHeap$i;" ./sequentialHeap/$i/SequentialHeap.java`	
#
#`sed -i "10i package mutants.sequentialHeap.sequentialHeap$i;" ./sequentialHeap/$i/PQueue.java`		
#done

for ((i=1;i<=$numSkipQueue;i++))
do

#`sed -i "12i package mutants.skipQueue.skipQueue$i;" ./skipQueue/$i/SkipQueue.java`	

`sed -i "12i package mutants.skipQueue.skipQueue$i;" ./skipQueue/$i/PrioritySkipList.java`		
done
