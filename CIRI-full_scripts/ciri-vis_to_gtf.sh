#!/bin/bash

input=$1
output=$2

mkdir temp

#keep only full reconstructed rows from ciri-vis output simu.list to simu_full.list
awk '{if ($10 == "Full") print $0;}' "$input" > temp/vis_full.list

#convert ciri-vis original file to standard gtf
python3 ciri-vis_to_gtf.py temp/vis_full.list "$output"

rm -r temp


