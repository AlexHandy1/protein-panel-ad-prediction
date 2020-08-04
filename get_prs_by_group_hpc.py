import pandas as pd
import numpy as np
import os
import sys

PROTEIN = sys.argv[1]
#GROUPS HASHED OUT FOR EXTRA ANONYMITY - WORKING GROUPING ON HPC
GROUPS = {"###":"A", "###":"B", "###":"C"}
output = pd.DataFrame()

for group in GROUPS.keys():
        #load .fam cases file
        os.chdir("/mnt/lustre/groups/proitsi/Alex/Protein_PRS_to_AD/Target_Data")
        cases_file = group + "_ForPRS.WITHAPOE.Original.Overlapping.fam"
        cases = pd.read_csv(cases_file, sep=" ", names=["FID", "IID", "FaID", "MoID", "Sex", "Case"])
      
        #load .best prs file
        os.chdir("/mnt/lustre/groups/proitsi/Alex/Protein_PRS_to_AD/Results/prs/protein_prs_all_with_apoe")
        prs_file = PROTEIN + "_" + group + ".best"
        prs = pd.read_csv(prs_file, sep=" ")

        #merge protein prs and cases on IDs
        prs_cases = pd.merge(prs, cases, on=["FID", "IID"])

        #select columns for analysis
        select_cols = prs_cases[["FID", "IID", "Case", "Sex", "PRS"]]

        #add group reference (throws SettingwithCopyWarning as false positive - https://www.dataquest.io/blog/settingwithcopywarning/)
        rows = select_cols.count()[0]
        select_cols["Group"] = np.array(list(GROUPS[group]*rows))

        #rename protein column
        select_cols.rename(columns={"PRS":PROTEIN}, inplace=True)

        print(select_cols.head())

        #add group data for protein
        output = output.append(select_cols)

#reset index and remove legacy index
output = output.reset_index()
del output["index"]

#create csv for output table 
os.chdir("/users/k1894983/protein-panel-ad-prediction/data")
output_filename = PROTEIN + ".csv"
output.to_csv(output_filename, sep='\t')