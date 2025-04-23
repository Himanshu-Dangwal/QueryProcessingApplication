# README.md

# Query Processing Engine

This project simulates a lightweight SQL engine in Python. It supports `SELECT` and `JOIN` queries using external sorting and block-based joins, mimicking real database management system behavior.

## 📁 Folder Structure

```
project/
├── data/
│   ├── User.txt
│   ├── Problem.txt
│   └── ... (all 9 tables as CSV)
├── queryProcessing.py
├── parser.py
├── select_processor.py
├── join_processor.py
├── external_sort.py
├── utils.py
└── README.md
```

## 🛠 Setup

1. Ensure all table `.txt` files are stored in the `data/` directory.
2. Each file must be CSV-formatted (first row is the header).
3. Install the required dependency:

```bash
pip install sqlparse
```

## ▶️ How to Run

Navigate to the project directory and run:

### 🔍 Select Query:
```bash
python queryProcessing.py "select * from User where user_id = 1 and username = 'alice'"
```

### 🔗 Join Query:
```bash
python queryProcessing.py "select * from User join User_Completed_Problems on User.user_id = User_Completed_Problems.user_id"
```

The output will be printed to the terminal.

## ✅ Supported Query Format

### SELECT
- Must be in the format:
```sql
select * from table where col1 = val1 and col2 = val2
```
- Both conditions are **required**.

### JOIN
- Must be in the format:
```sql
select * from table1 join table2 on table1.col = table2.col
```
- Only **equal joins** are supported.

## ⚠️ Restrictions

- No in-memory sorting or full-table reads.
- External sorting and block nested loop join are used to simulate database query processing.

---

## 👥 Team
CSUEB - Team 08
