#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:13:43 2019
remove the repetitive test frames and corresponding test cases

@author: phantom
"""

test_frames = []

repetitive_test_frame_line = []

line_counter = 0

#read testframe
with open ('TestFrames_grep', 'r') as file:
    
    for line in file:
        
        line_counter += 1
        
        temp_line = line.strip()
        
        if temp_line not in test_frames:
            
            test_frames.append(temp_line)
            
        else:
            
            repetitive_test_frame_line.append(line_counter)
            
file.close()

# write non-repeatitive test frame
f = open('TestFrames_grep_no_repeat', 'w')
for line in test_frames:
    f.write(line + '\n')
f.close()

nonrepeatitive_test_cases = []
# read test cases

with open('TestPool_grep', 'r') as test_case_file:
    
    temp_line_counter = 0
    
    for line in test_case_file:
        
        temp_line_counter += 1
        
        if temp_line_counter not in repetitive_test_frame_line:
            
            nonrepeatitive_test_cases.append(line)
            
test_case_file.close()

suite_file = open('TestPool_grep_no_repeat', 'w')
for line in nonrepeatitive_test_cases:
    suite_file.write(line)
suite_file.close()


#print(len(repetitive_test_frame_line))
#print(len(test_frames))
#print(len(repetitive_test_frame_line) + len(test_frames))
#print(line_counter)




