

for((i=1;i<158;i++))
do
`cp ../sourceCode/PQueue.java ./submutants/sequentialHeap/$i/`
done


for((j=1;j<=230;j++))
do

`cp ../sourceCode/PQueue.java ./submutants/fineGrainedHeap/$j/`
`cp ../sourceCode/ThreadID.java ./submutants/fineGrainedHeap/$j/`

done


for((k=1;k<=253;k++))

do

`cp ../sourceCode/SkipQueue.java ./submutants/skipQueue/$k/`

done

