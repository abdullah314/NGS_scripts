#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:48:17 2019

@author: ahmed
"""
import os 
import time

from taxadb.names import SciName
start_t=time.time()

def kraken_krona(directory):
    os.chdir(directory)
    import pandas as pd
    file_myreport='my_report'
    file_report1='report1.txt'
    
    df_myreport=pd.read_csv(file_myreport,sep='\t',header=None)
    Tmp1=list(df_myreport[5].copy())
    Tmp2=[i.strip() for i in Tmp1]
    df_myreport[5]=Tmp2
    
    df_report1=pd.read_csv(file_report1,sep='\t',header=None)
    
    
    
    taxn_lst=[]
    for tid in df_report1[2]:
        t_index=df_myreport[df_myreport[4]==tid].index
        tax_n=df_myreport.loc[t_index[0],5]
        taxn_lst.append(tax_n)
    
    
    names = SciName(dbtype='sqlite', dbname='taxadb3.sqlite')
    
    
    a=type(None)
    finalTaxIds=[]
    for i in taxn_lst:
        taxid= names.taxid(i)
        if type(taxid) == a:
            finalTaxIds.append(32644)
        else:
            finalTaxIds.append(taxid)
            
    
       
    summary_kraken=pd.DataFrame()
    summary_kraken['reads']=df_report1[1].copy()
    summary_kraken['ncbi_ids']=finalTaxIds
    summary_kraken.to_csv('summary.kraken.krona',sep='\t',index=False,header=False)
    
    
    end_t=time.time()
    print('Total time : %s'%(end_t-start_t))


main_folder=('/home/ahmed/Lab_HD/16s_Metagenomics-139760630/FASTQ'
         '_Generation_2019-08-09_23_32_57Z-191348157/1')
os.chdir(main_folder)

# loop over all folder
for foldr in os.listdir():
    os.chdir(foldr)
    kraken_krona(os.path.join(main_folder,foldr))
    os.chdir('..')