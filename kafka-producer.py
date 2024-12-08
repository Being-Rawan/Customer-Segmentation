from kafka import KafkaProducer
import pandas as pd
import json

# Load the processed dataset (purchase frequency)
purchase_frequency = pd.read_excel('processed_purchase_frequency.xlsx')

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializing JSON data
)

# Publish each row to the Kafka topic
for index, row in purchase_frequency.iterrows():
    message = {
        'CustomerID': row['CustomerID'],
        'PurchaseCount': row['PurchaseCount'],
        'FrequencyCategory': row['FrequencyCategory']
    }
    producer.send('purchase-frequency', value=message)

# Close the producer connection
producer.close()

print("Data published to Kafka successfully!")
