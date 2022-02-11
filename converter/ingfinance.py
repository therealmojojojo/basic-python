import pandas
import glob
from datetime import datetime
import dateparser



input_folder = "D:\\Users\\costin\\Downloads\\"
processed_sufix = "- processed.csv"
separator = "|"

current_date = datetime.today().strftime("%d-%m-%Y")
print(current_date);

files = glob.glob(input_folder + "Tranzactii_" + current_date + "*csv")
files = [x for x in files if not x.find(processed_sufix) != -1]
print (files)

def convert_ro_date(datestring):
    dateobj = dateparser.parse(datestring, locales = ["ro-MD"])
    return dateobj.strftime("%d/%m/%Y")

def convert_decimal(decimalstring):
    return decimalstring.replace(".", "").replace(",", ".")

def write_line(line):
    output_file.write(line + "\n")


print(convert_ro_date("12 ianuarie 2020"))

for filename in files:
    processed_filename = filename + processed_sufix
    print("input:" + filename);
    print("output:" + processed_filename);
    
    output_file = open(processed_filename, "w")
    
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

    result = pandas.read_csv(processed_filename, 
                                delimiter=",",
                                header=0,
                                skiprows=1,
                                names=["Date", "Detalii Tranzactii", "Value", "X", "Y", "Z"],
                                usecols=[0, 3, 5, 9, 15, 21],
                                converters = {"Date":convert_ro_date, "Value":convert_decimal}
                            )
    result.to_csv(processed_filename, sep = ",")

print("Done")



