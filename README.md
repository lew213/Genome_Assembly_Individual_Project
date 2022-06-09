In this repository I have included two scripts that will write batch files for a get organelle mitochondria and chloroplast assembly 
the script output is based on the successful assembly commands. to find these raw commands open up the chlor and mito log files in this repo 
in addition to this I have included an example bash script out put to check if the structure is suitable for the research cluster. 

starting the script running 
first install get organelle conda install -c bioconda getorganelle
second add the data bases get_organelle_config.py --add embplant_pt,embplant_mt
this is how I installed the assembler but for reproducability ill also include a yml file of the used enviroment 

running the scripts 
the two command lines for mito and chlor assembly scripts called on the given example directory structure 

python3 /Users/lewiswood/Desktop/project_2/CHLOROPLAST_assembly.py -i /Users/lewiswood/Desktop/test_python/02.trimmed -o /Users/lewiswood/Desktop/test_python/output

python3 /Users/lewiswood/Desktop/project_2/Mitchondria_assembly.py -i /Users/lewiswood/Desktop/test_python/02.trimmed -o /Users/lewiswood/Desktop/test_python/output

extra input that the script asks from you 

the chloro and mito script will both ask you to input settings for the job you want to run 
aswell as this both will ask you for a three capital letter population code ie BEA,ALO,BRI

with the mitochondria assembly script, itll ask for a seed file input. this is the A_thaliana.fasta file in this repro. 
give the input the absoulte path so that it can write out the batch file correctly. 
