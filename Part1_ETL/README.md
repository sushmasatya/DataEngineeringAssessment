# Part 1 - ETL Pipeline Implementation

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using PySpark and MySQL.

The pipeline extracts sales data, performs data cleansing and validation, applies business transformations, logs invalid records, and loads valid data into the target database.

---

## Project Structure

Part1_ETL/

├── firpy.py

├── sqlPart1.sql.txt

├── logs/

│ └── invalid_sales.csv

├── hadoop/

└── lib/

---

## Technologies Used

* Python
* PySpark
* MySQL
* Hadoop (winutils.exe)
* MySQL JDBC Connector

---

## ETL Process

### Extract

* Read source sales and customer data files.
* Load data into PySpark DataFrames.

### Transform

The following transformations are implemented in `firpy.py`:

* Removed duplicate records.
* Handled null and missing values.
* Filtered invalid records.
* Filtered negative quantity or invalid sales values.
* Derived calculated columns required for reporting.
* Performed data quality validation checks.
* Logged invalid records to `logs/invalid_sales.csv`.

### Incremental Loading

Incremental loading is implemented using a watermark approach.

* Previously processed records are identified.
* Only new records are loaded into the target database.
* Duplicate processing is avoided.

### Load

* Valid records are loaded into MySQL database tables.
* Invalid records are stored separately for auditing.

---

## Database Schema

The database schema is provided in:

`sqlPart1.sql.txt`

The script creates the required database objects and tables used by the ETL pipeline.

---

## Error Logging

Invalid records generated during ETL processing are stored in:

`logs/invalid_sales.csv`

This file captures records that fail validation checks.

---

## Execution

Run the ETL pipeline:

```bash
python firpy.py
```

## Deliverables

* Python ETL Script (`firpy.py`)
* SQL Schema Script (`sqlPart1.sql.txt`)
* Invalid Data Log (`logs/invalid_sales.csv`)
* README Documentation

## Author

Sushma
