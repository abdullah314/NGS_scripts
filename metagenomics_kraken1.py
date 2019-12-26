#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 12:31:22 2019

@author: ahmed
"""

import os
os.chdir('/home/ahmed/Lab_HD/16s_Metagenomics-139760630/FASTQ'
         '_Generation_2019-08-09_23_32_57Z-191348157/1')

# loop over all folder
for foldr in os.listdir():
    os.chdir(foldr)
    A=os.listdir()
    for f in A:
        if 'forward_paired' in f:
            forward=f
        elif 'reverse_paired' in f:
            reverse=f
    os.system('kraken2 --db  ~/My_16S  --report my_report '
              '--paired %s %s > report1.txt' %(forward,reverse))
    os.chdir('..')
