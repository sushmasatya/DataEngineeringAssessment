# Part 3 - SSIS Pipeline Implementation

## Overview

This part of the assessment implements an ETL pipeline using SQL Server Integration Services (SSIS).

The package extracts customer data from a flat file source, performs transformations and validation, removes duplicate records, and loads the validated data into the destination database.

---

## Project Structure

Part3_SSIS/

├── LoadCustomers.dtsx

├── README.md

└── screenshots/

├── controlflow.png

├── dataflow.png

└── ResultsDataFlow.png

---

## SSIS Package Design

### Extract

The SSIS package uses a **Flat File Source** to read customer data from the input file and load it into the Data Flow pipeline.

### Transform

The following transformations are implemented in the Data Flow:

#### Flat File Source

Reads the customer data file and passes records to the transformation pipeline.

#### Derived Column Transformation

Creates and modifies columns using expressions and business rules required for processing and loading.

#### Sort Transformation

Records are sorted and duplicate rows are removed before validation and loading.

#### Conditional Split Transformation

Records are validated based on predefined business rules.

After duplicate removal, the records are evaluated and routed through the valid output stream.

### Load

Validated records are loaded into the destination database table using the destination component.

The overall data flow is:

Flat File Source → Derived Column → Sort → Conditional Split → Destination

---

## Data Validation

Data validation is implemented using the **Conditional Split** transformation.

Validation checks ensure that records meet the required business rules before loading.

Duplicate records are removed during the Sort transformation. The remaining records satisfy the validation conditions and are loaded into the destination table.

No invalid records were generated during the final execution because duplicate records were removed and the remaining records passed all validation checks.

---

## Scaling Approach

The SSIS solution is designed to support larger datasets through:

* Efficient Data Flow design
* Separation of extraction, transformation, and loading stages
* Batch-oriented processing
* Parallel execution where applicable
* Database indexing for improved query performance

These techniques help improve scalability and execution efficiency.

---

## Screenshots

### Control Flow

Screenshot showing the SSIS Control Flow design.

### Data Flow

Screenshot showing the complete Data Flow pipeline:

Flat File Source → Derived Column → Sort → Conditional Split → Destination

### Results Data Flow

Screenshot showing the successful processing and loading of records into the destination table.

---

## Deliverables

* SSIS Package (`LoadCustomers.dtsx`)
* Control Flow Screenshot (`control_flow.png`)
* Data Flow Screenshot (`data_flow.png`)
* Results Data Flow Screenshot (`ResultsDataFlow.png`)
* README Documentation

---

## Author

Sushma
