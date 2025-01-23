'''
Given a fasta file with sequences on multi-line, calculate GC content
and return ID with highest GC content and its percentage

>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
'''


# readSequence function creates a dictionary of accession IDs to sequence data
# computeGC function prints the accession ID of the sequence with the highest GC content and its percentage

def readSequence(input_file):
    seq = ''
    acc_seq = {}
    
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line[0] == ">": # If it's an accession line
                if seq:  # If sequence collected from previous run, collect it
                    acc_seq[id] = seq


                id = line[1:] # id stored in this line
                seq = ''  # Reset the sequence for the current accession
            else:
                seq += line  # Append the sequence data to the current sequence

        if seq: # For the very last line since there's no ">" to complete the GC calculations & dictionary adding
            acc_seq[id] = seq

        # print(type(acc_seq))
        return acc_seq

def computeGC(input_file):
    GC_dict = readSequence(input_file)

    for key in list(GC_dict.keys()): # can't directly iterate over GC_dict bc while iterating, python expects stable dict size
        seq = GC_dict[key]
        GC_count = seq.count("G") + seq.count("C")
        GC_per = (GC_count / len(seq)) * 100
        GC_dict[key] = [GC_count, GC_per]
    
    # Now, output the ID and the GC percent of the sequence that has the highest GC count
    max_GC =  max(GC_dict, key=lambda k: GC_dict[k][0])
    max_GC_per = GC_dict[max_GC][1]
    print(max_GC)
    print(max_GC_per)





if __name__ == "__main__" :
    input_file = 'GC_file.txt'
    computeGC(input_file)



''' Learning Notes:
- due to mult-line structure of the sequences, pay attention to the structure
of code and how I appended the multi-line of the sequences in the same iteration the > accession line was detected

'''