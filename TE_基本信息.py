#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import re
import os
import pandas as pd


#  Length 统计

# In[2]:


path ="D:/working/2019-2020学年/毕设/Data/TE.gtf"
files=os.listdir(path)
for file in files:
    #print(file)
    f=pd.read_csv(open(r'D:/working/2019-2020学年/毕设/Data/TE.gtf/{}'.format(file),'r',encoding='utf-8'),sep='\t',header=None);
    gcut=pd.cut((f[4]-f[3]),10,right=False)
    result=gcut.value_counts()
    result=str(result)
    #print(result)
    filename = r'D:/working/2019-2020学年/毕设/Data/TE_length_10/{}_length.txt'.format(file[:-4])
    with open(filename, 'w') as g:
        for each in result.split('\n')[:-1]:
            g.write (each +"\n") 


# Length 统计bins100 全部

# In[109]:


path ="D:/working/2019-2020学年/毕设/Data/TE.gtf"
files=os.listdir(path)
df=pd.DataFrame([{'bins': 'bins','counts': 'counts','genename':'genename' }])
for file in files:
    #print(file)
    f=pd.read_csv(open(r'D:/working/2019-2020学年/毕设/Data/TE.gtf/{}'.format(file),'r',encoding='utf-8'),sep='\t',header=None);
    length=pd.Series(f[4]-f[3])
    bins=list(range(0,length.max(),100))
    length_cut=pd.cut(length,bins)
    length_bins=pd.value_counts(length_cut).sort_index()
    df_part=pd.DataFrame()
    df_part['bins']=list(length_bins.index)
    df_part['counts']=list(length_bins.values)
    df_part['genename']=list([file[:-4]]*(len(bins)-1))
    df=pd.concat([df,df_part])


# Length 统计bins10 

# In[112]:


path ="D:/working/2019-2020学年/毕设/Data/TE.gtf"
files=os.listdir(path)
df=pd.DataFrame([{'bins': 'bins','counts': 'counts','genename':'genename' }])
for file in files:
    #print(file)
    f=pd.read_csv(open(r'D:/working/2019-2020学年/毕设/Data/TE.gtf/{}'.format(file),'r',encoding='utf-8'),sep='\t',header=None);
    length=pd.Series(f[4]-f[3])
    bins=list(range(0,length.max(),10))
    length_cut=pd.cut(length,bins)
    length_bins=pd.value_counts(length_cut).sort_index()
    df_part=pd.DataFrame()
    df_part['bins']=list(length_bins.index)
    df_part['counts']=list(length_bins.values)
    df_part['genename']=list([file[:-4]]*(len(bins)-1))
    df=pd.concat([df,df_part])


# In[114]:


df.to_csv('D:/working/2019-2020学年/毕设/Data/TE_length_bins10.csv',index=False,header=False)


# GC含量统计

# In[4]:


import csv


# In[26]:


path="D:/working/2019-2020学年/毕设/Data/TE_fasta"
files=os.listdir(path)
with open(r'D:/working/2019-2020学年/毕设/Data/TE_AGCT/TE_AGCT_v1.csv','a',newline='') as csv_file:
    csv_file=csv.writer(csv_file)
    for file in files:
        f=open(r'D:/working/2019-2020学年/毕设/Data/TE_fasta/{}'.format(file),'r')
        f=f.read()
        f=str(f)
        f=re.sub('>.*\n|\n', '', f)
        nA=f.count('A')
        nG=f.count('G')
        nC=f.count('C')
        nT=f.count('T')
        size=nA+nG+nC+nT
        A_percent=nA/size
        G_percent=nG/size
        C_percent=nC/size
        T_percent=nT/size
        CG_percent=(nG+nC)/size
        data=[file[:-3],A_percent,G_percent,C_percent,T_percent,CG_percent]
        csv_file.writerow(data)


# In[148]:


def read_fasta(f):
    fasta = {}
    for line in f:
        line = line.strip()
        if line[0] == '>':
            header = line[1:]
            result=re.findall(".*\"(.*)\".*",header)
            name=result[0]
        else:
            sequence = line
            fasta[name] = fasta.get(name, '') + sequence
    return fasta


# In[151]:


def get_atgc(seqdict):
    namels=list(seqdict.keys())
    seqls=list(seqdict.values())
    A_percent=[]
    G_percent=[]
    C_percent=[]
    T_percent=[]
    for i in list(range(0,len(seqls))):
        A_percent.append(seqls[i].count('A')/len(seqls[i]))
        G_percent.append(seqls[i].count('G')/len(seqls[i]))
        C_percent.append(seqls[i].count('C')/len(seqls[i]))
        T_percent.append(seqls[i].count('T')/len(seqls[i]))
    df_part=pd.DataFrame()
    df_part['genename']=list([file[:-4]]*(len(seqls)))
    df_part['transcriptid']=namels
    df_part['A_percent']=A_percent
    df_part['G_percent']=G_percent
    df_part['C_percent']=C_percent
    df_part['T_percent']=T_percent
    return df_part


