import os
import requests
from Bio import Entrez
from collections import Counter

# Load email from environment variable
Entrez.email = os.environ.get("NCBI_EMAIL")

if not Entrez.email:
  raise ValueError("NCBI_EMAIL environment variable not set")

handle = Entrez.efetch(db="nucleotide", id="NM_001200025", rettype="fasta", retmode="text")
sequence = handle.read()
handle.close()

print(sequence)

# Nucleotide frequencies
freq = Counter(sequence)
print(freq)

# GC Content
gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
print(f"GC content: {gc:.2f}%")

# Reverse complement
complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
reverse_complement = ''.join(complement[base] for base in reversed(sequence))
print(reverse_complement)

ncbi_id = "NM_001200025"  # Example RefSeq ID
url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
params = {
    "db": "nucleotide",
    "id": ncbi_id,
    "rettype": "fasta",
    "retmode": "text"
}

response = requests.get(url, params=params)

if response.ok:
    print(response.text)
else:
    print(f"Error: {response.status_code}")