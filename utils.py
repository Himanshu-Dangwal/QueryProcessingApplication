# utils.py
import csv

def read_blocks(table, block_size=100):
    path = f'data/{table}.txt'
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        block = []
        for row in reader:
            block.append(row)
            if len(block) == block_size:
                yield block
                block = []
        if block:
            yield block