# Part 4 - Power BI Dashboard

## Overview

This part of the assessment presents a Power BI dashboard built using the sales and customer data loaded through the ETL pipeline and SQL database.

The dashboard provides business insights through interactive visualizations and DAX measures that help analyze sales performance, customer loyalty, product performance, and regional trends.

---

## Project Structure

Part4_PowerBI/

├── SalesDashboard.pbix

├── README.md

└── Screenshots_bi/

├── average_sales_per_transaction.png

├── high_value&sales_YTD.png

├── sales_by_region.png

└── Total_Loyalty_Points.png

---

## Dashboard Components

The dashboard includes the following reports and visualizations:

### Sales by Region

Displays total sales generated across different regions and helps identify the highest-performing region.

### Average Sales per Transaction

Shows the average revenue generated per transaction.

### High-Value Transactions and Sales YTD

Displays:

* Number of transactions with value greater than 1000.
* Year-to-Date (YTD) cumulative sales.

### Total Loyalty Points

Visualizes loyalty point distribution across customer regions.

---

## Key Insights

### 1. Total Sales

Total Sales amounted to approximately **3.01K**, representing the overall revenue generated from transactions.

### 2. Average Sale per Transaction

Average Sale per Transaction was **601.23**, showing the average revenue earned per transaction.

### 3. High-Value Transactions

Only **1 transaction exceeded 1000**, indicating that high-value purchases are relatively rare.

### 4. Regional Performance

The **North region contributed the highest sales**, significantly outperforming the East, West, and South regions.

### 5. Product Performance

The **Laptop product generated the highest revenue** among all products, making it the top-performing product.

### 6. Loyalty Points Distribution

A large proportion of loyalty points are associated with customers whose region is marked as **Unknown**, suggesting potential data quality or customer profiling issues.

### 7. Sales Trend Analysis

Sales fluctuate across months, with a noticeable peak early in the period followed by lower sales in subsequent months.

---

## DAX Logic Used

### Total Sales

```DAX
Total Sales =
SUM(transactions[total_value])
```

Calculates the total revenue generated from all transactions.

### Average Sale per Transaction

```DAX
Average Sale per Transaction =
DIVIDE(
    [Total Sales],
    DISTINCTCOUNT(transactions[transaction_id])
)
```

Calculates the average value of each transaction.

### Total Loyalty Points

```DAX
Total Loyalty Points =
SUM(customers[loyalty_points])
```

Calculates the total loyalty points accumulated by customers.

### High-Value Transactions (>1000)

```DAX
High-Value Transactions (>1000) =
CALCULATE(
    DISTINCTCOUNT(transactions[transaction_id]),
    transactions[total_value] > 1000
)
```

Counts transactions with a value greater than 1000.

### Sales YTD

```DAX
Sales YTD =
TOTALYTD(
    [Total Sales],
    transactions[transaction_date]
)
```

Calculates cumulative sales from the beginning of the year up to the selected date.

---

## Screenshots

### Sales by Region

File: `sales_by_region.png`

Shows total sales generated across regions and identifies the highest-performing region.

### Average Sales per Transaction

File: `average_sales_per_transaction.png`

Displays the average revenue generated per transaction.

### High-Value Transactions and Sales YTD

File: `high_value&sales_YTD.png`

Displays the count of high-value transactions and cumulative Year-to-Date sales.

### Total Loyalty Points

File: `Total_Loyalty_Points.png`

Shows loyalty point distribution across customer regions.

---

## Deliverables

* Power BI Dashboard File (`SalesDashboard.pbix`)
* Dashboard Screenshots
* DAX Measures Documentation
* Business Insights Summary
* README Documentation

---

## Author

Sushma
