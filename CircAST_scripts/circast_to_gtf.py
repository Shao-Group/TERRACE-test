import sys
import csv

csv.field_size_limit(sys.maxsize)

# total arguments
#n = len(sys.argv)

#input = "circularRNA_known.txt"
#output = "simu_circexplorer2.gtf"

input = sys.argv[1]
output = sys.argv[2]

#print(input)
#print(output)

with open(input, "r", encoding="utf8") as circast_file:
    tsv_reader = csv.reader(circast_file, delimiter="\t")

    # Skip the first row, which is the header
    #next(tsv_reader)

    with open(output, "w") as f:

        cnt = 0
        for row in tsv_reader:
            #print(row)
            (chrm, start, end, name, gene, strand, exonCount, exonSizes, exonOffsets, juncReadCount, FPKM, TPM, assignedReadCount) = row
            #print (chrm, start, end, name, gene, strand, exonCount, exonSizes, exonOffsets, juncReadCount, FPKM, TPM, assignedReadCount)
        
            f.write(chrm + "\t" + "CircAST" + "\t" + "circRNA" + "\t" + str(int(start)) + "\t" + end + "\t" + "." + "\t" + strand + "\t" + "." + "\t" + "gene_id \"" + gene + "\"; " "transcript_id \"" +  "transcript_" + str(cnt) + "\"; " + "cov \"" + juncReadCount + "\";" + "\n")
            
            exon_sizes = exonSizes.split(",")
            exon_Offsets = exonOffsets.split(",")

            #last_element = my_list.pop()
            #print(my_list)

            exon_cnt = 1
            for i in  range(0,int(exonCount)):
                exon_start = int(start) + int(exon_Offsets[i])
                exon_end = exon_start + int(exon_sizes[i])-1

                #print('start', exon_start, 'end', exon_end)
                
                f.write(chrm + "\t" + "CircAST" + "\t" + "exon" + "\t" + str(exon_start) + "\t" + str(exon_end) + "\t" + "." + "\t" + strand + "\t" + "." + "\t" + "gene_id \"" + gene + "\"; " "transcript_id \"" + "transcript_" + str(cnt) + "\"; " + "cov \"" + str(exon_cnt) + "\";" + "\n")
                exon_cnt = exon_cnt + 1
        
            cnt = cnt + 1
        print(cnt)
