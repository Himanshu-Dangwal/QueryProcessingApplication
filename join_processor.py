# join_processor.py
import csv
from utils import read_blocks

def process_join(parsed):
    table1 = parsed['table1']
    table2 = parsed['table2']
    cond1 = parsed['cond1'].split('.')[-1]
    cond2 = parsed['cond2'].split('.')[-1]

    for block1 in read_blocks(table1):
        for block2 in read_blocks(table2):
            for row1 in block1:
                for row2 in block2:
                    if row1[cond1] == row2[cond2]:
                        print({**row1, **row2})