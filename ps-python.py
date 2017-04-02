# python file for VMSTAT 
import csv
from subprocess import check_output

def read_ps_output():
    with open('test.csv', 'wb') as file_excel:
        for x in check_output(['ps','-ef']).strip().splitlines():
            wr = csv.writer(file_excel, delimiter=' ', quoting=csv.QUOTE_ALL)
            wr.writerow(x.split())


read_ps_output()

