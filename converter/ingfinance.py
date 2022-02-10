import pandas
import glob
from datetime import datetime

input_folder = "D:\\Users\\costin\\Downloads\\"
processed_sufix = "- processed.csv"
separator = "|"

current_date = datetime.today().strftime("%d-%m-%Y")
print(current_date);

files = glob.glob(input_folder + "Tranzactii_" + current_date + "*csv")
files = [x for x in files if not x.find(processed_sufix) != -1]
print (files)

def write_line(line):
    output_file.write(line + "\n")

for filename in files:
    output_file = open(filename + processed_sufix, "w")
    
    input_file = open(filename)

    buffer = ""
    for line in input_file:
        line = line[:-1]
        if line[0].isnumeric():
            buffer = buffer.replace(':','')
            write_line(buffer)
            buffer = line
        else:
            buffer += line + separator
    buffer = buffer.replace(':','')
    write_line(buffer)

    output_file.close()
    input_file.close()

print("Done")



