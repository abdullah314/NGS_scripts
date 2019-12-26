#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 16:53:53 2019

@author: ahmed
"""

import os
import re
source='/media/ahmed/Seagate Backup Plus Drive/Klebsiella_WGS-144254113/edited/E_coli_new'
destination='/home/ahmed/E_coli_assembly2'
def assembly_script(source, destination):
    os.chdir(source)
    
    A=os.listdir()
    A=[str(i) for i in A]
    
    for folder in A:
        os.chdir(folder)
        files=os.listdir()
        if files:
            os.system('spades.py --threads 4 --memory 24 -1 %s_R1.fq.gz -2 %s_R2.fq.gz -o %s'  %(folder,folder,os.path.join(destination,folder)))
                      
        os.chdir('..')

assembly_script(source, destination)
#%%
import shutil    
    
os.chdir('/home/ahmed/E_coli_assembly')
A=os.listdir()
for folder in A:
    os.chdir(folder)
    shutil.copy('contigs.fasta','/media/ahmed/Seagate Backup Plus Drive/E. coli data/UPEC-143295152/assembly/%s' %(folder))
    os.chdir('..')
    
    

