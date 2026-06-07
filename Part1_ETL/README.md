# Part 1 - ETL Pipeline Implementation

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using PySpark and MySQL. The pipeline extracts sales data from JSON files, performs data cleansing and validation, logs invalid records, and loads valid data into a MySQL database.

---

## Project Structure

```text
Part1_ETL/
├── README.md
├── firpy.py
├── sqlPart1.sql.txt
├── logs/
│   └── invalid_sales.csv
├── hadoop/
└── lib/
```

---

## Technologies Used

* Python
* PySpark
* MySQL
* Hadoop (WinUtils)
* MySQL JDBC Connector

---

## ETL Approach

### Extract

The pipeline reads sales data from JSON files and loads the data into PySpark DataFrames for processing.

### Transform

The following transformations are performed:

* Flattened nested JSON fields.
* Standardized date formats.
* Handled missing and null values.
* Replaced null customer IDs with a default value.
* Renamed columns for consistency.
* Filtered and validated sales records.
* Created separate datasets for products and transactions.

### Data Validation

Validation checks are applied to identify invalid records.

Examples include:

* Missing customer IDs.
* Invalid quantity values.

Invalid records are excluded from loading and written to a log file.

### Load

Validated records are loaded into MySQL tables using the MySQL JDBC connector.

The following tables are populated:

* products
* transactions
* etl_watermark

---

## Incremental Loading Logic

To avoid loading duplicate data, the ETL pipeline implements incremental loading based on the `transaction_id`.

### Process

1. Existing transaction IDs are read from the MySQL `transactions` table.
2. Incoming transaction records are compared with existing records.
3. A left anti join is performed to identify records that do not already exist in the database.
4. Only new transactions are loaded into the target table.

This ensures that when the ETL process is executed multiple times, previously loaded transactions are not inserted again.

### Example

```python
existing = spark.read.jdbc(
    JDBC_URL,
    "transactions",
    properties=JDBC_PROPS
).select("transaction_id")

new_tx = transactions_mysql.join(
    existing,
    "transaction_id",
    "left_anti"
)
```

### Watermark Tracking

After a successful load, the ETL pipeline updates the `etl_watermark` table with the current timestamp.

The watermark table records:

* Pipeline name
* Last successful load time

This provides a simple mechanism for monitoring ETL executions.

---

## Error Logging

Invalid sales records are stored in:

```text
logs/invalid_sales.csv
```

This file captures records that fail validation checks and require further review.

---

## Database Schema

The SQL script used to create the database schema is provided in:

```text
sqlPart1.sql.txt
```

---

## Execution

Run the ETL pipeline using:

```bash
python firpy.py
```

---

## Screenshots of Results

The following screenshots are included:

1. Successful ETL execution in PySpark.
2. Products table loaded into MySQL.
3. Transactions table loaded into MySQL.
4. Invalid records stored in `invalid_sales.csv`.
5. ETL watermark table showing the latest load timestamp.

---

## Deliverables

* Python ETL Script (`firpy.py`)
* SQL Schema Script (`sqlPart1.sql.txt`)
* Invalid Data Log (`logs/invalid_sales.csv`)
* README Documentation
* Public GitHub Repository

---

## Author

Sushma
