# **Customer Segmentation using Kafka, Spark, and MySQL**

This project demonstrates the use of Apache Kafka, Apache Spark Structured Streaming, and MySQL to process and analyze customer purchase frequency data from the *Online Retail* dataset. The primary goal is to categorize customers as **Low Frequency** or **High Frequency** based on their purchasing patterns.

---

## **Project Overview**

### **Dataset**
- Source: [UCI Machine Learning Repository - Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail).
- Format: Excel (`.xlsx`).
- Preprocessed to remove missing or invalid values and calculate the number of unique invoices per customer.

### **Workflow**
1. **Data Preprocessing**:
   - Cleaned the dataset in Jupyter Notebook using Python and Pandas.
   - Calculated purchase frequency for each customer based on unique invoice numbers.
   - Categorized customers as:
     - **Low Frequency**: Customers with ≤ 5 purchases.
     - **High Frequency**: Customers with > 5 purchases.

2. **Publishing to Kafka**:
   - Sent the processed data to a Kafka topic (`purchase-frequency`) using a Python Kafka producer.

3. **Real-Time Streaming and Processing with Spark**:
   - Consumed data from the Kafka topic.
   - Used Spark Structured Streaming to process the data.

4. **Storing Data in MySQL**:
   - Stored the processed data (`CustomerID`, `PurchaseCount`, and `FrequencyCategory`) in a MySQL database.

---

## **Technologies Used**

- **Python**:
  - Data preprocessing: Pandas, OpenPyXL.
  - Kafka producer: Kafka-Python.
- **Apache Kafka**:
  - For real-time messaging and data streaming.
- **Apache Spark**:
  - Structured Streaming for real-time data processing.
- **MySQL**:
  - Storing the processed data.
- **Git**:
  - Version control for project files.
- **XAMPP**:
  - For running the MySQL database locally.

---

## **Steps to Reproduce**

### **1. Preprocessing the Dataset**
- Use the Jupyter Notebook script (`jupyter.ipynb`) to clean and preprocess the dataset.
- Save the output as `processed_purchase_frequency.xlsx`.

### **2. Setting Up Kafka**
- Install and configure Kafka.
- Create a topic: `purchase-frequency`.

### **3. Running the Kafka Producer**
- Use the `kafka-producer.py` script to publish the processed data to the Kafka topic.

### **4. Running the Spark Consumer**
- Use the `spark-consumer.py` script to consume and process data from Kafka in real time.
- Ensure Spark is configured to connect to Kafka.

### **5. Storing Data in MySQL**
- Run the `insert_data.py` script to store the processed data in a MySQL database.

---

## **File Structure**

```
customer-segmentation/
│
├── Online Retail.xlsx                 # Original dataset
├── processed_purchase_frequency.xlsx  # Preprocessed dataset
├── jupyter.ipynb                      # Jupyter Notebook for preprocessing
├── kafka-producer.py                  # Kafka producer script
├── spark-consumer.py                  # Spark consumer script
├── insert_data.py                     # Script for storing data in MySQL
└── README.md                          # Project documentation
```

---

## **How to Run**

### **Prerequisites**
- Install Python libraries:
  ```bash
  pip install pandas openpyxl kafka-python pymysql
  ```
- Install Apache Kafka, Apache Spark, and MySQL.
- Configure MySQL to match the credentials in `insert_data.py`.

### **Steps**
1. Run the Jupyter Notebook to preprocess the dataset.
2. Start Kafka and create the topic.
3. Run the Kafka producer:
   ```bash
   python kafka-producer.py
   ```
4. Start the Spark consumer:
   ```bash
   spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.4,org.apache.kafka:kafka-clients:2.8.2 spark-consumer.py
   ```
5. Run the MySQL insertion script:
   ```bash
   python insert_data.py
   ```

---

## **Results**
- Data is categorized and stored in a MySQL table:
  - **Columns**: `CustomerID`, `PurchaseCount`, `FrequencyCategory`.
  - Example:
    | CustomerID | PurchaseCount | FrequencyCategory |
    |------------|---------------|--------------------|
    | 12345      | 3             | Low Frequency      |
    | 54321      | 10            | High Frequency     |

---

## **License**
This project is licensed under the MIT License.
