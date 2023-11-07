#!/bin/bash

len=100 #length of the paired end reads, change accordingly
output=/path/to/output/directory/
ref_file=/path/to/reference/genome/file/fasta
anno_file=/path/to/reference/annotation/file/gtf

bwa index "$ref_file"

bwa mem -T 19 -t 8 "$ref_file" paired-end_1.fq paired-end_2.fq > "$output"/test.sam

perl CIRI2.pl -I "$output"/test.sam -O "$output"/test.ciri -F "$ref_file" -A "$anno_file"

perl CIRI_AS_v1.2.pl" -S "$output"/test.sam -C "$output"/test.ciri -F "$ref_file" -A "$anno_file" -O "$output"/test -D yes

java -jar CIRI-Full_v2.1.2.jar RO1 -1 paired-end_1.fq -2 paired-end_2.fq -o "$output"/test

bwa mem -T 19 -t 8 "$ref_file" "$output"/test_ro1.fq > "$output"/test_ro1.sam

java -jar CIRI-Full_v2.1.2.jar RO2 -r "$ref_file" -s "$output"/test_ro1.sam -l "$len" -o "$output"/test

java -jar CIRI-Full_v2.1.2.jar Merge -c "$output"/test.ciri -as "$output"/test_jav.list -ro "$output"/test_ro2_info.list -a "$anno_file" -r "$ref_file" -o "$output"/test

java -jar CIRI-vis_v1.4.jar -i "$output"/test_merge_circRNA_detail.anno -l "$output"/test_library_length.list -r "$ref_file" -d "$output""/vis_output" -o test -min 1 
