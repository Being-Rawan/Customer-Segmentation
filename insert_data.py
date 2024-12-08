import pandas as pd
import pymysql

# Load the Excel file into a DataFrame
purchase_frequency = pd.read_excel('processed_purchase_frequency.xlsx')

# Establish a connection to MySQL
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='customer_data'
)

# Create a cursor object using the connection
cursor = connection.cursor()

# Loop through each row in the DataFrame and insert it into the MySQL table
for index, row in purchase_frequency.iterrows():
    customer_id = row['CustomerID']
    purchase_count = row['PurchaseCount']
    frequency_category = row['FrequencyCategory']

    # Insert data into the table
    cursor.execute("""
        INSERT INTO purchase_frequency (CustomerID, PurchaseCount, FrequencyCategory)
        VALUES (%s, %s, %s)
    """, (customer_id, purchase_count, frequency_category))

# Commit the transaction to save the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
