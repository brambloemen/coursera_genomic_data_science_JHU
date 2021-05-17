#!/Anaconda/python  # in unix, put this in front to run from terminal

"""
biopython introduction: BLAST
"""
from Bio.Blast import NCBIWWW
fasta_string = open("myseq.fa").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

from Bio.Blast import NCBIXML
blast_record = NCBIXML.read(result_handle)
print(len(blast_record))

E_VALUE_THRESH = 0.01
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH
