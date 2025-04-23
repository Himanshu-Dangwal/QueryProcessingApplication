import sqlparse

def parse_query(query):
    query = query.strip().lower()
    if 'join' in query:
        return parse_join(query)
    elif 'select' in query and 'from' in query:
        return parse_select(query)
    else:
        return {'type': 'unknown'}

def parse_select(query):
    tokens = query.replace('select * from ', '').split(' where ')
    table = tokens[0].strip()
    conds = tokens[1].split(' and ')
    conditions = []
    for cond in conds:
        key, val = cond.split('=')
        conditions.append((key.strip(), val.strip().strip("'")))
    return {'type': 'select', 'table': table, 'conditions': conditions}

def parse_join(query):
    tokens = query.replace('select * from ', '').split(' join ')
    t1 = tokens[0].strip()
    t2, cond = tokens[1].split(' on ')
    cond_left, cond_right = cond.split('=')
    return {
        'type': 'join',
        'table1': t1,
        'table2': t2.strip(),
        'cond1': cond_left.strip(),
        'cond2': cond_right.strip()
    }