#!/bin/bash
parentDir=`pwd`
cd $parentDir
fileNames=`ls`
for fileName in $fileNames
do
		cd $parentDir/$fileName
	    nohup java -jar cptiscasv2-1.0-SNAPSHOT.jar&
		cd $parentDir
done
