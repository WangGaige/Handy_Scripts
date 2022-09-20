import csv

# open the file in the write mode
f = open('./csv_file1', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
for r in range(255):
    for g in range(255):
        for b in range(255):
            row = [str(r), str(g), str(b), '255']
            writer.writerow(row)
# close the file
f.close()
