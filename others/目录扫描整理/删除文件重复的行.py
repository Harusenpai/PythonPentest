#
import shutil
import os 
source="综合目录.txt"

destination = "bak_"+ source

lines_seen = set() 
outfile = open("temp.txt", "w")
for line in open(source, "r"):
    print(line)
    if line not in lines_seen: 
        outfile.write(line)
        lines_seen.add(line)

outfile.close()
os.renames(source,destination)
os.renames( "temp.txt",source)
