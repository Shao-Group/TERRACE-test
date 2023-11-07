#!/bin/bash

out=/path/to/STAR/alignment/directory/
ref=/path/to/reference/genome/file/fasta
gtf=/path/to/reference/annotation/file/genepred/format

#parse
CIRCexplorer2 parse -t STAR "$out"/[prefix]_Chimeric.out.junction > CIRCexplorer2_parse.log

#annotate
CIRCexplorer2 annotate -r "$gtf" -g "$ref" -b back_spliced_junction.bed -o circularRNA_known.txt 

#output circularRNA_known.txt
