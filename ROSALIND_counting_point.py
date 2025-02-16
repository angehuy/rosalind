# Computes the Hamming Distance between two sequences
# Assume sequences are of equal lengths


def count_mut(seq1, seq2):
    count = 0
    l_1 = len(seq1)
    for i in l_1:
        if seq1[i] != seq2[i]:
            count += 1

def count_mut2(seq1, seq2):
    count = 0
    for a,b in zip(seq1, seq2):
        if a!= b:
            count += 1

count_mut2("bch", "bcb")




'''
- zip uses lazy evaluation (returns iterator); values needed are not computed until they're used (i.e. when you iterate over them)
- for loop with indexing requires access to full list at once, so all the elements are already stored in memory


'''
