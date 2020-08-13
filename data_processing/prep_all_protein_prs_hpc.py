import os
import protein_prs_prep_hpc as pp 

os.chdir("/users/k1894983/protein-panel-ad-prediction/data")

with open("protein_shortlist.txt") as f:
	proteins = f.readlines()
	
	for protein in proteins:
		pp.protein_prs_to_csv(protein.rstrip())