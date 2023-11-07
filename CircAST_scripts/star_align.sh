#!/bin/bash

out=/path/to/output/directory/[prefix]
genome=/path/to/STAR/index
ref=/path/to/reference/genome/file/fasta

#genome index generation
STAR --runThreadN 8 \
     --runMode genomeGenerate\
     --genomeDir $genome \
     --genomeFastaFiles $ref\

#mapping
STAR --runThreadN 8\
     --outSAMstrandField intronMotif\
     --chimSegmentMin 20\
     --genomeDir $genome\
     --readFilesIn paired-end_1.fq paired-end_2.fq\
     --outFileNamePrefix "$out"\
     --chimOutType WithinBAM\
     --outSAMtype BAM SortedByCoordinate

# output [prefix]_Aligned.sortedByCoord.out.bam