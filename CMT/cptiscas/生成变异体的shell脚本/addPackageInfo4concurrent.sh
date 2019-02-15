#!/bin/bash

function addpackageinfo(){

	for file in `ls $1`
	do
		`sed -i "12i package mutants.fineGrainedHeap.$file;" ./concurrentmutants/$file/PQueue.java`

		`sed -i "12i package mutants.fineGrainedHeap.$file;" ./concurrentmutants/$file/FineGrainedHeap.java`
	done



}


path="/home/phantom/cptMutants/mutants/concurrentmutants/"

addpackageinfo $path



#for ((i=1;i<=$numFineGrainedHeap;i++))
#do
#
##`sed -i "12i package mutants.skipQueue.skipQueue$i;" ./skipQueue/$i/SkipQueue.java`	
#
#`sed -i "12i package mutants.skipQueue.skipQueue$i;" ./skipQueue/$i/PrioritySkipList.java`		
#done
