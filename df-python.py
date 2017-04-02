# python file for VMSTAT 
import csv
from subprocess import check_output

def read_df_output():
    with open('test.csv', 'wb') as file_excel:
        for x in check_output(['df','-h']).strip().splitlines():
            wr = csv.writer(file_excel, delimiter=' ')
            wr.writerow(x.split())


read_df_output()

