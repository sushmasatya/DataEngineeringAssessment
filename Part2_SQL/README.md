# Part 2 - SQL Database Design and Analysis

## Overview

This part of the assessment focuses on database schema creation, SQL query development, indexing, and performance optimization using MySQL.

The database stores sales transaction data loaded from the ETL pipeline implemented in Part 1.

---

## Project Structure

```text
Part2_SQL/
├── README.md
├── sqlPart1.sql
├── sqlPart2.sql
└── indexes.sql
```

---

## Files Description

### sqlPart1.sql

Contains the database schema creation scripts including:

* Database creation
* Table creation
* Primary keys
* Foreign key relationships
* ETL watermark table

### sqlPart2.sql

Contains analytical SQL queries used to generate business insights from the sales data.

Example analyses include:

* Total sales by region
* Top-selling products
* Monthly sales trends
* Customer transaction analysis
* Product category performance

### indexes.sql

Contains index creation scripts used to improve query performance on frequently searched columns.

Example indexes include:

* Transaction date index
* Product ID index
* Region index

---

## Indexing Strategy

The following indexes were created to optimize query performance:

### Transaction Date Index

```sql
CREATE INDEX idx_transaction_date
ON transactions(transaction_date);
```

Improves filtering and aggregation on transaction dates.

### Product ID Index

```sql
CREATE INDEX idx_product_id
ON transactions(product_id);
```

Improves join performance between transactions and products tables.

### Region Index

```sql
CREATE INDEX idx_region
ON transactions(region);
```

Improves filtering and grouping by sales region.

---

## Performance Impact

Indexes reduce the amount of data scanned during query execution.

Benefits include:

* Faster filtering operations
* Improved JOIN performance
* Faster aggregations and reporting queries
* Reduced query execution time on large datasets

---

## Execution

### Create Schema

Run:

```sql
SOURCE sqlPart1.sql;
```

### Create Indexes

Run:

```sql
SOURCE indexes.sql;
```

### Execute Queries

Run:

```sql
SOURCE sqlPart2.sql;
```

---

## Deliverables

* SQL Schema Creation Script (`sqlPart1.sql`)
* SQL Query Script (`sqlPart2.sql`)
* Index Creation Script (`indexes.sql`)
* README Documentation

---

## Author

Sushma
