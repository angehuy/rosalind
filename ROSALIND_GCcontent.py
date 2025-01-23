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


def format_fasta(input_file):
    seq = ''
    acc_seq = {}
    
    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line.startswith(">"):  # If it's an accession line
                if seq:  # If sequence collected from previous run, collect it
                    GC_count = seq.count("G") + seq.count("C")
                    GC_per = GC_count / len(seq)
                    acc_seq[id] = [GC_count, GC_per]


                id = line[1:] # id stored in this line
                seq = ''  # Reset the sequence for the current accession
            else:
                seq += line  # Append the sequence data to the current sequence

        if seq: # For the very last line since there's no ">" to complete the GC calculations & dictionary adding
            GC_count = seq.count("G") + seq.count("C")
            GC_per = (GC_count / len(seq)) * 100
            acc_seq[id] = [GC_count, GC_per]

        max_GC =  max(acc_seq, key=lambda k: acc_seq[k][0])
        max_GC_per = acc_seq[max_GC][1]
        print(max_GC)
        print(max_GC_per)


if __name__ == "__main__" :
    input_file = 'GC_file.txt'
    format_fasta(input_file)


''' What I learned
- due to mult-line structure of the sequences, pay attention to the structure
of code and how I appended the multi-line of the sequences in the same iteration the > accession line was detected

'''


