def format_fasta(input_file):
    seq = ''
    acc_seq = {}
    
    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.strip()
            if line.startswith(">"):  # If it's an accession line
                if seq:  # If sequence collected from previous accession, calculate GC
                    GC_count = seq.count("G") + seq.count("C")
                    GC_per = GC_count / len(seq)  # GC percentage
                    acc_seq[id] = [GC_count, GC_per]
                
                id = line  # Store the accession line as id
                seq = ''  # Reset the sequence for the current accession
            else:
                seq += line  # Append the sequence data to the current sequence

        # Handle the last sequence after the loop
        if seq:  # For the very last sequence
            GC_count = seq.count("G") + seq.count("C")
            GC_per = GC_count / len(seq)
            acc_seq[id] = [GC_count, GC_per]

    return acc_seq

# Example usage
input_file = 'GC_file.txt'  # replace with your input file path
fasta_data = format_fasta(input_file)

# Print the results
for accession, (GC_count, GC_per) in fasta_data.items():
    print(f"{accession}: GC Count = {GC_count}, GC Percentage = {GC_per:.2f}")
