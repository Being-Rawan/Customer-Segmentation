from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Read data from the Kafka topic
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "purchase-frequency") \
    .load()

# Convert Kafka's binary data to string format
purchase_frequency_df = kafka_df.selectExpr("CAST(value AS STRING)")

# Perform data processing: parse the JSON and select relevant columns
parsed_df = purchase_frequency_df.selectExpr("json_tuple(value, 'CustomerID', 'PurchaseCount', 'FrequencyCategory') as (CustomerID, PurchaseCount, FrequencyCategory)")

# Optional: Convert the data types if needed (e.g., cast CustomerID to Integer)
processed_df = parsed_df.withColumn("CustomerID", col("CustomerID").cast("int"))

# Show the output for debugging (console output for streaming)
query = processed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
