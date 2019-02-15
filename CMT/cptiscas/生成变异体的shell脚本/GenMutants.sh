# 生成Bin类的变异体
javac -J-Dmajor.export.mutants=true -J-Dmajor.export.directory=./mutants/Bin -XMutator:ALL Bin.java
# 生成SimpleLinear类的变异体
javac -cp . -J-Dmajor.export.mutants=true -J-Dmajor.export.directory=./mutants/SimpleLinear -XMutator:ALL SimpleLinear.java
# 生成SimpleTree类的变异体
javac -cp . -J-Dmajor.export.mutants=true -J-Dmajor.export.directory=./mutants/SimpleTree -XMutator:ALL SimpleTree.java
# 生成SequentialHeap类的变异体
javac -cp . -J-Dmajor.export.mutants=true -J-Dmajor.export.directory=./mutants/sequentialHeap -XMutator:ALL SequentialHeap.java
# 生成FineGrainedHeap类的变异体
javac -cp . -J-Dmajor.export.mutants=true -J-Dmajor.export.directory=./mutants/fineGrainedHeap -XMutator:ALL FineGrainedHeap.java
# 生成skipQueue类的变异体
javac -cp . -J-Dmajor.export.mutants=true -J-Dmajor.export.directory=./mutants/skipQueue -XMutator:ALL PrioritySkipList.java
