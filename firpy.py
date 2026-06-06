import os
import urllib.request
import ssl

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

data_dir1 = "hadoop/bin"
os.makedirs(data_dir1, exist_ok=True)

urls_and_paths = {
    "https://raw.githubusercontent.com/saiadityaus1/SparkCore1/master/test.txt": os.path.join(data_dir, "test.txt"),
    "https://github.com/saiadityaus1/SparkCore1/raw/master/winutils.exe": os.path.join(data_dir1, "winutils.exe"),
    "https://github.com/saiadityaus1/SparkCore1/raw/master/hadoop.dll": os.path.join(data_dir1, "hadoop.dll")
}

# Create an unverified SSL context
ssl_context = ssl._create_unverified_context()

for url, path in urls_and_paths.items():
    # Use the unverified context with urlopen
    with urllib.request.urlopen(url, context=ssl_context) as response, open(path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
import os, urllib.request, ssl; ssl_context = ssl._create_unverified_context(); [open(path, 'wb').write(urllib.request.urlopen(url, context=ssl_context).read()) for url, path in { "https://github.com/saiadityaus1/test1/raw/main/df.csv": "df.csv", "https://github.com/saiadityaus1/test1/raw/main/df1.csv": "df1.csv", "https://github.com/saiadityaus1/test1/raw/main/dt.txt": "dt.txt", "https://github.com/saiadityaus1/test1/raw/main/file1.txt": "file1.txt", "https://github.com/saiadityaus1/test1/raw/main/file2.txt": "file2.txt", "https://github.com/saiadityaus1/test1/raw/main/file3.txt": "file3.txt", "https://github.com/saiadityaus1/test1/raw/main/file4.json": "file4.json", "https://github.com/saiadityaus1/test1/raw/main/file5.parquet": "file5.parquet", "https://github.com/saiadityaus1/test1/raw/main/file6": "file6", "https://github.com/saiadityaus1/test1/raw/main/prod.csv": "prod.csv", "https://raw.githubusercontent.com/saiadityaus1/test1/refs/heads/main/state.txt": "state.txt", "https://github.com/saiadityaus1/test1/raw/main/usdata.csv": "usdata.csv", "https://github.com/saiadityaus1/SparkCore1/raw/refs/heads/master/data.orc": "data.orc", "https://github.com/saiadityaus1/test1/raw/main/usdata.csv": "usdata.csv", "https://raw.githubusercontent.com/saiadityaus1/SparkCore1/refs/heads/master/rm.json": "rm.json"}.items()]

# ======================================================================================

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from datetime import datetime
from pyspark.sql.functions import *
import sys

python_path = sys.executable
os.environ['PYSPARK_PYTHON'] = python_path

from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
os.chdir(PROJECT_DIR)

HADOOP_HOME = str(PROJECT_DIR / "hadoop")
os.environ["HADOOP_HOME"] = HADOOP_HOME
os.environ["hadoop.home.dir"] = HADOOP_HOME

python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

winutils = PROJECT_DIR / "hadoop" / "bin" / "winutils.exe"
if winutils.exists():
    print("HADOOP_HOME OK:", HADOOP_HOME)
else:
    print("ERROR: Run download section first. Missing:", winutils)
######################🔴🔴🔴################################

#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.datastax.spark:spark-cassandra-connector_2.12:3.5.1 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-avro_2.12:3.5.4 pyspark-shell'
#os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4 pyspark-shell'


#conf = SparkConf().setAppName("pyspark").setMaster("local[*]").set("spark.driver.host","localhost").set("spark.default.parallelism", "1")
#sc = SparkContext(conf=conf)

#spark = SparkSession.builder.getOrCreate()

# MySQL JDBC driver for Spark (MUST be before SparkContext)
MYSQL_JAR = str(PROJECT_DIR / "lib" / "mysql-connector-j-8.4.0.jar")
if not os.path.exists(MYSQL_JAR):
    raise FileNotFoundError(f"Missing MySQL JAR: {MYSQL_JAR}")

conf = (
    SparkConf()
    .setAppName("pyspark")
    .setMaster("local[*]")
    .set("spark.driver.host", "localhost")
    .set("spark.default.parallelism", "1")
    .set("spark.jars", MYSQL_JAR)                    # <-- FIX
    .set("spark.driver.extraClassPath", MYSQL_JAR)   # <-- FIX
    .set("spark.executor.extraClassPath", MYSQL_JAR) # <-- FIX
)

sc = SparkContext(conf=conf)
spark = SparkSession.builder.getOrCreate()

spark.read.format("csv").load("data/test.txt").toDF("Success").show(20, False)

##################🔴🔴🔴🔴🔴🔴 #############################
sales_df = spark.read.format("json").option("multiline", "true").load("sales_data.json")
sales_df.show()
sales_df.printSchema()
flatten_df = sales_df.select(
    "customer_id",
    "date",
    "discount",
    "product.category",
    "product.id",
    "product.name",
    "product.price",
    "quantity",
    "region",
    "transaction_id"
)
flatten_df.show()
sls_df=(flatten_df.withColumn("quantity",expr("abs(quantity)"))
        .withColumn("date",expr("translate(date,'/','-')"))
        .withColumn("date", expr("split(split(date,'T')[0],' ')[0]"))
        .withColumn("customer_id",expr("case when customer_id is null then 'invalid_id' else customer_id end "))
        .withColumnRenamed("region","sale_region")
        .withColumnRenamed("id","product_id")

        .fillna(0))
sls_df.show()
sale_df=sls_df.withColumn("date",expr('''case 
                                                  when date like '__-__-____'
                                                  then date_format(to_date(date,'dd-MM-yyyy'),'yyyy-MM-dd')
                                                   else date_format(to_date(date,'yyyy-MM-dd'),'yyyy-MM-dd')
                                                   end
                                               '''))
sale_df.show()
dup_df = sale_df.crossJoin(spark.range(120)).drop("id")
dup_df.show()
from pyspark.sql.functions import col, to_date, lit, round as spark_round, current_timestamp
MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DATABASE = "sales_db"
MYSQL_USER = "root"
MYSQL_PASSWORD = "sushma123"
JDBC_URL = (
    f"jdbc:mysql://{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    "?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC"
)
JDBC_PROPS = {
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "driver": "com.mysql.cj.jdbc.Driver",
}




os.makedirs("logs", exist_ok=True)

# --- Error logs (Part 1) ---
'''bad_cust = customer_df.filter(
    (col("customer_name") == "") | col("customer_name").isNull()
    | (col("email") == "") | col("email").isNull()
)

if bad_cust.count() > 0:
    bad_cust.toPandas().to_csv("logs/invalid_customers.csv", index=False)'''

bad_sales = flatten_df.filter((col("quantity") <= 0) | col("customer_id").isNull())
if bad_sales.count() > 0:
    bad_sales.toPandas().to_csv("logs/invalid_sales.csv", index=False)

# --- 3 tables for MySQL ---
'''customers_mysql = dup_df.select(
    "customer_id", "customer_name", "email",
    col("customer_region").alias("region"),
    to_date(col("join_date")).alias("join_date"),
    col("loyalty_points").cast("int"),
)'''

products_mysql = sale_df.select(
    col("product_id"), col("name").alias("product_name"),
    "category", col("price").cast("double")
)

transactions_mysql = sale_df.select(
    "transaction_id", "customer_id", "product_id",
    col("quantity").cast("int"),
    col("discount").alias("discount_pct"),
    spark_round(col("price") * col("quantity") * (lit(1) - col("discount")), 2).alias("total_value"),
    col("sale_region").alias("region"),
    to_date(col("date")).alias("transaction_date")
)

# --- INCREMENTAL: only new transaction_id ---
try:
    existing = spark.read.jdbc(JDBC_URL, "transactions", properties=JDBC_PROPS).select("transaction_id")
    new_tx = transactions_mysql.join(existing, "transaction_id", "left_anti")
except Exception:
    new_tx = transactions_mysql

print("New transactions:", new_tx.count())

FULL_RELOAD = True  # False on 2nd run for incremental test

import pymysql

def drop_all_tables():
    conn = pymysql.connect(
        host=MYSQL_HOST,
        port=int(MYSQL_PORT),
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )
    try:
        with conn.cursor() as cur:
            cur.execute("SET FOREIGN_KEY_CHECKS = 0")
            cur.execute("DROP TABLE IF EXISTS transactions")
            cur.execute("DROP TABLE IF EXISTS products")
          #  cur.execute("DROP TABLE IF EXISTS customers")
            cur.execute("DROP TABLE IF EXISTS etl_watermark")
            cur.execute("SET FOREIGN_KEY_CHECKS = 1")
        conn.commit()
        print("All tables DROPPED")
    finally:
        conn.close()

if FULL_RELOAD:
    drop_all_tables()
    tx_to_load = transactions_mysql
else:
    tx_to_load = new_tx

if FULL_RELOAD:
   # customers_mysql.write.jdbc(JDBC_URL, "customers", mode="overwrite", properties=JDBC_PROPS)
    products_mysql.write.jdbc(JDBC_URL, "products", mode="overwrite", properties=JDBC_PROPS)
    print("Products loaded")

if tx_to_load.count() > 0:
    tx_to_load.write.jdbc(JDBC_URL, "transactions", mode="append", properties=JDBC_PROPS)
    print("Transactions loaded:", tx_to_load.count())
else:
    print("No new transactions to load")

wm = spark.createDataFrame([("sales_transactions",)], ["pipeline_name"]) \
    .withColumn("last_loaded_at", current_timestamp())
wm.write.jdbc(JDBC_URL, "etl_watermark", mode="overwrite", properties=JDBC_PROPS)

spark.stop()
print("Part 1 load complete")
