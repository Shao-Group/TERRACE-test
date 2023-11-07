import sys
import csv

csv.field_size_limit(sys.maxsize)

class Item:
  def __init__(self, chr=0, src='', feature='', start=0, end=0, score=0, strand='', frame='', attribute=''):
    self.chr = chr
    self.src = src
    self.feature = feature
    self.start = start
    self.end = end 
    self.score = score
    self.strand = strand
    self.frame = frame
    self.attribute = attribute

class Group:
    def __init__(self, circRNA=0, exon_list=[]):
        self.circRNA = circRNA
        self.exon_list = exon_list

#input = "lung_annotation_org"
#output = "lung_anno.gtf"

input = sys.argv[1]
output = sys.argv[2]

groups = []

#read each line, form a group of circRNA with exons and add to groups
with open(input, "r", encoding="utf8") as isocirc_file:
    tsv_reader = csv.reader(isocirc_file, delimiter="\t")

    #Skip the first row, which is the header
    #next(tsv_reader)

    row_list = list(tsv_reader)
    print('before sort length',len(row_list))
    #print(row_list[0])

    for i in range(0,len(row_list)):
        row = row_list[i]
        converted_row = [int(ele) if ele.isdigit() else ele for ele in row] #convert int to int and str to str inside a row
        row_list[i] = converted_row
        #print(row)

    #print(row_list)

    bundle = []

    row = row_list[0]
    item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
    lst = row[8].split(";")
    prev_trans_id = lst[1]

    bundle.append(item)

    if len(row_list) == 1: #add this single instance in groups, for loop does not run
        grp = Group()
        exon = bundle[0]
        circ = Item(exon.chr, exon.src, "circRNA", bundle[0].start, bundle[len(bundle)-1].end, exon.score, exon.strand, exon.frame, exon.attribute)
        grp.circRNA = circ
        grp.exon_list = bundle.copy()
        #print("exon list size:",len(grp.exon_list))
        groups.append(grp)

    for i in range(1,len(row_list)):
        row = row_list[i]
        item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        lst = row[8].split(";")
        trans_id = lst[1]
        #print(trans_id)

        if trans_id != prev_trans_id:
            #add to groups
            grp = Group()
            exon = bundle[0]
            circ = Item(exon.chr, exon.src, "circRNA", bundle[0].start, bundle[len(bundle)-1].end, exon.score, exon.strand, exon.frame, exon.attribute)
            grp.circRNA = circ
            grp.exon_list = bundle.copy()
            #print("exon list size:",len(grp.exon_list))
            groups.append(grp)

            bundle.clear()
            bundle.append(item)

        if trans_id == prev_trans_id:
            #print(item.attribute)
            bundle.append(item)

        prev_trans_id = trans_id
        
        if i == len(row_list) - 1:
            #add the last group
            grp = Group()
            exon = bundle[0]
            circ = Item(exon.chr, exon.src, "circRNA", bundle[0].start, bundle[len(bundle)-1].end, exon.score, exon.strand, exon.frame, exon.attribute)
            grp.circRNA = circ
            grp.exon_list = bundle.copy()
            #print("exon list size:",len(grp.exon_list))
            groups.append(grp)

# for i in range(0,len(groups)):
#     grp = groups[i]
#     print("size:",len(grp.exon_list))

print("Number of distinct circRNAs:",len(groups))

with open(output, "w") as f:

    for i in range(0,len(groups)):
        group = groups[i]
        circRNA = group.circRNA
        exon_list = group.exon_list

        f.write(str(circRNA.chr) + "\t" + str(circRNA.src) + "\t" + str(circRNA.feature) + "\t" + str(circRNA.start) + "\t" + str(circRNA.end) + "\t" + str(circRNA.score) + "\t" + str(circRNA.strand) + "\t" + str(circRNA.frame) + "\t" + str(circRNA.attribute) + "\n")

        for j in range(0,len(exon_list)):
            exon = exon_list[j]

            f.write(str(exon.chr) + "\t" + str(exon.src) + "\t" + str(exon.feature) + "\t" + str(exon.start) + "\t" + str(exon.end) + "\t" + str(exon.score) + "\t" + str(exon.strand) + "\t" + str(exon.frame) + "\t" + str(exon.attribute) + "\n")
     


