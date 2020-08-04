import pandas as pd
import numpy as np
import os
import glob

#set up path to csv file
path = "/users/k1894983/protein-panel-ad-prediction/data"
csv_file_path = os.path.join(path, "*.csv")

#load all .csv files
csv_files = glob.glob(path + "/*.csv")

#setup the first file as output table e.g. output = files[0]
output = pd.read_csv(csv_files[0], sep="\t", index_col=0)

#make sure iterable object
csv_files = iter(csv_files)

#skip first entry used as ref table
next(csv_files)

for file in csv_files:
	entry = pd.read_csv(file, sep="\t", index_col=0)
	output = pd.merge(output, entry, on=["FID", "IID", "Case", "Sex", "Group"])

#select analysis columns
group = output["Group"]
output.drop(labels = ["FID", "IID", "Group"], axis=1, inplace=True)
output.insert(0, "Group", group)

print(output)

#create csv for output table 
os.chdir("/users/k1894983/protein-panel-ad-prediction/data")
output.to_csv("protein_prs_cases.csv", sep='\t')