
# external_sort.py
import csv
import os

def external_sort(table, conditions):
    col = conditions[0][0]  # sort on first condition
    temp_chunks = []
    chunk_size = 100
    with open(f'data/{table}.txt', 'r') as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) == chunk_size:
                chunk.sort(key=lambda x: x[col])
                path = f'temp_{len(temp_chunks)}.csv'
                with open(path, 'w', newline='') as w:
                    writer = csv.DictWriter(w, fieldnames=row.keys())
                    writer.writeheader()
                    writer.writerows(chunk)
                temp_chunks.append(path)
                chunk = []
        if chunk:
            chunk.sort(key=lambda x: x[col])
            path = f'temp_{len(temp_chunks)}.csv'
            with open(path, 'w', newline='') as w:
                writer = csv.DictWriter(w, fieldnames=chunk[0].keys())
                writer.writeheader()
                writer.writerows(chunk)
            temp_chunks.append(path)

    output_file = f'sorted_{table}.csv'
    merge_chunks(temp_chunks, output_file, col)
    for temp in temp_chunks:
        os.remove(temp)
    return output_file

def merge_chunks(chunks, output_file, col):
    files = [open(chunk, 'r') for chunk in chunks]
    readers = [csv.DictReader(f) for f in files]
    heads = [next(reader, None) for reader in readers]

    with open(output_file, 'w', newline='') as out:
        writer = None
        while any(head is not None for head in heads):
            min_idx = None
            for i, head in enumerate(heads):
                if head is not None:
                    if min_idx is None or head[col] < heads[min_idx][col]:
                        min_idx = i
            if writer is None:
                writer = csv.DictWriter(out, fieldnames=heads[min_idx].keys())
                writer.writeheader()
            writer.writerow(heads[min_idx])
            heads[min_idx] = next(readers[min_idx], None)

    for f in files:
        f.close()