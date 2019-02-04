

source_file_name = "C:\\Users\\costi\\Downloads\\Tranzactii_pe_perioada - ianuarie.csv"
target_file_name = "C:\\Users\\costi\\Downloads\\Tranzactii_pe_perioada - ianuarie - processed.csv"
separator = "|"

output_file = open(target_file_name, "a")
def write_line(line):
    output_file.write(line + "\n")

input_file = open(source_file_name)

buffer = ""
for line in input_file:
    line = line[:-1]
    if line[0].isnumeric():
        write_line(buffer)
        buffer = line
    else:
        buffer += line + separator
write_line(buffer)

output_file.close()
input_file.close()



