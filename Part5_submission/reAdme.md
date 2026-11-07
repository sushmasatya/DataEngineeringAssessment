# Data Engineering Assessment

## Overview

This project demonstrates an end-to-end Data Engineering solution covering:

1. ETL Pipeline Development using PySpark and MySQL
2. SQL Query Development and Performance Optimization
3. SSIS Package Implementation
4. Power BI Dashboard and Business Insights

The solution extracts sales data, performs cleansing and validation, loads data into MySQL, analyzes the data using SQL queries, processes data through SSIS, and visualizes business insights using Power BI.

---

# Project Structure

```text
DataEngineeringAssessment/

├── Part1_ETL/
├── Part2_SQL/
├── Part3_SSIS/
├── Part4_PowerBI/
└── Part5_SUBMISSION/
```

---

# Part 1 - ETL Pipeline

## ETL Approach

The ETL pipeline was implemented using PySpark.

### Extract

* Read source sales data files.
* Load data into PySpark DataFrames.

### Transform

The following transformations were applied:

* Data cleansing
* Null value handling
* Duplicate removal
* Negative quantity filtering
* Data validation checks
* Derived column creation
* Invalid record logging

Invalid records are stored separately for auditing purposes.

### Incremental Loading

Incremental loading is implemented using a watermark approach.

* Existing transaction records are retrieved from MySQL.
* New records are identified using transaction IDs.
* Previously loaded records are excluded.
* Only new transactions are loaded into the target tables.

This prevents duplicate processing and improves performance.

### Load

Validated records are loaded into the MySQL database.

### Database Tables

* products
* transactions
* etl_watermark

---

# Part 2 - SQL Analysis

## Database Schema

Database schema creation scripts are provided in:

* sqlPart1.sql

## SQL Query Scripts

Analytical SQL queries are provided in:

* sqlPart2.sql

The queries demonstrate:

* Sales analysis
* Regional analysis
* Product performance
* Aggregations
* Business reporting

## Index Optimization

Indexes were created to improve query performance.

Example indexes:

```sql
CREATE INDEX idx_transaction_date
ON transactions(transaction_date);

CREATE INDEX idx_region
ON transactions(region);

CREATE INDEX idx_product_id
ON transactions(product_id);
```

### Performance Impact

Indexes improve query performance by:

* Reducing full table scans
* Improving filtering speed
* Improving JOIN performance
* Improving aggregation execution time

---

# Part 3 - SSIS Package

## Package Design

The SSIS package loads customer data through the following pipeline:

```text
Flat File Source
       ↓
Derived Column
       ↓
Sort (Remove Duplicates)
       ↓
Conditional Split
       ↓
Destination
```

## Data Validation

Validation is implemented using Conditional Split.

The package:

* Removes duplicate records
* Applies validation checks
* Routes valid records to destination tables

## Screenshots

The project includes screenshots of:

* Control Flow
* Data Flow
* Results Data Flow

These screenshots are available in the Part3_SSIS folder.

---

# Part 4 - Power BI Dashboard

## Dashboard Components

The dashboard includes:

* Sales by Region
* Average Sales per Transaction
* High Value Transactions
* Sales YTD
* Total Loyalty Points

## Key Insights

* Total Sales reached approximately 3.01K.
* Average Sale per Transaction was 601.23.
* Only one transaction exceeded 1000.
* North region generated the highest sales.
* Laptop was the highest revenue-generating product.
* Loyalty points were heavily concentrated in customers with Unknown region values.
* Sales trends showed fluctuations across months.

## DAX Measures

Examples include:

### Total Sales

```DAX
Total Sales =
SUM(transactions[total_value])
```

### Average Sale per Transaction

```DAX
Average Sale per Transaction =
DIVIDE(
    [Total Sales],
    DISTINCTCOUNT(transactions[transaction_id])
)
```

### Sales YTD

```DAX
Sales YTD =
TOTALYTD(
    [Total Sales],
    transactions[transaction_date]
)
```

---

# Challenges Faced and Solutions

## 1. MySQL JDBC Connector Configuration

### Challenge

Connecting PySpark to MySQL required the correct JDBC driver configuration.

Finding a compatible MySQL Connector/J version and matching JAR file took several attempts.

### Solution

* Downloaded the appropriate MySQL Connector/J version.
* Added the JAR file to the Spark configuration.
* Configured driver and executor class paths correctly.

---

## 2. Dependency and Version Compatibility

### Challenge

Multiple version compatibility issues occurred between:

* Python
* PySpark
* MySQL Connector
* Hadoop utilities

### Solution

* Installed compatible versions incrementally.
* Verified configurations step by step.
* Tested connectivity before implementing the complete pipeline.

---

## 3. Duplicate Data Loading in MySQL

### Challenge

During testing, transactions were loaded multiple times, creating duplicate records.

### Solution

* Implemented incremental loading logic.
* Used transaction IDs to identify previously loaded records.
* Introduced watermark tracking to prevent duplicate processing.

---

## 4. SSIS Configuration and Setup

### Challenge

SSIS was a completely new technology for this project.

Initial package configuration and execution required significant learning and troubleshooting.

### Solution

* Learned SSIS fundamentals from documentation and tutorials.
* Built the package incrementally.
* Configured components one step at a time.
* Validated the package using test executions.

---

## 5. Power BI Connectivity

### Challenge

A suitable 64-bit MySQL connector for Power BI was difficult to obtain and configure.

### Solution

* Used ODBC connectivity instead of the MySQL connector.
* Successfully connected Power BI to MySQL through ODBC.
* Imported data and built the dashboard visualizations.

---

# Suggestions for Production Deployment

For production environments, the following improvements are recommended:

## ETL

* Schedule ETL jobs using Airflow or enterprise schedulers.
* Implement automated monitoring and alerting.
* Store configuration values securely.

## Database

* Implement partitioning for large transaction tables.
* Add additional indexing based on workload patterns.
* Implement backup and recovery procedures.

## SSIS

* Deploy packages to SSIS Catalog.
* Use package configurations and environment variables.
* Implement centralized logging.

## Power BI

* Configure scheduled refresh.
* Implement Row-Level Security (RLS).
* Publish dashboards to Power BI Service.

## Monitoring

* Add ETL execution logs.
* Track load metrics.
* Monitor failures and performance statistics.

---

# Author

Sushma


<!-- Assessment documentation reviewed: November 2026 -->
