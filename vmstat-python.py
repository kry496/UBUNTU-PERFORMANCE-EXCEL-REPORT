# python file for VMSTAT 
import csv
from subprocess import check_output


def read_vmstat_output():
    with open('test.csv', 'wb') as file_excel:
        for x in check_output(['vmstat','1','10']).strip().splitlines():
            wr = csv.writer(file_excel, delimiter=' ')
            wr.writerow(x.split())


read_vmstat_output()

