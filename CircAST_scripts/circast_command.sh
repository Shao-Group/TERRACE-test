#!/bin/bash

gtf=/path/to/reference/annotation/file
ciri_file=/path/to/CIRI2/output/file/[prefix].ciri
len=100 #length of the paired end reads, change accordingly

samtools sort -n -o accepted_hits.sorted.bam prefix_Aligned.sortedByCoord.out.bam

samtools view accepted_hits.sorted.bam > accepted_hits.sorted.sam

#use ciri file
python2.7 CircAST.py -F accepted_hits.sorted.sam -G "$gtf" -J "$ciri_file" -L "$len"

#output CircAST_result.txt
