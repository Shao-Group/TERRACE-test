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

groups = []

#input = "simu_circ_star.gtf"
#output = "simu_circ_star_sorted.gtf"

input = sys.argv[1]
output = sys.argv[2]

#print(input)
#print(output)

#read each line, form a group of circRNA with exons and add to groups
with open(input, "r", encoding="utf8") as circ_star_file:
    tsv_reader = csv.reader(circ_star_file, delimiter="\t")

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
    
    if len(row_list) > 0:
        row = row_list[0]
        item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        #print("item first:",item.feature)

    idx = 1
    while(idx <= len(row_list)):
        group = Group()
        group.circRNA = item

        #print(idx)
        if idx > len(row_list)-1 and item.feature == 'circRNA':
            exon_list = []
            group.exon_list = exon_list
            groups.append(group)
            break
        if idx > len(row_list)-1 and item.feature == 'exon':
            break

        row = row_list[idx]
        item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])

        #print('dtype')
        #for val in row:
        #    print(type(val))

        exon_list = []
        cnt = idx+1
        #print("item:",item.feature)

        while item.feature == 'exon':
            exon_list.append(item)
            #print('idx=',idx)
            #print('cnt=',cnt)
            if cnt > len(row_list)-1:
                break
            row = row_list[cnt]

            item = Item(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
            cnt = cnt + 1

        #print('exon list:',len(exon_list),'\n')
        #for i in range(0,len(exon_list)):
        #    exon = exon_list[i]
        #    print('exon:',exon.chr,exon.start,exon.end)
            
        group.exon_list = exon_list
        #print('\n')
        groups.append(group)
        idx = cnt

#print('len of groups:',len(groups))

#print('before sorting.........')
#for i in range(0,len(groups)):
#    group = groups[i]
#    print('circRNA:',group.circRNA.chr,group.circRNA.start,group.circRNA.end)
#    print('exons:')
#    print(len(group.exon_list))
#
#   for j in range(0,len(group.exon_list)):
#        exon = group.exon_list[j]
#        print('exon:',exon.chr,exon.start,exon.end)

for i in range(0,len(groups)):
    group = groups[i]
    group.exon_list.sort(key=lambda x:(int(x.start),int(x.end))) #sort exons by start position

groups.sort(key=lambda x:(isinstance(x.circRNA.chr,str),x.circRNA.chr,int(x.circRNA.start),int(x.circRNA.end))) #sort groups by chr and start position, ifchr is str, go to the end

#print('after sorting.........')
cnt = 0
for i in range(0,len(groups)):
    group = groups[i]
    #print('circRNA:',group.circRNA.chr,group.circRNA.start,group.circRNA.end)
    #print('exons:')
    #print(len(group.exon_list))
    cnt = cnt + 1

    for j in range(0,len(group.exon_list)):
        exon = group.exon_list[j]
        #print('exon:',exon.chr,exon.start,exon.end)
        cnt = cnt +1

print('after sort length',cnt)

with open(output, "w") as f:

    for i in range(0,len(groups)):
        group = groups[i]
        circRNA = group.circRNA
        exon_list = group.exon_list

        f.write(str(circRNA.chr) + "\t" + str(circRNA.src) + "\t" + str(circRNA.feature) + "\t" + str(circRNA.start) + "\t" + str(circRNA.end) + "\t" + str(circRNA.score) + "\t" + str(circRNA.strand) + "\t" + str(circRNA.frame) + "\t" + str(circRNA.attribute) + "\n")

        for j in range(0,len(exon_list)):
            exon = exon_list[j]

            f.write(str(exon.chr) + "\t" + str(exon.src) + "\t" + str(exon.feature) + "\t" + str(exon.start) + "\t" + str(exon.end) + "\t" + str(exon.score) + "\t" + str(exon.strand) + "\t" + str(exon.frame) + "\t" + str(exon.attribute) + "\n")
     


