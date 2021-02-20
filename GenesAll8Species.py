#this script makes table of orthologs that all 8 species have (from the YO dataset)

#dashes represent genes that the species does not have
bad_words = ['-', '-----------']

r = open("YOortholog_list (5).txt", "r")
w = open("YOGenesAll8.txt", "w")

#remove the lines that contain the dashes
for line in r:
    if not bad_words[0] in line and not bad_words[1] in line:
        w.write(line)
#output is table of YO ortholog ID's that all 8 species have