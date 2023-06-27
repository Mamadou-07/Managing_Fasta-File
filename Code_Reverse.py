# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 10:33:10 2023

@author: mdcoulibaly
"""

def reverse_fastq_reads(input_file, output_file):
    with open(input_file, 'r') as input_f, open(output_file, 'w') as output_f:
        while True:
            # Read four lines at a time from the input FASTQ file
            header = input_f.readline().strip()
            sequence = input_f.readline().strip()
            plus_line = input_f.readline().strip()
            quality = input_f.readline().strip()

            # Break the loop if we've reached the end of the file
            if not header:
                break

            # Reverse the sequence and quality scores
            reversed_sequence = sequence[::-1]
            reversed_quality = quality[::-1]

            # Write the reversed reads to the output FASTQ file
            output_f.write(header + '\n')
            output_f.write(reversed_sequence + '\n')
            output_f.write(plus_line + '\n')
            output_f.write(reversed_quality + '\n')

    print("Reverse reads FASTQ file created successfully.")

# Usage example
reverse_fastq_reads('C:\\Users\\mdcoulibaly\\Documents\\PhD_PROJECT_MDC\\New Project_18-05-2023\\New_Articles_For DR\\SeqFw.fastq', 'C:\\Users\\mdcoulibaly\\Documents\\PhD_PROJECT_MDC\\New Project_18-05-2023\\New_Articles_For DR\\SeqRev.fastq')
