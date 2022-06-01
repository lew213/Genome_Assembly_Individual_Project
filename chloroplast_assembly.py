
#importing modules
import os, sys, argparse, glob
#dictionary with file names (thinking of having another program that can automate the writing of larger dictionaries
Dict = {1: 's47_EDSW210019158-1a_HNT5FDSX2_L4_1.fq.gz', 2: 's47_EDSW210019158-1a_HNT5FDSX2_L4_2.fq.gz',
        3: 's51_EDSW210019162-1a_HNT5FDSX2_L3_1.fq.gz', 4: 's51_EDSW210019162-1a_HNT5FDSX2_L3_2.fq.gz',
        5: 's46_EDSW210019157-1a_HNT5FDSX2_L4_1.fq.gz', 6: 's46_EDSW210019157-1a_HNT5FDSX2_L4_2.fq.gz',
        7: 's52_EDSW210019163-1a_HNT5FDSX2_L1_1.fq.gz', 8: 's52_EDSW210019163-1a_HNT5FDSX2_L1_2.fq.gz',
        9: 's56_EDSW210019167-1a_HNT5FDSX2_L2_1.fq.gz', 10: 's56_EDSW210019167-1a_HNT5FDSX2_L2_2.fq.gz',
        11: 's57_EDSW210019168-1a_HNT5FDSX2_L2_1.fq.gz', 12: 's57_EDSW210019168-1a_HNT5FDSX2_L2_2.fq.gz',
        13: 's5_EDSW210019116-1a_HMWFMDSX2_L2_1.fq.gz', 14: 's5_EDSW210019116-1a_HMWFMDSX2_L2_2.fq.gz',
        15: 's59_EDSW210019170-1a_HNT5FDSX2_L1_1.fq.gz', 16: 's59_EDSW210019170-1a_HNT5FDSX2_L1_1.fq.gz',
        17: 's29_EDSW210019140-1a_HNT5FDSX2_L1_1.fq.gz', 18: "s29_EDSW210019140-1a_HNT5FDSX2_L1_2.fq.gz",}


#user input for hps cluster 
mem = input('How much memory would you like to use? (e.g. 16):')
time = input('How long would you like the job to run for? (e.g. 05:00:00):')
partition = 'hpc'
name = input('Create a job name:')
o = input('Choose output location with full path:')


# Create batch files 
out_file = open('index_file.sh', 'w')
out_file.write(f"#!/bin/bash\n" +
               f"#SBATCH --job-name{name}\n" +
               f"#SBATCH --partition={partition}\n" +
               f"#SBATCH --mem={mem}g\n" +
               f"#SBATCH --time={time}\n" +
               f"#SBATCH --output=%.out\n" +
               f"#SBATCH --error=%x.err\n" +
               f"source $HOME/.bash_profile\n")


count = 0
while (count < 10):
    count = count + 1
    out_file.write( f"get_organelle_from_reads.py -1 {(Dict.get(1))} -2 {(Dict.get(2))} -t 1 -o {o} -F embplant_pt -R 10\n")
    if (count < 2):
        out_file.write(
            f"get_organelle_from_reads.py -1 {(Dict.get(3))} -2 {(Dict.get(4))} -t 1 -o {o} -F embplant_pt -R 10\n")
        if (count < 3):
            out_file.write(
                f"get_organelle_from_reads.py -1 {(Dict.get(5))} -2 {(Dict.get(6))} -t 1 -o {o} -F embplant_pt -R 10\n")
            if (count < 4):
                out_file.write(
                    f"get_organelle_from_reads.py -1 {(Dict.get(7))} -2 {(Dict.get(8))} -t 1 -o {o} -F embplant_pt -R 10\n")
                if (count < 5):
                    out_file.write(
                        f"get_organelle_from_reads.py -1 {(Dict.get(9))} -2 {(Dict.get(10))} -t 1 -o {o} -F embplant_pt -R 10\n")
                    if (count < 6):
                        out_file.write(
                            f"get_organelle_from_reads.py -1 {(Dict.get(11))} -2 {(Dict.get(12))} -t 1 -o {o} -F embplant_pt -R 10\n")
                        if (count < 7):
                            out_file.write(
                                f"get_organelle_from_reads.py -1 {(Dict.get(13))} -2 {(Dict.get(14))} -t 1 -o {o} -F embplant_pt -R 10\n")
                            if (count < 8):
                                out_file.write(
                                    f"get_organelle_from_reads.py -1 {(Dict.get(15))} -2 {(Dict.get(16))} -t 1 -o {o} -F embplant_pt -R 10\n")
                                if (count < 9):
                                    out_file.write(
                                        f"get_organelle_from_reads.py -1 {(Dict.get(17))} -2 {(Dict.get(18))} -t 1 -o {o} -F embplant_pt -R 10\n")
                                    if (count = < 10)
                                        print('10 jobs submitted for choloroplast assembly')
out_file.close()
