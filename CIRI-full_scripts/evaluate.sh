#!/bin/bash

ground_truth_file=$1
predicted_file=$2

sed -i '/^chrM/d' "$predicted_file"

#compare ground truth simu_sorted.gtf with simu_circ_star_sorted.gtf
python3 compare_chains_gtf_two.py "$ground_truth_file" "$predicted_file"

