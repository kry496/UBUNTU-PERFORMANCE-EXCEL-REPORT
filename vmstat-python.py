# python file for VMSTAT 
import csv
from subprocess import check_output
from pprint import pprint as pp

vm_stat = []
def read_vmstat_output():
    with open('test.csv', 'wb') as file_excel:
        for x in check_output(['vmstat','1','10']).strip().splitlines():
            vm_stat.append(x)
        pp(vm_stat)
        wr = csv.writer(file_excel, delimiter=' ')
        wr.writerows(vm_stat)


read_vmstat_output()

