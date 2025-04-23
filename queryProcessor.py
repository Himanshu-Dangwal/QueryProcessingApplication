# queryProcessing.py
import sys
from parser import parse_query
from select_processor import process_select
from join_processor import process_join

def main():
    if len(sys.argv) < 2:
        print("Usage: python queryProcessing.py \"<SQL QUERY>\"")
        return

    query = sys.argv[1]
    parsed = parse_query(query)

    if parsed['type'] == 'select':
        process_select(parsed)
    elif parsed['type'] == 'join':
        process_join(parsed)
    else:
        print("Unsupported or malformed query.")

if __name__ == "__main__":
    main()