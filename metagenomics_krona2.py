#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:47:00 2019

@author: ahmed
"""


import os 
import time

start_t=time.time()
def kraken_krona(directory):
    os.system('cat report1.txt | cut -f 2,3 > summary.kraken.krona')
    os.system('ktImportTaxonomy -tax /home/ahmed/krona/taxonomy_RDP summary.kraken.krona')


main_folder=('/home/ahmed/Lab_HD/16s_Metagenomics-139760630/FASTQ'
         '_Generation_2019-08-09_23_32_57Z-191348157/1')
os.chdir(main_folder)

# loop over all folder
for foldr in os.listdir():
    os.chdir(foldr)
    kraken_krona(os.path.join(main_folder,foldr))
    os.chdir('..')
    
print(time.time()-start_t)
