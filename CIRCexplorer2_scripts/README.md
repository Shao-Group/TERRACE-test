# Download and Install CIRCexplorer2

CIRCexplorer2 can be downloaded and installed using instructions from https://github.com/YangLab/CIRCexplorer2. 

# Run CIRCexplorer2

The general instructions to run CIRCexplorer2 is available in the CIRCexplorer2 Documentation https://circexplorer2.readthedocs.io/en/latest/.

CIRCexplorer2 needs to be run with specific parameters to ensure reproducibility of results. For details of the parameters used to run CIRCexplorer2, see the provided guideline scripts `star_align.sh` and `parse_and_annotate.sh`.

`star_align.sh` contains information to align paired-end RNA-seq reads using STAR (https://github.com/alexdobin/STAR) to produce `[prefix]_Chimeric.out.junction` file. 

`parse_and_annotate.sh` takes the `[prefix]_Chimeric.out.junction` as input to produce a list of circular RNAs `circularRNA_known.txt `. The reference annotation used when annotating should be converted to genepred format (see details in https://circexplorer2.readthedocs.io/en/latest/tutorial/setup/#setup).

The simulated paired-end reads used in TERRACE can be downloaded from [doi:10.26208/AZ99-RQ38](https://doi.org/10.26208/AZ99-RQ38). The total-RNA paired-end reads from human tissues used in TERRACE can be downloaded from BIGD (accession number: PRJCA000751).

We recommend to use [GRCh38 reference/annotation](https://ftp.ensembl.org/pub/release-97/gtf/homo_sapiens/Homo_sapiens.GRCh38.97.gtf.gz) for simulated data and [GRCh37 reference](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_43/GRCh37_mapping/GRCh37.primary_assembly.genome.fa.gz),  [GRCh37 annotation](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_43/GRCh37_mapping/gencode.v43lift37.basic.annotation.gtf.gz) for biological data to ensure reproducibility.

# Convert CIRCexplorer2 Output

The output file `circularRNA_known.txt` from CIRCexplorer2 is not in the standard gtf format. Use `circexplorer2_to_gtf.py` to convert this file to a standard gtf format to run our evaluation pipeline. The usage is:

```
python3 circexplorer2_to_gtf.py <circularRNA_known.txt> <CIRCexplorer2-output.gtf>
```

# Evaluate CIRCexplorer2

1. Download - Download the appropriate ground truth file to evaluate CIRCexplorer2-output.gtf produced by CIRCexplorer2. The ground truth files for simulated data can be downloaded from [doi:10.26208/AZ99-RQ38](https://doi.org/10.26208/AZ99-RQ38). The ground truth files for simulated data are already in the standard gtf format. Ignore step 2 if you are evaluating on the simulated data. 

The ground truth files for the biological data can be downloaded from the isocirc catalog (https://genome.ucsc.edu/s/xinglab_chop/isoCirc). To download groud the truth file, got to the [Table Browser](https://genome.ucsc.edu/cgi-bin/hgTables?hgsid=1761281632_7eq71llIPltZklaNkDC972ZYv5N6&db=hg19&position=chr1:23356962-23380332&hgta_regionType=range), choose the appropriate `tissue` for the `track`, select `genome` for the `region` field, select output format as `GTF - gene transfer format (limited)`, and assign an `output filename` before clicking `get output`.  See step 2 to convert the biological ground truth to a standard gtf format adjusted for our evaluation pipeline.

2. Convert - (Ignore this step if you are evaluating on simulated data) Convert the biological ground truth file to a standard gtf file adjusted for our evaluation pipeline using the script `convert_isocirc_gtf.py` provided. The usage is:
    ```
    python3 convert_isocirc_gtf.py <dowloaded-ground-truth.gtf> <ground-truth-adjusted.gtf>
    ```

3. Sort - Sort both CIRCexplorer2-output.gtf and ground-truth.gtf using `sort_circ_gtf.py` script provided. The usage is:
    ```
    python3 sort_circ_gtf.py <input-file.gtf> <input-file-sorted.gtf>
    ```
4. Evaluate - Run the evaluation script `evaluate.sh` provided to get recall and precision for a given ground truth file (sorted) and predicted file (sorted). The usage is:
    ```
    ./evaluate.sh <ground-truth-sorted.gtf> <CIRCexplorer2-output-sorted.gtf>
    ```

