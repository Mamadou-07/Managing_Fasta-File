# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:19:46 2023

@author: mdcoulibaly
"""


from Bio import SeqIO
from Bio.SeqIO.QualityIO import FastqGeneralIterator

def fasta_to_fastq(fasta_file, fastq_file):
    with open(fastq_file, "w") as fq_output:
           with open(fasta_file, "r") as fa_input:
               for record in SeqIO.parse(fa_input, "fasta"):
                # Assigning default quality scores of "I" with a score of 40
                seq = record.seq
                qual = "I" * len(seq)
                fastq_record = "@{}\n{}\n+\n{}\n".format(record.id, seq, qual)
                fq_output.write(fastq_record)

# Example usage

fasta_file = 'C:\\Users\\mdcoulibaly\\Documents\\PhD_PROJECT_MDC\\New Project_18-05-2023\\Seqq.fasta'
fastq_file = 'C:\\Users\\mdcoulibaly\\Documents\\PhD_PROJECT_MDC\\New Project_18-05-2023\\New_Articles_For DR\\output.fastq'
fasta_to_fastq(fasta_file, fastq_file)

