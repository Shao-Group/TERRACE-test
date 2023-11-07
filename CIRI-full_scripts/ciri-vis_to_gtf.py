import sys
import csv

csv.field_size_limit(sys.maxsize)

# total arguments
n = len(sys.argv)

#input = "simu_full.list"
#output = "simu_ciri-full.gtf"

input = sys.argv[1]
output = sys.argv[2]

#print(input)
#print(output)

with open(input, "r", encoding="utf8") as ciri_full_file:
    tsv_reader = csv.reader(ciri_full_file, delimiter="\t")

    # Skip the first row, which is the header
    #next(tsv_reader)

    with open(output, "w") as f:
        
        cnt = 0
        for row in tsv_reader:
            (image_id, circ_id, chr, start, end, total_exp, isoform_number, isoform_exp, isoform_length, isoform_state, strain, gene_id, isoform_cirexon) = row

            f.write(chr + "\t" + "CIRI-full" + "\t" + "circRNA" + "\t" + start + "\t" + end + "\t" + "0.0000" + "\t" + strain + "\t" + "." + "\t" + "gene_id \"" + gene_id + "\"; " "transcript_id \"" +  "transcript_" + str(cnt) + "\"; " + "cov \"" + isoform_exp + "\";" + "\n")
            
            my_list = isoform_cirexon.split(",")
            last_element = my_list.pop()
            #print(my_list)

            exon_cnt = 1
            for val in my_list:
                start_end_pair = val.split("-")
                #print('start', start_end_pair[0], 'end', start_end_pair[1])

                f.write(chr + "\t" + "CIRI-full" + "\t" + "exon" + "\t" + start_end_pair[0] + "\t" + start_end_pair[1] + "\t" + "0.0000" + "\t" + strain + "\t" + "." + "\t" + "gene_id \"" + gene_id + "\"; " "transcript_id \"" +  "transcript_" + str(cnt) + "\"; " + "cov \"" + str(exon_cnt) + "\";" + "\n")
                exon_cnt = exon_cnt + 1
        
            cnt = cnt + 1
        print(cnt)
