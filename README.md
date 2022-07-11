Introduction to the assembly repository

This repository contains the files necessary to assembly the chloroplast and mitochondrial genomes that were included in the project. The scripts “Mitochondria_assembly.py” and “Chloroplast_assembly.py” are written in python with Unix wrapped commands to create batch scripts. Running these scripts on the project directory structure creates a batch script for each individual sample. From here the scripts were ran in parallel to run multiple assemblies. The repository also includes two GetOrganelle assembly logs to demonstrate evidence that the scripts ran successfully in line with the objectives set out in the project. Furthermore in practicing reproducibility with coding this GitHub also includes an example batch file “output_batch_file”, the conda environment used for assembly “getorganelle.yml” and the seed used for mitochondrial assembly with GetOrganelle “A_thaliana_mitochondria.fasta”. 

Running the assemblies

Starting the script running -

first install GetOrganelle conda install -c bioconda getorganelle

second add the data bases get_organelle_config.py --add embplant_pt, embplant_mt

Running the scripts the two command lines for mito and chlor assembly 

python3 /Users/lewiswood/Desktop/project_2/CHLOROPLAST_assembly.py -i /Users/lewiswood/Desktop/test_python/02.trimmed -o /Users/lewiswood/Desktop/test_python/output

python3 /Users/lewiswood/Desktop/project_2/Mitchondria_assembly.py -i /Users/lewiswood/Desktop/test_python/02.trimmed -o /Users/lewiswood/Desktop/test_python/output

Extra input that the script requests

The chloroplast and mitochondria script will both ask you to input settings for the job you want to run as well as this both will ask you for a three-capital letter population code i.e. BEA, ALO, BRI. The mitochondria assembly script requires an additional seed file. The file can be found under the name “A_thaliana_mitochondria.fasta”. 

Results 

Due to the size of the end assembly file containing results for approximately 150 individuals it is not appropriate or possible to present all of the assemblies by write up or GitHub repository. Therefore, the end assemblies for the ahh population have been used to demonstrate the final product of running assembly scripts through GetOrganelle and the research cluster at The University of Nottingham. 
