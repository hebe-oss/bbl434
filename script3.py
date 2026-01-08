import sys

if len(sys.argv) != 2:
    print("Usage: python count_fasta_records.py <seq.mfa>")
    sys.exit(1)

fasta_file = sys.argv[1]

record_count = 0

with open(fasta_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            record_count += 1

print(record_count)

