import sys

if len(sys.argv) != 2:
    print("Usage: python unique_kmers.py <seq.fa>")
    sys.exit(1)

fasta_file = sys.argv[1]
k = 3

seq = ""

with open(fasta_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            continue
        seq += line.strip()

unique_kmers = set()

for i in range(len(seq) - k + 1):
    kmer = seq[i:i+k]
    unique_kmers.add(kmer)

print(len(unique_kmers))

