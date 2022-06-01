the chloroplast assembly script takes files for one individual form (aah_1 ,bre_1 ,cha_1 ,cht_1
cum_1 ,dar1 ,ers_1 ,for_1 ,Ftw_1) populations and writes a bash script file for getorganelle chloroplast assemblies. this should the be able to subitted to a cluster by slurm. 

files required to be read from the same directory as the script is ran as the script currently doesnt browse for file paths. 

only allows 10 assemblies at a time 

the script takes a dictionary and reads the files into command lines. 
