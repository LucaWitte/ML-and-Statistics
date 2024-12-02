# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 17:37:21 2022

@author: Luca Witte
"""
import os
import sys
import argparse
import pandas as pd
import numpy as np


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Compute nbayes for tumor-data."
    )
    parser.add_argument(
        "--traindir",
        required=True,
        help="Path to input directory containing data set for training (tumor_info.txt)"
    )
    parser.add_argument(
        "--outdir",
        required=True,
        help="Path to output directory in which output_summary_class_2.txt and output_summary_class_4.txt are written"
    )

    args = parser.parse_args()

    out_dir = args.outdir

    file_name_train = "{}/tumor_info.txt".format(args.traindir)
    
    input_train_2 = pd.read_table(file_name_train)
    input_train_2.columns = ["clump", "uniformity", "marginal", "mitoses", "class"]
 
    # 2 classes 
    
    input_train_2_benign = input_train_2.loc[input_train_2["class"] == 2].drop(columns = "class")
    input_train_2_malignant = input_train_2.loc[input_train_2["class"] == 4].drop(columns = "class")
 
    os.makedirs(args.outdir, exist_ok=True)  
       
    out_benign = pd.DataFrame(np.zeros([10,5]))
    out_benign.columns = ["value", "clump", "uniformity", "marginal", "mitoses"]
    out_benign["value"] = np.array(range(1, 11))
    
    out_malignant = pd.DataFrame(np.zeros([10,5]))
    out_malignant.columns = ["value", "clump", "uniformity", "marginal", "mitoses"]
    out_malignant["value"] = np.array(range(1, 11))
    
    for i in range(np.shape(input_train_2_benign)[1]): 
      for j in out_benign["value"]:
        try:
            freq_benign = input_train_2_benign.iloc[:,i].value_counts()[j]/len(input_train_2_benign[~np.isnan(input_train_2_benign.iloc[:,i])])
        except KeyError:
            freq_benign = 0
            
        try:
            freq_malignant = input_train_2_malignant.iloc[:,i].value_counts()[j]/len(input_train_2_malignant[~np.isnan(input_train_2_malignant.iloc[:,i])])
        except KeyError:
            freq_malignant = 0
            
        out_benign.iloc[j-1,i+1] = (f'{freq_benign:.3f}')
        out_malignant.iloc[j-1,i+1] = (f'{freq_malignant:.3f}')
        
    try:
        file_name = "{}/output_summary_class_2.txt".format(args.outdir)
        f_out = open(file_name, 'w')
    except IOError:
        print("Output file {} cannot be created".format(file_name))
        sys.exit(1)
        
    f_out.write('{}\t{}\t{}\t{}\t{}\n'.format(
        'Value','clump', 'uniformity', 'marginal', 'mitoses'))
    
    for col_dim in range(np.shape(out_benign)[0]):
            val_1 = out_benign.iloc[col_dim,0]
            val_2 = out_benign.iloc[col_dim,1]
            val_3 = out_benign.iloc[col_dim,2]
            val_4 = out_benign.iloc[col_dim,3]
            val_5 = out_benign.iloc[col_dim,4]

            f_out.write('{}\t{}\t{}\t{}\t{}\n'.format(
                val_1, val_2, val_3, val_4, val_5))
    try:
        file_name = "{}/output_summary_class_4.txt".format(args.outdir)
        f_out = open(file_name, 'w')
    except IOError:
        print("Output file {} cannot be created".format(file_name))
        sys.exit(1)
        
    f_out.write('{}\t{}\t{}\t{}\t{}\n'.format(
        'Value','clump', 'uniformity', 'marginal', 'mitoses'))
    
    for col_dim in range(np.shape(out_malignant)[0]):
            val_1 = out_malignant.iloc[col_dim,0]
            val_2 = out_malignant.iloc[col_dim,1]
            val_3 = out_malignant.iloc[col_dim,2]
            val_4 = out_malignant.iloc[col_dim,3]
            val_5 = out_malignant.iloc[col_dim,4]

            f_out.write('{}\t{}\t{}\t{}\t{}\n'.format(
                val_1, val_2, val_3, val_4, val_5))
    
           
        
        
        
