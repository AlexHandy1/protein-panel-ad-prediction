### Overview of data processing steps

- Scripts transform de-identified protein PRS data held on King's College London's high performance computing cluster [Rosalind](https://rosalind.kcl.ac.uk) to further anonymised datasets for local analysis.  

- Run [``` python prep_all_proteins_prs_hpc.py ```](hhttps://github.com/AlexHandy1/protein-panel-ad-prediction/blob/master/data_processing/prep_all_protein_prs_hpc.py) on Rosalind. Wrapper for [```protein_prs_prep_hpc.py```](https://github.com/AlexHandy1/protein-panel-ad-prediction/blob/master/data_processing/protein_prs_prep_hpc.py) which prepares each individual protein and converts into a csv file.  

- Run [``` python merge_prs_files_hpc.py ```](https://github.com/AlexHandy1/protein-panel-ad-prediction/blob/master/data_processing/merge_prs_files_hpc.py) on Rosalind to combine individual csvs into one csv file for analysis. 
