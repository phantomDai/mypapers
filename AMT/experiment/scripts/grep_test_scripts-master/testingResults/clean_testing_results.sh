#!/bin/bash

for((i=23;i<=30;i++));
do
    for((j=1;j<=10000;j++));
    do
        rm -rf ./repetitive1/"${j}"*
        rm -rf ./repetitive1/"${j}"*
    done
    for((j=10001;j<=30000;j++));
    do
        rm -rf ./repetitive1/"${j}"*
        rm -rf ./repetitive1/"${j}"*
    done
    for((j=30001;j<=60000;j++));
    do
        rm -rf ./repetitive1/"${j}"*
        rm -rf ./repetitive1/"${j}"*
    done
    for((j=60001;j<=90000;j++));
    do
        rm -rf ./repetitive1/"${j}"*
        rm -rf ./repetitive1/"${j}"*
    done
    for((j=90001;j<=101193;j++));
    do
        rm -rf ./repetitive1/"${j}"*
        rm -rf ./repetitive1/"${j}"*
    done
done

