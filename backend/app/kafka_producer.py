from kafka import KafkaProducer
import json
import pandas as pd
from kafka import KafkaConsumer
import psycopg2 

def send_to_kafka(data: dict):
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda data: json.dumps(data).encode('utf-8') )
    
    producer.send('data', value=data)
    
    producer.flush()  # Ensure all messages are sent
    print("Finished sending all rows.")

def consume_by_kafka():
    consumer = KafkaConsumer('data', 
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

    conn = psycopg2.connect(
        dbname="your_db",
        user="your_user",
        password="your_pw",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO food_logs (input_text, protein, fat, carbs) VALUES (%s, %s, %s, %s)",
        (message.value['input'], message.value['protein'], message.value['fat'], message.value['carbs'])
    )

    conn.commit()
    
    # Consume and process messages
    for message in consumer:
        print(f"Received: {message.value}")
        #store in database
        #CREATE DATABASE new_database_name;

