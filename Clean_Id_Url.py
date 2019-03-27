import sys
import csv

with open(sys.argv[3], newline='') as csvfile:
    ids = list(csv.reader(csvfile))
    ids = [val for sublist in ids for val in sublist]
with open(sys.argv[2], 'w+') as outputFile:
    outputFile.write('{0},{1}\n'.format("FaceID","Image"))
    with open(sys.argv[1]) as inputFile:
        for line in inputFile:
            data = line.split("\t")
            if(data[0] in ids):
                outputFile.write('{0}\t{1}\n'.format(data[0],data[6]))
                outputFile.flush()
print('Done')
