from contextlib import nullcontext
from sre_constants import NOT_LITERAL
import pandas
import glob
from datetime import datetime, timedelta
import dateparser



input_folder = "D:\\Users\\costin\\Downloads\\"
intermediate_sufix = " - intermediate.csv"
processed_sufix = "- processed.csv"
ing_prefix = "Tranzactii_"
revolut_prefix = "account-statement-"
separator = "|"
#"%d-%m-%Y"
current_date = "02-05-2022" 

current_date = current_date if current_date else datetime.today().strftime("%d-%m-%Y")
print(current_date);

def convert_ro_date(datestring):
    dateobj = dateparser.parse(datestring, locales = ["ro-MD"])
    return dateobj.strftime("%d/%m/%Y")

def convert_decimal(decimalstring):
    return decimalstring.replace(".", "").replace(",", ".")

def convert_revolut_decimal(decimalstring):
    return str(-float(decimalstring))

def convert_revolut_datetime(datestring):
    dateobj = dateparser.parse(datestring)
    return dateobj.strftime("%d/%m/%Y")
    

#revolut statement file is generated with the start_date_end_date for the previous month
def generate_revolut_statement_period():
    last_day_of_prev_month = datetime.today().replace(day=1) - timedelta(days=1)
    start_day_of_prev_month = datetime.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)
    return start_day_of_prev_month.strftime("%Y-%m-%d") + "-" + last_day_of_prev_month.strftime("%Y-%m-%d")

def process_ing_files(files):
    for filename in files:
        intermediate_filename = filename + intermediate_sufix
        processed_filename = filename + processed_sufix
        print("input:" + filename);
        print("output:" + intermediate_filename);
        
        output_file = open(intermediate_filename, "w")
        
        input_file = open(filename)

        buffer = ""
        for line in input_file:
            line = line[:-1]
            if line[0].isnumeric():
                buffer = buffer.replace(':','')
                output_file.write(buffer + "\n")
                buffer = line
                
            else:
                buffer += line + separator
        buffer = buffer.replace(':','')
        output_file.write(buffer + "\n")
        output_file.close()
        input_file.close()

        result = pandas.read_csv(intermediate_filename, 
                                    delimiter=",",
                                    header=0,
                                    skiprows=1,
                                    names=["Date", "Detalii Tranzactii", "Value", "X", "Y", "Z"],
                                    usecols=[0, 3, 5, 9, 15, 21],
                                    converters = {"Date":convert_ro_date, "Value":convert_decimal}
                                )
        result.to_csv(processed_filename, sep = ",")

def process_revolut_files(files):
    for filename in files:
        processed_filename = filename + processed_sufix
        print("input:" + filename);
        print("output:" + processed_filename);
        
        result = pandas.read_csv(filename, 
                                    delimiter=",",
                                    header=0,
                                    skiprows=1,
                                    names=["Type", "Date Completed", "Description", "Value"],
                                    usecols=[0, 3, 4, 5],
                                    converters = {"Date Completed":convert_revolut_datetime, "Value":convert_revolut_decimal}
                                )
        result = result.iloc[:,[1, 0, 3, 2] ]
        result.to_csv(processed_filename, sep = ",")


files = glob.glob(input_folder + ing_prefix + current_date + "*csv")
files = [x for x in files if not x.find(processed_sufix) != -1]
print("Processing ING files")
print (files)
process_ing_files(files)
print("____________________________________________")

files = glob.glob(input_folder + revolut_prefix + generate_revolut_statement_period() + "*csv")
files = [x for x in files if not x.find(processed_sufix) != -1]
print("Processing Revolut files")
print (files)
process_revolut_files(files)
print("____________________________________________")


print("Done")



