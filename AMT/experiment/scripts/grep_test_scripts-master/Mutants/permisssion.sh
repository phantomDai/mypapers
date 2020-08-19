#!/bin/bash


for((i=1;i<=20;i++));
do
  chmod  777 /home/phantom/dmt-paper/grep/Mutants/grep_v"${i}"/bin/*
done