# In[153]:


path="D:/working/2019-2020学年/毕设/Data/TE_fasta"
files=os.listdir(path)
df=pd.DataFrame([{'genename': 'genename','transcriptid': 'transcriptid','A_percent':'A_percent','G_percent':'G_percent','T_percent':'T_percent','C_percent':'C_percent' }])
for file in files:
    f=open(r'D:/working/2019-2020学年/毕设/Data/TE_fasta/{}'.format(file),'r')
    fasta = {}
    for line in f:
        line = line.strip()
        if line[0] == '>':
            header = line[1:]
            result=re.findall(".*\"(.*)\".*",header)
            name=result[0]
        else:
            sequence = line
            fasta[name] = fasta.get(name, '') + sequence
    seqdict=fasta
    namels=list(seqdict.keys())
    seqls=list(seqdict.values())
    A_percent=[]
    G_percent=[]
    C_percent=[]
    T_percent=[]
    for i in list(range(0,len(seqls))):
        A_percent.append(seqls[i].count('A')/len(seqls[i]))
        G_percent.append(seqls[i].count('G')/len(seqls[i]))
        C_percent.append(seqls[i].count('C')/len(seqls[i]))
        T_percent.append(seqls[i].count('T')/len(seqls[i]))
    df_part=pd.DataFrame()
    df_part['genename']=list([file[:-3]]*(len(seqls)))
    df_part['transcriptid']=namels
    df_part['A_percent']=A_percent
    df_part['G_percent']=G_percent
    df_part['C_percent']=C_percent
    df_part['T_percent']=T_percent
    df=pd.concat([df,df_part])


# In[ ]:


path="D:/working/2019-2020学年/毕设/Data/TE_fasta_test"
files=os.listdir(path)
df=pd.DataFrame([{'genename': 'genename','transcriptid': 'transcriptid','A_percent':'A_percent','G_percent':'G_percent','T_percent':'T_percent','C_percent':'C_percent' }])
for file in files:
    f=open(r'D:/working/2019-2020学年/毕设/Data/TE_fasta/{}'.format(file),'r')
    fasta = {}
    for line in f:
        line = line.strip()
        if line[0] == '>':
            header = line[1:]
            result=re.findall(".*\"(.*)\".*",header)
            name=result[0]
        else:
            sequence = line
            fasta[name] = fasta.get(name, '') + sequence
    seqdict=fasta
    namels=list(seqdict.keys())
    seqls=list(seqdict.values())
    A_percent=[]
    G_percent=[]
    C_percent=[]
    T_percent=[]
    for i in list(range(0,len(seqls))):
        A_percent.append(seqls[i].count('A')/len(seqls[i]))
        G_percent.append(seqls[i].count('G')/len(seqls[i]))
        C_percent.append(seqls[i].count('C')/len(seqls[i]))
        T_percent.append(seqls[i].count('T')/len(seqls[i]))
    df_part=pd.DataFrame()
    df_part['genename']=list([file[:-3]]*(len(seqls)))
    df_part['transcriptid']=namels
    df_part['A_percent']=A_percent
    df_part['G_percent']=G_percent
    df_part['C_percent']=C_percent
    df_part['T_percent']=T_percent
    df=pd.concat([df,df_part])


# In[ ]:


df.to_csv('D:/working/2019-2020学年/毕设/Data/TE_full_copynumber_test.csv',index=False,header=False)


# In[154]:


df.to_csv('D:/working/2019-2020学年/毕设/Data/TE_full_copynumber.csv',index=False,header=False)


# In[149]:


seqdict=read_fasta(f)
namels=list(seqdict.keys())
seqls=list(seqdict.values())
A_percent=[]
G_percent=[]
C_percent=[]
T_percent=[]
for i in list(range(0,len(seqls))):
    A_percent.append(seqls[i].count('A')/len(seqls[i]))
    G_percent.append(seqls[i].count('G')/len(seqls[i]))
    C_percent.append(seqls[i].count('C')/len(seqls[i]))
    T_percent.append(seqls[i].count('T')/len(seqls[i]))
df_part=pd.DataFrame()
df_part['genename']=list(['MLT2A1']*(len(seqls)))
df_part['transcriptid']=namels
df_part['A_percent']=A_percent
df_part['G_percent']=G_percent
df_part['C_percent']=C_percent
df_part['T_percent']=T_percent


# In[ ]:




