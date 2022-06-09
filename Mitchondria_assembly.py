# Pseudo code 7th June 2022
#  Make batch files for the cluster
# command line will look like this:
# python3 script_name.py -i input_dir -o output_dir

#import modules and assign command line arguments
import argparse, os, glob, fnmatch, sys
parser = argparse.ArgumentParser(
    description='this script runs through the given directory and writes bash scripts for getorganelle chloroplast and mitochondria assemblies ')

parser.add_argument('-i', type=str, metavar='input_file', required=True, help='Path to the input .pdb file')
parser.add_argument('-o', type=str, metavar='output_file', required=True, help='Name for the output .pdb file. The output file will be created in your current directory.')
args = parser.parse_args()

# assigning variables
input_directory = args.i
output_directory = args.o
path = args.i
file_list =[]
dir_name = args.i

# Get list of all files in a given directory & sub-directories
list_of_files = sorted( filter( os.path.isfile,
                        glob.glob(dir_name + '/**/*', recursive=True) ) )
for file_path in list_of_files:
    print(file_path)
print('all files found')

#filters out the unpaired data
print("searching for paired reads only")
for path, folders, files in os.walk(path):
    for file in files:
        if fnmatch.fnmatch( '*P*', file):
            file_list.append(os.path.join(path, file))

#prints the paired file paths to the terminal window and a text file
for file_path in file_list:
    print(file_path)

    original_stdout = sys.stdout # Save a reference to the original standard output

    with open(args.o + '_' + 'filename.txt', 'w') as f:
        sys.stdout = f # Change the standard output to the file we created.
        for file_path in file_list:
            print(file_path)
        sys.stdout = original_stdout

#read the file paths out of the text file
print("**************")
list_of_lists = []
with open('/Users/lewiswood/Desktop/test_python/output_filename.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        # in alternative, if you need to use the file content as numbers
        # inner_list = [int(elt.strip()) for elt in line.split(',')]
        list_of_lists.append(inner_list)

print('unsorted list')
list_of_lists.sort()
#coverts list of list into normal list
new_list=[]
for item in list_of_lists:
	item = item[0]
	new_list.append(item)
new_list.sort()
print(new_list)
#sort list alpha
pop_code = input('input population code i.e ALO, BRI, ELI:')
for item in new_list:
    alpha = list(filter(lambda k: pop_code in k, new_list))
print(alpha)
print('cccccc')

#next part
l = (alpha)
for i in range(0, len(l), 2):
    print(str(l[i]), '+', str(l[i + 1]))

print('sorted lists of files in correct output')


#creating the batch file
seed = input('give absolute path to A_thaliana_mitochondria seed file for mitochondria assembly:')
mem = input('How much memory would you like to use? (e.g. 16):')
time = input('How long would you like the job to run for? (e.g. 05:00:00):')
partition = 'hpc'
name = input('Create a job name:')
o = input('Choose output location with for cluster job:')


# Create batch files for
out_file = open(args.o + '_' + 'batch_file', 'w')
out_file.write(f"#!/bin/bash\n" +
               f"#SBATCH --job-name{name}\n" +
               f"#SBATCH --partition={partition}\n" +
               f"#SBATCH --mem={mem}g\n" +
               f"#SBATCH --time={time}\n" +
               f"#SBATCH --output=%.out\n" +
               f"#SBATCH --error=%x.err\n" +
               f"source $HOME/.bash_profile\n" +
               f"\n")

for i in range(0, len(l), 2):
    out_file.write(f"get_organelle_from_reads.py -1 {(l[i])} -2 {(l[i + 1])} -s {seed} -t 32 -o {o} -R 2 -F embplant_mt \n")
    out_file.write(f"\n")
print('batch file written for get organelle mitochondria assembly')
print('thank you')




