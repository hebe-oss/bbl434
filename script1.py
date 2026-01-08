import sys

if len(sys.argv) != 2:
    print("Usage: python fasta_length.py <seq.fa>")
    sys.exit(1)

fasta_file = sys.argv[1]

seq = ""

with open(fasta_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            continue
        seq += line.strip()

print(len(seq))

