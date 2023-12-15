#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# START
# =============================================================================
import pandas as pd
import os
import sys
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

path_input="/home/dnanexus/filtered_vcfs/"
path_output="/home/dnanexus/"

df_vcf_merge=pd.DataFrame()

for filename in os.listdir(path_input):
    if filename.endswith(".g.vcf.filtered.csv"):
        plik = pd.read_csv(path_input+filename, delimiter="	", header=None)
        plik.columns=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'END', 'INFO', filename.split('.')[0]]
        plik=plik.drop(['ID', 'QUAL', 'FILTER', 'END', 'INFO'],axis=1)
        plik.index = plik[['CHROM', 'POS', 'REF', 'ALT']].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
        plik=plik.drop(['CHROM', 'POS', 'REF', 'ALT'],axis=1)
        plik = plik[plik[filename.split('.')[0]].str.split(':', 1, expand=True)[0] != '0/0']
        df_vcf_merge = df_vcf_merge.merge(plik, how='outer', left_index=True, right_index=True)

df_vcf_merge_filtered=df_vcf_merge.copy()
for col in df_vcf_merge_filtered.columns:
    df_vcf_merge_filtered[col] = df_vcf_merge_filtered[col].str.split(':').str[0]

#split index again in multiple column df1
df_vcf_merge=df_vcf_merge.reset_index()
df_vcf_merge[['CHROM', 'POS', 'REF', 'ALT']] = df_vcf_merge["index"].str.split(pat="_", expand=True)
df_vcf_merge['INFO']= 'GT:GQ:DP:AD:VAF:PL'
cols = list(df_vcf_merge.columns)
cols = cols[-5:] + cols[:-5]
df_vcf_merge = df_vcf_merge[cols]
df_vcf_merge=df_vcf_merge.drop(['index'],axis=1)

#split index again in multiple column df2
df_vcf_merge_filtered=df_vcf_merge_filtered.reset_index()
df_vcf_merge_filtered[['CHROM', 'POS', 'REF', 'ALT']] = df_vcf_merge_filtered["index"].str.split(pat="_", expand=True)
cols = list(df_vcf_merge_filtered.columns)
cols = cols[-4:] + cols[:-4]
df_vcf_merge_filtered = df_vcf_merge_filtered[cols]
df_vcf_merge_filtered=df_vcf_merge_filtered.drop(['index'],axis=1)

#export to CSV
df_vcf_merge.to_csv(path_output+"UKB_VCFmerge_info."+str(sys.argv[1])+".csv", index=False)
df_vcf_merge_filtered.to_csv(path_output+"UKB_VCFmerge."+str(sys.argv[1])+".csv", index=False)

