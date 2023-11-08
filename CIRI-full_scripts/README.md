# Download and Install CIRI-full and CIRI-vis

CIRI-full jar file can be downloaded from https://github.com/bioinfo-biols/CIRI-full/releases/tag/v2.1.2. Please make sure to use this latest jar file and not any older version.

CIRI-full uses of CIRI2, CIRI-AS in its pipeline. They are avilable inside the CIRI-full package (https://sourceforge.net/projects/ciri-full/) To generate the full structure of circular RNA isoforms CIRI-vis (https://github.com/bioinfo-biols/CIRI-vis) needs to be run on the CIRI-full output. The versions to be used for reproducibility are as follows.

CIRI2 = CIRI_v2.0.6/CIRI2.pl

CIRI_AS = CIRI_AS_v1.2/CIRI_AS_v1.2.pl

CIRI_vis = CIRI_vis_v1.4.jar

# Run CIRI-full and CIRI-vis

The general instructions to run CIRI-full is available at https://ciri-cookbook.readthedocs.io/en/latest/CIRI-full.html. 

The general instructions to run CIRI-vis is available https://ciri-cookbook.readthedocs.io/en/latest/CIRI-vis.html.

It is recommended to run CIRI-full step by step instead of using the full pipeline. See the provided guideline script `ciri-full_command.sh` to ensure reprodicibility of results.

`ciri-full_command.sh` uses bwa-aligner (https://sourceforge.net/projects/bio-bwa/files/), CIRI2.pl, CIRI_AS_v1.2.pl, CIRI-Full_v2.1.2.jar, CIRI-vis_v1.4.jarstep by step to get the final output `[prefix].list` in the `vis_output` folder.

`ciri-full_command.sh` shows the steps to run CIRI-full/CIRI-vis with reference annotation (`anno_file`). If you want to run CIRI-full without reference annotation, do not use the `anno_file`. Make sure to remove the parameters that use `anno_file` in the CIRI2.pl, CIRI_AS_v1.2.pl, and CIRI-Full_v2.1.2.jar Merge commands.

The simulated paired-end reads used in TERRACE can be downloaded from [doi:10.26208/AZ99-RQ38](https://doi.org/10.26208/AZ99-RQ38). The total-RNA paired-end reads from human tissues used in TERRACE can be downloaded from BIGD (accession number: PRJCA000751).

We recommend to use [GRCh38 reference](https://ftp.ensembl.org/pub/release-97/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz), [GRCh38 annotation](https://ftp.ensembl.org/pub/release-97/gtf/homo_sapiens/Homo_sapiens.GRCh38.97.gtf.gz) for simulated data and [GRCh37 reference](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_43/GRCh37_mapping/GRCh37.primary_assembly.genome.fa.gz), [GRCh37 annotation](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_43/GRCh37_mapping/gencode.v43lift37.basic.annotation.gtf.gz) for biological data to ensure reproducibility of results.

# Convert CIRI-vis Output

The output file `[prefix].list` from CIRI-vis is not in the standard gtf format. Use `ciri-vis_to_gtf.sh` to convert this file to a standard gtf format to run our evaluation pipeline. The usage is:

```
./ciri-vis_to_gtf.sh <[prefix].list> <CIRI-full-output.gtf>
```

# Evaluate CIRI-full/CIRI-vis

1. Download - Download the appropriate ground truth file to evaluate CIRI-full-output.gtfproduced by CIRI-full. The ground truth files for simulated data can be downloaded from [doi:10.26208/AZ99-RQ38](https://doi.org/10.26208/AZ99-RQ38). The ground truth files for simulated data are already in the standard gtf format. Ignore step 2 if you are evaluating on the simulated data.

The ground truth files for the biological data can be downloaded from the isocirc catalog (https://genome.ucsc.edu/s/xinglab_chop/isoCirc). To download groud the truth file, got to the [Table Browser](https://genome.ucsc.edu/cgi-bin/hgTables?hgsid=1761281632_7eq71llIPltZklaNkDC972ZYv5N6&db=hg19&position=chr1:23356962-23380332&hgta_regionType=range), choose the appropriate `tissue` for the `track`, select `genome` for the `region` field, select output format as `GTF - gene transfer format (limited)`, and assign an `output filename` before clicking `get output`.  See step 2 to convert the biological ground truth to a standard gtf format adjusted for our evaluation pipeline.

2. Convert - (Ignore this step if you are evaluating on simulated data) Convert the biological ground truth file to a standard gtf file adjusted for our evaluation pipeline using the script `convert_isocirc_gtf.py` provided. The usage is:
    ```
    python3 convert_isocirc_gtf.py <dowloaded-ground-truth.gtf> <ground-truth-adjusted.gtf>
    ```

3. Sort - Sort both CIRI-full-output.gtf and ground-truth.gtf using `sort_circ_gtf.py` script provided. The usage is:
    ```
    python3 sort_circ_gtf.py <input-file.gtf> <input-file-sorted.gtf>
    ```
4. Evaluate - Run the evaluation script `evaluate.sh` provided to get recall and precision for a given ground truth file (sorted) and predicted file (sorted). The usage is:
    ```
    ./evaluate.sh <ground-truth-sorted.gtf> <CIRI-full-output-sorted.gtf>
    ```

